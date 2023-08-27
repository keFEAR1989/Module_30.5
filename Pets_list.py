import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from settings import valid_email, valid_password
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    # Инициализация веб-драйвера
    driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
    # Неявное ожидание
    driver.implicitly_wait(10)
    # Возврат объекта драйвера
    yield driver
    # Завершение сессии драйвера
    driver.quit()

def test_show_all_pets(driver):
    """Проверка карточек питомцев всех пользователей
    на наличие фото, имени и описания (порода и возраст)"""

    url = "https://petfriends.skillfactory.ru/all_pets"

    # Переход на страницу авторизации
    driver.get('http://petfriends.skillfactory.ru/login')

    # Ввод электронной почты
    driver.find_element(By.ID, 'email').send_keys(valid_email)

    # Ввод пароля
    driver.find_element(By.ID, 'pass').send_keys(valid_password)

    # Клик по кнопке "Войти"
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    # Ожидание загрузки главной страницы
    WebDriverWait(driver, 10).until(EC.url_to_be(url))

    # Проверка наличия всех питомцев
    pet_cards = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card')
    assert len(pet_cards) > 0

    # Ожидание появления половины фото
    photos = driver.find_elements(By.CSS_SELECTOR, '.card-deck img')
    half_of_pets = len(pet_cards) // 2
    WebDriverWait(driver, 10).until(lambda driver: len(list(filter(lambda photo: photo.is_displayed(), photos))) >= half_of_pets)

    for pet in pet_cards:
        # Проверка наличия фото
        assert pet.find_element(By.CSS_SELECTOR, 'img').is_displayed()

        # Проверка наличия имени
        pet_name = pet.find_element(By.CSS_SELECTOR, '.card-title').text
        assert pet_name

        # Проверка наличия возраста
        pet_age = pet.find_element(By.CSS_SELECTOR, '.card-text .age').text
        assert pet_age

        # Проверка наличия породы
        pet_breed = pet.find_element(By.CSS_SELECTOR, '.card-text .breed').text
        assert pet_breed

    # Проверка, что у всех питомцев разные имена
    pets_names = set([pet.find_element(By.CSS_SELECTOR, '.card-title').text for pet in pet_cards])
    assert len(pets_names) == len(pet_cards)

    # Проверка, что в списке нет повторяющихся питомцев
    pets_ids = set([pet.get_attribute('data-id') for pet in pet_cards])
    assert len(pets_ids) == len(pet_cards)

def test_pets_table(driver):
    """Проверка таблицы питомцев на наличие всех колонок"""

    url = "https://petfriends.skillfactory.ru/pets"

    # Переход на страницу авторизации
    driver.get('http://petfriends.skillfactory.ru/login')

    # Ввод электронной почты
    driver.find_element(By.ID, 'email').send_keys(valid_email)

    # Ввод пароля
    driver.find_element(By.ID, 'pass').send_keys(valid_password)

    # Клик по кнопке "Войти"
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    # Ожидание загрузки главной страницы
    WebDriverWait(driver, 10).until(EC.url_to_be(url))

    # Переход на страницу со списком питомцев
    driver.get(url)

    # Ожидание появления таблицы
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.table')))

    # Проверка наличия всех колонок в таблице
    expected_columns = ['Name', 'Animal Type', 'Age', 'Actions']
    table_head = driver.find_element(By.CSS_SELECTOR, '.table thead tr')
    columns = table_head.find_elements(By.TAG_NAME, 'th')
    column_names = [column.text for column in columns]
    assert column_names == expected_columns
