#!/usr/bin/env bash
# Verifica la regla "una carpeta por archivo": cada archivo no-Markdown debe estar
# en una carpeta que contenga <nombre de la carpeta>.md.
# Excepciones: las páginas web con carpeta assets (infografías) y herramientas/.
set -euo pipefail
cd "$(dirname "$0")/.."

faltan=0
while IFS= read -r -d '' f; do
  dir=$(dirname "$f")
  if [ ! -f "$dir/$(basename "$dir").md" ]; then
    echo "SIN CARPETA/.md: $f"
    faltan=$((faltan + 1))
  fi
done < <(find curso proyecto-newbit descartado -type f -not -name '*.md' -not -name '.DS_Store' \
  -not -path '*/infografias/*' -not -path '*/Infografias_NewBit/*' \
  -not -path 'proyecto-newbit/app/*' -not -path 'proyecto-newbit/ml/*' -not -path 'proyecto-newbit/tests/*' \
  -not -path 'proyecto-newbit/storage/*' -not -name '.gitkeep' -not -name 'requirements.txt' -print0)

# Archivos sueltos en la raíz (recién agregados, aún sin clasificar)
while IFS= read -r -d '' f; do
  echo "SIN CLASIFICAR (raíz): $f"; faltan=$((faltan + 1))
done < <(find . -maxdepth 1 -type f -not -name '*.md' -not -name '.*' -not -name 'run.bat' -not -name 'run.ps1' -print0)

if [ "$faltan" -eq 0 ]; then echo "OK: cada archivo está en su carpeta con su .md."; else exit 1; fi
