# Weather-App
# Overview
This is a simple Django-based weather app that provides current weather and a 5-day forecast for one or two cities using the Weatherbit API. The app is Dockerized for easy deployment and scalability.

# Features
Fetches current weather data for one or two cities.
Displays a 5-day weather forecast for each city.
Utilizes the Weatherbit API for weather data.
Dockerized for easy setup and deployment.

# Requirements
Docker
Docker Compose (optional, but recommended for easier management)

# Setup
1. Clone the Repository
bash
Copy code
git clone https://github.com/your-username/weather-app.git
cd weather-app

2. Configure Environment Variables
Create a .env file in the root directory of the project and add your Weatherbit API key:
API_KEY=your_weatherbit_api_key

3. Build and Run the Docker Container
To build and run the Docker container, use the following command:

bash
Copy code
docker-compose up --build
If you prefer not to use Docker Compose, you can manually build and run the Docker container with these commands:
docker build -t weather-app .
docker run -p 8000:8000 weather-app

4. Access the Application
Once the container is running, you can access the application at http://localhost:8000/.

# Usage
On the homepage, enter the names of one or two cities to get current weather and a 5-day forecast.
The results will display temperature, weather description, and an icon representing the weather condition.

# Code Structure
weather_app/views.py: Contains the view logic for fetching and displaying weather data.
weather_app/templates/weather_app/index.html: The HTML template for displaying weather information.
Dockerfile: Defines the Docker image for the application.
docker-compose.yml: (Optional) Defines the Docker services for the application.

# Troubleshooting
Ensure you have a valid API key from Weatherbit and it's correctly set in the .env file.
Check Docker logs for any errors if the container fails to start.

# Contributing
Feel free to submit issues or pull requests. If you have any improvements or suggestions, they are always welcome!

# License
This project is licensed under the MIT License. See the LICENSE file for details.

