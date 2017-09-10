from geopy.geocoders import Nominatim
from geopy.distance import great_circle


def choice_1():
    place_1_longitude = input("Enter 1st place longitude: ")
    place_1_latitude = input("Enter 1st place latitude: ")
    place_2_latitude = input("Enter 2nd place longitude: ")
    place_2_longitude = input("Enter 2nd place latitude: ")

    place_1 = (place_1_latitude, place_1_longitude)
    place_2 = (place_2_latitude, place_2_longitude)

    print("Distance between 2 cities is : ")
    print(great_circle(place_1, place_2).kilometers)



def choice_2():
    city_1 = input("Enter city 1 name: ")
    city_2 = input("Enter city 2 name: ")
    geolocator = Nominatim()
    location_1 = geolocator.geocode(city_1)
    location_2 = geolocator.geocode(city_2)
    place1 = (location_1.latitude, location_1.longitude)
    place2 = (location_2.latitude, location_2.longitude)
    print(great_circle(place1, place2).kilometers)


def choice_3():
    place = input("Enter city: ")
    geolocator = Nominatim()
    location = geolocator.geocode(place)
    print((location.longitude, location.latitude))


def choice_4():
    place_1_longitude = float(input("Enter 1st place longitude: "))
    place_1_latitude = float(input("Enter 1st place latitude: "))
    geolocator = Nominatim()
    location = geolocator.reverse((place_1_latitude,place_1_longitude))
    print(location.address)

print("Welcome to distance calculator")

print("Enter your choice: ")
print(" 1. Distance between 2 cities (longitude,latidude version)")
print(" 2. Distance between 2 cities (city name known)")
print(" 3. Longitude and Latitude of a Particular place")
print(" 4. Vice versa of 3rd option")

choice = int(input("Your choice: "))

if choice == 1:
    choice_1()
elif choice == 2:
    choice_2()
elif choice == 3:
    choice_3()
elif choice == 4:
    choice_4()









