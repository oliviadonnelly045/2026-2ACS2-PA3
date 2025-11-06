

import time

sunday = {}

monday = {}

tuesday = {}

wednesday = {}

thursday = {}

friday = {}

saturday = {}

full_schedule = [sunday, monday, tuesday, wednesday, thursday, friday, saturday]

def add_event(schedule): #function to add an event to the schedule
    schedule_add = input("What day would you like to add to? (Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday)").lower()
    valid_actions = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
    while schedule_add not in valid_actions:
        print("Error. Please pick a valid action.")
        schedule_add = input("What day would you like to add to? (Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday)").lower()
    if schedule_add == "sunday":
        schedule_sun = input("Enter the event you want to add on Sunday ").lower()
        schedule ["Sunday"] = schedule_sun
        #write statement
    elif schedule_add == "monday":
        schedule_mon = input("Enter the event you want to add on Monday ").lower()
        schedule ["Monday"] = schedule_mon
    elif schedule_add == "tuesday":
        schedule_tues = input("Enter the event you want to add on Tuesday ").lower()
        schedule ["Tuesday"] = schedule_tues
    elif schedule_add == "wednesday":
        schedule_wed = input("Enter the event you want to add on Wednesday ").lower()
        schedule ["Wednesday"] = schedule_wed
    elif schedule_add == "thursday":
        schedule_thurs = input("Enter the event you want to add on Thursday ").lower()
        schedule ["Thursday"] = schedule_thurs
    elif schedule_add == "friday":
        schedule_fri = input("Enter the event you want to add on Friday ").lower()
        schedule ["Friday"] = schedule_fri
    elif schedule_add == "saturday":
        schedule_sat = input("Enter the event you want to add on Saturday ").lower()
        schedule ["Saturday"] = schedule_sat
    return schedule

def remove_event(schedule): #function to drop an event in the schedule
    schedule_remove = input("What day would you like to remove from? (Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday)").lower()
    valid_actions = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
    while schedule_remove not in valid_actions:
        print("Error. Please pick a valid action.")
        schedule_remove = input("What day would you like to reset? (Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday)").lower()
    if schedule_remove == "sunday":
        schedule ["Sunday"] = ""
    elif schedule_remove == "monday":
        schedule ["Monday"] = ""
    elif schedule_remove == "tuesday":
        schedule ["Tuesday"] = ""
    elif schedule_remove == "wednesday":
        schedule ["Wednesday"] = ""
    elif schedule_remove == "thursday":
        schedule ["Thursday"] = ""
    elif schedule_remove == "friday":
        schedule ["Friday"] = ""
    elif schedule_remove == "saturday":
        schedule ["Saturday"] = ""
    return schedule

def show_schedule():
    try:
        with open("full_schedule.txt", "r") as f:
            print("\nYour Schedule:\n-----------------")
            for line in f:
                print(line.strip())
                time.sleep(0.2)
    except FileNotFoundError:
        print("No schedule file found yet")
        

def add_schedule():
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    with open("full_schedule.txt", "w") as f:
        for i, day_dict in enumerate(full_schedule):
            if days[i] in day_dict and day_dict[days[i]]:
                f.write(f"{days[i]}: {day_dict[days[i]]}\n")
            else:
                f.write(f"{days[i]}: (no events\n")


#main function
def main():
    global sunday, monday, tuesday, wednesday, thursday, friday, saturday
    user_schedule = {} 
    print("Welcome to your weekly schedule planner!")
    dontstop = True
    while dontstop:
        user_option = input("What would you like to do? (edit, view, or exit) ").lower()
        valid_actions = ["edit", "view", "exit"]
        while user_option not in valid_actions:
            print("Error. Please pick edit, view, or exit.")
            user_option = input("What would you like to do? (edit, view, or exit) ").lower()
        if user_option == "exit":
            add_schedule()
            dontstop = False
            show_schedule()
            break
        elif user_option == "edit":
            edit_choice = input("What would you like to do? (add or remove) ").lower()
            valid_actions = ["add", "remove"]
            while edit_choice not in valid_actions:
                print("Error. Please pick add or remove")
                edit_choice = input("What would you like to do? (add or remove) ").lower()

            if edit_choice == "add":
                user_schedule = add_event(user_schedule)
            elif edit_choice == "remove":
                user_schedule = remove_event(user_schedule)

            for day_dict in full_schedule:
                day_dict.update(user_schedule)
            
            add_schedule()
    


        elif user_option == "view":
            show_schedule()
        


        ask = input("Would you like to keep going? (yes/no) ")
        valid_actions = ["yes", "y", "no", "n"]
        if ask == "no":
            add_schedule()
            dontstop = False
            show_schedule()
                    
            

main()
