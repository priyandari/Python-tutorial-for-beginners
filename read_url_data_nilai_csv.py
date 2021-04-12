import requests
import csv

data_nilai = []

def read_data(url):
    response = requests.get(url)
    if response.status_code != 200:
        print('Failed to get data:', response.status_code)
    else:
        wrapper = csv.reader(response.text.strip().split('\n'))
        for record in wrapper:
            data_nilai.append(record)
    #return wrapper
url = 'https://raw.githubusercontent.com/priyandari/Python-tutorial-for-beginners/tutorial2021/nilaiKuliah.csv'

read_data(url)
print(type(data_nilai))

for data in data_nilai:
    print(data)


