import requests
URL = 'https://api.weather.gov/zones/forecast/CAZ529/forecast'
response = requests.get(URL)
forecast = response.json()['properties']
print('Forecast updated:', forecast['updated'])
for period in forecast ['periods']:
    print(period['name'])
    print(period['detailedForecast'])
    print('')