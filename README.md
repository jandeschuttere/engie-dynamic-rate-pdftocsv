# Engie Dynamic Rate PDF to CSV

At the time of writing Engie communicates its hourly dynamic rate through PDF and a publicly documented API was not identified. 
PDF is hard to integrate with in an automatic way, this tool is a very naive implementation into exposing the pricing information 
extracted from the PDF into a CSV allowing it to be used by whatever automation tool you desire to use.

Usage:
```bash
docker run --rm -ti -v $(pwd):/files jandeschuttere/engie-dynamic-rate-pdftocsv:latest /files/daily_prices_eSpot.pdf 
```

It is expected that the above command is run in the directory where the file "daily_prices_eSpot.pdf" is located which is the name of the PDF retrieved from [Engie](https://www.engie.be/api/engie/be/ms/pricing/v1/public/pricesHourlyPdf?document=SC_DYNAMIC_R_N_WEB202105&segment=R&language=N).
