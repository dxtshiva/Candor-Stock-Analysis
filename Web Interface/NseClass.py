import requests
import pandas as pd

class Nse:

    headers  = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
           'accept-language': 'en,gu;q=0.9,hi;q=0.8', 'accept-encoding': 'gzip, deflate, br'}
    
    def nse_index_code(self, name=""):
        
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
    
    def nse_index_quote(self, clean_names = False):

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

    def nse_index_data(self,symbol,clean_names=False):
        dict  = self.nse_index_code()
        name = list(filter(lambda x: dict[x] == symbol.upper(), dict))[0]
        data = self.nse_index_quote(clean_names)
        return data.loc[str(name).upper()]
    
    def is_valid_index(self, symbol):
        return str(symbol).upper() in list(nse.nse_index_code().values())
    
    def nse_stock_code(self, symbol=''):
        data = pd.read_csv('https://www1.nseindia.com/content/equities/EQUITY_L.csv')
        data.drop(list(data.columns[2:]),axis='columns',inplace=True)
        if symbol=='':
            return data
        # return(data[data.SYMBOL.isin([symbol.upper()])])
        return data[data['SYMBOL'].str.contains(symbol.upper())]
    
    def is_valid_stock(self, symbol):
        return str(symbol).upper() in list(nse.nse_stock_code().SYMBOL)

nse = Nse()

# data= nse.is_valid_index("banknifty")
# print(data)
print(nse.is_valid_stock("sbin"))
