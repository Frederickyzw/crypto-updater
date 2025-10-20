import requests
import pandas as pd
from datetime import datetime

def fetch_crypto(symbol="BTC", currency="USDT", limit=1440):
    url = f"https://min-api.cryptocompare.com/data/v2/histominute?fsym={symbol}&tsym={currency}&limit={limit}"
    r = requests.get(url)
    data = r.json()
    if data["Response"] != "Success":
        raise Exception("Failed to fetch data:", data)

    df = pd.DataFrame(data["Data"]["Data"])
    df["time"] = pd.to_datetime(df["time"], unit="s")
    return df

def save_csv():
    df = fetch_crypto(symbol="BTC", currency="USDT", limit=1440)  # 1 hari data per menit
    df.to_csv("data/crypto_data.csv", index=False)
    print(f"[{datetime.now()}] Data updated and saved to crypto_data.csv")

if __name__ == "__main__":
    save_csv()