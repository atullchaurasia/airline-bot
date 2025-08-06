import requests
import os
from typing import Optional

API_KEY = os.getenv("AVIATIONSTACK_API_KEY")

def get_flight_status(flight_number: str, date: Optional[str] = None) -> dict:
    """
    Fetches live flight status from the AviationStack API.

    Args:
        flight_number (str): IATA flight code (e.g., 'AI202').
        date (Optional[str]): Optional flight date in YYYY-MM-DD format.

    Returns:
        dict: Flight status details or error message.
    """
    if not API_KEY:
        return {
            "error": "❌ Missing API key. Please set AVIATIONSTACK_API_KEY in your environment."
        }

    url = f"http://api.aviationstack.com/v1/flights?access_key={API_KEY}&flight_iata={flight_number}"
    if date:
        url += f"&flight_date={date}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        if "data" in data and data["data"]:
            flight = data["data"][0]
            return {
                "flight_number": flight.get("flight", {}).get("iata", flight_number),
                "status": flight.get("flight_status", "Unknown"),
                "departure_time": flight.get("departure", {}).get("scheduled", "-"),
                "arrival_time": flight.get("arrival", {}).get("scheduled", "-"),
                "gate": flight.get("departure", {}).get("gate", "-"),
                "terminal": flight.get("departure", {}).get("terminal", "-"),
                "date": flight.get("flight_date", date or "-")
            }

        else:
            return {
                "flight_number": flight_number,
                "status": "Not found",
                "departure_time": "-",
                "arrival_time": "-",
                "gate": "-",
                "terminal": "-",
                "date": date or "-"
            }

    except requests.exceptions.RequestException as e:
        return {
            "flight_number": flight_number,
            "status": "API Error",
            "error": f"Request failed: {str(e)}",
            "departure_time": "-",
            "arrival_time": "-",
            "gate": "-",
            "terminal": "-",
            "date": date or "-"
        }
