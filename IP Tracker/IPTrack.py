import requests
import pyfiglet

# Print the ASCII banner using pyfiglet
ascii_banner = pyfiglet.figlet_format("IP Tracker - Made By Exploits")
print(ascii_banner)

# Function to get geolocation data for the IP address
def get_ip_info(ip):
    try:
        # Sending request to API to get IP info in JSON format
        geoip = requests.get(f"http://ip-api.com/json/{ip}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,zip,lat,lon,timezone,currency,isp,org,as,asname,mobile,proxy,hosting,query")
        
        # Check if the API returned a valid JSON response
        try:
            data = geoip.json()
        except ValueError:
            print("Error: API response is not in JSON format.")
            return

        # Check if the request was successful
        if data["status"] == "fail":
            print(f"Error: {data['message']}")
        else:
            # Print the geolocation data
            print(f"""
Continent: {data["continent"]}
Continent Code: {data["continentCode"]}
Country: {data['country']}
Country Code: {data['countryCode']}
Region Name: {data['regionName']}
Region: {data['region']}
City: {data['city']}
Time Zone: {data['timezone']}
ZIP: {data['zip']}
Latitude: {data['lat']}
Longitude: {data['lon']}
IP: {data['query']}
ISP: {data['isp']}
AS Number: {data['as']}
AS Name: {data['asname']}
Organization: {data['org']}
Hosting: {data['hosting']}
Mobile: {data['mobile']}
Proxy: {data['proxy']}
""")
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while trying to reach the API: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Main loop to keep asking for IP addresses
while True:
    ip = input("Enter IP address to track (or type 'exit' to quit): ")

    # Exit the loop if the user types 'exit'
    if ip.lower() == 'exit':
        print("Exiting program. Goodbye!")
        break

    # Call the function to get the IP information
    if ip.strip():  # Check if IP input is not empty or just spaces
        get_ip_info(ip)
    else:
        print("Please enter a valid IP address.")
