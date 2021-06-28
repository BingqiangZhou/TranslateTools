import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from .translator import Translator

class ATranslator(Translator):
    def __init__(self, web_driver, source_language='zh-CHS', to_language='en') -> None:
        self.url = 'https://fanyi.sogou.com/text?transfrom=[1]&transto=[2]'
        self.supprt_source_language_list = ['en', 'zh-CHS']
        self.to_language_list = ['en', 'zh-CHS']
        
        super().__init__(web_driver, self.url, 
                        self.supprt_source_language_list, self.to_language_list, 
                        source_language, to_language)
        
        self.last_result = None

    def translate(self, text):
        self.web_driver.switch_to.window(self.window_handle)
        textarea = self.web_driver.find_element_by_tag_name("textarea")
        textarea.clear()
        textarea.send_keys(text+ Keys.ENTER)
        xpath = f'//*[@id="trans-result"]'
        e = WebDriverWait(self.web_driver, timeout=10).until(lambda d: d.find_element_by_xpath(xpath))
        while True:
            if e.text != self.last_result and e.text != "":
                break
            time.sleep(0.1)
        self.last_result = e.text
        return e.text
    
    def get_translator_name(self):
        return 'Sogou Translator'

# https://blog.csdn.net/czczczzczc/article/details/106690185
# https://zhuanlan.zhihu.com/p/270296193
