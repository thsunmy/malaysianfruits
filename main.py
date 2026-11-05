from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

BASE_DIR = Path(__file__).parent
STATIC_DIR = BASE_DIR / "static"

app = FastAPI(title="Malaysian Fruits")

FRUITS = [
    {
        "name": "Durian",
        "local_name": "Durian",
        "emoji": "🟢",
        "tagline": "The King of Fruits",
        "description": "Famous for its spiky husk and strong aroma, durian has rich, creamy, "
        "custard-like flesh. Varieties such as Musang King and D24 are prized across Malaysia.",
        "season": "June – August, and December – February",
    },
    {
        "name": "Mangosteen",
        "local_name": "Manggis",
        "emoji": "🟣",
        "tagline": "The Queen of Fruits",
        "description": "A deep purple rind hides sweet, tangy white segments. Often eaten "
        "alongside durian, as it is traditionally believed to balance the durian's 'heatiness'.",
        "season": "June – September",
    },
    {
        "name": "Rambutan",
        "local_name": "Rambutan",
        "emoji": "🔴",
        "tagline": "The Hairy Fruit",
        "description": "Its name means 'hairy' in Malay. Peel the red, soft-spined skin to "
        "reveal a juicy, translucent, lychee-like fruit with a sweet and slightly sour taste.",
        "season": "June – October",
    },
    {
        "name": "Starfruit",
        "local_name": "Belimbing",
        "emoji": "⭐",
        "tagline": "Star-Shaped Refreshment",
        "description": "Slice it crosswise and you get perfect stars. Crisp, juicy and "
        "mildly tart, it is eaten fresh, juiced or dipped in a sweet-salty plum powder.",
        "season": "Year-round",
    },
    {
        "name": "Pulasan",
        "local_name": "Pulasan",
        "emoji": "🟤",
        "tagline": "The Sweeter Cousin of Rambutan",
        "description": "Related to rambutan but with shorter, thicker warts on its skin. "
        "The flesh is sweeter, less watery and clings less to the seed.",
        "season": "June – August",
    },
]


@app.get("/api/fruits")
def list_fruits():
    return FRUITS


@app.get("/", include_in_schema=False)
def index():
    return FileResponse(STATIC_DIR / "index.html")


app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
