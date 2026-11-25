import csv
# PROJECT: CAMPUSCONNECT
# College Event Management System
# Language: Python
# Data Storage: CSV Files

# Display the main menu
def display_menu():
    print("WELCOME TO CAMPUSCONNECT")
    print(" College Event Management System")
    print("1. Student Portal")
    print("2. Admin / Coordinator Portal")
    print("3. Exit")


# Control the main program
def main():

    while True:

        display_menu()

        choice = input("\nEnter your choice: ")

        if choice == "1":
            student_portal()

        elif choice == "2":

            # Check admin password before login
            password = input("Enter Admin Password: ")

            if password == "admin123":
                print("Login Successful!")
                admin_portal()
            else:
                print("Wrong Password!")

        elif choice == "3":
            print("\nThank you for using CampusConnect!")
            break

        else:
            print("\nInvalid choice! Please try again.")

# STUDENT PORTAL FUNCTIONS

# Display all available college events
def view_events():

    print("\n     ALL COLLEGE EVENTS    ")

    # Read event details from CSV file
    with open("events.csv", "r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        for event in reader:
            print("\nEvent ID:", event["event_id"])
            print("Name:", event["event_name"])
            print("Category:", event["category"])
            print("Date:", event["date"])
            print("Venue:", event["venue"])
            print("Organizer:", event["organizer"])
            print("Registration:", event["registration_status"])


# Search events according to category
def search_events():

    category = input("\nEnter category (Cultural/Sports): ")

    found = False

    # Read events and match the selected category
    with open("events.csv", "r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        for event in reader:
            if category.lower() in event["category"].lower():
                print("\n", event["event_name"])
                print("Date:", event["date"])
                print("Venue:", event["venue"])
                found = True

    # Display message if no event matches
    if found == False:
        print("No event found.")


# Register a student for an event
def register_event():

    name = input("\nEnter your name: ")
    student_id = input("Enter your student ID: ")
    event_id = input("Enter event ID: ")

    # Check whether the entered event ID exists
    event_found = False

    with open("events.csv", "r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        for event in reader:
            if event["event_id"].lower() == event_id.lower():
                event_found = True
                event_name = event["event_name"]

    # Stop registration if event ID is invalid
    if event_found == False:
        print("Invalid event ID.")
        return

    # Read all previous registrations
    registrations = []

    with open("registration.csv", "r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        for row in reader:
            registrations.append(row)

    # Prevent the same student from registering twice
    for row in registrations:
        if row["student_id"] == student_id and row["event_id"] == event_id:
            print("You are already registered for this event.")
            return

    # Generate a new registration ID
    registration_id = "R" + str(len(registrations) + 1)

    # Save old and new registrations in CSV file
    with open("registration.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        # Write CSV column headings
        writer.writerow(["registration_id", "student_name", "student_id", "event_id"])

        # Keep all previous registrations
        for row in registrations:
            writer.writerow([
                row["registration_id"],
                row["student_name"],
                row["student_id"],
                row["event_id"]
            ])

        # Add the new registration
        writer.writerow([registration_id, name, student_id, event_id])

    print("\nRegistration successful!")
    print("Registration ID:", registration_id)
    print("Event:", event_name)


# Display all student registrations
def view_registrations():

    print("\n     ALL REGISTRATIONS    ")

    # Read registration details from CSV file
    with open("registration.csv", "r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        for row in reader:
            print("\nRegistration ID:", row["registration_id"])
            print("Student Name:", row["student_name"])
            print("Student ID:", row["student_id"])
            print("Event ID:", row["event_id"])


# Remove a student registration
def remove_registration():

    registration_id = input("Enter Registration ID to remove: ")

    registrations = []

    # Read all existing registrations
    with open("registration.csv", "r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        for row in reader:
            registrations.append(row)

    new_registrations = []
    found = False

    # Keep all registrations except the selected one
    for row in registrations:
        if row["registration_id"].lower() == registration_id.lower():
            found = True
        else:
            new_registrations.append(row)

    # Check whether registration ID exists
    if found == False:
        print("Registration ID not found.")
        return

    # Update the registration CSV file
    with open("registration.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["registration_id", "student_name", "student_id", "event_id"])

        for row in new_registrations:
            writer.writerow([
                row["registration_id"],
                row["student_name"],
                row["student_id"],
                row["event_id"]
            ])

    print("Registration removed successfully!")


# Display the student portal menu
def student_portal():

    while True:

        print("\n     STUDENT PORTAL    ")
        print("1. View Events")
        print("2. Search Events")
        print("3. Register for Event")
        print("4. View Registrations")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_events()

        elif choice == "2":
            search_events()

        elif choice == "3":
            register_event()

        elif choice == "4":
            view_registrations()

        elif choice == "5":
            break

        else:
            print("Invalid choice. Try again.")



# ADMIN PORTAL FUNCTIONS

# Add a new college event
def add_event():

    print("\n    ADD NEW EVENT    ")

    event_name = input("Enter event name: ")
    category = input("Enter category: ")
    date = input("Enter event date: ")
    time = input("Enter event time: ")
    venue = input("Enter venue: ")
    description = input("Enter description: ")
    organizer = input("Enter organizer: ")
    status = input("Enter registration status: ")
    link = input("Enter registration link (if any): ")
    seats = input("Enter number of seats (if known): ")

    # Read existing events to generate a new ID
    with open("events.csv", "r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        events = list(reader)

    # Generate a unique event ID
    event_id = "E" + str(101 + len(events))

    # Save the new event in the CSV file
    with open("events.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow([
            event_id, event_name, category, date, time,
            venue, description, organizer, status, link, seats
        ])

    print("\nEvent added successfully!")
    print("Your Event ID is:", event_id)


# Remove an event and its related registrations
def remove_event():

    event_id = input("Enter Event ID to remove: ")

    events = []

    # Read all existing events
    with open("events.csv", "r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        for row in reader:
            events.append(row)

    new_events = []
    found = False

    # Keep all events except the selected event
    for event in events:
        if event["event_id"].lower() == event_id.lower():
            found = True
        else:
            new_events.append(event)

    # Stop if event ID does not exist
    if found == False:
        print("Event ID not found.")
        return

    # Remove registrations linked to this event
    registrations = []

    with open("registration.csv", "r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["event_id"].lower() != event_id.lower():
                registrations.append(row)

    # Update the registration CSV file
    with open("registration.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["registration_id", "student_name", "student_id", "event_id"])

        for row in registrations:
            writer.writerow([
                row["registration_id"],
                row["student_name"],
                row["student_id"],
                row["event_id"]
            ])

    # Update the events CSV file
    with open("events.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow([
            "event_id", "event_name", "category", "date", "time",
            "venue", "description", "organizer", "registration_status",
            "registration_link", "seats"
        ])

        # Write all events except the deleted event
        for event in new_events:
            writer.writerow([
                event["event_id"],
                event["event_name"],
                event["category"],
                event["date"],
                event["time"],
                event["venue"],
                event["description"],
                event["organizer"],
                event["registration_status"],
                event["registration_link"],
                event["seats"]
            ])

    print("Event removed successfully!")


# Display the admin portal menu
def admin_portal():

    while True:

        print("\n    ADMIN PORTAL   ")
        print("1. View All Events")
        print("2. View All Registrations")
        print("3. Add New Event")
        print("4. Remove Registration")
        print("5. Remove Event")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_events()

        elif choice == "2":
            view_registrations()

        elif choice == "3":
            add_event()

        elif choice == "4":
            remove_registration()

        elif choice == "5":
            remove_event()

        elif choice == "6":
            break

        else:
            print("Invalid choice! Try again.")

# START THE PROGRAM
main()
