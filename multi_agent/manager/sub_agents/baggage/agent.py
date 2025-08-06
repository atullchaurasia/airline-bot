import sys
import os

# Adjust the path to reach the root where `tools` is
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../..")))

from google.adk.agents import Agent
from tools.baggage_info import get_baggage_policy

baggage_info_agent = Agent(
    name="baggage_info_agent",
    model="gemini-2.5-flash",
    description="Provides baggage policies for airlines.",
    instruction="""
ROLE: Baggage Information Agent 🧳

You help users understand baggage rules.

FLOW:
1️⃣ If airline is not mentioned, ask the user politely.
2️⃣ Once airline is known, call `get_baggage_policy(airline="<name>")`
3️⃣ Present the details **clearly in bullet points** using this format:

✈️ Baggage Policy for <airline>:
- Cabin Baggage: <value>
- Check-in Baggage: <value>
- Extra Baggage Fee: <value>
- Number of Checked Bags: <value>
- Max Bag Dimensions: <value>
- International Baggage Rules: <value>
- Special Items: <value>

If any info is unavailable, say "Not specified" or guide the user to check the airline website.
""",
    tools=[get_baggage_policy]
)
