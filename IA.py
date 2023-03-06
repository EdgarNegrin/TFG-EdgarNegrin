import pandas as pd

def datos(partidos):
  
  dataframe = pd.DataFrame(partidos, columns=['Equipo', 'Adversario', 'Goles_favor', 'Goles_contra', 'Resultado'])
  print(dataframe.head())
  x = dataframe['Adversario']
  
  # Extraemos el diccionario de los equipos
  equipos_nombre = {}
  indice = 0
  for equipo in x:
    if equipo not in equipos_nombre.keys():
      equipos_nombre[equipo] = indice
      indice += 1
    
  print(equipos_nombre)
  
  
def prediccion():
  dato = pd.read_csv('Datos/prediccion/LaLiga_Matches_1995-2021')
  