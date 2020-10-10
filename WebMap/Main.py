# @author - Shobhit 

# folium is a library in python, used to create base map by converting the parameters
#into javascript and HTML code. It uses Leaflet library
import folium
import pandas

df = pandas.read_csv("Volcanoes.csv")
longitude = list(df["LON"])
latitude  = list(df["LAT"])
elevation = list(df["ELEV"])

# function to return color based on elevation
def getColor(inp):
    if inp > 3000:
        return 'red'
    elif inp >= 1000 and inp <2000:
        return 'blue'
    else:
        return 'green'      

# creating a base map
map = folium.Map(location=[39.291681, -94.651297], zoom_start=6, tiles = "Stamen Terrain")

# creating a feature group, feature group helps in enabling/disabling layers of map
fgv = folium.FeatureGroup(name="Volcanoes")
# creating  markers on the map

for lat,lon,elev in zip(latitude,longitude,elevation):
    
    fgv.add_child(folium.Marker(location=[lat, lon], popup=elev, icon=(folium.Icon(color=getColor(elev)))))

fgp = folium.FeatureGroup(name="Population")
# GeoJson adds polygon layer to the map and based on population we are assoigning different layers to the polygon
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), 
style_function=lambda x: {'fillColor':'red' if x['properties']['POP2005'] > 20000000 else 'yellow'}))

map.add_child(fgv)
map.add_child(fgp)

# adding layer control
map.add_child(folium.LayerControl())
map.save("baseMap.html")