import pandas as pd
from scrapper_boilerplate import dataToCSV


def csvToList(filename):
    df = pd.read_csv(filename)
    links = df['nickname'].tolist()
    return links


def save_user(url):
    href = url.get_attribute('href')
    dataToCSV(dataDict={ 'followed': href }, filename='followed.csv')
