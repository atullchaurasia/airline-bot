from google.adk.agents import Agent

from .sub_agents.flight_search.agent import flight_search_agent
from .sub_agents.baggage.agent import baggage_info_agent
from .sub_agents.booking.agent import booking_agent
from .sub_agents.status.agent import flight_status_agent
from .sub_agents.manage_booking.agent import manage_booking_agent
from .sub_agents.faq_retriever.agent import faq_agent
from .sub_agents.intent_identifier.agent import intent_identifier


root_agent = Agent(
    name="manager",
    model="gemini-2.0-flash",
    description="Manager agent",
    instruction="""
ROLE: ✈️ Airline Manager Agent

You manage and delegate user queries to the right sub-agent. Do not answer directly — always route tasks.

---

DELEGATION GUIDE:

- ❓ Unclear intent → `intent_identifier_agent`
- 🛫 Book a ticket → `booking_agent`
- 🔍 Search flights → `flight_search_agent`
- 📡 Flight status → `flight_status_agent`
- 🧳 Baggage info → `baggage_info_agent`
- ⚙️ Modify/Cancel → `manage_booking_agent`
- 📘 General questions → `faq_agent`

---
Be precise. Route correctly. Keep it brief.
""",
    sub_agents=[
        intent_identifier,
        booking_agent,
        flight_status_agent,
        flight_search_agent,
        baggage_info_agent,
        manage_booking_agent,
        faq_agent
    ],
)
