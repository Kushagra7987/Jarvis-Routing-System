# Jarvis Routing System

## Overview

The **Jarvis Routing System** project aims to address critical challenges in logistics and transportation by developing a Dynamic Route Optimization System. The system leverages real-time data from multiple APIs to optimize delivery routes, estimate vehicle emissions, and promote environmental sustainability.

## Features

- **Route Optimization**: Calculates the best routes based on current traffic conditions.
- **Traffic Incident Reporting**: Displays real-time traffic incidents along the route.
- **Air Quality Index (AQI)**: Provides air quality information for both the origin and destination locations.
- **Emission Calculations**: Estimates CO2 emissions based on the distance traveled and vehicle fuel efficiency.
- **User -Friendly Interface**: Simple and intuitive web interface for easy navigation.

## Technologies Used

- **Backend**: Flask
- **Frontend**: HTML, CSS
- **Python**: For core logic, API integrations, and emissions calculations.

 
## APIs Used

- Google Maps API: For route generation and distance calculations.
- TomTom API: For real-time traffic incident data.
- AQICN API: For air quality data.
- OSRM: For alternative route optimization (future integration).


 ## Project Structure

├── templates/  
│   ├── base.html       # Base template for UI structure  
│   ├── index.html      # Home page with user input form  
│   ├── result.html     # Results page with route and emissions data  
├── static/  
│   ├── style.css       # Stylesheet for the project  
├── app.py              # Main application file  
├── README.md           # Project documentation  
├── requirements.txt    # Python dependencies  


## Screenshots 

- ![Screenshot_2025-01-06_232805 1](https://github.com/user-attachments/assets/7469fa96-7d69-483e-addc-ab4584f5bd26)
- ![Screenshot_2025-01-06_232838 1](https://github.com/user-attachments/assets/3457ca1a-7e7e-4797-a43c-3a36f4cbe913)
- ![Screenshot_2025-01-06_232910 1](https://github.com/user-attachments/assets/b97c0892-3890-460c-b0b3-a06667435dc3)






