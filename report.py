from storage import load_data
from booking import BOOKING_FILE


def show_sales_report():
    bookings = load_data(BOOKING_FILE)
    active_bookings = [b for b in bookings if b["status"] == "CONFIRMED"]

    if not active_bookings:
        print("No sales data available yet.")
        return

    total_tickets = 0
    total_revenue = 0
    movie_count = {}

    for b in active_bookings:
        total_tickets += b["seats"]
        total_revenue += b["amount"]
        title = b["movie_title"]
        movie_count[title] = movie_count.get(title, 0) + b["seats"]

    top_movie = max(movie_count, key=movie_count.get)

    print("\n--- Sales Report ---")
    print(f"Total confirmed bookings : {len(active_bookings)}")
    print(f"Total tickets sold       : {total_tickets}")
    print(f"Total revenue            : Rs.{total_revenue}")
    print(f"Most popular movie       : {top_movie} ({movie_count[top_movie]} tickets)")
    print()