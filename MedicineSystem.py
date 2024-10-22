import schedule
import time
from datetime import datetime

# Dictionary to store medicine details
medicines = {}

# Function to add a medicine to the schedule
def add_medicine(medicine_name, dose, time_to_take):
    medicines[medicine_name] = {'dose': dose, 'time': time_to_take}
    schedule.every().day.at(time_to_take).do(remind_medicine, medicine_name, dose)

# Function to remind the user to take the medicine
def remind_medicine(medicine_name, dose):
    print(f"Reminder: It's time to take {dose} of {medicine_name} ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')})")

# Function to display all medicines
def list_medicines():
    if not medicines:
        print("No medicines scheduled.")
    else:
        for med_name, details in medicines.items():
            print(f"{med_name}: {details['dose']} at {details['time']}")

# Main loop to keep the schedule running
def start_reminder_system():
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    # Example: Add some medicines with their respective times
    add_medicine("Paracetamol", "1 pill", "12:00")
    add_medicine("Vitamin C", "500 mg", "14:00")
    
    print("Medicine reminder system started!")
    list_medicines()
    
    # Start the reminder system
    start_reminder_system()


