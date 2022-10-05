
from jsonpath_ng.ext import parse
for y in range(2007, 2023):
    for m in range(1, 13):
        for d in range(1, 32):
            y, m, d = str(y), str(m), str(d)
            if len(m) == 1:
                m = "0" + m
            if len(d) == 1:
                d = "0" + d
            try:
                with open(f"C:\\Users\\pelli\\Desktop\\datos gasolineras\\data\\{y}\\{m}\\{y}-{m}-{d}.json", "r", encoding='utf-8') as f:
                    data = f.read()
            except (FileExistsError, FileNotFoundError):
                continue
            with open(f"C:\\Users\\pelli\\Desktop\\datos gasolineras\\data\\{y}\\{m}\\{y}-{m}-{d}.json", "w", encoding='utf-8') as f:
                f.write(data.replace("ó", "o"))
