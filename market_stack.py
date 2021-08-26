from sensitive import api_key

import requests

# Error Codes
# 401	invalid_access_key	An invalid API access key was supplied.
# 401	missing_access_key	No API access key was supplied.
# 401	inactive_user	The given user account is inactive.
# 403	https_access_restricted	HTTPS access is not supported on the current subscription plan.
# 403	function_access_restricted	The given API endpoint is not supported on the current subscription plan.
# 404	invalid_api_function	The given API endpoint does not exist.
# 404	404_not_found	Resource not found.
# 429	usage_limit_reached	The given user account has reached its monthly allowed request volume.
# 429	rate_limit_reached	The given user account has reached the rate limit.
# 500	internal_error	An internal error occurred.


class MarketStack:
    def __init__(self, ticker):
        self.ticker = ticker.upper().strip()

        self.api_key = api_key

    def latest_end_of_day_data(self):
        try:
            params = {
                'access_key': self.api_key
            }
            api_result = requests.get(
                f'https://api.marketstack.com/v1/tickers/{self.ticker}/eod/latest', params)

            api_response = api_result.json()
            print(api_response)
            return api_response
        except Exception as e:
            print(api_result.status_code)
            print(e)

    def ticker_information(self):
        """
        Obtain information about a specific ticker symbol by attach it to your API request.
        """
        try:
            params = {
                'access_key': self.api_key
            }
            api_request = requests.get(
                f"https://api.marketstack.com/v1/tickers/{self.ticker}", params)
            api_response = api_request.json()
            print(api_response)
            return api_response
        except Exception as e:
            print(e)

    def ticker_information_eod(self):
        """
        Obtain end-of-day data for a specific stock ticker. This route supports parameters of the End-of-day Data endpoint.
        """
        try:
            params = {
                'access_key': self.api_key
            }
            api_request = requests.get(
                f"https://api.marketstack.com/v1/tickers/{self.ticker}/eod", params)
            api_response = api_request.json()
            data = api_response["data"]
            print(data)
            return data
        except Exception as e:
            print(e)

    def ticker_information_eod_specific_date(self, date):
        """
        Specify a date in YYYY-MM-DD format. You can also specify an exact time in ISO-8601 date format, e.g. 2020-05-21T00:00:00+0000.
        """
        try:
            params = {
                'access_key': self.api_key
            }
            api_request = requests.get(
                f"https://api.marketstack.com/v1/tickers/{self.ticker}/eod/{date}", params)
            api_response = api_request.json()
            print(api_response)
            return api_response
        except Exception as e:
            print(e)

    def ticker_information_eod_latest(self):
        """
        Specify a date in YYYY-MM-DD format. You can also specify an exact time in ISO-8601 date format, e.g. 2020-05-21T00:00:00+0000.
        """
        try:
            params = {
                'access_key': self.api_key
            }
            api_request = requests.get(
                f"https://api.marketstack.com/v1/tickers/{self.ticker}/eod/latest", params)
            api_response = api_request.json()
            print(api_response)
            return api_response
        except Exception as e:
            print(e)

    def ticker_information_splits(self, limit=100):
        """
       Obtain end-of-day data for a specific stock ticker (splits). This route supports parameters like date period date_from and date_to and also you can sort the results DESC or ASC.
       limit = [Optional] Specify a pagination limit (number of results per page) for your API request. Default limit value is 100, maximum allowed limit value is 1000.
        """
        try:
            params = {
                'access_key': self.api_key,
                "limit": limit
            }
            api_request = requests.get(
                f"https://api.marketstack.com/v1/tickers/{self.ticker}/splits", params)
            api_response = api_request.json()
            data = api_response["data"]
            print(data)
            return data
        except Exception as e:
            print(e)

    def ticker_information_intraday(self, interval, limit=100):
        """
       Obtain real-time & intraday data for a specific stock ticker (intraday). This route supports parameters of the Intraday Data endpoint.
       interval = [Optional] Specify your preferred data interval. Available values: 1min, 5min, 10min, 15min, 30min, 1hour (Default), 3hour, 6hour, 12hour and 24hour.
       limit = [Optional] Specify a pagination limit (number of results per page) for your API request. Default limit value is 100, maximum allowed limit value is 1000.
        """
        try:
            params = {
                'access_key': self.api_key,
                "interval": interval
            }
            api_request = requests.get(
                f"https://api.marketstack.com/v1/tickers/{self.ticker}/intraday", params)
            api_response = api_request.json()
            data = api_response["data"]
            intraday = data["intraday"]
            print(intraday)
            return intraday
        except Exception as e:
            print(e)

    def ticker_information_intraday_latest(self, interval, limit=100):
        """
       Obtain real-time & intraday data for a specific stock ticker (intraday latest). This route supports parameters of the Intraday Data endpoint.
       interval = [Optional] Specify your preferred data interval. Available values: 1min, 5min, 10min, 15min, 30min, 1hour (Default), 3hour, 6hour, 12hour and 24hour.
       limit = [Optional] Specify a pagination limit (number of results per page) for your API request. Default limit value is 100, maximum allowed limit value is 1000.
        """
        try:
            params = {
                'access_key': self.api_key,
                "interval": interval,
                "limit": limit
            }
            api_request = requests.get(
                f"https://api.marketstack.com/v1/tickers/{self.ticker}/intraday/latest", params)
            api_response = api_request.json()
            print(api_response)
            return api_response
        except Exception as e:
            print(e)

    def market_indices(self):
        """
        Obtain end of day data for NDX and DJI
        """
        try:
            params = {
                'access_key': self.api_key
            }
            api_request = requests.get(
                f"https://api.marketstack.com/v1/tickers/NDX.INDX/eod", params)
            api_response = api_request.json()
            nasdaq_data = api_response["data"]

            api_request = requests.get(
                f"https://api.marketstack.com/v1/tickers/DJI.INDX/eod", params)
            api_response = api_request.json()
            dow_data = api_response["data"]
            return_object = {"nasdaq_data": nasdaq_data,
                             "dow_data": dow_data}
            return return_object
        except Exception as e:
            print(e)

    def exchanges(self):
        """
        Using the exchanges API endpoint you will be able to look up information any of the 70+ stock exchanges.
        """
        try:
            params = {
                'access_key': self.api_key
            }
            api_request = requests.get(
                "https://api.marketstack.com/v1/exchanges", params)
            api_response = api_request.json()
            print(api_response)
            return api_response
        except Exception as e:
            print(e)

    def exchanges_specific(self, mic):
        """
        Obtain information about a specific stock exchange by attaching its MIC identification.
        """
        try:
            params = {
                'access_key': self.api_key
            }
            mic = mic.upper()
            api_request = requests.get(
                f"https://api.marketstack.com/v1/exchanges/{mic}", params)
            api_response = api_request.json()
            print(api_response)
            return(api_response)
        except Exception as e:
            print(e)

    def exchanges_tickers(self, mic):
        """
        Obtain all available tickers for a specific exchange by attaching the exchange MIC.
        """
        try:
            params = {
                'access_key': self.api_key
            }
            mic = mic.upper()
            api_request = requests.get(
                f"https://api.marketstack.com/v1/exchanges/{mic}/tickers", params)
            api_response = api_request.json()
            print(api_response)
            return(api_response)
        except Exception as e:
            print(e)

    def exchanges_eod(self, mic):
        """
        Obtain end-of-day data for all available tickers from a specific exchange. For parameters, refer to End-of-day Data endpoint.
        """
        try:
            params = {
                'access_key': self.api_key
            }
            mic = mic.upper()
            api_request = requests.get(
                f"https://api.marketstack.com/v1/exchanges/{mic}/eod", params)
            api_response = api_request.json()
            print(api_response)
            return(api_response)
        except Exception as e:
            print(e)

    def exchanges_intraday(self, mic):
        """
        Obtain intraday data for tickers from a specific exchange. For parameters, refer to Intraday Data endpoint.
        """
        try:
            params = {
                'access_key': self.api_key
            }
            mic = mic.upper()
            api_request = requests.get(
                f"https://api.marketstack.com/v1/exchanges/{mic}/intraday", params)
            api_response = api_request.json()
            print(api_response)
            return(api_response)
        except Exception as e:
            print(e)

    def exchanges_eod_latest(self, mic):
        """
        Obtain the latest end-of-day data for tickers of the given exchange.
        """
        try:
            params = {
                'access_key': self.api_key
            }
            mic = mic.upper()
            api_request = requests.get(
                f"https://api.marketstack.com/v1/exchanges/{mic}/eod/latest", params)
            api_response = api_request.json()
            print(api_response)
            return(api_response)
        except Exception as e:
            print(e)

    def exchanges_intraday_latest(self, mic):
        """
        Obtain the latest intraday data for tickers of the given exchange.
        """
        try:
            params = {
                'access_key': self.api_key
            }
            mic = mic.upper()
            api_request = requests.get(
                f"https://api.marketstack.com/v1/exchanges/{mic}/intraday/latest", params)
            api_response = api_request.json()
            print(api_response)
            return(api_response)
        except Exception as e:
            print(e)

    def timezones(self):
        """
        Using the timezones API endpoint you will be able to look up information about all supported timezones.
        """
        try:
            params = {
                "access_key": self.api_key
            }

            api_request = requests.get(
                "https://api.marketstack.com/v1/timezones", params)

            api_response = api_request.json()
            return api_response
        except Exception as e:
            print(e)


if __name__ == '__main__':
    print("market_stack.py file executed")
