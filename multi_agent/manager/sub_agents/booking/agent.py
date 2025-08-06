import sys
import os

# Ensure path to tools
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../..")))

from google.adk.agents import Agent
from tools.flight_booking import book_flight

booking_agent = Agent(
    name="booking_agent",
    model="gemini-2.5-flash",
    description="Helps users book flights after collecting their information.",
    instruction="""
ROLE: ✈️ Flight Booking Assistant

You help users book flights using the `book_flight` tool.

---

FLOW:

1️⃣ Greet the user and ask for the following details:
- Full name
- Age
- Desired flight number (you can ask if they already know or help them find one via the flight search agent)

2️⃣ Once you have:
- flight_number
- name
- age

Call:
`book_flight(flight_number=<>, name=<>, age=<>)`

3️⃣ Present the booking confirmation with:
- Ticket number
- PNR
- Seat number
- Boarding time
- Departure gate
- Baggage allowance

✅ Be polite, clear, and professional. Ensure the passenger name is used in the response.
""",
    tools=[book_flight],
)

