import json
from jsonpath_ng.ext import parse
year = "2022"
month = "09"
day = "01"
contentMap = {"Localidad": {}}
try:
    with open(f"C:\\Users\\pelli\\Desktop\\datos gasolineras\\data\\{year}\\{month}\\{year}-{month}-{day}.json","r",encoding='utf-8') as f:
        data = json.load(f)
    for pl in parse("$.ListaEESSPrecio[*].Municipio").find(data):
        if pl.value not in contentMap["Localidad"]:
            contentMap["Localidad"][pl.value] = [mr.value for mr in parse(f"$.ListaEESSPrecio[?(@.Municipio =~ '{pl.value}')].Rotulo").find(data)]
    with open("C:\\Users\\pelli\\Desktop\\datos gasolineras\\code\\contentMap.json","w",encoding='utf-8') as f:
        f.write(str(contentMap).replace("'","\""))
        print(str(contentMap).replace("'","\""))
except (FileExistsError,FileNotFoundError):
    print("File does not exist.")