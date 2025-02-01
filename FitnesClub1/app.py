import tkinter as tk
from tkinter import messagebox, ttk
from Models.Users import Users
from Controllers.UserContr import UserContr
class AuthWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Авторизация")
        self.root.geometry("300x200")

        # Поле для логина
        self.label_login = tk.Label(root, text="Логин:")
        self.label_login.pack(pady=5)

        self.entry_login = tk.Entry(root)
        self.entry_login.pack(pady=5)

        # Поле для пароля
        self.label_password = tk.Label(root, text="Пароль:")
        self.label_password.pack(pady=5)

        self.entry_password = tk.Entry(root, show="*")
        self.entry_password.pack(pady=5)

        # Кнопка входа
        self.button_login = tk.Button(root, text="Войти", command=self.login)
        self.button_login.pack(pady=10)

    def login(self):
        login = self.entry_login.get()
        password = self.entry_password.get()

        if UserContr.auth(login, password):
            self.root.destroy()  # Закрыть окно авторизации
            admin_window = tk.Tk()  # Открыть окно администратора
            AdminWindow(admin_window)
            admin_window.mainloop()
        else:
            messagebox.showerror("Ошибка", "Неверный логин или пароль")

class AdminWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Панель администратора")
        self.root.geometry("1200x600")

        # Таблица для отображения сотрудников
        self.tree = ttk.Treeview(
            root,
            columns=("ID", "FirstName", "LastName", "Login", "RoleID", "SpecialityID"),
            show="headings"
        )
        self.tree.heading("ID", text="ID")
        self.tree.heading("FirstName", text="Имя")
        self.tree.heading("LastName", text="Фамилия")
        self.tree.heading("Login", text="Логин")
        self.tree.heading("RoleID", text="Роль (ID)")
        self.tree.heading("SpecialityID", text="Специальность (ID)")
        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Кнопка для обновления списка сотрудников
        self.button_refresh = tk.Button(root, text="Обновить список", command=self.refresh_users)
        self.button_refresh.pack(pady=5)

        # Фрейм для размещения блоков "Добавление пользователя" и "Изменение данных пользователя"
        self.control_frame = tk.Frame(root)
        self.control_frame.pack(fill=tk.X, padx=10, pady=10)

        # Блок "Добавление пользователя" (левая колонка)
        self.add_user_frame = tk.Frame(self.control_frame)
        self.add_user_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.label_new_user = tk.Label(self.add_user_frame, text="Добавить нового пользователя", font=("Arial", 12))
        self.label_new_user.pack(pady=5)

        self.label_new_firstname = tk.Label(self.add_user_frame, text="Имя:")
        self.label_new_firstname.pack(pady=5)

        self.entry_new_firstname = tk.Entry(self.add_user_frame)
        self.entry_new_firstname.pack(pady=5)

        self.label_new_lastname = tk.Label(self.add_user_frame, text="Фамилия:")
        self.label_new_lastname.pack(pady=5)

        self.entry_new_lastname = tk.Entry(self.add_user_frame)
        self.entry_new_lastname.pack(pady=5)

        self.label_new_login = tk.Label(self.add_user_frame, text="Логин:")
        self.label_new_login.pack(pady=5)

        self.entry_new_login = tk.Entry(self.add_user_frame)
        self.entry_new_login.pack(pady=5)

        self.label_new_password_add = tk.Label(self.add_user_frame, text="Пароль:")
        self.label_new_password_add.pack(pady=5)

        self.entry_new_password_add = tk.Entry(self.add_user_frame, show="*")
        self.entry_new_password_add.pack(pady=5)

        self.button_add_user = tk.Button(self.add_user_frame, text="Добавить пользователя", command=self.add_user)
        self.button_add_user.pack(pady=10)

        # Блок "Изменение данных пользователя" (правая колонка)
        self.update_user_frame = tk.Frame(self.control_frame)
        self.update_user_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.label_update_user = tk.Label(self.update_user_frame, text="Изменить данные пользователя", font=("Arial", 12))
        self.label_update_user.pack(pady=5)

        self.label_update_user_id = tk.Label(self.update_user_frame, text="ID пользователя:")
        self.label_update_user_id.pack(pady=5)

        self.entry_update_user_id = tk.Entry(self.update_user_frame)
        self.entry_update_user_id.pack(pady=5)

        self.label_update_firstname = tk.Label(self.update_user_frame, text="Новое имя:")
        self.label_update_firstname.pack(pady=5)

        self.entry_update_firstname = tk.Entry(self.update_user_frame)
        self.entry_update_firstname.pack(pady=5)

        self.label_update_lastname = tk.Label(self.update_user_frame, text="Новая фамилия:")
        self.label_update_lastname.pack(pady=5)

        self.entry_update_lastname = tk.Entry(self.update_user_frame)
        self.entry_update_lastname.pack(pady=5)

        self.label_update_role_id = tk.Label(self.update_user_frame, text="Новая роль (ID):")
        self.label_update_role_id.pack(pady=5)

        self.entry_update_role_id = tk.Entry(self.update_user_frame)
        self.entry_update_role_id.pack(pady=5)

        self.label_update_speciality_id = tk.Label(self.update_user_frame, text="Новая специальность (ID):")
        self.label_update_speciality_id.pack(pady=5)

        self.entry_update_speciality_id = tk.Entry(self.update_user_frame)
        self.entry_update_speciality_id.pack(pady=5)

        self.button_update_user = tk.Button(self.update_user_frame, text="Изменить данные", command=self.update_user_data)
        self.button_update_user.pack(pady=10)

        # Блок "Изменение пароля"
        self.update_password_frame = tk.Frame(self.control_frame)
        self.update_password_frame.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

        self.label_update_password = tk.Label(self.update_password_frame, text="Изменить пароль", font=("Arial", 12))
        self.label_update_password.pack(pady=5)

        self.label_password_user_id = tk.Label(self.update_password_frame, text="ID пользователя:")
        self.label_password_user_id.pack(pady=5)

        self.entry_password_user_id = tk.Entry(self.update_password_frame)
        self.entry_password_user_id.pack(pady=5)

        self.label_new_password = tk.Label(self.update_password_frame, text="Новый пароль:")
        self.label_new_password.pack(pady=5)

        self.entry_new_password = tk.Entry(self.update_password_frame, show="*")
        self.entry_new_password.pack(pady=5)

        self.button_update_password = tk.Button(self.update_password_frame, text="Изменить пароль", command=self.update_password)
        self.button_update_password.pack(pady=10)

        # Блок "Блокировка/разблокировка пользователя"
        self.block_user_frame = tk.Frame(self.control_frame)
        self.block_user_frame.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

        self.label_block_user = tk.Label(self.block_user_frame, text="Блокировка/разблокировка", font=("Arial", 12))
        self.label_block_user.pack(pady=5)

        self.label_block_user_id = tk.Label(self.block_user_frame, text="ID пользователя:")
        self.label_block_user_id.pack(pady=5)

        self.entry_block_user_id = tk.Entry(self.block_user_frame)
        self.entry_block_user_id.pack(pady=5)

        self.button_toggle_block = tk.Button(self.block_user_frame, text="Изменить блокировку",
                                             command=self.toggle_user_block)
        self.button_toggle_block.pack(pady=10)



        # Загрузить список сотрудников при запуске
        self.refresh_users()

    def refresh_users(self):
        """Обновить список сотрудников в таблице"""
        for row in self.tree.get_children():
            self.tree.delete(row)  # Очистить таблицу

        users = Users.select()  # Вывод всех пользователей
        for user in users:
            self.tree.insert("",tk.END,values=(user.id,
                                               user.FirstName,
                                               user.LastName,
                                               user.login,
                                               user.role_id,
                                               user.speciality_id)
                             )

    def add_user(self):
        """Добавить нового пользователя"""
        firstname = self.entry_new_firstname.get()
        lastname = self.entry_new_lastname.get()
        login = self.entry_new_login.get()
        password = self.entry_new_password_add.get()

        if firstname and lastname and login and password:
            try:
                # Вызов метода регистрации
                UserContr.registration(login, password, firstname, lastname)
                messagebox.showinfo("Успех", "Пользователь успешно добавлен")
                self.refresh_users()  # Обновить список
            except ValueError:
                messagebox.showerror("Ошибка", f"Не удалось добавить пользователя:")

    def update_user_data(self):
        """Обновление данных пользователя"""
        user_id = self.entry_update_user_id.get()
        firstname = self.entry_update_firstname.get()
        lastname = self.entry_update_lastname.get()
        role_id = self.entry_update_role_id.get()
        speciality_id = self.entry_update_speciality_id.get()

        if user_id:
            try:
                user_id = int(user_id)
                role_id = int(role_id) if role_id else None
                speciality_id = int(speciality_id) if speciality_id else None

                # Вызов метода обновления данных пользователя
                UserContr.update_user(
                    user_id=user_id,
                    in_FirstName=firstname,
                    in_LastName=lastname,
                    in_role_id=role_id,
                    in_speciality_id=speciality_id
                )
                messagebox.showinfo("Успех", "Данные пользователя успешно обновлены")

            except ValueError:
                messagebox.showerror("Ошибка", f"Не удалось обновить данные пользователя:")


    def update_password(self):
        """Изменение пароля пользователя"""
        user_id = self.entry_password_user_id.get()
        new_password = self.entry_new_password.get()

        if user_id and new_password:
            try:
                user_id = int(user_id)
                UserContr.update_password(user_id, new_password)
                messagebox.showinfo("Успех", "Пароль успешно изменен")
                self.refresh_users()  # Обновить список
            except ValueError:
                messagebox.showerror("Ошибка", f"Не удалось изменить пароль:")

    def toggle_user_block(self):
        """Блокировка/разблокировка пользователя"""
        user_id = self.entry_block_user_id.get()

        if user_id:
            try:
                user_id = int(user_id)
                user = Users.get_or_none(Users.id == user_id)
                if user:
                    if user.closed:
                        UserContr.un_closed(user_id)
                        messagebox.showinfo("Успех", "Пользователь успешно разблокирован")
                    else:
                        UserContr.closed(user_id)
                        messagebox.showinfo("Успех", "Пользователь успешно заблокирован")
                else:
                    messagebox.showerror("Ошибка", "Пользователь с таким ID не найден")
            except: pass

if __name__ == "__main__":
    root = tk.Tk()
    auth_window = AuthWindow(root)
    root.mainloop()