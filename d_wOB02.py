class User:
    def __init__(self, user_id, name):
        self._user_id = user_id  # Защищенный атрибут
        self._name = name  # Защищенный атрибут
        self._access_level = 'user'  # Уровень доступа по умолчанию

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = 'admin'  # Уровень доступа для администраторов
        self._users = []  # Список пользователей

    def add_user(self, user):
        if isinstance(user, User):
            self._users.append(user)
            print(f"Пользователь {user.get_name()} добавлен.")
        else:
            print("Только объекты User могут быть добавлены.")

    def remove_user(self, user_id):
        for user in self._users:
            if user.get_user_id() == user_id:
                self._users.remove(user)
                print(f"Пользователь {user.get_name()} удален.")
                return
        print("Пользователь не найден.")

    def list_users(self):
        for user in self._users:
            print(f"ID: {user.get_user_id()}, Имя: {user.get_name()}, Уровень доступа: {user.get_access_level()}")


                #Пример использования

admin = Admin(1, "Алексей")
user1 = User(2, "Иван")
user2 = User(3, "Мария")

admin.add_user(user1)
admin.add_user(user2)

admin.list_users()  # Список пользователей

admin.remove_user(2)  # Удаляем пользователя Ивана
admin.list_users()  # Обновленный список пользователей


