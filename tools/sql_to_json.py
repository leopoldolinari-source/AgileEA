"""Convierte un backup SQL de AgileEA (INSERTs) en un JSON {tabla: [filas]}.

Uso: python3 tools/sql_to_json.py backup.sql estratos/data.json
Sirve para correr Estratos sin base de datos (demo / offline).
"""
import json, re, sys

def parse_values(s, i):
    rows, row, n = [], None, len(s)
    while i < n:
        c = s[i]
        if c == '(':
            row = []; i += 1
        elif c == "'":
            j, buf = i + 1, []
            while True:
                if s[j] == '\\':
                    buf.append({'n': '\n', 'r': '\r', 't': '\t', '0': '\0'}.get(s[j+1], s[j+1])); j += 2
                elif s[j] == "'" and s[j+1:j+2] == "'":
                    buf.append("'"); j += 2
                elif s[j] == "'":
                    break
                else:
                    buf.append(s[j]); j += 1
            row.append(''.join(buf)); i = j + 1
        elif s.startswith('NULL', i):
            row.append(None); i += 4
        elif c == ')':
            rows.append(row); i += 1
        elif c == ';':
            return rows, i + 1
        elif c.isdigit() or c == '-':
            m = re.match(r'-?[\d.]+', s[i:]); row.append(m.group()); i += len(m.group())
        else:
            i += 1
    return rows, i

def main(src, dst):
    s = open(src, encoding='utf-8').read()
    out = {}
    for m in re.finditer(r"INSERT INTO `(\w+)` \(([^)]*)\) VALUES\s*", s):
        cols = [c.strip(' `') for c in m.group(2).split(',')]
        rows, _ = parse_values(s, m.end())
        out.setdefault(m.group(1), []).extend(dict(zip(cols, r)) for r in rows)
    json.dump(out, open(dst, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print({k: len(v) for k, v in out.items()})

if __name__ == '__main__':
    main(*sys.argv[1:3])
