# ✈️ Airline Virtual Assistant – Multi-Agent System

## 📌 Overview

This project is a **multi-agent conversational AI system** for an airline that can:

* Book flights
* Search live flight schedules
* Check flight status in real time
* Provide baggage policies
* Manage bookings (cancel/modify)
* Answer airline FAQs

It is built using **Google ADK Agents**, **tool integrations**, and **API calls** to AviationStack for live flight data.

---

## 🏗️ Architecture

The system uses a **Manager → Sub-Agent** structure:

### 1️⃣ **Root Manager Agent**

* **File:** `root_agent.py`
* **Role:** Routes user queries to the correct sub-agent.
* **Logic:**

  * Detect intent → Delegate task
  * Never answers directly — only routes.

**Delegation Guide:**

| Intent             | Sub-Agent              |
| ------------------ | ---------------------- |
| Greeting / Unknown | `intent_identifier`    |
| Flight Booking     | `booking_agent`        |
| Flight Search      | `flight_search_agent`  |
| Flight Status      | `flight_status_agent`  |
| Baggage Info       | `baggage_info_agent`   |
| Manage Booking     | `manage_booking_agent` |
| General FAQ        | `faq_agent`            |

---

## 🤖 Sub-Agents

### 1. **Intent Identifier Agent**

* **File:** `intent_identifier.py`
* **Role:** Classifies user queries into **6 predefined intents**:

  * `flight_booking`
  * `flight_status`
  * `flight_search`
  * `baggage_info`
  * `manage_booking`
  * `general_faq`
* **Special case:** Detects greetings and responds politely.

---

### 2. **Flight Search Agent**

* **File:** `flight_search_agent.py`
* **Tool:** `search_live_flights()`
* **API:** [AviationStack](https://aviationstack.com/)
* **Function:** Finds **live flights** between two IATA airport codes.

**Example Output:**

```
✈️ Flights from DEL to BOM
1. Air India AI101 — Dep: 14:00, Arr: 16:30 — Status: On Time
2. IndiGo 6E202 — Dep: 18:10, Arr: 20:20 — Status: Scheduled
```

---

### 3. **Flight Status Agent**

* **File:** `flight_status_agent.py`
* **Tool:** `get_flight_status()`
* **API:** AviationStack
* **Function:** Gets **real-time flight status** by flight number.

**Example Output:**

```
📡 Flight AI202 Status (2025-08-01)
- Departure: 14:30
- Arrival: 17:05
- Terminal: 3
- Gate: 12
- Status: On Time
```

---

### 4. **Manage Booking Agent**

* **File:** `manage_booking_agent.py`
* **Tool:** `manage_booking_api()`
* **Function:**

  * Cancel a booking (returns refund details)
  * Modify booking (updates seat assignment)

**Booking ID format:** `TK123456`

---

### 5. **FAQ Agent**

* **File:** `faq_agent.py`
* **Tool:** `retrieve_faq_answer()`
* **Function:**

  * Answers from a **local JSON FAQ database** using fuzzy matching.
  * Handles policies like check-in, refunds, cancellations, baggage rules.

---

### 6. **Baggage Info Agent**

* **File:** `baggage_info_agent.py`
* **Tool:** `get_baggage_policy()`
* **Function:** Returns baggage allowance, extra baggage charges, etc.

---

## 🔧 Tools

| Tool                  | File                          | Purpose                               |
| --------------------- | ----------------------------- | ------------------------------------- |
| `search_live_flights` | `tools/flight_search.py`      | Fetch live flights from AviationStack |
| `get_flight_status`   | `tools/flight_status.py`      | Get flight status from AviationStack  |
| `manage_booking_api`  | `tools/manage_booking.py`     | Cancel/Modify bookings                |
| `retrieve_faq_answer` | `tools/faq_retriever_tool.py` | Keyword/fuzzy FAQ search              |
| `get_baggage_policy`  | `tools/baggage_info.py`       | Baggage rules and policies            |

---

## 📂 Project Structure

```
airline_assistant/
│── sub_agents/
│   ├── intent_identifier/
│   ├── flight_search/
│   ├── flight_status/
│   ├── baggage/
│   ├── booking/
│   ├── manage_booking/
│   ├── faq_retriever/
│
│── tools/
│   ├── flight_search.py
│   ├── flight_status.py
│   ├── manage_booking.py
│   ├── faq_retriever_tool.py
│   ├── baggage_info.py
│
│── data/
│   ├── airline_faq.json
│
│── root_agent.py
│── README.md
│── .env
```

---

## ⚙️ Installation & Setup

1. **Clone the repo**

```bash
git clone https://github.com/yourusername/airline-assistant.git
cd airline-assistant
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Set environment variables**
   Create `.env` file:

```env
AVIATIONSTACK_API_KEY=your_api_key_here
```

4. **Run the system**

```bash
python run.py
```

---

## 🚀 Features Demo

**Example conversation:**

```
User: What's my baggage allowance?
→ FAQ Agent → "You are allowed 15kg check-in and 7kg cabin baggage."

User: Search flights from DEL to BLR
→ Flight Search Agent → Shows top 5 live flights.

User: Cancel my booking TK123456
→ Manage Booking Agent → Shows refund/fee details.
```

---
