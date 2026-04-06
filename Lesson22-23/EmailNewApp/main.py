import requests
from send_email import send_email
api_key = "8d3a6b4394584d1683aa107621068d3e"
topic = "tesla"
url = f"https://newsapi.org/v2/everything?q={topic}&from=2026-03-06&sortBy=publishedAt&language=en&apiKey={api_key}"

request = requests.get(url)
content = request.json()
print(content["articles"])
subject = "Subject: Today's news" + "\n"
body = ""
for article in content["articles"][:10]:
    if article["title"] is not None:
        body =  body + article["title"] + "\n" + article["description"] + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
subject = subject.encode("utf-8")
message = subject + body
send_email(message)