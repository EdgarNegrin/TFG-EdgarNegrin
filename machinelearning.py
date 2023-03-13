'''
Universidad de la Laguna
Proyecto: Footdata
Autor: Edgar Negrín Gonzalez
Email: alu0101210964@ull.edu.es
Fichero: machinelearning.py: Este fichero contiene la
implementación de las funciones necesarias para crear el modelo de predicción
'''

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

import numpy as np
import pandas as pd
import xgboost as xgb


#
# Descripcion: Esta función se encarga de crear el modelo de predicción
# Parametros: 
# Return: model(XGBClassifier): Modelo de predicción, lb_make_outs(LabelEncoder): Codificador de resultados, equipos_nombre(dict): Diccionario con los equipos, precicion(float): Precisión del modelo
#
def crear_modelo():
    dato = pd.read_csv('./Datos/prediccion/LaLiga_Matches_1995-2021.csv')
    
    # Creamos un diccionario con los equipos
    equipos_nombre = {}
    index = 0
    for idx, row in dato.iterrows():
        name = row['HomeTeam']
        if(name not in equipos_nombre.keys()):
            equipos_nombre[name] = index
            index += 1
        name = row['AwayTeam']
        if(name not in equipos_nombre.keys()):
            equipos_nombre[name] = index
            index += 1
            
    # Asignamos un valor numerico a los equipos y los resultados
    lb_make_outs = LabelEncoder() 
    dato['categorical FTR'] = lb_make_outs.fit_transform(dato['FTR'])
    dato['categorical Home'] = dato.HomeTeam.apply(lambda x: equipos_nombre[x])
    dato['categorical Away'] = dato.AwayTeam.apply(lambda x: equipos_nombre[x])
    
    # Transformamos la fecha a un formato que pueda ser leido y extraemos el dia de la semana
    dato.Date = pd.to_datetime(dato.Date, dayfirst=True)
    dato['weekday'] = dato.Date.dt.weekday
    
    # Separamos los datos en variables independientes y dependientes
    columns_name=['weekday','categorical Home','categorical Away']
    X_all = dato
    y_all = dato['categorical FTR']
    
    # Separamos aleatoriamente los datos en entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split( X_all, y_all, test_size=0.2, random_state=53)

    # Creamos el modelo
    model = xgb.XGBClassifier(n_estimators=4, max_depth=4)
    model.fit(X_train[columns_name],y_train)
    
    # Evaluamos el modelo
    y_pred = model.predict(X_test[columns_name])
    precicion = np.mean(y_pred == y_test)
    
    return model, lb_make_outs, equipos_nombre, precicion
    

#
# Descripcion: Esta función se encarga de realizar una prediccion con el modelo
# Parametros: prediccion(DataFrame): DataFrame con los datos de la prediccion, modelo(XGBClassifier): Modelo de predicción, lb_make_outs(LabelEncoder): Codificador de resultados, team_name(dict): Diccionario con los equipos
# Return: resultado(array): Array con los resultados de la prediccion
#
def crear_prediccion(prediccion, modelo, lb_make_outs, team_name):
    df = prediccion.copy()
    df.Date = pd.to_datetime(df.Date, dayfirst=True)
    df['weekday'] = df.Date.dt.weekday
    df['categorical Home'] = df.HomeTeam.apply(lambda x: team_name[x])
    df['categorical Away'] = df.AwayTeam.apply(lambda x: team_name[x])
    cols = ['weekday', 'categorical Home', 'categorical Away']
    predictions = modelo.predict(df[cols])
    resultado = lb_make_outs.inverse_transform(predictions)
    return resultado


#
# Descripcion: Esta función se extrae la informacion del dataset
# Parametros: 
# Return: num_partidos(int): Numero de partidos, num_local(int): Numero de partidos ganados por el equipo local, num_empate(int): Numero de partidos empatados, num_visitante(int): Numero de partidos ganados por el equipo visitante
#
def informacion_dataframe():
    dato = pd.read_csv('./Datos/prediccion/LaLiga_Matches_1995-2021.csv')
    
    num_partidos = dato.shape[0]
    num_local = len(dato[dato.FTR == 'H'])
    num_empate = len(dato[dato.FTR == 'D'])
    num_visitante = len(dato[dato.FTR == 'A'])
    
    return num_partidos, num_local, num_empate, num_visitante
    