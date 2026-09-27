## Problem Statement: 
Traditional small-scale cinemas often rely on manual booking records or complex, heavy software solutions that require active internet connections and database configurations. This can lead to double-booking errors, inconsistent seat tracking, lack of revenue visibility, and inefficient management of movie schedules.
There is a need for a lightweight, self-contained terminal-based application that simplifies theater ticket reservations, keeps track of seat inventory in real time, provides access control for administrative duties, and logs operational events without requiring third-party library dependencies.

## Scope of the Project: 
The Cinema Seat Booking System is designed as a local terminal-based Python program using persistent JSON files for data management.
·	User registration and authentication (Customer vs. Admin role separation).
·	Movie catalog listing, searching, and seating capacity management.
·	Ticket reservation workflow with instant seat calculation and unique booking reference generation.
·	Booking cancellation mechanism that restores canceled seats back to available inventory.
·	Admin dashboard for adding movies and viewing aggregated revenue/sales metrics.
·	System activity logging to logs.txt with timestamp tracking.

## Target Users: 
1.	Cinema Customers / Moviegoers: 
2.	Cinema Administrators / Staff

## High-Level Features: 
·	Authentication Module (auth.py): Handles user sign-up and sign-in, granting admin access to accounts registered under the username admin.
·	Catalog Management (movies.py): Supports adding new movies, viewing available titles in a formatted table, and searching listings by keyword.
·	Reservation Engine (booking.py): Enables ticket booking with real-time seat availability checks, price calculations, and cancellation processing.
·	Reporting Engine (report.py): Summarizes overall sales performance, total tickets sold, gross revenue, and identifies top-selling movies.
·	Audit Logger (logger.py): Automatically appends system actions and timestamps to a persistent logs.txt file.
·	Storage Handler (storage.py): Manages file I/O operations with the data/ directory using JSON storage.
