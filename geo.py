import requests

def geolocalizar_ip(ip):
    try:
        # Hacer una solicitud GET a ipinfo.io con la IP especificada
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        data = response.json()

        # Extraer los datos relevantes
        ip_address = data.get('ip', '')
        city = data.get('city', '')
        region = data.get('region', '')
        country = data.get('country', '')
        location = data.get('loc', '').split(',')

        latitude = location[0]
        longitude = location[1]

        # Mostrar la información de ubicación
        print(f"Ubicación de la IP {ip_address}:")
        print(f"Ciudad: {city}")
        print(f"Región: {region}")
        print(f"País: {country}")
        print(f"Latitud: {latitude}")
        print(f"Longitud: {longitude}")

    except Exception as e:
        print(f"Error al geolocalizar la IP {ip}: {str(e)}")

if __name__ == "__main__":
    ip = input("Ingresa la dirección IP que deseas geolocalizar: ").strip()

    # Llamar a la función para geolocalizar la IP ingresada
    geolocalizar_ip(ip)