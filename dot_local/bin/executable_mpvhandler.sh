#!/bin/bash

function urldecode() {
  local url_encoded="${1//+/ }"
  printf '%b' "${url_encoded//%/\\x}"
}

decoded="$(urldecode "${1:6}")"
exec sh -c "exec mpv $decoded"
