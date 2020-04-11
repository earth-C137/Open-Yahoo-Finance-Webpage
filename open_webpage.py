"""
A simple module with three functions to open different yahoo finance web pages.
The argument is a stock ticker symbol passed in as a string.
"""

import webbrowser

def yahoo_finance_summary(ticker):
    webpage = "https://finance.yahoo.com/quote/{}?p={}&.tsrc=fin-srch".format(ticker, ticker)
    webbrowser.open(webpage, autoraise=True)

def yahoo_finance_profile(ticker):
    webpage = "https://finance.yahoo.com/quote/{}/profile?p={}".format(ticker, ticker)
    webbrowser.open(webpage, autoraise=True)

def yahoo_finance_options(ticker):
    webpage = "https://finance.yahoo.com/quote/{}/options?p={}".format(ticker, ticker)
    webbrowser.open(webpage, autoraise=True)

if __name__ == '__main__':
    #for example and to test
    list = ['AMZN', 'BA']
    for each in list:
        yahoo_finance_summary(each)

