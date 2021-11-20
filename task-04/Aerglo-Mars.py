import sys
import wget
import requests
import json

DEMO_API_KEY = "Q68JMpIohCh8mMblRksNFYoPdPcTSdwABcYE0z1Z"

if len(sys.argv) > 3:
    print('You have specified too many arguments')
    sys.exit()

if len(sys.argv) < 2:
    print('You need to specify the date and id of the image')
    sys.exit()

date = sys.argv[1]
id = sys.argv[2]

url = f'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date={date}&api_key={DEMO_API_KEY}'
response_API = requests.get(url)
data = json.loads(response_API.content)

flag = True

for i in range(len(data['photos'])):
    
    if data['photos'][i]['id'] == int(id):
        img_url = data['photos'][i]['img_src']
        print(img_url)

        #at times the download time is so slow :)
        wget.download(img_url,'NASA_img.jpg')                
        
        flag = False
        break

if flag:
    print("No data found!")