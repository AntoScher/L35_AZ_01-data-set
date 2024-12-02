from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Настройка веб-драйвера
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Инициализация веб-драйвера
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # Открытие страницы
    driver.get('https://www.cian.ru/snyat-1-komnatnuyu-kvartiru/')

    # Ожидание загрузки элементов с ценами
    WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class, "c6e8ba0eec--header--")]//span[@data-mark="MainPrice"]'))
    )

    # Поиск элементов с ценами
    prices = driver.find_elements(By.XPATH, '//div[contains(@class, "c6e8ba0eec--header--")]//span[@data-mark="MainPrice"]')

    # Извлечение и вывод цен
    for price in prices:
        print(price.text)

finally:
    # Закрытие драйвера
    driver.quit()

