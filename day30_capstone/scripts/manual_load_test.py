import requests
from concurrent.futures import ThreadPoolExecutor

URL = "http://127.0.0.1:8000/recommend/1"

def hit():
    return requests.get(URL).status_code

with ThreadPoolExecutor(max_workers=10) as executor:
    results = list(executor.map(lambda _: hit(), range(10)))

print("Successful requests:", results.count(200))