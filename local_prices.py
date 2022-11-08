from urllib.request import Request, urlopen
import pandas as pd
import json
from datetime import date

# Fecha del dia y nombre del archivo donde guardara las consultas.
today = str(date.today())
arg_daily_csv = f'arg_tickets/arg_tickets_{today}.csv'

req = Request(
    url='https://www.byma.com.ar/wp-admin/admin-ajax.php?action=get_panel&panel_id=5', 
    headers={'User-Agent': 'Mozilla/5.0'}
)
webpage = urlopen(req).read()
data = json.loads(webpage)

table = pd.DataFrame(data['Cotizaciones'])
table.to_csv(arg_daily_csv, index=False, sep=',')