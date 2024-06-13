import requests


print(r'''
 ___ _   _ _______     _____ _____  _    ____  _     _____ ____   ___ _____ 
|_ _| \ | | ____\ \   / /_ _|_   _|/ \  | __ )| |   | ____| __ ) / _ \_   _|
 | ||  \| |  _|  \ \ / / | |  | | / _ \ |  _ \| |   |  _| |  _ \| | | || |  
 | || |\  | |___  \ V /  | |  | |/ ___ \| |_) | |___| |___| |_) | |_| || |  
|___|_| \_|_____|  \_/  |___| |_/_/   \_\____/|_____|_____|____/ \___/ |_|  

        ''')
class Data:
    def __init__(self, city, loc, country, postal, region, org):
        self.city = city
        self.loc = loc
        self.country = country
        self.postal = postal
        self.region = region
        self.org = org

def main():
    print("geolocator")
    ip = input("Enter IP address: ")
    url = f"https://ipinfo.io/{ip}/json"

    try:
        response = requests.get(url)
        response.raise_for_status()
        print("[+] Request Successfully Made")
        ipinfo = response.json()

        print(f"country: {ipinfo['country']}")
        print(f"city   : {ipinfo['city']}")
        print(f"cordinates: {ipinfo['loc']}")
        print(f"Postal code: {ipinfo['postal']}")
        print(f"region : {ipinfo['region']}")
        print(f"ASN: {ipinfo['org']}")
        
        cords = ipinfo['loc'].split(',')
        print(f"google maps: https://www.google.com/maps/?q={cords[0]},{cords[1]}")

    except requests.exceptions.RequestException as ex:
        print(f"ERROR: {ex}")

if __name__ == "__main__":
    main()
