# Malaysian Fruits

A small web app built with Python FastAPI. It serves a main page that introduces five local Malaysian fruits (Durian, Mangosteen, Rambutan, Starfruit and Pulasan), along with its static assets and a JSON API.

## User Guide

### Requirements

- Python 3.9 or later
- pip

### Installation

```
pip install -r requirements.txt
```

### Running the app

```
python main.py
```

Or run uvicorn directly:

```
python -m uvicorn main:app --reload
```

Then open <http://127.0.0.1:8000> in your browser. Press `Ctrl+C` in the terminal to stop the server.

### Using the main page

The main page shows one card per fruit, with its emoji, English and Malay names, tagline, description and season. The cards are loaded from the API when the page opens.

### API endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/` | Main page |
| GET | `/api/fruits` | List all five fruits as JSON |
| GET | `/api/fruits/{name}/description` | Description of one fruit (name is case-insensitive) |
| GET | `/static/...` | Static assets (CSS, JavaScript) |
| GET | `/docs` | Interactive API documentation (Swagger UI) |

Example:

```
curl http://127.0.0.1:8000/api/fruits/durian/description
```

```json
{"name": "Durian", "description": "Famous for its spiky husk and strong aroma, ..."}
```

An unknown fruit name returns HTTP 404 with `{"detail": "Fruit 'apple' not found"}`.

### Project structure

```
main.py            FastAPI app, fruit data and routes
static/index.html  Main page
static/style.css   Styles
static/app.js      Fetches fruits and renders the cards
requirements.txt   Python dependencies
```

### Customising

Edit the `FRUITS` list in `main.py` to change, add or remove fruits. The page and API update after a restart (or automatically when run with `--reload`).

### Troubleshooting

- **Port 8000 already in use:** run `python -m uvicorn main:app --port 8001` and open that port instead.
- **"Could not load fruits." on the page:** make sure the server is running and open the page through the server URL, not by double-clicking `index.html`.