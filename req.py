import requests
urlI = "https://sedeaplicaciones.minetur.gob.es/ServiciosRESTCarburantes/PreciosCarburantes/EstacionesTerrestresHist/FiltroProvinciaProducto/"
urlF = "/48/4"
day = "01"
month= "01"
year = "2007"
for year in range(2007,2023):
    for month in range(1,13):
        for day in range(1,32):
            year, month, day = str(year), str(month), str(day)
            if len(month) == 1:
                month = "0"+month
            if len(day) == 1:
                day = "0" + day
            date = day + "-" + month + "-" + year
            url = urlI + date + urlF
            response = requests.request("GET", url, headers={}, data={})
            if str(response) == "<Response [200]>":
                date = year + "-" + month + "-" + day
                with open(f"C:\\Users\\pelli\\Desktop\\datos gasolineras\\data\\{year}\\{month}\\{date}.json","w",encoding='utf-8') as f:
                    f.write(response.text)
