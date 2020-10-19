# Selenium-automation-example
### Пример проекта автоматизации тестирования с использование Селениума на PyTest с применением Page Object паттерна. С возможностью смены браузеров (для каждокого тестового комплекта браузер запускатся отдельно и закрывается после теста), маркировкой тестов и возможностью получить отчеты через Allure
1.  Клонируйте проект с GitHub и активируйте виртуальное окружение:
    ##### python -m venv selenium_env
    For Win:
    ##### selenium_env\Scripts\activate.bat
    For Unix:
    ##### selenium_env\Scripts\activate
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
    ##### pytest test_main_script.py
    Для детального отчета:
    ##### pytest -s -v test_main_script.py
    Смена браузера на Firefox (по умолчанию тесты запускаются на Chrome):
    ##### pytest --browser_name=firefox test_main_script.py
    Выполнение основного тестового комплекта (main task):
    ##### pytest -m main_task test_main_script.py
    Выполнение дополнительного тестового комплекта (additional task):
    ##### pytest -m additional_task test_main_script.py
    Запуск тестов с генерацией отчетов Allure:
    ##### pytest --alluredir [some_folder] 
    ##### allure serve [some_folder]