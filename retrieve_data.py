import click
import pandas as pd
from datetime import date, timedelta, datetime
from binance import Client

@click.command()
@click.option('--num_assets', default=5, help='Enter the number of assets to return',type=int)
@click.option('--day', default=None, help='Enter the reference date from which data will be retrieved in YYYY-MM-DD format. Otherwise today will be taken.',type=str)
@click.option('--look_back', default=30, help='Days to look back from refereence date',type=int)
def get_binance_data(num_assets, day = None, look_back = 0):
    """ 
    Obtains historic data from a list of assets using Binance's API and stores it on a CSV file under data folder
    """
    client = Client()
    info = client.get_all_tickers()
    print(info)
    
    # Time frame
    if day:
        today = datetime.strptime(day, '%Y-%m-%d') - timedelta(days=look_back)
    else:
        today = date.today() - timedelta(days=look_back)
    yearago = today.replace(year = today.year -1).strftime("%Y.%m.%d")
    today = today.strftime("%Y.%m.%d")
    timeframe="1d"

    # Main dataframe structure
    df = pd.DataFrame(columns=["Asset","Open time","Open","High","Low","Close","Volume", "Closing time","Quote asset vol", "Num traders", "Taker buy base asset vol", "Taker buy quote asset vol","To be ignored"])

    # Iterate for each asset
    an = 0
    for tick in info:
        asset = tick["symbol"]
        # We will filter the assets to work with
        if an < num_assets:
            data = client.get_historical_klines(asset, timeframe, yearago, today)
            if len(data) >= 365:
                df_tmp = pd.DataFrame(data, columns=["Open time","Open","High","Low","Close","Volume", "Closing time","Quote asset vol", "Num traders", "Taker buy base asset vol", "Taker buy quote asset vol","To be ignored"])
                df_tmp["Asset"] = asset
                df = pd.concat([df, df_tmp])
                an += 1
        else:
            break

    # Write to file under data folder     
    df.to_csv("data/binance_data.csv")

# Entrypoint
if __name__ == "__main__":
    get_binance_data()