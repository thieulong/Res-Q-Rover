import requests
from bs4 import BeautifulSoup

def retrieve_current_location():

    response = requests.get("https://iplocation.com/")

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        lat = soup.find("td", class_="lat")
        lon = soup.find("td", class_="lng")
        country = soup.find("span", class_="country_name")
        state = soup.find("span", class_="region_name")
        region = soup.find("td", class_="city")

        current_lat = lat.text.strip()
        # print("Latitude:", current_lat)
        current_lon = lon.text.strip()
        # print("Longtitude:", current_lon)
        current_country = country.text.strip()
        # print("Country:", current_country)
        current_state = state.text.strip()
        # print("State:", current_state)
        current_region = region.text.strip()
        # print("Region:", current_region)

        return [current_lat, current_lon, current_region, current_state, current_country]

    else:
        print("Failed to retrieve location data.")

