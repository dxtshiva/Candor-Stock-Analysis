# from nsetools import Nse
# nse = Nse()
# try:
#     for i in range(50):
#         print(i)
#         q = nse.get_quote("sbin")
#         print(q["lastPrice"])
# except:
#     pass

# from rpy2.robjects.packages import importr
# from rpy2.robjects import pandas2ri
# from time import sleep
# pandas2ri.activate()
# r_nse = importr("nse2r")
# for i in range(50):
#     # print(r_nse.nse_stock_quote("sbin")[0])
#     print(r_nse.nse_index_quote())
#     sleep(2)

# import urllib.request, json
# import pprint
# print("Started")
# url = "https://www.nseindia.com/api/chart-databyindex"
# payloads = {"index":"AXISBANKEQN"}
# print("URL FOUND")
# response = urllib.request.urlopen(url)
# # data = json.loads(response.read())
# print("Data Fetched")
# data = response.read()
# pprint(data)

# import requests
# import pprint
# r = requests.get('https://api.github.com/events')
# print(r.text)
# payload = {'key1': 'value1', 'key2': ['value2', 'value3']}

# r = requests.get('https://httpbin.org/get', params=payload)
# print(r.url)

# import requests
# url = "https://www.nseindia.com/api/chart-databyindex"
# print("URL Fetched")
# payloads = {"index":"SBINEQN"}
# print("payload deployed")
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
# r = requests.get(url,params = payloads,headers=headers)
# print(r.url)
# print(r.text)
# print("done")

# import urllib.request
# url = 'https://www1.nseindia.com'
# r = urllib.request.urlopen(url)
# # print(r.text)
# print("done")
# # print(r.json())

# import requests
# url = "https://www1.nseindia.com/live_market/dynaContent/live_watch/equities_stock_watch.htm"
# print("URL Fetched")
# r = requests.get(url,timeout = 30)
# print(r.text)
# print("done")

# import requests
# import pandas as pd
# url = "https://www1.nseindia.com/homepage/Indices1.json"
# print("URL Fetched")
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
# r = requests.get(url,headers=headers)
# print(r.url)
# df = pd.DataFrame(r.json())
# data = [df["data"][i] for i in df["data"].keys()]
# for i in data:
#     print(i)

# import requests
# # url = "https://www.nseindia.com/api/quote-equity?symbol=SBIN"
# url = "https://www.nseindia.com/api/chart-databyindex?index=AXISBANKEQN"

# print("URL Fetched")
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
# r = requests.get(url,headers=headers)
# print(r.url)
# print(r.text)
# print("done")

# import requests
# # url = "https://www.nseindia.com/api/quote-equity?symbol=SBIN"
# url = "https://www.nseindia.com/api/chart-databyindex?index=AXISBANKEQN"

# print("URL Fetched")
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
#                          'like Gecko) '
#                          'Chrome/80.0.3987.149 Safari/537.36',
#            'accept-language': 'en,gu;q=0.9,hi;q=0.8', 'accept-encoding': 'gzip, deflate, br'}
# session = requests.Session()
# r = session.get(url,headers=headers)
# print(r.url)
# print(r.text)
# print("done")

# import pandas as pd
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
# options = Options()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get("https://www.nseindia.com/api/chart-databyindex")
# # html=driver.page_source
# # soup = BeautifulSoup(html,'html.parser')

# from selenium import webdriver
# from bs4 import BeautifulSoup
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# from time import sleep
# chrome_options = Options()
# # chrome_options.add_argument("--no-startup-window")
# # chrome_options.add_argument("headless")
# WINDOW_SIZE = "1920,1080"
# chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
# driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
# driver.get("https://www.nseindia.com/api/quote-equity?symbol=SBIN&section=trade_info")
# sleep(30)
# html=driver.page_source
# soup = BeautifulSoup(html,'html.parser')

# import requests
# url = "https://www1.nseindia.com/homepage/Indices1.json"

