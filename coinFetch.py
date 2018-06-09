from crypto_news_api import CryptoControlAPI

api = CryptoControlAPI("c1aa1e963a46da33d9889161fc85ddf3")

# print(api.getTopNews())
# print(api.getTopNewsByCoin("bitcoin"))

art = api.getLatestNewsByCoin('bitcoin')
print(art)

for article in art:
	print(article)
	print("\n")