import requests
query=input("what news do you want to search for?")
print("press ctr key and click the link to get the news ")
api="97d3a6982dff497a838e69f6d02a57c8"



url=f"https://newsapi.org/v2/everything?q={query}&from=2025-04-30&sortBy=publishedAt&apiKey={api}"
print(url)

response=requests.get(url)
data=response.json()
articles=data["articles"]
for article in articles:

    print(article["title"],article["url"])
    print("\n*****************************\n")