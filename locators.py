

from selenium.webdriver.common.by import By


class TestLocators:

    """Страница авторизации:"""
    # Локатор для поля ввода email
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")

    # Локатор для отображения пароля
    EYE_BUTTON = ()

    # Локатор для поля ввода пароля
    PASSWORD_INPUT = (By.XPATH, "//input[@name = 'Пароль']")

    # Локатор для кнопки входа
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")

    # Локатор для кнопки Зарегистрироваться
    REGISTRATION_BUTTON = (By.CLASS_NAME, "Auth_link__1fOlj")

    # Локатор для кнопки восстановления пароля
    RESTORE_PASSWORD_BUTTON = (By.XPATH, "//a[text() = 'Восстановить пароль']")

    """Главная страница:"""
    # Локатор Войти в аккаунт
    LOGIN_TO_ACCOUNT = (By.XPATH, ".//button[text() = 'Войти в аккаунт']")

    # Локатор для кнопки личного кабинета
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text() = 'Личный Кабинет']")

    # Локатор оформить заказ
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")

    # Локатор для заголовка страницы конструктора
    TITLE_CONSTRUCTOR = (By.XPATH, "//p[text() = 'Конструктор']")

    # Локатор для ленты заказов
    ORDER_FEED = (By.XPATH, "//p[text() = 'Лента Заказов']")

    # Локатор для заголовка Соберите булки
    BUILD_BURGER_TITLE = (By.XPATH, "//h1[text() = 'Соберите бургер']")

    # Локатор для булок
    BUNS_BLOCK = (By.XPATH, "//span[text() = 'Булки']")

    # Локатор для пространства булочек
    BUNS_AREA = (By.XPATH, "//h2[text() = 'Булки']")

    # Локатор для соусов
    SAUCE_BLOCK = (By.XPATH, "//span[text() = 'Соусы']")

    # Локатор для пространства соуcов
    SAUCE_AREA = (By.XPATH, "//h2[text()='Соусы']")

    # Локатор для начинок
    FILLING_BLOCK = (By.XPATH, "//span[text() = 'Начинки']")

    # Локатор для пространства начинок
    FILLING_AREA = (By.XPATH, "//h2[text()='Начинки']")

    # Локатор для logo
    LOGO = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")

    """Форма регистрации:"""
    # Локатор для кнопки регистрации
    REGISTRATION_SUBMIT = (By.XPATH, "//button[text() = 'Зарегистрироваться']")

    # Локатор для поля имени
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")

    # Локатор для ошибки-сообщения о существующем пользователе
    USER_EXISTS_MESSAGE = (By.XPATH, "//p[text() = 'Такой пользователь уже существует']")

    # Локатор для ошибки-сообщения о неверном пароле
    INCORRECT_PASSWORD_MESSAGE = (By.XPATH, "//p[text() = 'Некорректный пароль']")

    # Локатор для входа в форме регистрации
    LOGIN_FROM_REGISTRATION = (By.XPATH, "//a[text() = 'Войти']")

    """Форма восстановления пароля:"""
    # Локатор для входа в форме восттановления пароля
    LOGIN_FROM_RESET_PASSWORD = (By.XPATH, "//a[text() = 'Войти']")

    """Личный кабинет"""
    # Локатор для раздела Профиль
    PROFILE = (By.XPATH, "//a[@href = '/account/profile']")

    # Локатор для разлогина
    LOGOUT_BUTTON = (By.XPATH, "//button[@type = 'button']")
