import requests
from datetime import date

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    data = response.json()
    quote = data[0]['q']
    author = data[0]['a']
    return quote, author

def save_quote(quote, author):
    today = date.today()
    with open("quotes_log.text", "a") as f:
        f.write(f"{today} - {quote} - {author}\n")

def main():
    quote, author = get_quote()
    print(f"\n📖 Quote of the Day:\n\n'{quote}'\n— {author}\n")
    save_quote(quote, author)
    print("✅ quote saved to quotes_log.text")

main()    