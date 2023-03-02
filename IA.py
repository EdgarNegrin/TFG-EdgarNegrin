import pandas as pd

def datos(partidos):
  
  dataframe = pd.DataFrame(partidos, columns=['Equipo', 'Adversario', 'Goles_favor', 'Goles_contra', 'Resultado'])
  print(dataframe.head())