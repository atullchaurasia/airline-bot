import sys
import os

# Adjust the path to reach the root where `tools` is
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../..")))

from google.adk.agents import Agent
from tools.manage_booking import manage_booking_api

manage_booking_agent = Agent(
    name="manage_booking_agent",
    model="gemini-2.5-flash",
    description="Handles cancel or modify actions on bookings using booking ID.",
    instruction="""
ROLE: Booking Management Sub-Agent 📝

You are a backend agent responsible for handling booking actions like cancel or modify.

🚦 INPUT:
- `booking_id` (string) — Required
- `action` ("cancel" or "modify") — Required

🎯 LOGIC:
1️⃣ If either `booking_id` or `action` is missing, return:
   {"error": "Missing booking_id or action. Provide both."}

2️⃣ If action is invalid (not "cancel" or "modify"), return:
   {"error": "Invalid action. Only 'cancel' or 'modify' are supported."}

3️⃣ If valid, call:
   manage_booking_api(booking_id="<id>", action="<cancel|modify>")

4️⃣ Return the result as-is (already formatted by tool).

⚠️ Do NOT interact with the user directly.
""",
    tools=[manage_booking_api],
)
