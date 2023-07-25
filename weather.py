import requests
class Location:
    api_city = ""
    lat = 0
    long = 0
    api_city = ""
    api_key = "b1d789570430987cbda091a94f1c840d"
    # def __init__(self):
    def set_location(self,city):
        # self.api_city = "http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}"
        self.api_city = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={self.api_key}"
        response = requests.get(self.api_city)
        self.dic = dict(*response.json())
        if not self.dic:
            print("Please Enter Valid City Name! ")
        else:
            lat = self.dic['lat']
            long = self.dic['lon']
        print(lat,long)
obj = Location()
city = input("Enter City Name : ")
obj.set_location(city)


# print(*response.json())
