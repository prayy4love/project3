import datetime

# Пример данных
users = [
    {'username': 'john_doe', 'password': 'password', 'role': 'user', 'history': [], 'created_at': '2024-09-01'},
    {'username': 'admin_user', 'password': 'password', 'role': 'admin'}
]

products = [
    {'id': 1, 'name': 'Роза', 'price': 50.0, 'category': 'Цветы', 'rating': 4.5, 'added_at': '2024-09-01'},
    {'id': 2, 'name': 'Тюльпан', 'price': 30.0, 'category': 'Цветы', 'rating': 4.2, 'added_at': '2024-09-02'}
]

# Функции для пользователя
def view_products(products):
    for product in products:
        print(f"ID: {product['id']}, Name: {product['name']}, Price: {product['price']}, Rating: {product['rating']}")

def buy_product(user, product_id, products):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        user['history'].append(product)
        print(f"Товар '{product['name']}' успешно добавлен в корзину.")
    else:
        print("Товар не найден.")

def view_history(user):
    print("История покупок:")
    for product in user['history']:
        print(f"Name: {product['name']}, Price: {product['price']}")

def filter_products(products, criterion, value):
    if criterion == 'price':
        return [p for p in products if p['price'] <= value]
    elif criterion == 'rating':
        return [p for p in products if p['rating'] >= value]
    else:
        return products

def update_profile(user, new_password):
    user['password'] = new_password
    print("Профиль успешно обновлен.")

# Функции для администратора
def add_product(products, name, price, category, rating):
    new_product = {
        'id': len(products) + 1,
        'name': name,
        'price': price,
        'category': category,
        'rating': rating,
        'added_at': datetime.datetime.now().strftime('%Y-%m-%d')
    }
    products.append(new_product)
    print(f"Товар '{name}' успешно добавлен.")

def delete_product(products, product_id):
    global products
    products = [p for p in products if p['id'] != product_id]
    print(f"Товар с ID {product_id} успешно удален.")

def edit_product(products, product_id, name, price, category, rating):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        product['name'] = name
        product['price'] = price
        product['category'] = category
        product['rating'] = rating
        print(f"Товар с ID {product_id} успешно изменен.")
    else:
        print("Товар не найден.")

def view_statistics(products):
    total_products = len(products)
    average_price = sum(p['price'] for p in products) / total_products if total_products > 0 else 0
    print(f"Общее количество товаров: {total_products}")
    print(f"Средняя цена товаров: {average_price}")

def manage_users(users, action, username, password=None, role=None):
    if action == 'add':
        users.append({'username': username, 'password': password, 'role': role, 'history': [], 'created_at': datetime.datetime.now().strftime('%Y-%m-%d')})
        print(f"Пользователь '{username}' успешно добавлен.")
    elif action == 'delete':
        global users
        users = [u for u in users if u['username'] != username]
        print(f"Пользователь '{username}' успешно удален.")
    elif action == 'edit':
        user = next((u for u in users if u['username'] == username), None)
        if user:
            user['password'] = password
            user['role'] = role
            print(f"Пользователь '{username}' успешно изменен.")
        else:
            print("Пользователь не найден.")

# Основной цикл приложения
def main():
    while True:
        print("Добро пожаловать в цветочный магазин!")
        username = input("Логин: ")
        password = input("Пароль: ")

        user = next((u for u in users if u['username'] == username and u['password'] == password), None)
        if user:
            if user['role'] == 'user':
                while True:
                    print("\nВыберите действие:")
                    print("1. Просмотреть каталог товаров")
                    print("2. Найти товар")
                    print("3. Сортировать товары по цене")
                    print("4. Купить товар")
                    print("5. Посмотреть историю покупок")
                    print("6. Обновить профиль")
                    print("7. Выйти")
                    choice = input("Введите номер действия: ")

                    if choice == '1':
                        view_products(products)
                    elif choice == '2':
                        name = input("Введите название товара: ")
                        filtered_products = [p for p in products if name.lower() in p['name'].lower()]
                        view_products(filtered_products)
                    elif choice == '3':
                        filtered_products = filter_products(products, 'price', float(input("Введите максимальную цену: ")))
                        view_products(filtered_products)
                    elif choice == '4':
                        product_id = int(input("Введите ID товара: "))
                        buy_product(user, product_id, products)
                    elif choice == '5':
                        view_history(user)
                    elif choice == '6':
                        new_password = input("Введите новый пароль: ")
                        update_profile(user, new_password)
                    elif choice == '7':
                        break
                    else:
                        print("Неверный выбор. Попробуйте снова.")
            elif user['role'] == 'admin':
                while True:
                    print("\nВыберите действие:")
                    print("1. Добавить новый товар")
                    print("2. Удалить товар")
                    print("3. Редактировать товар")
                    print("4. Просмотреть статистику")
                    print("5. Управлять пользователями")
                    print("6. Выйти")
                    choice = input("Введите номер действия: ")

                    if choice == '1':
                        name = input("Введите название товара: ")
                        price = float(input("Введите цену товара: "))
                        category = input("Введите категорию товара: ")
                        rating = float(input("Введите рейтинг товара: "))
                        add_product(products, name, price, category, rating)
                    elif choice == '2':
                        product_id = int(input("Введите ID товара: "))
                        delete_product(products, product_id)
                    elif choice == '3':
                        product_id = int(input("Введите ID товара: "))
                        name = input("Введите новое название товара: ")
                        price = float(input("Введите новую цену товара: "))
                        category = input("Введите новую категорию товара: ")
                        rating = float(input("Введите новый рейтинг товара: "))
                        edit_product(products, product_id, name, price, category, rating)
                    elif choice == '4':
                        view_statistics(products)
                    elif choice == '5':
                        action = input("Введите действие (add/delete/edit): ")
                        username = input("Введите логин пользователя: ")
                        if action in ['add', 'edit']:
                            password = input("Введите пароль пользователя: ")
                            role = input("Введите роль пользователя (user/admin): ")
                            manage_users(users, action, username, password, role)
                        elif action == 'delete':
                            manage_users(users, action, username)
                    elif choice == '6':
                        break
                    else:
                        print("Неверный выбор. Попробуйте снова.")
        else:
            print("Неверный логин или пароль. Попробуйте снова.")

if __name__ == "__main__":
    main()
