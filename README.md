# Sprint_5
# сервис Stellar Burgers https://stellarburgers.nomoreparties.site

# Сервис Stellar Burgers - космический фастфуд: можно собрать и заказать бургер из необычных ингредиентов.
```
1. Создание проекта для автоматизированного тестирования сервиса

Создать в IDE новый проект
Развернуть тестовое окуржение
Подключить Selenium
Установить Сhrome Driver согласно версии Google Chrome
В корне проекта создать папку tests - в ней заводить файлы с тестами в разрезе функционала
В корне проекта добавить файл .gitignore - (JetBrains,Python), чтобы в проект не попало ничего лишнего
В корне проекта создать файл с локаторами для всего проекта -над каждым локатором краткое описание    
В корне проекта создать README.md c описанием функционала и структуры проекта

```
```
2. Фикстура conftest:
Настроить в conftest запуск chromedriver браузера для каждого метода
После каждого метода закрывать браузер
```

```
3. Как добавить новый тест

- Создать новый файл теста в директории `tests` с префиксом `test_`:
test_new_feature.py
Написать класс TestSomeFeature():
Все методы начинать с префиксом `test_`
В конце каждого метода добпавлять assert
```
```
4. Импорты:
# conftest 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

# locators
from selenium.webdriver.common.by import By

# в каждый тестовый файл
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from conftest import driver
from locators import TestLocators
если есть парметризация - import pytest
```
```
5.Создать новый класс теста:

```python
class TestNewFeature():
    def setUp(self):
        # Необходимые предусловия для тестов

    def test_new_feature(self):
        # Проверка новой функциональности

    def test_new_feature_edge_cases(self):
        # Проверка граничных случаев
```
```
6. Запустить тесты и убедиться, что все проходят успешно:

Команда для запуска всех тестов — pytest -v.
```
```

## Как внести изменения

1. Создать отдельную ветку для разработки:
```
```
git checkout -b feature/new_feature
```
```
2. Внести необходимые изменения в тесты.

3. Запустить тесты и убедиться, что все проходят успешно:
```
```
4. Закоммитить изменения:
git commit -m "Add new feature"
```
```
5. Запушить изменения в репозиторий:

git push origin feature/new_feature
```
```
6. Создать Pull Request на GitHub и ожидать ревью.
```
### Структура файлов проекта
- `[test_registration_page.py]`: позитивный тест создания нового пользователя,
        регистрация с использованными данными, тестирование пароля неалидными данными
- `[test_login_page.py]`: логин флоу на 4-х экранах приложения
- `[test_logout.py]`: разлогин из личного кабинета
- `[test_go_from_constructor_personal_account_page.py]`: 
              переход из конструктора на экран личного кабинета
- `[test_go_from_personal_account_to_constructor_page.py]`: переход из личного кабинета
                на главный экран через конструктор и через лого
- `[test_blocks_in_constructor_page.py]`: перход между блоками конструктора - булки - соусы - начика
