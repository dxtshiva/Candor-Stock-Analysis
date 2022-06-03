# Candor-Stock-Analysis

The given project is an attempt to design a system that predicts stock price using the ARIMA model. It takes the past six years of data from NSE and then uses this data to train the model and then uses the trained model to predict the close price of a stock based on the live stock data. The pages have an auto-refresh script of 8 seconds that keeps updating the live data after every 8 seconds. 

### WebInterace is the file that has the web interface of the project created using flask

### GUI.py is the file that has a GUI interface designed using Tkinter.


## Python Libraries used:
##### nsepy
##### nsetools
##### statsmodels
##### bokeh
##### rpy2
##### flask
##### ttkwidgets

## R libraries used
nse2r

# Steps to start the project
### 1. Install python and its libraries mentioned above (to install the python library use pip command: pip install <library_name>)
### 2. Install R and its libraries mentioned above (to install the R packages use install.packages(): install.packages("<package_name>")
### 3. To start the web interface run ProjWeb.py and open the deployment server URL in the browser
### 4. To start the GUI interface simply run the GUI.py file.

<p align="center">
<img src = "./Screenshot 2022-06-03 105312.jpg">
