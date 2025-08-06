import random
from datetime import datetime

def is_valid_booking_id(booking_id: str) -> bool:
    return booking_id.startswith("TK") and booking_id[2:].isdigit() and len(booking_id) == 8

def manage_booking_api(booking_id: str, action: str) -> dict:
    """
    Simulates managing a booking: cancel or modify.
    """
    if action not in ["cancel", "modify"]:
        return {"status": "failed", "message": "Invalid action. Use 'cancel' or 'modify'."}
    
    if not is_valid_booking_id(booking_id):
        return {"status": "failed", "message": "Invalid booking ID format. Should be like 'TK123456'."}

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if action == "cancel":
        refund_status = random.choice(["Full refund", "Partial refund", "No refund (non-refundable ticket)"])
        fee = random.randint(0, 2000) if refund_status != "Full refund" else 0
        return {
            "status": "success",
            "action": "cancel",
            "message": f"Booking {booking_id} has been cancelled.",
            "cancellation_fee": f"₹{fee}" if fee > 0 else "No fee",
            "refund_status": refund_status,
            "timestamp": now
        }

    elif action == "modify":
        new_seat = f"{random.randint(1, 30)}{random.choice(['A', 'B', 'C', 'D', 'E', 'F'])}"
        return {
            "status": "success",
            "action": "modify",
            "message": f"Booking {booking_id} has been modified.",
            "new_seat_assignment": new_seat,
            "modification_note": "Seat updated. Other details unchanged.",
            "timestamp": now
        }
