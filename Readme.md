# Readme Cedears

### Objetivo
- *Analizar precios* de Cedears *y* su acción correspondiente para evaluar *posible arbitraje*.

### Método de obtención de datos
- Se extrae el listado de tickers de origen y de bolsa de buenos aires con su ratio de equivalencia.
- Con tickers de origen se utiliza la API de *Alpha-Vantage* para conseguir las cotizaciones. (demora 72min)
- Con tickers locales se extraen los *json* de panel de bolsa de buenos aires.
