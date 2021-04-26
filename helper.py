from bisect import bisect
import requests

#This is a list of names of our icons on the webpage, in order to differentiate from the list of api horoscope names, we used Chinese pinyin here.
constellations = ["mojie","shuiping","shuangyu", "baiyang", "jinniu","shuangzi","shizi","juxie","chunv","tiancheng", "tianxie", "sheshou"]

#This is a list of names of all horoscopes from our horoscope api.
en_constellations = [
    "Capricorn","Aquarius","Pisces","Aries","Taurus","Gemini","Leo","Cancer","Virgo","Libra","Scorpio","Sagittarius"
]
#Here we matched the pinyin and English names of all horoscopes together.
en_2_ch = {
    "Capricorn":"mojie",
    "Aquarius":"shuiping",
    "Pisces":"shuangyu",
    "Aries":"baiyang",
    "Taurus":"jinniu",
    "Gemini":"shuangzi",
    "Leo":"shizi",
    "Cancer":"juxie",
    "Virgo":"chunv",
    "Libra":"tiancheng",
    "Scorpio":"tianxie",
    "Sagittarius":"sheshou"
}

#In order to relate the date input entered by users and the time range of horoscopes, we assigned months, dates, and horoscopes names.
signs = [(1,20,"Capricorn"), (2,18,"Aquarius"), (3,20,"Pisces"), (4,20,"Aries"),
         (5,21,"Taurus"), (6,21,"Gemini"), (7,22,"Cancer"), (8,23,"Leo"),
         (9,23,"Virgo"), (10,23,"Libra"), (11,22,"Scorpio"), (12,22,"Sagittarius"),
         (12,31,"Capricorn")]


def zodiac_sign(m,d):
    '''This function return the horoscope names when month and date of the user's birthday were entered'''
    return signs[bisect(signs,(m,d))][2]


def constellation_en_2_ch(sign):
    '''According to the horoscopes names returned by the previous function, this function will checked the icons' names and returned the correspnding results'''
    return en_2_ch[sign]


def get_info_by_time(m,d):
    '''This function returns the horoscope info based on the horoscope dates'''
    sign = zodiac_sign(m,d)

    return get_info_by_sign(sign)


def get_info_by_sign(sign):
    #sign = zodiac_sign(5, 12)
    '''This function returns the detailed horoscope detailed results based on the horoscope names'''
    params = (
        ('sign', sign),
        ('day', 'today'),
    )
    #Using requests to call our horoscope api
    res = requests.post('https://aztro.sameerkumar.website/', params=params)
    a = res.json()
    return a


def get_ch_2_en(chSign):
    '''Another function to return the English version of horoscopes based on the pinyin version'''
    for k,v in en_2_ch.items():
        if v==chSign:
            return k



