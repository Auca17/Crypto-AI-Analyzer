import requests
from fastapi import FastAPI
from dotenv import load_dotenv
import os
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Crypto AI Analyzer running"}

@app.get("/crypto")
def get_crypto(symbol: str):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd&include_24hr_change=true&include_24hr_vol=true"
    response = requests.get(url)
    data = response.json()
    return {
        "symbol": symbol,
        "price": data[symbol]["usd"],
        "volume_24h": data[symbol]["usd_24h_vol"],
        "change_24h": data[symbol]["usd_24h_change"],
    }
