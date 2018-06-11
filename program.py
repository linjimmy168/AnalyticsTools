import getLatLng
import pandas as pd

df = pd.read_csv('D:\Dropbox\#NEUStuff\Visualization\Week3\xxx.csv')

array = []
array.append("Location Name,Lat,Lng")

latLng = getLatLng.GetLat()
for index,value in df.iterrows():
    if index == (len(df) - 1):
        break
    print(value['Location Name'])
    try:
        lat,lng = latLng.getLat(value['Location Name'])
    except:
        print(value['Location Name'])
        lat,lng =0,0
        pass
    tempStr = ','.join([str(value['Location Name']),str(lat),str(lng)])
    array.append(tempStr)


pd.DataFrame(data=array).to_csv('LatLng.csv',index=False)
