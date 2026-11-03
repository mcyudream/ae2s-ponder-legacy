#!/usr/bin/env python3
"""Generate original, deterministic 1.12 structure NBT using only the Python standard library.

AE2S 1.1.0 stores cable/face parts as named compounds in ae2:cable_bus tiles.
The visual compounds preserve cable connections in Ponder's client-only virtual world.
Run with --check to verify committed assets without changing them.
"""
from __future__ import annotations
import argparse
import gzip
import io
from pathlib import Path
import struct

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "src/main/resources/assets/ae2s_ponder/ponder"

class Byte(int):
    pass

class Short(int):
    pass

def kind(value):
    if isinstance(value, Byte): return 1
    if isinstance(value, Short): return 2
    if isinstance(value, int): return 3
    if isinstance(value, str): return 8
    if isinstance(value, list): return 9
    if isinstance(value, dict): return 10
    raise TypeError(type(value))

def utf8(value):
    raw = value.encode("utf-8")
    return struct.pack(">H", len(raw)) + raw

def payload(value):
    tag = kind(value)
    if tag in (1, 2, 3): return struct.pack({1: ">b", 2: ">h", 3: ">i"}[tag], value)
    if tag == 8: return utf8(value)
    if tag == 9:
        element = kind(value[0]) if value else 10
        assert all(kind(v) == element for v in value), "heterogeneous NBT list"
        return bytes([element]) + struct.pack(">i", len(value)) + b"".join(payload(v) for v in value)
    if tag == 10:
        return b"".join(bytes([kind(v)]) + utf8(k) + payload(v) for k, v in value.items()) + b"\0"
    raise AssertionError(tag)

def item(name, count=1, slot=0):
    return {"Slot": Byte(slot), "id": name, "Count": Byte(count), "Damage": Short(0)}

class Structure:
    def __init__(self, size=7):
        self.size = size
        self.palette = []
        self.blocks = {}
        for x in range(size):
            for z in range(size):
                self.block(x, 0, z, "minecraft:concrete",
                           {"color": "gray" if x in (0, size - 1) or z in (0, size - 1) else "silver"})

    def block(self, x, y, z, name, properties=None, nbt=None):
        state = {"Name": name}
        if properties: state["Properties"] = properties
        if state not in self.palette: self.palette.append(state)
        entry = {"pos": [x, y, z], "state": self.palette.index(state)}
        if nbt: entry["nbt"] = nbt
        self.blocks[x, y, z] = entry
        return self

    def machine(self, x, y, z, name, **nbt):
        tile = name if name != "dense_energy_cell" else "energy_cell"
        if name.endswith("_crafting_storage") or name == "crafting_accelerator": tile = "crafting_unit"
        return self.block(x, y, z, "ae2:" + name, nbt={
            "id": "ae2:" + tile, "x": x, "y": y, "z": z, "forward": "SOUTH", "up": "UP", **nbt})

    def chest(self, x, y, z, contents=None):
        return self.block(x, y, z, "minecraft:chest", {"facing": "north"},
                          {"id": "minecraft:chest", "x": x, "y": y, "z": z, "Items": contents or []})

    def cable(self, x, y, z, cable="fluix_glass_cable", connections=(), channels=0, **parts):
        nbt = {"id": "ae2:cable_bus", "x": x, "y": y, "z": z}
        if cable:
            nbt["cable"] = {"id": "ae2:" + cable, "visual": {
                "powered": Byte(1), "missingChannel": Byte(0), "channels": channels,
                "connections": list(connections)}}
        for side, part in parts.items():
            nbt[side] = {"id": "ae2:" + part, "visual": {"powered": Byte(1), "missingChannel": Byte(0)}}
        return self.block(x, y, z, "ae2:cable_bus", nbt=nbt)

    def data(self):
        height = max(p[1] for p in self.blocks) + 1
        root = {"DataVersion": 1343, "author": "AE2S Ponder", "size": [self.size, height, self.size],
                "palette": self.palette, "blocks": list(self.blocks.values()), "entities": []}
        output = io.BytesIO()
        with gzip.GzipFile(fileobj=output, mode="wb", filename="", mtime=0) as compressed:
            compressed.write(b"\x0a\0\0" + payload(root))
        return output.getvalue()

def first_network():
    s = Structure()
    s.machine(1, 1, 2, "vibration_chamber").machine(1, 1, 3, "energy_cell")
    s.machine(1, 1, 4, "energy_acceptor").machine(5, 1, 3, "drive")
    for x in range(2, 5):
        s.cable(x, 1, 3, connections=("west", "east"), **({"south": "terminal"} if x == 3 else {}))
    return s

def storage_cells():
    s = Structure()
    s.machine(1, 1, 3, "energy_cell").machine(2, 1, 3, "drive").machine(4, 1, 1, "cell_workbench")
    s.cable(3, 1, 3, connections=("west", "east"), south="terminal").cable(4, 1, 3, connections=("west",))
    return s

