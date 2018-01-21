from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def before_all(context):
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument('--start-fullscreen')
    context.browser = webdriver.Chrome(options=options)
    #context.browser.implicitly_wait(4)