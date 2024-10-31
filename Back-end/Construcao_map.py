import folium
import webbrowser
def map(coordenadas):
    # Lista de locais de IP com latitude e longitude

    lat, lon = coordenadas[0]["lat"], coordenadas[0]["lon"]
    #print(lat)
    #print(lon)

    # Crie um mapa centrado em uma localização inicial
    m = folium.Map(location=[lat, lon], zoom_start=5)

    # Adicione marcadores para cada local de IP
    for location in coordenadas:
        lat, lon = location["lat"], location["lon"]
        ip = location["ip"]
        folium.Marker([lat, lon], tooltip=ip).add_to(m)

    # Salve o mapa em um arquivo HTML
    m.save("mapa.html")
    webbrowser.open_new_tab("mapa.html")
#coordenadas = [
       # {"ip": "192.168.1.1", "lat": 37.7749, "lon": -122.4194},
        #{"ip": "203.0.113.1", "lat": 40.7128, "lon": -74.0060},
        #{"ip": "203.0.113.1", "lat": 40.7128, "lon": -74.0060},
        #{"ip": "203.0.113.1", "lat": 40.7128, "lon": -74.0060},
        #{"ip": "203.0.113.1", "lat": 40.7128, "lon": -74.0060},
    #]

#print(coordenadas)
#map(coordenadas)