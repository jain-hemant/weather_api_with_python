import requests
# class Location:
#     def __init__(self):
#         api_city = "http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}"

api_key = "b1d789570430987cbda091a94f1c840d"
city = input("Enter City Name : ")
api_city = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={api_key}"

# api_url = "https://api.weather.gov/"
# api_url = "https://api.weather.gov/points/39.7456,-97.0892"
# api_url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m"
# api_url = f"https://api.openweathermap.org/data/3.0/onecall?appid=""b1d789570430987cbda091a94f1c840d"
response = requests.get(api_city)
# print(*response.json())
dic = dict(*response.json())
if not dic:
    print("Please Enter Valid City Name! ")
print(dic)
# print(dic.keys())
# for key in dic:
#     print(key + ": " + str(dic[key]))
#     print()