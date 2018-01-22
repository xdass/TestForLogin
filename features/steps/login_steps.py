from behave import given, when, then, step
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@given('Зайти на сайт "{site_url}"')
def step_impl(context, site_url):
    context.browser.get(site_url)


@when('Нажать на кнопку "{button_name}" "{value}"')
def step_impl(context, button_name, value):
    if int(value) == 1:
        xpath_for_btn = '//a[normalize-space(.)="{}"]'.format(button_name)
        context.browser.find_element_by_xpath(xpath_for_btn).click()
    else:
        WebDriverWait(context.browser, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#signup #signUPBtn'))
        ).click()


@then("Появилось окно Входа/Регистрации")
def step_impl(context):
    context.browser.find_element_by_xpath('//*[@id="PromoteSignUpPopUp"]')


@then("Появилось окно ввода регистрационных данных")
def step_impl(context):
    try:
        context.browser.find_element_by_xpath('//*[@id="signingPopup"]')
    except NoSuchElementException:
        return False


@step('Ввести "{value}" в поле "{field_placeholder}"')
def step_impl(context, value, field_placeholder):
    xpath_for_placeholder = '//*[@placeholder="{}"]'.format(field_placeholder)
    input_el = context.browser.find_element_by_xpath(xpath_for_placeholder)
    input_el.send_keys(value)


@step('Выбрать страну "{country}" в выпадающем меню')
def step_impl(context, country):
    xpath_for_placeholder = "//a[@id='DropdownBtn']"
    dropdown = WebDriverWait(context.browser, 60).until(
        EC.element_to_be_clickable((By.XPATH, xpath_for_placeholder))
    )
    dropdown.click()
    context.browser.find_element_by_xpath('//*[@id="countriesUL"]/li[text()="{}"]'.format(country)).click()


@step("Приянть правилами использования и политику конфиденциальности")
def step_impl(context):
    checkbox = context.browser.find_element_by_xpath('//*[@id="in_termsAndConditions"]')
    checkbox.click()


@step("Сделать скриншот")
def step_impl(context):
    context.browser.save_screenshot('login_page.png')
    context.browser.delete_all_cookies()


@then('Появилось сообщение об ошибке "{warn_message}"')
def step_impl(context, warn_message):
    xpath_for_warn = "//*[contains(@data-tooltip, '{}')][contains(@class, beigeTooltip)]".format(warn_message)
    context.browser.find_element_by_xpath(xpath_for_warn)

