user_1 = {
    'данные': {
        'амир жумабеков': {'age': 13, 'телефон': 804167615, 'код': "7615"},
        'али жумабеков': {'age': 22, 'телефон': 804830937, 'код': "0937"},
        'актан жумабеков': {'age': 19, 'телефон': 806270407, 'код': "0407"},
    }
}


def confirm_action():
    danet = input('Добро пожаловать в систему банка. Вы хотите восстановить аккаунт? (да/нет): ')
    if danet != 'да':
        print("Штраф 5000 сом за беспокойство")
        exit()


def find_user(data):
    name = input('Введите логин (имя фамилия): ')
    if name in data:
        print("Ваши данные найдены в банковской базе.")
        return name
    else:
        print("Данные не найдены. Доступ запрещён.")
        exit()


def check_age(user):
    age = int(input("Сколько вам лет? "))
    if age == user['age']:
        print("Возраст подтверждён.")
    else:
        print("Возраст не совпадает с данными.")
        exit()


def check_phone(user):
    phone = int(input("Укажите номер телефона: +996 "))
    if phone == user['телефон']:
        print("Номер подтверждён.")
    else:
        print("Неверный номер телефона.")
        exit()


def check_code(user):
    kod = input("Введите последние 4 цифры номера: ")
    if kod == user['код']:
        print("Код подтверждён.")
    else:
        print("Код не совпадает.")
        exit()


def change_password():
    attempts = 3
    while attempts > 0:
        password1 = input("Введите новый пароль: ")
        password2 = input("Подтвердите пароль: ")

        if password1 == password2:
            print("Пароль успешно сброшен. Вы вошли в аккаунт.")
            return
        else:
            attempts -= 1
            if attempts > 0:
                print("Пароли не совпадают. Попробуйте ещё раз.")
            else:
                print("Слишком много попыток.")
                exit()


confirm_action()

name = find_user(user_1['данные'])
user = user_1['данные'][name]

print("Чтобы сбросить пароль, ответьте на несколько вопросов.")

check_age(user)
check_phone(user)
check_code(user)

change_password()
