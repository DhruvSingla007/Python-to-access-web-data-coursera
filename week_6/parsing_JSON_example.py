import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input("Enter the address : ")
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode({'address' : address})

    print("Retrieving URL : ",url)

    fhandle = urllib.request.urlopen(url).read()
    data = fhandle.decode()

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print("==============FAILED==============")
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lat = js['results'][0]['geometry']['location']['lat']
    lon = js['results'][0]['geometry']['location']['lon']
    location = js['results'][0]['formatted_address']
    print("LAT : ", lat, " LON : ", lon)
    print("LOCATION : ", location)

