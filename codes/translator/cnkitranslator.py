from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.by import By

from .translator import Translator

class ATranslator(Translator):
    def __init__(self, web_driver, source_language='zh-CN', to_language='en') -> None:
        self.url = 'https://dict.cnki.net/index'
        self.supprt_source_language_list = ['en', 'zh-CN']
        self.to_language_list = ['en', 'zh-CN']
        
        super().__init__(web_driver, self.url, 
                        self.supprt_source_language_list, self.to_language_list, 
                        source_language, to_language)
    
    # 让翻译网站自己判断语言，重写父类Translator获取url的方法
    def get_url(self, source_language=None, to_language=None):
        return self.url

    def translate(self, text):
        # 切换到翻译页面
        self.web_driver.switch_to.window(self.window_handle) 
        
        # 清空输入框内容
        textarea = self.web_driver.find_element_by_tag_name("textarea") 
        textarea.clear()

        # 输入待翻译内容，并点击“翻译按钮进行翻译
        textarea.send_keys(text)
        btn_xpath = '//*[@id="app"]/div/section/div/div[1]/div[1]/div[2]/button'
        self.web_driver.find_element_by_xpath(btn_xpath).click()

        # 当复制按钮可用时，获取翻译结果
        span_xpath = '/html/body/div[4]/div/section/div/div[2]/div[1]/div[2]/div[3]/span[1]'
        WebDriverWait(self.web_driver, timeout=10).until(EC.visibility_of_element_located((By.XPATH, span_xpath)))
        xpath = '/html/body/div[4]/div/section/div/div[2]/div[1]/div[2]/div[2]/div/pre'
        e = self.web_driver.find_element_by_xpath(xpath)

        return e.text
    
    def get_translator_name(self):
        return 'CNKI Translator'
