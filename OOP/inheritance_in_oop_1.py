class User:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def show(self):
        print(f'{self.name} ({self.phone})')


class Friend(User):
    def show(self):
        print(f'Имя: {self.name} || Телефон: {self.phone}')


user = User("Виктор Гюго", "+33 1 42 72 10 16")
# у класса friend нет конструктора, но он есть
# у родительского класса User, поэтому код сработает
friend = Friend("Виктор Гюго", "+33 1 42 72 10 16")

user.show()
friend.show()
