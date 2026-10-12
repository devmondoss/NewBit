#!/usr/bin/env bash
# Verifica la regla "una carpeta por archivo": cada archivo no-Markdown debe estar
# en una carpeta que contenga <nombre de la carpeta>.md.
# Excepciones: infografias/ (página web del equipo) y scripts/.
set -euo pipefail
cd "$(dirname "$0")/.."

faltan=0
while IFS= read -r -d '' f; do
  dir=$(dirname "$f")
  if [ ! -f "$dir/$(basename "$dir").md" ]; then
    echo "SIN CARPETA/.md: $f"
    faltan=$((faltan + 1))
  fi
done < <(find docs proyecto archivo -type f -not -name '*.md' -not -name '.DS_Store' \
  -not -path '*/infografias/*' -not -path '*/Infografias_NewBit/*' -print0)

# Archivos sueltos en la raíz (recién agregados, aún sin clasificar)
while IFS= read -r -d '' f; do
  echo "SIN CLASIFICAR (raíz): $f"; faltan=$((faltan + 1))
done < <(find . -maxdepth 1 -type f -not -name '*.md' -not -name '.*' -print0)

if [ "$faltan" -eq 0 ]; then echo "OK: cada archivo está en su carpeta con su .md."; fi
