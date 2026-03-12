# AI Crypto Market Explainer

A web app that fetches real-time cryptocurrency data and uses AI to explain the numbers in plain human language.

Built with **FastAPI** (Python backend) + **CoinGecko API** (market data) + **Groq / Llama 3** (AI explanations).

---

## What it does

- Type a crypto symbol like `BTC`, `ETH`, or `SOL`
- Get the current price, 24h change, and trading volume
- The AI explains what those numbers mean in simple language
- See a sentiment badge: Bullish / Neutral / Bearish
- Compare two coins side by side with an AI analysis
- Search history tracks everything you checked this session

---

## Preview

```
Symbol:  BTC
Price:   $70,374
Change:  ▲ 1.47%   [🟢 Bullish]

"Bitcoin is showing moderate bullish momentum. The high trading volume
of $45B suggests strong market interest, which could indicate continued
positive movement in the short term..."
```

---

## Setup

### 1. Clone the project

```bash
git clone https://github.com/your-username/crypto-ai-analyzer.git
cd crypto-ai-analyzer
```

### 2. Create a virtual environment

```powershell
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

### 4. Get your free Groq API key

> ⚠️ The API key is NOT included in this repo. Each user needs their own — it's free.

1. Go to [https://console.groq.com](https://console.groq.com)
2. Sign up for a free account
3. Go to **API Keys** and create a new key
4. Copy the key

### 5. Create your `.env` file

Create a file called `.env` in the project root with this content:

```
GROQ_API_KEY=paste_your_key_here
```

> The `.env` file is listed in `.gitignore` — it will never be uploaded to GitHub.

### 6. Run the app

```powershell
uvicorn main:app --reload
```

Open your browser and go to:
```
http://localhost:8000
```

---

## Supported coins

| Symbol | Name |
|--------|------|
| BTC | Bitcoin |
| ETH | Ethereum |
| SOL | Solana |
| BNB | BNB |
| XRP | XRP |
| ADA | Cardano |
| DOGE | Dogecoin |

---

## Project structure

```
crypto-ai-analyzer/
├── main.py              # FastAPI backend — all endpoints
├── static/
│   └── index.html       # Frontend — UI, styles, JavaScript
├── .env                 # Your secret API key (never share this)
├── .gitignore           # Tells Git to ignore .env
├── requirements.txt     # All Python dependencies
└── README.md
```

---

## API endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Opens the web UI |
| GET | `/crypto?symbol=BTC` | Returns raw market data |
| GET | `/crypto/explain?symbol=BTC` | Returns AI explanation |
| GET | `/crypto/compare?symbol1=BTC&symbol2=ETH` | Compares two coins with AI |

---

## Want to contribute or extend it?

Some ideas to keep building:

- Add more coins to `SYMBOL_MAP` in `main.py`
- Add a 7-day price chart using a charting library
- Add a price alert feature
- Translate the AI response to different languages

---

## Tech stack

- [FastAPI](https://fastapi.tiangolo.com/) — Python web framework
- [CoinGecko API](https://www.coingecko.com/en/api) — Free crypto market data
- [Groq](https://console.groq.com) — Free AI inference (Llama 3)
- [python-dotenv](https://pypi.org/project/python-dotenv/) — Environment variable management
