from Models.Users import Users
class UserContr:
    # Метод регистрации
    @classmethod
    def registration(cls, login, password,FirstName,LastName):
        Users.create(login = login,
                     password = password,
                     FirstName = FirstName,
                     LastName = LastName,
                     role_id = 2
                     )
    # Мктод авторизации
    @classmethod
    #Метод аутентификации
    def auth(cls,login,password):
        #Проверка наличия логина в таблице
        if Users.get_or_none(Users.login == login) != None:
            #Проверить соответствие введенного логина и пароля
            if Users.get_or_none(Users.login == login, Users.password == password) != None:
                return True
        else:
            return False



if __name__ == "__main__":
    #UserContr.registration('Вася', "Вася123", 'Василия', 'Петров')
    print(UserContr.auth('Вася', "Вася123"))

