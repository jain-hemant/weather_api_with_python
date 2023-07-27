import os
import requests
class Location:
    api_city = ""
    lat = 0
    long = 0
    api_city = ""
    api_key = "b1d789570430987cbda091a94f1c840d"
    # def __init__(self):
    def __init__(self):
        self.lat = 0
        self.long = 0
    def set_location(self,city):
        # self.api_city = "http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}"
        self.api_city = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={self.api_key}"
        response = requests.get(self.api_city)
        self.dic = dict(*response.json())
        if not self.dic:
            os.system("cls")
            print("Please Enter Valid City Name! ")
            return False
        else:
            lat = self.dic['lat']
            long = self.dic['lon']
            return [lat,long]

class Weather:
    def __init__(self):
        self.api_city = ""
    def set_weather(self,city,cord_xy,api_key):
        # print(cord_xy[0])
        # print(cord_xy[1])
        self.api_city = ""
        self.api_weather = f"https://api.openweathermap.org/data/2.5/weather?lat={cord_xy[0]}&lon={cord_xy[1]}&appid={api_key}"
        response = requests.get(self.api_weather)
        dic = dict(response.json())
        get_temp = dic['main']
        kelvin = get_temp['temp']
        celcius = kelvin - 273.15
        os.system("cls")        
        print(f"The tempreture of {city} {round(celcius,2)}°C\n\n")

flag = True
while flag:
    city = input("Enter City Name : ")
    os.system("cls")
    print("\n Please Wait...\n")
    obj_location = Location()
    cord_xy = obj_location.set_location(city)    
    # flag = False
    # print(cord_xy)
    if cord_xy:
        obj_weather = Weather()
        obj_weather.set_weather(city,cord_xy,obj_location.api_key)
        again = input("Do you want to continue? (Y/N) : \n\n")
        again = again.upper()
        if again == "Y":
            flag = True
        else:
            flag = False        
    else:
        flag = True


# print(*response.json())
