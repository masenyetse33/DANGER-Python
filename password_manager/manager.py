entries = {}

class Manager:
    def __init__(self, master_password = "password9", program_running = False):
        self.master_password = master_password
        self.program_running = program_running
    
    def check_master_password(self):
        wrong_attempts = 0

        while wrong_attempts < 3:
            password_attempt = input("Enter the master password: ")
            if password_attempt == self.master_password:
                self.program_running = True
                break
            else:
                wrong_attempts += 1
                if wrong_attempts <= 2:
                    print("Wrong Password. Try again.")
                if wrong_attempts == 3:
                    print("You've entered the wrong password three times and have been locked out.")
                    self.program_running = False
    
    def add_entry(self, site, username, password):
        entries[site] = username, password
        entry = f"""\n{site} = username: "{username}", password: "{password}" """
        with open("secrets.txt", "a") as secrets:
            secrets.write(entry)
        print("Entry added succesfuly.")
    
    def get_entry(self, site):
        for key in entries:
            if key == site:
                value = entries[site]
                print(value)
            else:
                print("Site not found.")
    
    def update_entry(self, site, new_username, new_password):
        for key in entries:
            if key == site:
                entries[key] = new_username, new_password
                print("Entry updated succesfully.")
            else:
                print("That site has not been registered before.")
    
    def delete_entry(self, site):
        for key in entries:
            if key == site:
                del entries[key]
                print("Entry deleted succesfully.")
                break
            else:
                print("That site does not exist.")
    
    def list_entries(self):
        if len(entries) == 0:
            print("There are no entries.")
        else:
            print(entries)

manager = Manager()

manager.check_master_password()

while manager.program_running == True:
    user_choice = input("""What would you like to do?
                        Choose 1 to add an entry.
                        Choose 2 to get an entry.
                        Choose 3 to update an entry.
                        Choose 4 to delete an entry.
                        Choose 5 to list all entries.
                        Choose 6 to exit.""")

    match user_choice:
        case "1":
            site = input("Enter the site: ")
            username = input("Enter the username: ")
            password = input("Enter the password: ")
            manager.add_entry(site, username, password)
        case "2":
            site = input("Enter the site of the credentials you'd like to retrieve: ")
            manager.get_entry(site)
        case "3":
            site_to_update = input("Enter the site you'd like to update the credentials of: ")
            new_username = input("Enter the new username: ")
            new_password = input("Enter the new password: ")
            manager.update_entry(site_to_update, new_username, new_password)
        case "4":
            site_to_delete = input("Enter the site of the entry you'd like to delete: ")
            manager.delete_entry(site_to_delete)
        case "5":
            manager.list_entries()
        case "6":
            print("Goodbye")
            manager.program_running = False
        case _:
            print("Choose a valid option")