import requests
import pandas as pd

# URL de la API del Banco Mundial para la población total
url = "https://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL?format=json&per_page=30000"

# Hacer la solicitud
response = requests.get(url)

# Verificar que la solicitud fue exitosa
if response.status_code == 200:
    data = response.json()[1]  # Extraer los datos

    # Convertir la respuesta en un DataFrame
    df = pd.DataFrame([
        {
            "país": entry["country"]["value"],
            "isoCode": entry["country"]["id"],
            "año": int(entry["date"]),  # Convertir año a entero
            "población": entry["value"]
        }
        for entry in data if entry["value"] is not None  # Evitar valores nulos
    ])

    # Mostrar primeras filas
    print(df.head())

else:
    print(f"❌ Error en la solicitud: {response.status_code}")
    df = None  # Definir df como None en caso de error

# Función para obtener los datos en otro script
def obtener_datos():
    return df  # Retorna el DataFrame global