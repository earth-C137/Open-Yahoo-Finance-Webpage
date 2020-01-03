import webbrowser


def yahoo_finance_profile(ticker):
        webpage = "https://finance.yahoo.com/quote/{}/profile?p={}".format(ticker, ticker)
        webbrowser.open(webpage, autoraise=True)

if __name__ == '__main__':
    list = ['AMZN', 'BA']
    for each in list:
        yahoo_finance_profile(each)
