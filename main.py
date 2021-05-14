from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from datetime import datetime

Builder.load_file('design.kv')

class MainScreen(Screen):
    def sign_up(self):
        self.manager.current = "sign_up_screen"
            
    def go_to_login(self):
        self.manager.current ="login_screen"


class SignUpScreen(Screen):
    def add_user(self, uname, pword, email):
        with open ('users.json') as file:
           users = json.load(file)
        
    
        #check if user already exist based on email
        emails=[users["user " +str(i+1)]["email"] for i in range(len(users))]
        if email.text in emails:
            print("User already registered")
            print(email.text)
            print(emails)
        else:
            # assign new user number
            user_no = "user " + str(len(users)+1)
            users[user_no] = {"username": uname.text, "email": email.text, "password": pword.text}

            print("New user")
            with open("users.json", "w") as f:
                json.dump(users, f)
                self.manager.current = "sign_up_screen_success"

class SignUpScreenSuccess(Screen):
    def go_to_login(self):
        self.manager.current ="login_screen"

class LoginScreen(Screen):
    def login(self, uname, pword):
        print(uname, pword)

        with open("users.json") as f:
            users = json.load(f)

    #check user exist and get user number
        for i in range(len(users)):
            username= users["user " +str(i+1)]["username"]
   
            if username == uname:      
                user_no = "user " +str(i+1)
                print(user_no)
                break
            else:
                self.ids.login_wrong.text = "User name does not exist"
                return

        #check user password
        if users[user_no]["password"] == pword:
            print('login successful')
            self.manager.transition.direction = 'right'
            self.manager.current = "main_screen"
        else:
            self.ids.login_wrong.text = "Wrong password"
            return
    
    def sign_up(self):
        self.manager.current = "sign_up_screen"

    def forgot_password(self):        
        self.manager.current = "Forgot_password_screen"

class ForgotPwordScreen(Screen):
    def send_details(self, email):
        print(email)
        #open file
        with open ('users.json') as file:
           users = json.load(file)
        
        #check email exists
        all_emails=[users["user " +str(i+1)]["email"] for i in range(len(users))]

        #check user exist and get user number
        if email in all_emails:                  
            print('We sent you an email with your details')
            print ('email')

            user_no =  'user ' + str(all_emails.index(email)+1)
            print(users[user_no]["password"])
            self.ids.info.text = 'We sent you an email with your details'               
        else:
            print('email not recognised')
            self.ids.info.text = 'email not recognised'
   
    def sign_up(self):
        self.manager.current = "sign_up_screen"

    def go_to_login(self):
        self.manager.current ="login_screen"


class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()
    
