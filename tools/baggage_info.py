import json
import os
from difflib import get_close_matches

def get_baggage_policy(airline: str) -> dict:
    airline_input = airline.strip().lower()
    file_path = os.path.join("data", "baggage_policies.json")

    try:
        with open(file_path, "r") as f:
            policies = json.load(f)
    except FileNotFoundError:
        return {
            "error": "Baggage policy data file not found."
        }

    # Normalize keys for matching
    policy_keys = list(policies.keys())
    lower_key_map = {k.lower(): k for k in policy_keys}
    
    # Try exact match
    if airline_input in lower_key_map:
        matched_key = lower_key_map[airline_input]
        return policies[matched_key]

    # Try fuzzy match
    close = get_close_matches(airline_input, lower_key_map.keys(), n=1, cutoff=0.6)
    if close:
        matched_key = lower_key_map[close[0]]
        return policies[matched_key]

    # If nothing matched
    return {
        "error": f"No baggage policy found for '{airline}'. Please try another airline or check the website.",
        "cabin_baggage": "Info not available",
        "check_in_baggage": "Info not available",
        "extra_baggage_fee": "Please check airline website",
        "number_of_checked_bags": "Not specified",
        "max_dimensions_checked_bag": "Not specified",
        "international_baggage": "Check with airline",
        "special_items": "Check with airline for allowed items"
    }
