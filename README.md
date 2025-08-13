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

* **File:** `multi_agent/manager/agent.py`
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

* **Folder:** `multi_agent/manager/sub_agents/intent_identifier`
* **Role:** Classifies user queries into **6 predefined intents**:

  * `flight_booking`
  * `flight_status`
  * `flight_search`
  * `baggage_info`
  * `manage_booking`
  * `general_faq`

---

### 2. **Flight Search Agent**

* **Folder:** `multi_agent/manager/sub_agents/flight_search`
* **Tool:** `tools/flight_search.py`
* **API:** [AviationStack](https://aviationstack.com/)
* **Function:** Finds **live flights** between two IATA airport codes.

---

### 3. **Flight Status Agent**

* **Folder:** `multi_agent/manager/sub_agents/status`
* **Tool:** `tools/flight_status.py`
* **API:** AviationStack
* **Function:** Gets **real-time flight status** by flight number.

---

### 4. **Manage Booking Agent**

* **Folder:** `multi_agent/manager/sub_agents/manage_booking`
* **Tool:** `tools/manage_booking.py`
* **Function:** Cancel or modify bookings.

---

### 5. **FAQ Agent**

* **Folder:** `multi_agent/manager/sub_agents/faq_retriever`
* **Tool:** `tools/faq_retriever_tool.py`
* **Function:** Search **local JSON FAQ** with fuzzy matching.

---

### 6. **Baggage Info Agent**

* **Folder:** `multi_agent/manager/sub_agents/baggage`
* **Tool:** `tools/baggage_info.py`
* **Function:** Returns baggage allowance & extra charges.

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
AIRLINE_BOT/
│── data/
│   ├── airline_faq.json
│
│── env/
│   ├── .env
│
│── mcp_config/
│   ├── mcp.yaml
│
│── multi_agent/
│   ├── manager/
│       ├── __init__.py
│       ├── agent.py
│       ├── app.py
│       ├── sub_agents/
│           ├── baggage/
│           ├── booking/
│           ├── faq_retriever/
│           ├── flight_search/
│           ├── intent_identifier/
│           ├── manage_booking/
│           ├── status/
│
│── tools/
│   ├── baggage_info.py
│   ├── faq_retriever_tool.py
│   ├── flight_booking.py
│   ├── flight_search.py
│   ├── flight_status.py
│   ├── manage_booking.py
│
│── airline_bot.db
│── app.py
│── requirements.txt
│── .env
```

---

## ⚙️ Installation & Setup

1. **Clone the repo**

```bash
git clone https://github.com/yourusername/airline-bot.git
cd airline-bot
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

4. **Run the bot**

```bash
python multi_agent/manager/app.py
```

---

## 🚀 Example Usage

```
User: What's my baggage allowance?
→ Baggage Agent → "You are allowed 15kg check-in and 7kg cabin baggage."

User: Search flights from DEL to BLR
→ Flight Search Agent → Shows top 5 live flights.

User: Cancel my booking TK123456
→ Manage Booking Agent → Shows refund/fee details.
```

---

I can also make you a **flow diagram** showing how `root_agent` delegates to sub-agents and how tools are called. That would be a strong addition for interviews.
