from flask import Flask, render_template, request
import requests
import os

# Replace these with your actual API keys
TOMTOM_API_KEY = '5WybauVArOzVPeDKGZXmus0uxF5OW9JJ'
GOOGLE_MAPS_API_KEY = 'AIzaSyC1JrSgRtVYT86yfKAarBRaFLJ1itUU-X8'
AQICN_API_KEY = '0b332e1a503a76636718ac342174088beefc1761'

def get_traffic_data(location):
    url = f"https://api.tomtom.com/traffic/services/4/incidentDetails.json?key={TOMTOM_API_KEY}&location={location}"
    response = requests.get(url)
    
    print("Traffic API Status Code:", response.status_code)
    print("Traffic API Raw Response:", response.text)
    
    if response.status_code == 200:
        try:
            data = response.json()
            # Check if there are incidents
            if 'incidents' in data and data['incidents']:
                return data['incidents']  # Return the list of incidents
            else:
                return None  # No incidents found
        except ValueError as e:
            print("Error decoding JSON:", e)
            return None
    else:
        print("Error: Received status code", response.status_code)
        return None

def get_route(origin, destination):
    url = f"https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&key={GOOGLE_MAPS_API_KEY}"
    response = requests.get(url)
    return response.json()

def get_air_quality(location):
    url = f"https://api.waqi.info/feed/{location}/?token={AQICN_API_KEY}"
    response = requests.get(url)
    return response.json()

def calculate_emissions(distance, fuel_efficiency):
    gallons_used = distance / fuel_efficiency
    co2_per_gallon = 19.6  # in pounds
    return gallons_used * co2_per_gallon

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    origin = request.form['origin']
    destination = request.form['destination']
    fuel_efficiency = float(request.form['fuel_efficiency'])  # Add this input in the form

    # Get route data
    route_data = get_route(origin, destination)
    
    # Debugging: Print the route data to the console
    print("Route Data:", route_data)

    if route_data.get('status') == 'OK':
        distance = route_data['routes'][0]['legs'][0]['distance']['value'] / 1000  # Convert to km
        emissions = calculate_emissions(distance, fuel_efficiency)

        # Get traffic data
        traffic_data = get_traffic_data(origin)

        # Get air quality data
        air_quality_data = get_air_quality(origin)

        # Extract relevant air quality information
        aqi = air_quality_data.get('data', {}).get('aqi', 'N/A')  # Air Quality Index
        city_name = air_quality_data.get('data', {}).get('city', {}).get('name', 'Unknown City')
        attributions = air_quality_data.get('data', {}).get('attributions', [])

        return render_template('result.html', 
                               origin=origin, 
                               destination=destination, 
                               distance=distance, 
                               emissions=emissions,
                               traffic=traffic_data,
                               air_quality_data=air_quality_data,
                               aqi=aqi,
                               city_name=city_name,
                               attributions=attributions)
    else:
        # Print the error message from the API response
        error_message = route_data.get('error_message', 'Could not find a route.')
        print("Error Message:", error_message)
        return render_template('result.html', error=error_message)

if __name__ == '__main__':
    app.run(debug=True)