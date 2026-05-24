from concurrent.futures import ThreadPoolExecutor, as_completed
from indicators import get_data, add_indicators
from scoring import score_stock
from universe import get_universe
from cache import get_cache, set_cache, init_db
import pandas as pd

init_db()

def scan_one(symbol):

    cached = get_cache(symbol)
    if cached:
        score, _ = cached
        return {"symbol": symbol, "score": score, "cached": True}

    try:
        df = get_data(symbol)
        if df is None or len(df) < 50:
            return None

        df = add_indicators(df)
        score = score_stock(df)

        set_cache(symbol, score, "data")

        return {
            "symbol": symbol,
            "score": score,
            "cached": False
        }

    except:
        return None


def run_full_scan(limit=None):

    universe = get_universe()

    if limit:
        universe = universe[:limit]

    results = []

    with ThreadPoolExecutor(max_workers=15) as ex:
        futures = [ex.submit(scan_one, s) for s in universe]

        for f in as_completed(futures):
            r = f.result()
            if r:
                results.append(r)

    return sorted(results, key=lambda x: x["score"], reverse=True)
