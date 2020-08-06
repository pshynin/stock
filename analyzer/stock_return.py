#!/usr/bin/env python
import json
import os
from sqlalchemy import create_engine
import sys
import pickle
import yfinance as yf
from stocks import *
import yfinance as yf
def download():
    data = yf.download(" ".join(VALID_EQUITIES),
                       #"GLD VTI TLT IEF DBC GLD PG MSFT GOOGL NVDA SPY",
                       period="max",
                       interval="1mo",
                       group_by="ticker",
                       auto_adjust=False,
                       prepost=False,
                       threads=True,
                       proxy=None)
    data.to_pickle(DATA_FILE)
def get_eligible_equities():
    from portfolio import Portfolio
    df = get_df()
    valid_equities = []
    for stock in ALL_STOCKS:
        if Portfolio(df, [stock], [1.0], CUTOFF).is_valid_portfolio():
            print("Evaluating %s" % stock)
            valid_equities.append(stock)
    with open(VALID_EQUITIES_PATH, "w") as f:
        f.write(json.dumps(valid_equities))
    return valid_equities
if __name__ == "__main__":
    download()