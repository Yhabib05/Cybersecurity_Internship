import geocoder
import folium

g = geocoder.ip("41.92.10.189")

myAddress = g.latlng

#print(myAddress)

my_map1 = folium.Map(location=myAddress, zoom_start=12)

folium.CircleMarker(location=myAddress, radius=50, color='red', fill=True).add_to(my_map1)

my_map1.save("my_map.html")