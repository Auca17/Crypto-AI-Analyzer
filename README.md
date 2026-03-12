# AI Crypto Market Explainer

A crypto analysis web app that combines live CoinGecko market data with AI-generated explanations so non-traders can understand what the numbers actually mean.

Built with FastAPI on the backend and a lightweight HTML, CSS, and JavaScript frontend.

## Features

- Live crypto market snapshots for supported coins
- AI-generated beginner-friendly explanations
- Compare two coins with an AI summary
- Sentiment badge based on 24-hour movement
- Search history for the current browser session
- Polished dashboard UI with loading and error states
- Short backend cache to reduce repeated CoinGecko calls
- Graceful fallback text if Groq is unavailable

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

## How it works

1. The user enters a symbol like `BTC` or compares `BTC` vs `ETH`.
2. The backend fetches live price, volume, and 24-hour change from CoinGecko.
3. The app sends a short market prompt to Groq using Llama 3.
4. The UI shows structured stats, a sentiment label, and a plain-language explanation.

## Setup

### 1. Clone the project

```bash
git clone https://github.com/your-username/crypto-ai-analyzer.git
cd crypto-ai-analyzer
```

### 2. Create and activate a virtual environment

```powershell
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

### 4. Optional: add your Groq API key

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Important:
The API key is not included in the repo and should never be shared publicly.

If you do not add a Groq key:
The project still runs. Market data will still work, and the backend will return a fallback explanation instead of a Groq-generated one.

If someone else clones your project:
They can either add their own Groq key or run the app without one and use the fallback summaries.

### 5. Run the app

```powershell
uvicorn main:app --reload
```

Open:

```text
http://localhost:8000
```

## API endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Opens the main dashboard |
| GET | `/crypto?symbol=BTC` | Returns market data for one coin |
| GET | `/crypto/explain?symbol=BTC` | Returns an explanation for one coin |
| GET | `/crypto/compare?symbol1=BTC&symbol2=ETH` | Returns two market payloads plus an AI comparison |

## Project structure

```text
crypto-ai-analyzer/
├── main.py
├── static/
│   └── index.html
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## Main dependencies

- `fastapi` for the backend API
- `uvicorn` as the ASGI server
- `requests` for CoinGecko requests
- `groq` for AI completions
- `python-dotenv` for loading `.env` values
