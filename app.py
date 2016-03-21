from flask import Flask, render_template, request, redirect,url_for,send_from_directory
from bokeh.embed import components
from helperFunctions import *

#http://stackoverflow.com/questions/20646822/how-to-serve-static-files-in-flask
app = Flask(__name__,static_folder='static')

app.vars={}

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index',methods=['GET','POST'])
def index():
	if request.method=='GET':
 		return render_template('index.html')
	else: #request was a POST
 		app.vars['ticker']=request.form['ticker']
 		requestedjson=requestjson_v2(app.vars['ticker'],base_url,requestParams)

 		#check if request resulted in valid data
		if requestedjson.keys()==[u'quandl_error']:
			#route to error_page
			return render_template('error.html')

		else:
			df=v2_json_to_dataframe(str(app.vars['ticker']),requestedjson)#put into pandas df
			makeplot(df)
#			return redirect('/static_from_root')
#			return redirect(url_for('static',filename='plot.html'))
			return render_template('plot.html')

@app.route('/static_from_root')
def static_from_root(): 
	return render_template('plot.html')
#	return render_template('index.html')
#	return 'I am Chug' 
#send_from_directory(app.static_folder,request.path[1:])


if __name__ == '__main__':
#	app.run(host='0.0.0.0',debug=True)
	app.run(port=33507)