def channels():
    s = Structure(9)
    s.machine(1, 1, 3, "controller").machine(1, 1, 2, "energy_cell").machine(4, 1, 2, "drive", forward="NORTH")
    for x in range(2, 8):
        cable = "fluix_smart_cable" if x < 5 else "fluix_smart_dense_cable"
        connections = ["west", "east"] if x != 7 else ["west"]
        if x == 4: connections.append("north")
        s.cable(x, 1, 3, cable, connections=connections, channels=4)
    # Separated comparison examples: touching different colors remain separate networks.
    s.cable(3, 1, 5, "red_glass_cable", connections=("west",))
    s.cable(4, 1, 5, "blue_glass_cable", connections=("east",))
    s.cable(5, 1, 5, "blue_glass_cable", connections=("west",))
    s.cable(3, 1, 7, "red_glass_cable", connections=("east",))
    s.cable(4, 1, 7, "blue_glass_cable", connections=("east",), west="quartz_fiber")
    s.cable(5, 1, 7, "blue_glass_cable", connections=("west",))
    return s

def storage_bus():
    s = Structure()
    s.machine(1, 1, 3, "energy_cell").machine(2, 1, 3, "drive")
    s.cable(3, 1, 3, connections=("west", "east"), south="terminal")
    s.cable(4, 1, 3, connections=("west",), east="storage_bus")
    s.chest(5, 1, 3, [item("minecraft:iron_ingot", 32), item("minecraft:gold_ingot", 16, 1)])
    return s

def import_export():
    s = Structure()
    s.machine(1, 1, 3, "energy_cell").machine(2, 1, 3, "drive")
    s.cable(3, 1, 3, connections=("west", "north", "east"), south="terminal")
    s.chest(1, 1, 1, [item("minecraft:iron_ingot", 32)])
    s.cable(2, 1, 1, connections=("east",), west="import_bus")
    s.cable(3, 1, 1, connections=("west", "south"))
    s.cable(3, 1, 2, connections=("north", "south"))
    s.cable(4, 1, 3, connections=("west", "south"))
    s.cable(4, 1, 4, connections=("north", "south"))
    s.cable(4, 1, 5, connections=("north",), east="export_bus")
    s.chest(5, 1, 5)
    return s

def autocrafting():
    s = Structure()
    s.machine(1, 1, 3, "drive").machine(1, 1, 2, "energy_cell")
    s.cable(2, 1, 3, connections=("west", "east", "north"), south="pattern_encoding_terminal")
    s.cable(3, 1, 3, connections=("west", "east"), south="crafting_terminal")
    s.machine(4, 1, 3, "pattern_provider").machine(5, 1, 3, "molecular_assembler")
    s.cable(2, 1, 2, connections=("north", "south"))
    s.machine(2, 1, 1, "1k_crafting_storage").machine(3, 1, 1, "crafting_accelerator")
    return s

def processing():
    s = Structure()
    s.machine(1, 1, 3, "drive").machine(1, 1, 2, "energy_cell")
    s.cable(2, 1, 3, connections=("west", "east", "north"), south="pattern_encoding_terminal")
    s.cable(3, 1, 3, connections=("west", "east"), south="crafting_terminal")
    s.cable(2, 1, 2, connections=("north", "south"))
    s.machine(2, 1, 1, "1k_crafting_storage")
    s.cable(4, 1, 3, connections=("west", "east", "up"))
    s.cable(4, 2, 3, connections=("down", "up"))
    s.cable(4, 3, 3, connections=("down", "east"))
    s.machine(5, 3, 3, "pattern_provider")
    s.block(5, 2, 3, "minecraft:furnace", {"facing": "south"},
            {"id": "minecraft:furnace", "x": 5, "y": 2, "z": 3, "Items": [item("minecraft:coal", 16, 1)]})
    s.cable(5, 1, 3, connections=("west",), up="import_bus")
    return s

def p2p():
    s = Structure(9)
    # The controller face feeds the OUTER side of the west-facing input.
    s.machine(1, 1, 3, "controller").machine(1, 1, 2, "energy_cell")
    s.cable(2, 1, 3, "fluix_smart_cable", connections=("south",), channels=2, west="me_p2p_tunnel")
    s.cable(6, 1, 3, "fluix_smart_cable", connections=("south",), channels=2, east="me_p2p_tunnel")
    s.cable(2, 1, 4, "fluix_smart_cable", connections=("north", "south", "west"), channels=2)
    s.cable(6, 1, 4, "fluix_smart_cable", connections=("north", "south"), channels=2)
    for x in range(2, 7):
        sides = ["east"] if x == 2 else ["west"] if x == 6 else ["west", "east"]
        if x in (2, 6): sides.append("north")
        s.cable(x, 1, 5, "fluix_smart_cable", connections=sides, channels=2)
    # Quartz fiber passes power from the source network to the separate carrier network.
    s.cable(1, 1, 4, "fluix_smart_cable", connections=("east",), north="quartz_fiber")
    s.cable(7, 1, 3, "fluix_smart_dense_cable", connections=("west", "east"), channels=1)
    # Leave air between the outer network and the carrier: the drive must not bridge them.
    s.machine(8, 1, 3, "drive", forward="SOUTH")
    s.blocks[2, 1, 3]["nbt"]["west"].update(freq=Short(4660), output=Byte(0))
    s.blocks[6, 1, 3]["nbt"]["east"].update(freq=Short(0), output=Byte(0))
    return s

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    scenes = (first_network, storage_cells, channels, storage_bus, import_export, autocrafting, processing, p2p)
    for factory in scenes:
        output = DEST / (factory.__name__ + ".nbt")
        data = factory().data()
        if args.check:
            if not output.exists() or output.read_bytes() != data:
                raise SystemExit(f"Structure differs: {output}")
        else:
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_bytes(data)
        print(f"{factory.__name__}: {len(data)} bytes")

if __name__ == "__main__": main()
