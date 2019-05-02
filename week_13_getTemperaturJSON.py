import urllib.request # Perhartikan bagian ini untuk Python3
import json

### API documentation from:  http://openweathermap.org/API
### Go to openweathermap.org, get an API Key, and paste it between the quotes below'

API_KEY = 'xxxxxxxxxxxxxxxxxxxx'  # <- ganti dengan API yang Anda peroleh

def getTemperatur(kota):
    urlAndParams = 'http://api.openweathermap.org/data/2.5/weather?q=' + kota + '&appid=' + API_KEY
    # urlAndParams =  'http://api.openweathermap.org/data/2.5/weather?q=London&appid=ec3c7d1c24f8bdb7769ed8a05899e1fa'
    # urlAndParams = 'api.openweathermap.org/data/2.5/weather?q=' + kota + '&mode=json' + '&APPID=' + API_KEY
    
    # Buat request dan simpan hasilnya sebagai string
    respon = urllib.request.urlopen(urlAndParams).read()
    print(respon)
    responseDict = json.loads(respon) # konversi dari JSON ke bentuk dictionary python
    mainDict = responseDict['main'] # mengambil informasi dari key 'main'
    degrees = mainDict['temp'] # mengambil informasi temperatur dari dictionary

    return float(degrees)

# Konversi dari kelvin ke fahrenheit
def konversiKtoF(temperaturK):
    degreesF = (1.8 * (temperaturK - 273)) + 32
    return degreesF

# Konversi dari kelvin ke Celcius
def konversiKtoC(temperaturK):
    degreesC = temperaturK - 273.15
    return degreesC


while True:
    kota = input('Inputkan kota yang ingin diketahui temperaturnya: ')
    if kota == '':
        break
    tempK = getTemperatur(kota)
    tempF = konversiKtoF(tempK)
    tempC = konversiKtoC(tempK)
    print("{0:.2f}".format(tempK), " K")
    print("{0:.2f}".format(tempF), " F")
    print("{0:.2f}".format(tempC), " C")
    print()