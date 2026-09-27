from storage import load_data, save_data
from utils import generate_id, is_valid_name, is_positive_number
from logger import log_action

MOVIE_FILE = "movies.json"

def add_movie():
    title = input("Enter movie title: ").strip()
    if not is_valid_name(title):
        print("Movie title cannot be empty.")
        return

    language = input("Enter language: ").strip()
    show_time = input("Enter show time (e.g. 6:00 PM): ").strip()
    price = input("Enter ticket price: ").strip()
    seats = input("Enter total number of seats: ").strip()

    if not is_positive_number(price):
        print("Price must be a positive number.")
        return

    if not seats.isdigit() or int(seats) <= 0:
        print("Total seats must be a positive whole number.")
        return

    movies = load_data(MOVIE_FILE)

    new_movie = {
        "movie_id": generate_id("MOV"),
        "title": title,
        "language": language if language else "N/A",
        "show_time": show_time if show_time else "N/A",
        "price": float(price),
        "total_seats": int(seats),
        "available_seats": int(seats)
    }

    movies.append(new_movie)
    save_data(MOVIE_FILE, movies)
    log_action(f"Movie added: {title} ({new_movie['movie_id']})")

    print(f"Movie '{title}' added successfully with ID {new_movie['movie_id']}.")


def view_movies():
    movies = load_data(MOVIE_FILE)

    if not movies:
        print("No movies have been added yet.")
        return

    print("\n--- Now Showing ---")
    print(f"{'ID':<8}{'Title':<20}{'Language':<12}{'Time':<10}{'Price':<8}{'Seats Left'}")
    for m in movies:
        print(f"{m['movie_id']:<8}{m['title']:<20}{m['language']:<12}"
              f"{m['show_time']:<10}{m['price']:<8}{m['available_seats']}")
    print()

def find_movie_by_id(movie_id):
    movies = load_data(MOVIE_FILE)
    for m in movies:
        if m["movie_id"].lower() == movie_id.lower():
            return m
    return None


def search_movie():
    keyword = input("Enter movie title to search: ").strip().lower()
    movies = load_data(MOVIE_FILE)

    results = [m for m in movies if keyword in m["title"].lower()]

    if not results:
        print("No matching movies found.")
        return

    print("\n--- Search Results ---")
    for m in results:
        print(f"{m['movie_id']} - {m['title']} ({m['language']}) "
              f"at {m['show_time']} - Rs.{m['price']} "
              f"[{m['available_seats']} seats left]")
    print()