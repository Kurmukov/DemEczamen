from SRC.Model.Users import *

class User_Controller():
    def log_in(self,input_login, input_password):
        user = Users.get(Users.login == input_login, Users.password == input_password)
        if user:
            return True
        else:
            return False


if __name__ == "__main__":
    users = User_Controller()
    print(users.log_in("Admin","1234"))