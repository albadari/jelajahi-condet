"""Jalankan setelah memperbarui data.json. Hanya memakai pustaka standar Python."""
import json
from pathlib import Path

root = Path(__file__).resolve().parent
data = json.loads((root / 'data.json').read_text(encoding='utf-8'))
ids = [entry['id'] for entry in data['entries']]
if len(ids) != len(set(ids)):
    raise ValueError('ID entri harus unik')
for relation in data['relations']:
    if relation['from'] not in ids or relation['to'] not in ids:
        raise ValueError('Hubungan mengarah ke ID yang tidak tersedia')
(root / 'data.js').write_text('window.CONDET_DATA = ' + json.dumps(data, ensure_ascii=False) + ';\n', encoding='utf-8')
print(f"Data diperbarui: {len(ids)} entri.")
