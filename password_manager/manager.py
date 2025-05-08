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
                print("Wrong Password. Try again.")
                wrong_attempts += 1
                if wrong_attempts == 3:
                    print("You've entered the wrong password three times and have been locked out.")
                    self.program_running = False

manager = Manager()

manager.master_password()