import re 

class Password():
    
    def __init__(self, user, password) -> None:
        """Class for a password detector."""
        self.user = user
        self.password = password
    
    def password_verification(self):
        """Check for a strong password"""
        regex = re.compile(r'\d*')
        match_object = regex.search(self.password)
        x = match_object.group()
        data = [char for char in x]
        if len(data) > 8:
            print("Secret password has at least 8 characters")
        else: 
            print("Please, type a password that has at least 8 characters.")
    
    def hello_user(self): 
        """Print a greeting to the user."""
        message = (f'Hello {self.user.title()}')
        print(message)

new_user = Password('Hayley', '995955595595')
new_user.password_verification()