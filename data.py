class CommonData:
    register_url = 'https://stellarburgers.nomoreparties.site/api/auth/register'
    login_url = 'https://stellarburgers.nomoreparties.site/api/auth/login'
    delete_user_url = 'https://stellarburgers.nomoreparties.site/api/auth/user'
    change_user_data_url = 'https://stellarburgers.nomoreparties.site/api/auth/user'
    create_order_url = 'https://stellarburgers.nomoreparties.site/api/orders'
    get_user_orders = 'https://stellarburgers.nomoreparties.site/api/orders'
    test_user_password = 'YouShallNotPass'
    test_user_name = 'Gandalf'
    creation_missing_fields = [
        {"password": 'YouShallNotPass', "name": 'Gandalf'},
        {"email": 'test_email_for missing_fields_check@ya.ru', "name": 'Gandalf'},
        {"email": 'test_email_for missing_fields_check1@ya.ru', "password": 'YouShallNotPass'}
    ]
