import random
import string
from datetime import datetime, timedelta
from google.adk.tools import FunctionTool

def generate_ticket_number() -> str:
    return "TK" + ''.join(random.choices(string.digits, k=6))

def generate_pnr() -> str:
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

def generate_seat() -> str:
    row = random.randint(1, 30)
    seat = random.choice(['A', 'B', 'C', 'D', 'E', 'F'])
    return f"{row}{seat}"

def generate_boarding_time() -> str:
    boarding_time = datetime.now() + timedelta(hours=random.randint(1, 6))
    return boarding_time.strftime("%Y-%m-%d %H:%M")

def book_flight(flight_number: str, name: str, age: int) -> dict:
    """
    Mocks booking a flight by generating realistic ticket data.
    """
    return {
        "status": "confirmed",
        "ticket_number": generate_ticket_number(),
        "pnr": generate_pnr(),
        "flight_number": flight_number,
        "passenger_name": name,
        "age": age,
        "seat_number": generate_seat(),
        "boarding_time": generate_boarding_time(),
        "departure_gate": random.randint(1, 20),
        "baggage_allowance": "1 cabin bag + 1 checked bag",
        "note": "Please arrive at the airport at least 2 hours before departure."
    }

tool = FunctionTool(book_flight)
