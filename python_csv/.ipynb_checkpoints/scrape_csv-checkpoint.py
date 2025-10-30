# scrape_csv.py
# Scrapes an example CSV from Wikipedia and saves + verifies it

import requests
from bs4 import BeautifulSoup
import pandas as pd
import io

URL = "https://en.wikipedia.org/wiki/Delimiter-separated_values"
OUT_CSV = "wikipedia_example.csv"
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

def looks_like_csv(text: str) -> bool:
    text = text.replace("\r", "")
    return ("," in text) and ("\n" in text)

resp = requests.get(URL, timeout=30, headers=HEADERS)
resp.raise_for_status()

soup = BeautifulSoup(resp.text, "html.parser")

# --- Find <pre> blocks that look like CSV ---
candidates = []
for pre in soup.find_all("pre"):
    t = pre.get_text()
    if looks_like_csv(t):
        lines = [ln for ln in t.split("\n") if ln.strip()]
        if len(lines) >= 2:
            candidates.append("\n".join(lines))

if not candidates:
    raise RuntimeError("No CSV-like <pre> block found on the page.")

csv_text = candidates[0]

# --- Save to CSV file ---
with open(OUT_CSV, "w", encoding="utf-8", newline="") as f:
    f.write(csv_text)

print(f"✅ Saved CSV to: {OUT_CSV}")

# --- Verify by loading it with pandas ---
df = pd.read_csv(io.StringIO(csv_text))
print("✅ Successfully read CSV into DataFrame:")
print(df.head())
