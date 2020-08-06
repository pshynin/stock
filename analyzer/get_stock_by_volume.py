import yfinance as yf


# data = yf.download("KODK", "2020-07-23", "2020-07-29")
# print(data)

def get_volume(tickets):
    index = yf.Ticker(tickets)
    history = index.history("1mo", "1d", "2020-07-23", "2020-07-29")
    return dict(history)['Volume']


print(get_volume('KODK'))
