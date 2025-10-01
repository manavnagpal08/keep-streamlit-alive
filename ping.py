import requests

URLS = [
    "https://candidate-screeneerpro.streamlit.app/",
    "https://screenerpro.streamlit.app/"
]

def ping():
    for url in URLS:
        try:
            resp = requests.get(url)
            print(f"Pinged {url}, status: {resp.status_code}")
        except Exception as e:
            print(f"Error pinging {url}: {e}")

if __name__ == "__main__":
    ping()
