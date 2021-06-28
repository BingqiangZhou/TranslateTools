from selenium.webdriver import Safari

def get_web_driver():
    driver = Safari()
    driver.implicitly_wait(3)
    return driver