
# Extraemos los resultados de la base de datos
def resultado(marcador):
  marcador_ = marcador.split('-')
  
  goles_local = marcador_[0]
  goles_visitante = marcador_[1]
  ganador = '1' # Local = 1, Visitante = 2, Empate = x
  
  if goles_local > goles_visitante:
    ganador = '1'
  else:
    if goles_local < goles_visitante:
      ganador = '2'
    else:
      ganador = 'x'

  return goles_local, goles_visitante, ganador  

