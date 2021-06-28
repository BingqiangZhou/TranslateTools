import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from .translator import Translator

class ATranslator(Translator):
    def __init__(self, web_driver, source_language='zh-CN', to_language='en') -> None:
        self.url = 'https://fanyi.qq.com'
        self.supprt_source_language_list = ['en', 'zh-CN']
        self.to_language_list = ['en', 'zh-CN']
        
        super().__init__(web_driver, self.url, 
                        self.supprt_source_language_list, self.to_language_list, 
                        source_language, to_language)

    def get_url(self, source_language=None, to_language=None):
        return self.url

    def translate(self, text):
        self.web_driver.switch_to.window(self.window_handle)
        textarea = self.web_driver.find_element_by_tag_name("textarea")
        textarea.clear()
        textarea.send_keys(text+ Keys.ENTER)
        xpath = f'/html/body/div[2]/div[2]/div[2]/div[2]/div[2]/span[2]'
        e = WebDriverWait(self.web_driver, timeout=10).until(lambda d: d.find_element_by_xpath(xpath))
        while True:
            if e.text != self.last_result and e.text != "":
                break
            time.sleep(0.1)
        self.last_result = e.text
        return e.text

    def get_translator_name(self):
        return 'Tencent Translator'