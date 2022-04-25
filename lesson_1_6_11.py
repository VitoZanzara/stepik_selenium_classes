from selenium import webdriver
from selenium.webdriver.common.by import By

def check_regform_required_fields(url: str) -> str:
    """
    проверяет прохождение регистрации при заполнении трех обязательных полей формы

    :param url:  адрес страницы регистрации
    :return: ответ сайта после заполнения формы
    """
    with webdriver.Chrome() as browser:
        browser.implicitly_wait(5)
        browser.get(url)
        required_classes = ['first', 'second', 'third']
        for required_class in required_classes:
            browser.find_element(By.CSS_SELECTOR, f'input.{required_class}[required]').send_keys('test')
        browser.find_element(By.CSS_SELECTOR, 'button').click()
        reg_form_answer = browser.find_element(By.TAG_NAME, 'h1').text
        return reg_form_answer

if __name__ == '__main__':
    url_good = 'http://suninjuly.github.io/registration1.html'
    url_bad = 'http://suninjuly.github.io/registration2.html'
    print(check_regform_required_fields(url_bad))


