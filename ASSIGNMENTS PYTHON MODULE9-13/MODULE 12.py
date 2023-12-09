import requests
# ex-1
'''
request = "https://api.chucknorris.io/jokes/random"
try:
    response = requests.get(request)
    if response.status_code == 200:
        print("It took" + str(response.elapsed) + "s")
        answer = response.json()
        print(answer["value"])

    else:
        print("There was an error with the server", response.status_code)
except requests.exceptions.ConnectionError as e:
    print("Request could not be completed: "+ str(e))

'''
# ex-2
def get_weather(api_key, city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key
    }
    response = requests.get(base_url, params=params)
    data = response.json()

    weather_description = data['weather'][0]['description']
    temp_kelvin = data['main']['temp']

    temp_celsius = temp_kelvin - 273.15

    return weather_description, temp_celsius

def main():
    api_key = "164fdd8efce152d159a3932e4fc0b518"
    city_name = input("Enter the name of a municipality: ")
    weather_description, temp_celsius = get_weather(api_key, city_name)

    print(f"Weather in {city_name}: {weather_description}")
    print(f"Temperature: {temp_celsius:.2f}°C")

if __name__ == "__main__":
    main()