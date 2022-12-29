import urllib.request
import json
import pymysql
from diputado import Diputado

conn = pymysql.connect(
    host='localhost',
    user='//', #Ingresar user de su DB
    password='//', #Ingresar pass de su DB
    db='diputados',
)

cursor = conn.cursor()

solicita = urllib.request.Request(
    '', #Completar con url del json
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)

respuesta = urllib.request.urlopen(solicita)

bodyrespuesta = respuesta.read()
jsonRespuesta = json.loads(bodyrespuesta.decode("utf-8"))
print('\n')
print('Lista de Entrada')
for entrada in jsonRespuesta:
    print(
        f'Nombre: {entrada["nombre"]}\n' # Completar con n Entradas
    )

for jsEntrada in jsonRespuesta:
    strEntrada = json.dumps(jsEntrada)
    jl = json.loads(strEntrada)
    dbEntrada = Entrada(**jl)

    query = 'insert into tabla () values (%s)'
    data = (
        dbEntrada.nombre, #n Entradas
    )
    cursor.execute(query, data)
    conn.commit()

print('\n')
print('LA BASE DE DATOS HA SIDO CARGADA SATISFACTORIAMENTE')

cursor.close()
conn.close()