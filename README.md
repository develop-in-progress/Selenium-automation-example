# Selenium-automation-example
### Пример проекта автоматизации тестирования на Selenium/PyTest с применением Page Object паттерна. Реализована возможность смены браузеров (для каждого тестового комплекта браузер запускатся отдельно и закрывается после теста), маркировка тестов и отчетность через Allure
1.  Клонируйте проект с GitHub и активируйте виртуальное окружение:
    ##### `python -m venv selenium_env`
    For Win:
    ##### `selenium_env\Scripts\activate.bat`
    For Unix:
    ##### `source selenium_env\Scripts\activate`
    Не сработает - запустите через sudo
2.  Для запуска вам потребуется актуальная версия Питона, Селениум и PyTest
    Установка зависимостей (при наличии [Python](https://www.python.org/)) через терминал:
    ##### pip install -r requirements.txt
3. Актульные версии ChromeDriver, Geckodriver и Allure:
    * ###### [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)
    * ###### [Geckodriver](https://github.com/mozilla/geckodriver/releases/)
    * ###### [Allure](https://docs.qameta.io/allure/)
   Скачайте архивы, распакуйте .exe файлы и обязательно добавьте драйвера (как на UNIX системах, так и Windows). Allure так же требует Java с добавлением JAVA_HOME системной переменной (значение - адрес к текущей версии Java)
4. Общий тест запускается командой 
    ##### `pytest test_main.py`
    Или просто (терминал открыт в папке проекта):
    ##### `pytest`
    Для детального отчета:
    ##### `pytest -s -v`
    Смена браузера на Firefox (по умолчанию тесты запускаются на Chrome):
    ##### `pytest --browser_name=firefox`
    Выполнение основного тестового комплекта (main task):
    ##### `pytest -m main_task`
    Выполнение дополнительного тестового комплекта (additional task):
    ##### `pytest -m additional_task`
    Запуск тестов с генерацией отчетов Allure:
    ##### `pytest --alluredir [some_folder]`
    ##### `allure serve [same_folder]`