import matplotlib
matplotlib.use('Agg')
#helper functions

import requests
from requests import get
import json
import simplejson as json
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pylab
from bokeh import mpl
from bokeh.plotting import output_file, show,save
from bokeh.plotting import figure
from bokeh.embed import components
import time
import datetime
import numpy as np
#####requesting data


currentDay=time.strftime("%Y-%m-%d")
requestParams={'start_date':'2016-02-18','end_date':currentDay,'api_key':'dLzgUM9W7Aqpmy3RRh4A','order':'asc',\
               'format':'json','column_index':'3','column_index':'4'\
              }

base_url='https://www.quandl.com/api/v3/datasets/WIKI/'
def requestjson_v2(ticker,base_url,requestParams):
    return requests.get(base_url+ticker,params=requestParams).json()


def checkjson(requestedjson):
	if requestedjson.keys()==[u'quandl_error']:
		print 'ERROR. Most likely the ticker you entered is not in the WIKI stock set.'
#print requestjson_v2('AAPL',base_url,requestParams)

def v2_json_to_dataframe(ticker,jsonInput):
    df=pd.read_json(json.dumps(jsonInput)).transpose()[['data']]
    ts=df['data'].apply(pd.Series).transpose()
    ts['date']=ts['dataset'].str[0]
    ts[ticker]=ts['dataset'].str[1]
    del ts['dataset']
    return ts 

def makeplot(dataframe):
	plt.figure(figsize=(11,8))
	dataframe.plot()#df plot function
#	ax.legend(bbox_to_anchor=(1,1),bbox_transform=plt.gcf().transFigure)    
	plt.legend(fontsize=20,bbox_to_anchor=(1.05,1),loc=2)
	plt.ylabel('Closing Price',fontsize=15)
	plt.xlabel('Day',fontsize=15)
#	fig.savefig('AAPL.png')
#	output_file("templates/plot.html",title="test")
	output_file("templates/plot.html",title="closingPrices")
#	show(mpl.to_bokeh())
	save(mpl.to_bokeh())
#	plot=mpl.to_bokeh()
#	return plot


#plot=figure()	

#requestedjson=requestjson_v2('AAPL',base_url,requestParams)
#checkjson(requestedjson)
#df=v2_json_to_dataframe('AAPL',requestedjson)
#df.to_csv("df.out.test")
#makeplot(df)
