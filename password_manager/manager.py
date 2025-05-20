class Manager:
    def __init__(self, password = "password9", program_running = False):
        self.password = password
        self.program_running = program_running
    
    def master_password(self):
        wrong_attempts = 0

        while wrong_attempts < 3:
            password_attempt = input("Enter the password: ")
            if password_attempt == self.password:
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
        entry = f"""\n{site} = username: "{username}", password: "{password}" """
        secrets = open("secrets.txt", "a")
        secrets.write(entry)

manager = Manager()

manager.master_password()

site = input("Enter the site: ")
username = input("Enter the username: ")
password = input("Enter the password: ")

manager.add_entry(site, username, password)