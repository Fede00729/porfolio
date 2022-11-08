import pandas as pd
import requests, json, time, csv
from datetime import date

# Importo el listado generado antes.
listado = pd.read_csv('listado.csv')

# Fecha del dia y nombre del archivo donde guardara las consultas.
today = str(date.today())
daily_csv = f'origin_tickets/origin_tickets_{today}.csv'

# Datos de la API para armar la query.
symbol = []
for ticket in listado['Ticker  en  mercado  de  origen']:
  symbol.append(ticket)
function = "GLOBAL_QUOTE"
with open('api_key.txt') as f:
    key = f.readlines()
type_data = "json"

# Se consulta a la API. Son 5 consultas por minuto.
executions = 0
count = 0
for ticket in symbol:
  url = f'https://www.alphavantage.co/query?function={function}&symbol={ticket}&apikey={key}&datatype={type_data}'
  response = requests.get(url)
  ticket_info = json.loads(response.text)
  time.sleep(3)     # Se agrega timer para evitar perder consutlas.

  for a in ticket_info:
    print(ticket_info[a])
    if executions == 0:
      headers = []
      for b, c in ticket_info[a].items():
        headers.append(b)
  with open(daily_csv, 'a') as f_object: 
    writer = csv.DictWriter(f_object, delimiter=',', fieldnames=headers)
    if executions == 0:
      writer.writeheader()
    writer.writerow(ticket_info[a]) 
    f_object.close()
  executions = executions +1
  count = count +1

  if count == 5:
    print('Waiting 60 sec...')
    count = 0
    time.sleep(65)  # Timer para empezar siguientes 5 consultas.
    continue