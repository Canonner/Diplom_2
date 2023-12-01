## Диплом Задание 2

Тесты API сервиса [StellarBurger](https://stellarburgers.nomoreparties.site//)

### Список файлов и описание проверок:

### Папка tests содержит файлы:
#### 1. test_user_creation.py 
<i>Проверяет ручку "Создание пользователя" POST /api/auth/register.</i>

Класс TestUserCreation содержит тесты:
- test_successful_user_creation
- test_creation_repeating_courier_failed
- test_creation_repeating_user_failed
- test_creation_user_with_any_missing_field_failed


#### 2. test_user_login.py
<i>Проверяет ручку "Авторизация пользователя" POST /api/auth/login.</i>

Класс TestUserLogin содержит тесты:
- test_successful_user_login
- test_login_with_any_wrong_field_failed


#### 3. test_change_user_data.py
<i>Проверяет ручку "Обновление данных пользователя" PATCH /api/auth/user.</i>

Класс TestChangeUserData содержит тесты:
- test_successful_user_data_change_with_auth
- test_failed_user_data_change_without_auth


#### 4. test_order_creation.py
<i>Проверяет ручку "Создание заказа" POST /api/v1/orders.</i>

Класс TestOrderCreation содержит тесты:
- test_order_creation_with_authorization_and_ingredients
- test_order_creation_without_authorization_failed
- test_order_creation_without_ingredients_failed
- test_order_creation_with_wrong_ingredients_hash_failed


#### 5. test_get_user_orders.py
<i>Проверяет ручку "Получение заказов конкретного пользователя" GET /api/orders.</i>

Класс TestGetUserOrders содержит тесты:
- test_get_user_orders_with_authorization
- test_get_last_fifty_user_orders_with_authorization
- test_sorting_user_orders_with_authorization
- test_get_user_orders_without_authorization_failed

#### 5. conftest.py
Содержит фикстуры
- create_user
- create_fifty_one_orders
- create_three_orders


Кроме того, в корневой папке проекта находятся:
- файл data.py c тестовыми данными, 
- файл requirements.txt c зависимостями проекта и
- файл .gitignore.

