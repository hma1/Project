from flask import Flask, render_template, request
from helper import *
import traceback
app = Flask(__name__)


# Homepage
@app.route("/")
def index():
    #list of all horoscopes
    constellation_list = en_2_ch
    #return homepage html
    return render_template("index.html", constellation_list=constellation_list)



# Search the horoscopes detailed information and results based on the horoscope names
@app.route("/get_info_by_sign/<chSign>")
def get_constellation_by_sign(chSign):
    try:
        '''Relate the pinyin horoscope names to the English names'''
        sign = get_ch_2_en(chSign)
        if sign is None:
            sign = chSign
        '''return the info html page based on the icon names and horoscope names'''
        data = get_info_by_sign(sign)
        data['sign'] = sign
        data['chSign'] = chSign
        print(data)
        '''jump to the horoscope detailed info webpage and user will get the desired results'''
        return render_template("info.html", data=data)
    except:
        '''If there is any error, print the error info and go to the error page'''
        traceback.print_exc()
        return render_template("error.html")





# Get the horoscope infor according to the birthday date of the user
@app.route("/get_constellation_by_birthday",methods=['post'])
def get_constellation_by_birthday():
    try:
        #birthday
        birthday = request.form['birthday']
        print(birthday)
        arr = birthday.split("-") #split the date by -
        #month of birthday
        month = int(arr[0])
        #day of birthday
        date = int(arr[1])
        #Get the corresponding horoscope name based on the entered birthday
        sign = zodiac_sign(month, date)
        #Get the corresponding horoscope detailed infor based on the entered birthday
        data = get_info_by_time(month, date)
        data['sign'] = sign
        data['chSign'] = en_2_ch[sign]
        print(data)
        #Skip to the detailed infor web page and the user will get today's fortune and all horoscope related information
        return render_template("info.html", data=data)
    except:
        #If there is any error, skip to the error page
        traceback.print_exc()
        return render_template("error.html")


if __name__ == '__main__':
    app.run(debug=True)