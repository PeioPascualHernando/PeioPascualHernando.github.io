
import json
from jsonpath_ng.ext import parse
import matplotlib.pyplot as plt
with open("C:\\Users\\pelli\\Desktop\\datos gasolineras\\data\\2022\\09\\2022-09-13.json","r",encoding='utf-8') as datosJson:
	data = json.load(datosJson)

findPrecios = parse("$.ListaEESSPrecio[*].PrecioProducto")
findPlaces = parse("$..Municipio")
precios = []
for pr in findPrecios.find(data):
	precios.append(pr.value)
print(precios)

