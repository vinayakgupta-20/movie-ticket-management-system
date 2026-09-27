from storage import load_data, save_data
from movies import find_movie_by_id, MOVIE_FILE
from utils import generate_id, is_valid_seat_count
from logger import log_action

BOOKING_FILE = "bookings.json"

def book_ticket(username):
    movie_id = input("Enter Movie ID you want to book: ").strip()
    movie = find_movie_by_id(movie_id)

    if movie is None:
        print("Movie ID not found. Please check and try again.")
        return

    print(f"Selected: {movie['title']} | Seats left: {movie['available_seats']} "
          f"| Price per seat: Rs.{movie['price']}")

    seat_input = input("How many seats do you want to book? ").strip()

    if not is_valid_seat_count(seat_input, movie["available_seats"]):
        print("Invalid number of seats, or not enough seats available.")
        return

    seats_wanted = int(seat_input)
    total_amount = seats_wanted * movie["price"]
    movies = load_data(MOVIE_FILE)

    for m in movies:
        if m["movie_id"] == movie["movie_id"]:
            m["available_seats"] -= seats_wanted
    save_data(MOVIE_FILE, movies)

    bookings = load_data(BOOKING_FILE)
    new_booking = {
        "booking_id": generate_id("BKG"),
        "username": username,
        "movie_id": movie["movie_id"],
        "movie_title": movie["title"],
        "seats": seats_wanted,
        "amount": total_amount,
        "status": "CONFIRMED"
    }
    bookings.append(new_booking)
    save_data(BOOKING_FILE, bookings)

    log_action(f"Booking done: {new_booking['booking_id']} by {username} "
               f"for {movie['title']} ({seats_wanted} seats)")

    print(f"Booking confirmed! Your Booking ID is {new_booking['booking_id']}. "
          f"Total amount: Rs.{total_amount}")

def view_my_bookings(username):
    bookings = load_data(BOOKING_FILE)
    my_bookings = [b for b in bookings if b["username"].lower() == username.lower()]

    if not my_bookings:
        print("You have not booked any tickets yet.")
        return

    print(f"\n--- Bookings for {username} ---")
    for b in my_bookings:
        print(f"{b['booking_id']} | {b['movie_title']} | Seats: {b['seats']} "
              f"| Amount: Rs.{b['amount']} | Status: {b['status']}")
    print()


def cancel_booking(username):
    booking_id = input("Enter Booking ID to cancel: ").strip()
    bookings = load_data(BOOKING_FILE)
    target = None

    for b in bookings:
        if b["booking_id"].lower() == booking_id.lower() and b["username"].lower() == username.lower():
            target = b
            break

    if target is None:
        print("Booking not found for your account.")
        return

    if target["status"] == "CANCELLED":
        print("This booking is already cancelled.")
        return

    target["status"] = "CANCELLED"
    save_data(BOOKING_FILE, bookings)

    movies = load_data(MOVIE_FILE)
    for m in movies:
        if m["movie_id"] == target["movie_id"]:
            m["available_seats"] += target["seats"]
    save_data(MOVIE_FILE, movies)

    log_action(f"Booking cancelled: {booking_id} by {username}")
    print("Your booking has been cancelled and the amount will be refunded.")