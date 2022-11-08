## Objetive
- Analyze the prices of Argentine Cedears and their equivalent share to detect a possible arbitrage due to the dollar price.                    
> **Note:** Cedears are instruments that are equivalent to major world shares. Cedear ratios indicate how many cedears are needed to equal one share.

## Process

1. Run **[listado.ipynb](https://github.com/Fede00729/Cedears/blob/main/Listado.ipynb "listado.ipynb")**, a table of stock and cedear tickers is generated with their equivalence ratio.                    
**listado.csv** is created.

2. **[api_consult.ipynb](https://github.com/Fede00729/Cedears/blob/main/api_consult.ipynb "api_consult.ipynb")** is run using the Alpha-Vantage API and the stock tickers from **listado.csv** to get the stock quotes.                    
**origin_tickets/origin_tickets_date.csv** is created.

3. **[local_prices.ipynb](https://github.com/Fede00729/Cedears/blob/main/local_prices.ipynb "local_prices.ipynb")** is executed using the tickers of the cedears of **listado.csv** to extract the prices of the cedears that are loaded through json in the Buenos Aires stock exchange panel.                    
**arg_tickets/arg_tickets_date.csv** is created.

4. **[data_union.ipynb](https://github.com/Fede00729/Cedears/blob/main/data_union.ipynb "data_union.ipynb")** is executed to merge the data of the 3 dataframes generated previously, calculate the values of the cedears according to their ratios, calculate the dollar quotes for each cedear and graph to show the best opportunities for arbitration.

[![](https://i.imgur.com/xEXhSQ6.png)](https://i.imgur.com/xEXhSQ6.png)
