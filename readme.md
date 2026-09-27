# Movie Ticket Booking System

A modular, lightweight Python terminal application designed for booking movie tickets, managing theater schedules, tracking real-time seat availability, and generating sales reports.

## Project Overview: 

**Cinema Seat** provides a command-line interface (CLI) for both moviegoers and cinema administrators. It addresses the need for a simple, dependency-free reservation platform by utilizing built-in Python modules and local JSON data storage. The application supports user authentication, seat allocation management, booking cancellations, and event logging.

## Features: 

### Customer Features: 
* **User Accounts:** Quick registration and sign-in functionality.
* **Movie Catalog:** View scheduled movies complete with showtimes, ticket pricing, and real-time seat counts.
* **Search:** Search active movie listings by title keyword.
* **Ticket Booking:** Reserve available seats with automated total cost calculations and unique booking IDs.
* **Booking History & Cancellation:** View active bookings and cancel reservations to automatically release seats back to the venue catalog.

### Admin Features: 
* **First-Time Admin Setup:** Registering with the username `admin` unlocks administrative capabilities.
* **Movie Inventory Management:** Add new movies with details like title, language, showtimes, price, and total capacity.
* **Sales & Revenue Reports:** View overall performance metrics, including total sales, total revenue, and the top-performing movie.
* **Activity Logging:** Key operational events (logins, bookings, catalog updates) are recorded with timestamps in `logs.txt`.

## Technologies & Tools Used: 

* **Language:** Python 3.14.6
* **Core Libraries:** `json`, `os`, `datetime`, `random` (Standard Library only)
* **Data Persistence:** Local JSON files (`users.json`, `movies.json`, `bookings.json`)
* **Logging:** Plain-text audit log (`logs.txt`)

## Steps to Install & Run the Project: 

### Prerequisites
Ensure you have **Python 3.14.6 or higher** installed on your system.

### Installation
1. Clone or download the repository to your local machine:
   ```bash
   git clone https://github.com/vinayakgupta-20/movie-ticket-management-system.git
   cd movie-ticket-management-system/
   ```
   > Ensure that git is installed on your system.

2. Verify project structure:
   ```text
   movie_ticket_system/
   ├── main.py
   ├── auth.py
   ├── booking.py
   ├── movies.py
   ├── report.py
   ├── storage.py
   ├── utils.py
   ├── logger.py
   └── data/
   ```

### Running the Application: 
Launch the terminal application by running:
```bash
python main.py
```

## 🧪 Instructions for Testing

Follow these manual testing steps to verify system functionality:

1. **Admin Registration & Login Test:**
   * Select `1. Create Account` and set the username to `admin`.
   * Log out and select `2. Sign In` using `admin`. Verify access to the **Admin Dashboard**.

2. **Movie Creation Test:**
   * In the Admin Dashboard, select `1. Add New Movie`.
   * Input details (e.g., Title: `Hanuman Ansh`, Language: `Hindi`, Time: `06:00 PM`, Price: `199`, Seats: `40`).
   * Verify the movie appears in `2. View All Movies`.

3. **Customer Registration & Booking Test:**
   * Log out of `admin` and create a new customer account (e.g., `john_doe`).
   * Select `1. Browse Movies` to check the Movie ID.
   * Select `3. Book Tickets`, enter the Movie ID, and reserve 2 seats.
   * Check `4. My Bookings` to confirm ticket reservation and unique reference ID generation.

4. **Cancellation Test:**
   * Select `5. Cancel a Booking` and input your Booking ID.
   * Verify that seat availability increases back to original count in `1. Browse Movies`.

5. **Log & Sales Report Test:**
   * Sign back into `admin` and select `3. View Revenue & Sales Report` to verify recorded statistics.
   * Check `logs.txt` in the root directory to confirm timestamped logs for all completed actions.
