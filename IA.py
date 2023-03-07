from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

import seaborn as sns
import numpy as np
import pandas as pd
import xgboost as xgb
    
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
    
    # Transformamos el dia de la semana a seno y coseno ya que es un datos ciclico
    dato['weekday_sin'] = np.sin(dato['weekday']*(2.*np.pi/7))
    dato['weekday_cos'] = np.cos(dato['weekday']*(2.*np.pi/7))
    
    # Separamos los datos en variables independientes y dependientes
    columns_name=['weekday_sin','weekday_cos','categorical Home','categorical Away']
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
    


def crear_prediccion(prediccion, modelo, lb_make_outs, team_name):
    df = prediccion.copy()
    df.Date = pd.to_datetime(df.Date, dayfirst=True)
    df['weekday'] = df.Date.dt.weekday #se puede acceder a la fecha
    df['weekday_sin'] = np.sin(df['weekday']*(2.*np.pi/7))
    df['weekday_cos'] = np.cos(df['weekday']*(2.*np.pi/7))
    df['categorical Home'] = df.HomeTeam.apply(lambda x: team_name[x])
    df['categorical Away'] = df.AwayTeam.apply(lambda x: team_name[x])
    cols = ['weekday_sin', 'weekday_cos', 'categorical Home', 'categorical Away']
    predictions = modelo.predict(df[cols])
    return lb_make_outs.inverse_transform(predictions)


def informacion_dataframe():
    dato = pd.read_csv('./Datos/prediccion/LaLiga_Matches_1995-2021.csv')
    
    num_partidos = dato.shape[0]
    num_local = len(dato[dato.FTR == 'H'])
    num_empate = len(dato[dato.FTR == 'D'])
    num_visitante = len(dato[dato.FTR == 'A'])
    
    return num_partidos, num_local, num_empate, num_visitante
    