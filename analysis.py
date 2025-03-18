from worldPopulation import obtener_datos

df = obtener_datos()  # Obtener el DataFrame

df_colombia = df[df["país"].str.contains("colombia", case=False, na=False)]

print(df_colombia)
