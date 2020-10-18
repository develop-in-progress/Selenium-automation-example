class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(10)  # Ожидаем загрузки контента до таймаута

    def open(self):
        return self.browser.get(self.url)
