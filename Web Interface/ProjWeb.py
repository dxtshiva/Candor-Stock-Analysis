#importing necessary libraries
from nsetools import Nse
from nsepy import *
from datetime import date
from flask import *
import random,string
from bokeh.plotting import *
from bokeh.embed import components
from bokeh.resources import CDN
from rpy2.robjects.packages import importr
from rpy2.robjects import pandas2ri
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import warnings
warnings.filterwarnings("ignore")

#Creating objects of Nse and Flask
nse= Nse()
pandas2ri.activate()
r_nse = importr("nse2r")
app = Flask(__name__)

#Defining secret key for session
app.secret_key = ''.join(random.choices(string.ascii_uppercase+string.digits+string.ascii_lowercase, k = 15))


#Getting all the stock codes listed on NSE
lis= nse.get_stock_codes()
lis.pop('SYMBOL')
test=1

#Creating the stock list with stock code and stock name
stocks= []
for i,j in lis.items():
    stocks.append(j+'  ('+i+')')


#Defining functionality to the landing page    
@app.route("/",methods=['GET','POST'])
def home():
    #Getting the index data
    # index_data = r_nse.nse_index_quote()
    # nifty50 = [str(i) for i in index_data[index_data['index_name'] == 'NIFTY 50' ].values[0]]
    # niftyit = [str(i) for i in index_data[index_data['index_name'] == 'NIFTY IT' ].values[0]]
    # niftybank = [str(i) for i in index_data[index_data['index_name'] == 'NIFTY BANK' ].values[0]]
    # niftymid = [str(i) for i in index_data[index_data['index_name'] == 'NIFTY MIDCAP 50' ].values[0]]
    # niftyfin = [str(i) for i in index_data[index_data['index_name'] == 'NIFTY FIN SERVICE' ].values[0]] 
    pass

    #Setting a method to check if user is searching for some stock code
    if request.method=='POST':

        #fetching the selected stock from webpage
        x=str(request.form['query_stock'])

        #Checking is user has tried to search with a stock code directly       
        if x.upper() in lis.keys():
            #Adding stock code and name to the session
            session['s_code']=x.upper()
            session['s_name']= lis.get(session['s_code'])

        #In case if the stock code is not searched then adding directly the value to the session
        else:
            #Adding the selected stock session
            session['s_name']= x[0:x.find("(")-1]
            session['s_code'] = x[x.find("(")+1:len(x)-1]
        
        #Redirecting to stock details page
        return redirect(url_for("usr"))

    #Incase user is not searching for something redirecting back to home page
    else:
        if 'test' not in session:
            session['test']=1
        kwargs = {'title':'Candor Stock Analysis','stock': stocks,'test':session['test']}
        session['test']=1
        return render_template("index.html", **kwargs)

#Defining functinoality to the stock details page
@app.route("/search")
def usr():
    #Checking if user is trying to manually access the page or has been redirected
    if "s_name" in session and session['s_code'] in lis.keys():

        #Fetching the data 
        global data
        now = date.today()
        data = pd.DataFrame(get_history(session['s_code'],start=date(now.year-6,now.month,now.day),end=date(now.year,now.month,now.day))['Close'])

        #Checking if the data for stock has been fetched or not
        if len(data)==0:
            session['test']= 0
            return redirect (url_for('home'))

        #If the data is fetched redirecting to the search page
        else:
            
            #Fetching the current market data of the stock
            prsnt_data = nse.get_quote(session['s_code'])
            price = r_nse.nse_stock_quote(session['s_code'])[0]
            pchange = round((price-prsnt_data['basePrice'])/(prsnt_data['basePrice'])*100,2)
            curprice= '₹ '+str(price) + ' (' + str(pchange) +'%)'
            openprice= '₹ '+str(prsnt_data['open'])
            dhigh = '₹ '+str(prsnt_data['dayHigh'])
            dlow = '₹ '+str(prsnt_data['dayLow'])
            l52 = '₹ '+str(prsnt_data['low52'])
            h52 = '₹ '+str(prsnt_data['high52'])

            #Plotting the graph for the searched stock
            plot = figure(title=session['s_name'], x_axis_label='Date', y_axis_label='Close Price',x_axis_type='datetime',
            plot_width=800,plot_height=370)
            plot.line(data.index.to_flat_index(),data['Close'])
            
            #Getting html components of the graoh to render on the webpage
            script,div= components(plot)
            cdn_js = CDN.js_files[0]

            #Displaying results in the webpage         
            kwargs = {'test':1,'title':session['s_name'],'stock': stocks,'script':script,'div':div,'cdn_js':cdn_js}
            return render_template("s_data.html", **kwargs)
    
    #Checking if the stock code entered id valid or not
    elif "s_name" in session and (not session['s_code'] in lis.keys()):
        session['test']= 2
        return redirect (url_for('home'))

    #Redirecting to home page if someone is manually trying to access the page.            
    else:
        return redirect(url_for("home"))

#Update route for live index data
@app.route("/index_update",methods=['POST'])

def index_update():
    #Fetching live index data 
    index_data = r_nse.nse_index_quote()
    nifty50 = [str(i) for i in index_data[index_data['index_name'] == 'NIFTY 50' ].values[0]]
    niftyit = [str(i) for i in index_data[index_data['index_name'] == 'NIFTY IT' ].values[0]]
    niftybank = [str(i) for i in index_data[index_data['index_name'] == 'NIFTY BANK' ].values[0]]
    niftymid = [str(i) for i in index_data[index_data['index_name'] == 'NIFTY MIDCAP 50' ].values[0]]
    niftyfin = [str(i) for i in index_data[index_data['index_name'] == 'NIFTY FIN SERVICE' ].values[0]]

    #Returning back the data to webpage
    return jsonify({'nifty50':nifty50,'niftyit':niftyit,'niftybank':niftybank,'niftyfin':niftyfin,'niftymid':niftymid})

#Update route for live stock data
@app.route("/stock_update",methods=['POST'])
def stock_update():
    #Fetching live stock data
    prsnt_data = nse.get_quote(session['s_code'])
    price = r_nse.nse_stock_quote(session['s_code'])[0]
    pchange = round((price-prsnt_data['basePrice'])/(prsnt_data['basePrice'])*100,2)
    curprice= '₹ '+str(price) + ' (' + str(pchange) +'%)'
    openprice= '₹ '+str(prsnt_data['open'])
    dhigh = '₹ '+str(prsnt_data['dayHigh'])
    dlow = '₹ '+str(prsnt_data['dayLow'])
    l52 = '₹ '+str(prsnt_data['low52'])
    h52 = '₹ '+str(prsnt_data['high52'])
       
    #Adding live data to the past data to retrain the model
    global data
    data = pd.concat([data,pd.DataFrame([int(price)],index=[date.today()],columns=['Close'])])

    #Returning back the live data to webpage
    return jsonify({'curprice':curprice, 'openprice':openprice,'dhigh':dhigh, 'dlow':dlow, 'h52':h52, 'l52':l52})

#update rroute for prediction
@app.route("/pred_update",methods=['POST'])
def pred_update():
    #Creating a prediction model
    global data
    model = ARIMA(data,order=(0,1,15))
    model_fit = model.fit()
    
    #Generating prediction based on the data
    prediction = "₹ " +str([round(num,2)for num in model_fit.predict(start=len(data),end=len(data),typ='levels')][0])

    #Returning back the prediction to webpage
    return jsonify({'prediction':prediction})

#Running flask app      
if __name__ == "__main__":
    app.run(debug=True,use_reloader=True)