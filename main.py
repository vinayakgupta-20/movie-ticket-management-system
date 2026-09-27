from auth import register_user, login_user
from movies import add_movie, view_movies, search_movie
from booking import book_ticket, view_my_bookings, cancel_booking
from report import show_sales_report
from logger import log_action

ADMIN_USERNAME = "admin"

def customer_menu(username):
    while True:
        print("\n--- CUSTOMER MENU ---")
        print("1. View Movies")
        print("2. Search Movie")
        print("3. Book Ticket")
        print("4. View My Bookings")
        print("5. Cancel Booking")
        print("6. Logout")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_movies()
        elif choice == "2":
            search_movie()
        elif choice == "3":
            book_ticket(username)
        elif choice == "4":
            view_my_bookings(username)
        elif choice == "5":
            cancel_booking(username)
        elif choice == "6":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

def admin_menu():
    while True:
        print("\n--- ADMIN MENU ---")
        print("1. Add New Movie")
        print("2. View Movies")
        print("3. View Sales Report")
        print("4. Logout")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_movie()
        elif choice == "2":
            view_movies()
        elif choice == "3":
            show_sales_report()
        elif choice == "4":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


def main():
    print("--- WELCOME TO MOVIE TICKET BOOKING SYSTEM ---")

    log_action("Application started")

    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            register_user()

        elif choice == "2":
            username = login_user()
            if username is not None:
                if username.lower() == ADMIN_USERNAME:
                    admin_menu()
                else:
                    customer_menu(username)

        elif choice == "3":
            print("Thank you for using the Movie Ticket Booking System.")
            log_action("Application closed")
            break

        else:
            print("Invalid choice. Please enter 1, 2 or 3.")

if __name__ == "__main__":
    main()