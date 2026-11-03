#!/usr/bin/env bash
set -euo pipefail
ae2s_ponder_project=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)
ae2s_ponder_local_jdk="$ae2s_ponder_project/../../.dev/jdk-25.0.5+8"
if [[ -n "${AE2S_PONDER_JAVA_HOME:-}" ]]; then
    export JAVA_HOME="$AE2S_PONDER_JAVA_HOME"
elif [[ -x "$ae2s_ponder_local_jdk/bin/java" ]]; then
    export JAVA_HOME="$ae2s_ponder_local_jdk"
fi
ae2s_ponder_proxy_args=()
ae2s_ponder_proxy="${HTTPS_PROXY:-${https_proxy:-}}"
if [[ "$ae2s_ponder_proxy" =~ ^https?://([^/:@]+):([0-9]+)/?$ ]]; then
    ae2s_ponder_proxy_args+=("-Dhttps.proxyHost=${BASH_REMATCH[1]}" "-Dhttps.proxyPort=${BASH_REMATCH[2]}")
    ae2s_ponder_proxy_args+=("-Dhttp.proxyHost=${BASH_REMATCH[1]}" "-Dhttp.proxyPort=${BASH_REMATCH[2]}")
fi
cd -- "$ae2s_ponder_project"
exec ./gradlew "${ae2s_ponder_proxy_args[@]}" "$@"
