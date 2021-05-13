from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from datetime import datetime

Builder.load_file('design.kv')

class MainScreen(Screen):
    def sign_up(self):
        self.manager.current = "sign_up_screen"
        print("sign up button pressed")

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
    pass

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()
    
