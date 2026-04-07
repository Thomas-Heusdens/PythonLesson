import requests
from send_email import send_email
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("NEWS_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
topic = "business"
url = f"https://newsapi.org/v2/everything?q={topic}&from=2026-04-01&sortBy=publishedAt&language=en&apiKey={api_key}"

request = requests.get(url)
content = request.json()
articles = content["articles"]

model = init_chat_model(
    model="gemini-3-flash-preview",
    model_provider="google-genai",
    api_key=GOOGLE_API_KEY
)

prompt = f"""you're a news summarizer. Write me a short paragraph analyszing 
those news articles and write another one 
telling me how they affect the stock market.
Here are the news articles:
{articles}
"""
response = model.invoke(prompt)
response_str = response.content[0]["text"]

body = "Subject: News Summary\n\n" + response_str
body = body.encode("utf-8")

send_email(message=body)