# print("URL Fetched")
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
#                          'like Gecko) '
#                          'Chrome/80.0.3987.149 Safari/537.36',
#            'accept-language': 'en,gu;q=0.9,hi;q=0.8', 'accept-encoding': 'gzip, deflate, br'}
# session = requests.Session()
# r = session.get(url,headers=headers)
# print(r.url)
# print(r.text)
# print("done")

# from urllib.request import urlopen
# url = "https://www1.nseindia.com/live_market/dynaContent/live_watch/get_quote/ajaxGetQuoteJSON.jsp?"
# payload = {"symbol":"SBIN","series":"EQ"}
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
#            'accept-language': 'en,gu;q=0.9,hi;q=0.8', 'accept-encoding': 'gzip, deflate, br'}
# res = urlopen(url, data = payload,timeout=30,headers=headers)
# print(res.read())

# import requests
# import pandas as pd
# url = "https://www1.nseindia.com/homepage/Indices1.json"
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
#            'accept-language': 'en,gu;q=0.9,hi;q=0.8', 'accept-encoding': 'gzip, deflate, br'}
# response = requests.get(url,headers=headers).json()
# data = pd.DataFrame(response['data'])
# data.drop(columns=['imgFileName'], inplace=True)
# print(data.columns)

# import pandas as pd
# url = "https://www1.nseindia.com/content/equities/EQUITY_L.csv"
# response = pd.read_csv(url)
# response.drop(list(response.columns[2:]),axis='columns',inplace=True)
# # data = pd.DataFrame(response)
# print(response)

# import yfinance as yf

# stock = yf.Ticker("SBIN.NS")
# # price = stock.info['regularMarketPrice']
# print(stock.info[0])

# from time import sleep
# import requests
# url = "https://www.nseindia.com/api/quote-equity?symbol=SBIN"
# headers  = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
#            'accept-language': 'en,gu;q=0.9,hi;q=0.8', 'accept-encoding': 'gzip, deflate, br'}
# for i in range(100):
#     response = requests.get(url, headers = headers).text
#     response = response[response.find('"lastPrice'):response.find(',"change"')]
#     print(response)
#     sleep(1)

# import requests
# from time import sleep
# import pandas as pd
# url  = 'https://query1.finance.yahoo.com/v8/finance/chart/HDFCBANK.NS'
# payloads = {
# 'region': 'US',
# 'lang': 'en-US',
# 'includePrePost': 'false',
# 'interval': '2m',
# 'useYfid': 'true',
# 'range': '1m',
# 'corsDomain': 'finance.yahoo.com',
# '.tsrc': 'finance'
# }
# headers  = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
#            'accept-language': 'en,gu;q=0.9,hi;q=0.8', 'accept-encoding': 'gzip, deflate, br'}

# for i in range(100):
#     response = requests.get(url, params = payloads,headers= headers).json()
#     data =  response['chart']['result'][0]['meta']['regularMarketPrice']
#     print(data)
#     # print(data['regularMarketPrice'])
#     sleep(1)

# import pandas as pd
# import requests
# url = "https://www1.nseindia.com/live_market/dynaContent/live_analysis/most_active/allTopValue1.json"
# headers  = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
#            'accept-language': 'en,gu;q=0.9,hi;q=0.8', 'accept-encoding': 'gzip, deflate, br'}
# response = requests.get(url, headers = headers).json()
# response = response['data']
# print(pd.DataFrame(response))

import pandas as pd
import requests
url = "https://www1.nseindia.com/products/dynaContent/equities/equities/json/online52NewHigh.json"
headers  = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
           'accept-language': 'en,gu;q=0.9,hi;q=0.8', 'accept-encoding': 'gzip, deflate, br'}

response = requests.get(url, headers = headers).json()
response = response['data']
response= pd.DataFrame(response)
for x in response.symbol:
    print(x)
print(response)
# print(response)