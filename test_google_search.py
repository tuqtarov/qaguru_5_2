import pytest
from selene.support.shared import browser
from selene import be, have


@pytest.fixture
def open_chrome_with_size():
    browser.open('https://google.com/')
    browser.driver.set_window_size(720, 600)


def test_coinciding_result(open_chrome_with_size):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('#search').should(have.text('Selene -'
                                                ' User-oriented Web UI browser tests in Python'))
    print(' тест успешно пройден - искомая фраза содержится в выдаче 1/2')

def test_empty_result(open_chrome_with_size):
    browser.element('[name="q"]').should(be.blank).type('flpagmdsgmkdspgmdsa').press_enter()
    browser.element('#result-stats').should(have.text('Результатов: примерно 0'))
    print(' тест успешно пройден - по запросу нет результатов в выдаче - 2/2')
