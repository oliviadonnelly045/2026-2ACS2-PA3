
DAYS = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
schedule = {day: [] for day in DAYS}




def load_schedule(filename="full_schedule.txt"): #load all saved events from file
    try:
        with open(filename, "r") as f:
            current_day = None #keeps track of current day being read
            for line in f:
                line = line.rstrip("\n")
                if line.endswith(":"): #if the line has a colon in it (the titles of the days do)
                    day_name = line[:-1] #remove colon
                    if day_name in DAYS: #check if it is a valid day
                        current_day = day_name #mark this as current day
                    else:
                        current_day = None
                    continue
                
                if current_day: #read events if inside of a valid day
                    if line.startswith(" - "):
                        schedule[current_day].append(line[3:])
    except FileNotFoundError:
        pass


def add_schedule(filename="full_schedule.txt"): #save the entire schedule
    with open(filename, "w") as f:
        for day in DAYS:
            f.write(day + ":\n") #if the selected day has events stored in the dictionary
            if schedule[day]: #checks if list is not empty
                for item in schedule[day]:
                    f.write(" - " + item + "\n")
            else: #if no events exist for that day
                f.write(" (no events)\n")
            f.write("\n")
    f.close()

def add_event(): #add one event to a chosen day
    day = input("What day would you like to add to? (Sunday-Saturday) ").strip().title() #ask user which day to add the event to
    while day not in DAYS: #if invalid day, ask again until valid
        print("Error. Please pick a valid action.")
        day = input("What day would you like to add to? (Sunday-Saturday) ").strip().title()

    time_str = input("Enter the time: ").strip() #have user enter a time
    event = input("Enter the event name: ").strip() #have user enter the event name

    for e in schedule[day]: #event can only occur once per day
        if event.lower() in e.lower(): #checks for event duplication
            print(f"That event already exits on {day}. Each event can only be on one day.")
            return #stop function if the event already exists
            
    if event: #add to schedule if event name is not empty
        new = f"{time_str} - {event}" if time_str else event#combines the time and event name into one string
        schedule[day].append(new)
        add_schedule()
    else:
        print("No event entered.")



def remove_event(): #function to drop all events from a day in the schedule
    day = input("Remove from which day? (Sunday-Saturday) ").strip().title() #ask user which day they want to clear
    while day not in DAYS: #if invalid day, ask again until valid
        print("Error. Please pick a valid action.")
        day = input("What day would you like to add to? (Sunday-Saturday) ").strip().title()
    
    if not schedule[day]: #if nothing is scheduled on that day exit
        print(f"{day} has no events.")
        return
    while True: #ask user to confirm removal
        confirm = input(f"Are you sure you want to remove all events from {day}? (yes/no) ").strip().lower()
        if confirm in ["yes", "y"]:
            removed_events = schedule[day].copy() #makes a copy of the list for that day before deleting
            schedule[day] = [] #clear all events on that day
            print(f"All events removed from {day}.")
            with open("full_schedule.txt", "a") as f:
                f.write(f"\n{day}: [removed all]\n")
                for item in removed_events:
                    f.write(f"  - {item}\n")
            add_schedule()
            break
        elif confirm in ("no", "n"): #user cancels removal
            print("Cancelled removal.")
            break
        else:
            print("please select a valid action")

  
def show_schedule(): #print current schedule
    print("\nYour Schedule:\n-----------------")
    try:
        with open("full_schedule.txt", "r") as txt: #open the file to read
            print(txt.read()) #print full saved schedule from .txt file
    except FileNotFoundError:
        print("(No schedule saved yet.)")
    print("---------------\n")


#main function
def main():
    print("Welcome to your weekly schedule planner!")
    load_schedule()
    dontstop = True #keep running until user chooses to exit
    while dontstop:
        user_option = input("What would you like to do? (add, remove, view, or exit) ").strip().lower() #ask user what they want to do
        valid_actions = ["add", "remove", "view", "exit"]
        while user_option not in valid_actions: #if not one of the valid actions, then ask again
            print("Error. Please pick add, remove, view, or exit.")
            user_option = input("What would you like to do? (add, remove, view, or exit) ").strip().lower()
        if user_option == "add": #user wants to add an event
            add_event() #call function to add event
            add_schedule() #make sure file is updated
        elif user_option == "remove": #user wants to remove all events on a day
            remove_event()
            add_schedule()
        elif user_option == "view": #user wants to see their full schedule
            show_schedule()
        elif user_option == "exit": #quits the program
            add_schedule()
            show_schedule() #print schedule before quitting
            print("schedule saved to full_schedule.txt. Goodbye.")
            break

main()
