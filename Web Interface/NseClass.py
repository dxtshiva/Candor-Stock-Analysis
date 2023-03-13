import requests
import pandas as pd
from time import sleep
import json

class InvalidStockException(Exception):
    def __init__(self, code_name):
        self.code_name = code_name
        self.message = f"Invalid stock code {code_name}"
        super().__init__(self.message)

class InvalidIndexException(Exception):
    def __init__(self, code_name):
        self.code_name = code_name
        self.message = f"Invalid index {code_name}"
        super().__init__(self.message)

class InvalidCompanyException(Exception):
    def __init__(self, symbol):
        self.code_name = symbol
        self.message = f"Invalid company name {symbol}"
        super().__init__(self.message)

class Nse:

    headers  = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
           'accept-language': 'en,gu;q=0.9,hi;q=0.8', 'accept-encoding': 'gzip, deflate, br'}
    
    def nse_index_code(self, name: str=""):
        
        data = {'NIFTY 50': 'NIFTY', 'NIFTY50 DIV POINT': 'NIFTYDIVIDEND', 'NIFTY NEXT 50': 'JUNIOR', 'NIFTY100 LIQ 15': 'LIX15', 'INDIA VIX': 'INDIAVIX', 'NIFTY 100': 'CNX100', 
                'NIFTY 500': 'CNX500', 'NIFTY MIDCAP 100': 'MIDCAP', 'NIFTY MIDCAP 50': 'NFTYMCAP50', 'NIFTY MID LIQ 15': 'NIFTYMIDLIQ15', 'NIFTY BANK': 'BANKNIFTY', 
                'NIFTY ENERGY': 'CNXENERGY', 'NIFTY FMCG': 'CNXFMCG', 'NIFTY INFRA': 'CNXINFRA', 'NIFTY MNC': 'CNXMNC', 'NIFTY GROWSECT 15': 'NI15', 'NIFTY100 QUALTY30': 'NIFTYQUALITY30',
                'NIFTY50 VALUE 20': 'NV20', 'NIFTY PHARMA': 'CNXPHARMA', 'NIFTY PSE': 'CNXPSE', 'NIFTY PSU BANK': 'CNXPSUBANK', 'NIFTY PVT BANK': 'NIFTYPVTBANK', 'NIFTY REALTY': 'CNXREALTY', 
                'NIFTY SERV SECTOR': 'CNXSERVICE', 'NIFTY IT': 'CNXIT', 'NIFTY SMLCAP 100': 'CNXSMCAP', 'NIFTY 200': 'CNX200', 'NIFTY AUTO': 'CNXAUTO', 'NIFTY MEDIA': 'CNXMEDIA', 
                'NIFTY METAL': 'CNXMETAL', 'NIFTY DIV OPPS 50': 'CNXDIVIDENDOPPT', 'NIFTY COMMODITIES': 'CNXCOMMODITIES', 'NIFTY CONSUMPTION': 'CNXCONSUMPTION', 'NIFTY CPSE': 'CPSE', 
                'NIFTY FIN SERVICE': 'CNXFINANCE', 'NIFTY50 TR 2X LEV': 'NIFTYTR2XLEV', 'NIFTY50 PR 2X LEV': 'NIFTYPR2XLEV', 'NIFTY50 TR 1X INV': 'NIFTYTR1XINV', 'NIFTY50 PR 1X INV': 'NIFTYPR1XINV',
                'NIFTY GS 8 13YR': 'NIFTYGS813YR', 'NIFTY GS 10YR': 'NIFTYGS10YR', 'NIFTY GS 10YR CLN': 'NIFTYGS10YRCLN', 'NIFTY GS 4 8YR': 'NIFTYGS48YR', 'NIFTY GS 11 15YR': 'NIFTYGS1115YR', 
                'NIFTY GS 15YRPLUS': 'NIFTYGS15YRPLUS', 'NIFTY GS COMPSITE': 'NIFTYGSCOMPSITE', 'NIFTY ALPHA 50': 'NIFTYALPHA50', 'NIFTY50 EQL WGT': 'NIFTY50EQLWGT', 
                'NIFTY100 EQL WGT': 'NIFTY100EQLWGT', 'NIFTY100 LOWVOL30': 'NIFTY100LOWVOL30', 'NIFTY MIDCAP 150': 'MIDCAP150', 'NIFTY SMLCAP 50': 'SMLCAP50', 
                'NIFTY SMLCAP 250': 'SMLCAP250', 'NIFTY MIDSML 400': 'MIDSML400', 'NIFTY200 QUALTY30': 'NIFTY200QLTY30'}
        
        if name=='':
            return data

        return data[name.upper()]
    
    def nse_index_data(self, clean_names:bool = False):

        url = "https://www1.nseindia.com/homepage/Indices1.json" 
        response = requests.get(url,headers=self.headers).json()
        data = pd.DataFrame(response['data'])
        data.drop(['imgFileName'], inplace=True,axis='columns')
        data.set_index('name',inplace=True)  

        if clean_names:
            data.rename({'lastPrice':'last_traded_price', 
                         'change':'day_change', 
                         'pChange':'percent_change'},
                         axis = 'columns',inplace=True)
        
        return data

    def nse_index_quote(self,symbol,clean_names: bool =False):
        if self.is_valid_index(symbol):
            dict  = self.nse_index_code()
            name = list(filter(lambda x: dict[x] == symbol.upper(), dict))[0]
            data = self.nse_index_quote(clean_names)
            return data.loc[str(name).upper()]
        else:
            raise InvalidIndexException(symbol)
    
    def is_valid_index(self, symbol):
        return str(symbol).upper() in list(nse.nse_index_code().values())
    
    def nse_stock_code(self, symbol=''):
        data = pd.read_csv('https://www1.nseindia.com/content/equities/EQUITY_L.csv')
        data.drop(list(data.columns[2:]),axis='columns',inplace=True)
        if symbol=='':
            return data
        # return(data[data.SYMBOL.isin([symbol.upper()])])
        val = data[data['SYMBOL'].str.contains(symbol.upper())]
        if val.empty :
            raise InvalidCompanyException(symbol)
    
    def is_valid_stock(self, symbol):
        return str(symbol).upper() in list(nse.nse_stock_code().SYMBOL)

    def nse_top_gainers(self, clean_names: bool =False):
        url = "https://www1.nseindia.com/live_market/dynaContent/live_analysis/gainers/niftyGainers1.json"
        data = pd.DataFrame(requests.get(url,headers=self.headers).json()['data'])
        data.drop(columns=['series','netPrice','tradedQuantity','turnoverInLakhs','lastCorpAnnouncementDate','lastCorpAnnouncement'],inplace=True)
        if(clean_names):
            data.rename({'symbol': 'stock_code',
                         'openPrice':'open_price', 
                         'highPrice':'day_high', 
                         'lowPrice':'day_low',
                         'ltp':'last_traded_price',
                         'previousPrice':'previous_trade_price'},
                         axis = 'columns',inplace=True)
        return data
    
    def nse_top_losers(self, clean_names: bool =False):
        url = "https://www1.nseindia.com/live_market/dynaContent/live_analysis/losers/niftyLosers1.json"
        data = pd.DataFrame(requests.get(url,headers=self.headers).json()['data'])
        data.drop(columns=['series','netPrice','tradedQuantity','turnoverInLakhs','lastCorpAnnouncementDate','lastCorpAnnouncement'],inplace=True)
        if(clean_names):
            data.rename({'symbol': 'stock_code',
                         'openPrice':'open_price', 
                         'highPrice':'day_high', 
                         'lowPrice':'day_low',
                         'ltp':'last_traded_price',
                         'previousPrice':'previous_trade_price'},
                         axis = 'columns',inplace=True)
        return data

    def nse_stock_quote(self, symbol):

        if(self.is_valid_stock(symbol)):

            url='https://query1.finance.yahoo.com/v8/finance/chart/'+str(symbol).upper()+'.NS'
            response = requests.get(url,headers = self.headers).json()
            lastPrice =  response['chart']['result'][0]['meta']['regularMarketPrice']
            pClose = response['chart']['result'][0]['meta']['previousClose']
            url1='https://www1.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?'
            payloads= {"symbol":str(symbol).upper(),"series":"EQ"}
            data = requests.get(url1,params = payloads,headers = self.headers).text
            index  = data.find('"data":')
            index1  = data.find(',"optLink"')
            response1 = pd.DataFrame(json.loads(data[index+len('"data":'):index1]))
            data = pd.DataFrame({
                'Symbol': response1['symbol'],
                'comapnyName': response1['companyName'],
                'previousClose': pClose,
                'openPrice': response1['open'],
                'lastPrice':lastPrice,
                'pchange':(lastPrice-float(response1['open']))/float(response1['open'])*100,
                'dayHigh':response1['dayHigh'],
                'dayLow':response1['dayLow'],
                'high52': response1['high52'],
                'low52': response1['low52']
            })

            return data
            
        else:
            raise  InvalidStockException(symbol)

    def nse_most_traded_stocks(self,clean_name=False):
        
        url = "https://www1.nseindia.com/products/dynaContent/equities/equities/json/mostActiveMonthly.json"
        response = requests.get(url,headers=self.headers).json()
        data = pd.DataFrame(response['data'])
        if clean_name:
            data.rename({
                'security':'Company Name',
                'sharetotal':'Percent trade',
                'trdQty':'Trade Quantity'
            })
        return data

    def nse_52week_low(self, clean_names=True):
        url = 'https://www1.nseindia.com/products/dynaContent/equities/equities/json/online52NewLow.json'
        response = pd.DataFrame(requests.get(url,headers=self.headers).json()['data'])
        for symbols in response.symbol:
            print(self.nse_stock_quote(symbols))
        # for symbols in response.symbol:
        #     data = self.nse_stock_quote(symbols)
        #     print(data)

            



nse = Nse()

# data= pd.DataFrame(nse.nse_52week_low('pocl'))
# print(data[['dt','value_old']])
# print(nse.nse_stock_quote("A2ZINFRA"))

# print(pd.DataFrame(nse.nse_52week_low()))
# nse.nse_52week_low()

nse.nse_stock_quote("ALKYLAMINE")

