import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from settings import valid_email, valid_password
from selenium import webdriver


def test_show_all_pets():
    """Проверка карточек питомцев всех пользователей
    на наличие фото, имени и описания (порода и возраст)"""

    # Переменные
    url = "https://petfriends.skillfactory.ru/all_pets"

    # Установка неявного ожидания
    pytest.driver.implicitly_wait(10)

    # Переход на страницу авторизации
    pytest.driver.get('http://petfriends.skillfactory.ru/login')

    # Ввод электронной почты
    pytest.driver.find_element(By.ID, 'email').send_keys(valid_email)

    # Ввод пароля
    pytest.driver.find_element(By.ID, 'pass').send_keys(valid_password)

    # Клик по кнопе "Войти"
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    # Проверка того, что осуществлен переход на главную страницу пользователя
    assert pytest.driver.current_url == url

    # Проверка наличия всех питомцев
    assert len(pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck')) > 0

    # Проверка наличия фото у половины питомцев
    photos = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck img')
    half_of_pets = len(photos) // 2
    assert len(list(filter(lambda photo: photo.is_displayed(), photos))) >= half_of_pets

    # Проверка наличия имени, возраста и породы у всех питомцев
    for pet in pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck'):
        # Проверка наличия фото
        assert pet.find_element(By.CSS_SELECTOR, '.card-deck img').is_displayed()

        # Проверка наличия имени
        pet_name = pet.find_element(By.CSS_SELECTOR, '.card-title').text
        assert pet_name.is_displayed()

        # Проверка наличия возраста
        pet_age = pet.find_element(By.CSS_SELECTOR, '.card-text .age').text
        assert pet_age.is_displayed()

        # Проверка наличия породы
        pet_breed = pet.find_element(By.CSS_SELECTOR, '.card-text .breed').text
        assert pet_breed.is_displayed()

    # Проверка, что у всех питомцев разные имена
    pets_names = set([pet.find_element(By.CSS_SELECTOR, '.card-title').text for pet in pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck')])
    assert len(pets_names) == len(pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck'))

    # Проверка, что в списке нет повторяющихся питомцев
    pets_ids = set([pet.get_attribute('data-id') for pet in pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck')])
    assert len(pets_ids) == len(pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck'))


def test_pets_table():
    """Проверка таблицы питомцев на наличие всех колонок"""

    # Переменные
    url = "https://petfriends.skillfactory.ru/pets"

    # Установка неявного ожидания
    pytest.driver.implicitly_wait(10)

    # Переход на страницу авторизации
    pytest.driver.get('http://pet
