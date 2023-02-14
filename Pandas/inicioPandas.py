import pandas as pd 
import numpy as np

etiquetas= ['a','b','c','d','e']
datos=np.arange(4,9)

serie= pd.Series(datos, index=etiquetas)
print(serie)

#aceeder valor
print(serie['c'])

#datos de distintos tipos

datos=['Eliseo',49,'Ro',46]

serie = pd.Series(datos)
print(serie)

#datos directos

serie=pd.Series([1000,500,1200,700],['emp01','emp02','emp03','emp04'])
print(serie)

#operaciones suma

serie1=pd.Series([1000,500,1200,700],['emp01','emp02','emp03','emp04'])
print(serie1)

serie2=pd.Series([100,50,120,70],['emp01','emp02','emp03','emp04'])
print(serie2)

serie3=serie1+serie2
print(serie3)

#data frames

filas=['tienda1','tienda2','tienda3','tienda4']
columnas= ['articulo1','articulo2','articulo3']
datos=[[np.nan,100,200],[np.nan,100,300],[300,np.nan,400],[400,100,500]]

dataFrame=pd.DataFrame(datos,filas,columnas)
print(dataFrame)

#seleccion fila
print(dataFrame.loc['tienda2'])
print(dataFrame.loc[['tienda2','tienda3']])

#seleccion columna

print(dataFrame['articulo3'])

#valor concreto

print(dataFrame.loc['tienda2','articulo3'])

#nueva columna
dataFrame['articulo4']=25
print(dataFrame)

dataFrame['total']=dataFrame['articulo1']+dataFrame['articulo2']+dataFrame['articulo3']+dataFrame['articulo4']
print(dataFrame)

#eliminar una columna
#dataFrame= dataFrame.drop(['total',axis=1])se borra definitivamente 
print(dataFrame.drop(['total'],axis=1, inplace=True))
print(dataFrame)

condicion=dataFrame > 200
print(dataFrame[condicion])

condicion = (dataFrame['articulo1']>=200) | (dataFrame['articulo2']>=100)
print(dataFrame[condicion])

nuevaColumna='1 2 3 4'.split()
dataFrame['indices']=nuevaColumna
print(dataFrame)

dataFrame=dataFrame.set_index('indices')
print(dataFrame)
#dataFrame.dropna(axis=1,inplace=True)#esto borra todos las columnas con valores nulos
#dataFrame.fillna(value=90,inplace=True)#aca rellenamos todos los datos nulos
media=dataFrame.mean()
print(f"la media es igual a {media}")
dataFrame.fillna(value=media,inplace=True)
print(dataFrame)

#union de dataframes

data1=dataFrame.copy()
data2=dataFrame.copy()
print(data1)
print(data2)
dataTotal=pd.concat([data1, data2], axis=0)
print(dataTotal)

print(dataFrame['articulo2'].unique())
print(dataFrame['articulo2'].value_counts())

print(dataTotal['articulo2'].unique())
print(dataTotal['articulo2'].value_counts())

dataTotal=dataTotal.apply(lambda x: x*3)
print(dataTotal)

print(dataTotal.columns)

print(dataTotal.index)

print(dataTotal.sort_values(['articulo3']))

print(dataTotal.describe())

#dataTotal.to_csv('dataTotal.csv')

dataFrame = pd.read_csv('dataTotal.csv', index_col=0)
print(dataFrame)
