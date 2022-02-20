import datetime
from flask import Flask
from flask import render_template


app=Flask(__name__)


@app.route('/')
def index():
    time_date=datetime.datetime.now()
    time=time_date.time()
    headline ="hello world! now the time is "
    return render_template("styles_css.html",headline=headline,time=time)

@app.route('/more')
def today_time():
    today=datetime.datetime.now()
    today_date=today.isocalendar()
    return render_template("more.html",today_date=today_date)

if __name__=="__main__":
    app.run(host='0.0.0.0',port=8080)
