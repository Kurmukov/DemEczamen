from Models.Users import Users
class UserContr:
    # Метод регистрации
    @classmethod
    def registration(cls, login, password,FirstName,LastName,):
        Users.create(login = login,
                     password = password,
                     FirstName = FirstName,
                     LastName = LastName,
                     role_id = 2,
                     speciality_id = 1
                     )
    # Метод авторизации
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
    @classmethod
    def check_new_user(cls,user_id):
        if Users.get_or_none(user_id).new:
            return True
    @classmethod
    def update_password(cls, user_id, new_password):
        Users.update({Users.password:new_password}).where(Users.id == user_id).execute()
    @classmethod
    def delete_user(cls,user_id):
        Users.delete().where(Users.id == user_id).execute()
    @classmethod
    def closed(cls, user_id):
        Users.update({Users.closed:True}).where(Users.id == user_id).execute()
    @classmethod
    def un_closed(cls,user):
        Users.update({Users.closed:False}).where(Users.id == user).execute()

    @classmethod
    def update_user(cls, user_id, in_FirstName, in_LastName, in_role_id, in_speciality_id,):
        Users.update({Users.FirstName:in_FirstName,
                        Users.LastName:in_LastName,
                        Users.role_id:in_role_id,
                        Users.speciality_id:in_speciality_id}).where(Users.id == user_id).execute()













if __name__ == "__main__":
    #UserContr.registration('Вася', "Вася123", 'Василия', 'Петров')
    #print(UserContr.auth('Вася', "Вася123"))
    #UserContr.un_closed(1)
    UserContr.update_user(1,"Алексей","Алексеев", "3","1" )

