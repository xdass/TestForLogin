import time
from behave import given, when, then, step
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#use_step_matcher('parse')


@given('Зайти на сайт "{site_url}"')
def step_impl(context, site_url):
    context.browser.get(site_url)


@when('Нажать на кнопку "{button_name}"')
def step_impl(context, button_name):
    xpath_for_btn = '//a[normalize-space(.)="{}"]'.format(button_name)
    context.browser.find_element_by_xpath(xpath_for_btn).click()
    #time.sleep(5)
    #button.click()
    #//a[normalize-space(.)="Бесплатная регистрация"]


@then("Появилось окно Входа/Регистрации")
def step_impl(context):
    try:
        context.browser.find_element_by_xpath('//*[@id="PromoteSignUpPopUp"]')
    except NoSuchElementException:
        return False


@then("Появилось окно ввода регистрационных данных")
def step_impl(context):
    try:
        context.browser.find_element_by_xpath('//*[@id="signingPopup"]')
    except NoSuchElementException:
        return False


@step('Ввести "{value}" в поле "{field_placeholder}"')
def step_impl(context, value, field_placeholder):
    xpath_for_placeholder = '//*[@placeholder="{}"]'.format(field_placeholder)
    #time.sleep(4) # Is there  besr way?
    input_el = context.browser.find_element_by_xpath(xpath_for_placeholder)
    input_el.send_keys(value)


@step('Выбрать страну "{country}" в выпадающем меню "{field_placeholder}"')
def step_impl(context, country, field_placeholder):
    xpath_for_placeholder = '//*[@placeholder="{}"]'.format(field_placeholder)
    dropdown = context.browser.find_element_by_xpath('//*[@id="DropdownBtn"]')
    time.sleep(5)
    dropdown.click()
    # dropdown = WebDriverWait(context.browser, 6).until(
    #     EC.presence_of_element_located((By.XPATH, '//*[@id="DropdownBtn"]'))
    # )
    # myElem = WebDriverWait(context.browser, 10).until(
    #     EC.visibility_of_element_located((By.XPATH, '//*[@id="countriesUL"]'))
    # )
    # print(myElem)
    #myElem.click()
    context.browser.find_element_by_xpath('//*[@id="countriesUL"]/li[text()="{}"]'.format(country)).click()


@step("Приянть правилами использования и политику конфиденциальности")
def step_impl(context):
    checkbox = context.browser.find_element_by_xpath('//*[@id="in_termsAndConditions"]')
    checkbox.click()


@step("Сделать скриншот")
def step_impl(context):
    context.browser.save_screenshot('login_page.png')


@when("дави сюда")
def step_impl(context):
    #context.browser.find_element_by_css_selector('#signUPBtn').click()
    el = WebDriverWait(context.browser, 60).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#signUPBtn'))
    )
    el.click()