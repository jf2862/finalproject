from flask import Flask
from flask import render_template
import pandas as pd
app = Flask(__name__)


import config


df1 = pd.read_csv(config.canada)
df2 = pd.read_csv(config.japan)


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/canada')
def canada():
    cols = list(df1.columns)
    return render_template('dataframe.html', data=df1.to_dict(), cols=cols, nrows=len(df1))  


@app.route('/japan')
def japan():
    cols = list(df2.columns)
    return render_template('dataframe.html', data=df2.to_dict(), cols=cols, nrows=len(df2))  

@app.route('/about')
def about():
	return render_template('about.html')

@app.errorhandler(404)
def not_found(error):
    return 'Page Not Found'


if __name__ == '__main__':
    app.run(debug=True)
