import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
datos= pd.read_csv("dataTotal.csv")
#datos.set_index('ID', inplace=True)
print("inicio dataFrame")
print(datos.head(5))
print("Final dataFrame")
print(datos.tail(5))

print(datos.info())
print(datos.describe())
print(datos.columns)
print(datos.index)

datosAgrupados=datos.groupby('articulo1').TOTAL.suma()
print(datosAgrupados.head(5))

plt.pie(datosAgrupados,labels=datosAgrupados.index)
plt.show()