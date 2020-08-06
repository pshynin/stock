import yfinance as yf

# data = yf.download("KODK", "2020-07-23", "2020-07-29")
# print(data)


index = yf.Ticker("KODK")
history = index.history("1mo", "1d", "2020-07-23", "2020-07-29")
volume = dict(history)['Volume']

print(volume)
