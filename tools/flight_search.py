import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load AVIATIONSTACK_API_KEY from .env file

API_KEY = os.getenv("AVIATIONSTACK_API_KEY")
BASE_URL = "http://api.aviationstack.com/v1/flights"

def search_live_flights(source_airport: str, destination_airport: str) -> dict:
    """
    Fetches live flights between source and destination using Aviationstack API.
    """
    if not API_KEY:
        return {"status": "failed", "message": "API key not set. Please add AVIATIONSTACK_API_KEY to .env"}

    params = {
        'access_key': API_KEY,
        'dep_iata': source_airport.upper(),
        'arr_iata': destination_airport.upper(),
        'limit': 5
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if "error" in data:
            return {"status": "failed", "message": data["error"]["info"]}

        flights = []
        for flight in data.get('data', []):
            flights.append({
                "airline": flight['airline']['name'],
                "flight_number": flight['flight']['iata'],
                "departure_time": flight['departure']['scheduled'],
                "arrival_time": flight['arrival']['scheduled'],
                "status": flight['flight_status']
            })

        if not flights:
            return {"status": "no_flights", "message": "No live flights found for the given route."}

        return {
            "status": "success",
            "source": source_airport.upper(),
            "destination": destination_airport.upper(),
            "flights": flights
        }

    except Exception as e:
        return {"status": "error", "message": str(e)}
