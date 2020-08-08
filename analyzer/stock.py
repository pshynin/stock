import os.path

import yfinance as yf

from ..notification.telegram import Telegram


class Stock:
    history: dict

    def __init__(self, token: str, period: str, interval: str, start: str, end: str):
        index = yf.Ticker(token)
        self.history = dict(index.history(period, interval, start, end))

    def get_volume(self):
        return self.history['Volume']


def main():
    volume = Stock('KODK', "1mo", "1d", "2020-07-23", "2020-07-29").get_volume()
    token = os.environ.get("TELEGRAM_TOKEN")
    notifier = Telegram(token, parse_mode="HTML")
    notifier.send(volume)

    print(volume)


if __name__ == '__main__':
    main()
