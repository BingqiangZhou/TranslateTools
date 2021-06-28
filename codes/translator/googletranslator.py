from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .translator import Translator

class ATranslator(Translator):
    def __init__(self, web_driver, source_language='zh-CN', to_language='en') -> None:
        self.url = 'https://translate.google.cn/?sl=[1]&tl=[2]'
        self.supprt_source_language_list = ['en', 'zh-CN']
        self.to_language_list = ['en', 'zh-CN']
        
        super().__init__(web_driver, self.url, 
                        self.supprt_source_language_list, self.to_language_list, 
                        source_language, to_language)

    def translate(self, text):
        #  切换到翻译页面
        self.web_driver.switch_to.window(self.window_handle)

        # 清空输入框
        clear_btn_xpath = '/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/div[1]/div/div/span/button'
        clear_btn = self.web_driver.find_element_by_xpath(clear_btn_xpath)
        if clear_btn.is_displayed():
            clear_btn.click()

        # 输入待翻译内容
        textarea = self.web_driver.find_element_by_tag_name("textarea")
        textarea.send_keys(text)

        # 当翻译结果所在元素可见时，获取翻译结果
        result_span_xpath = "/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div[5]/div/div[1]/span[1]"
        result_span = WebDriverWait(self.web_driver, timeout=10).until(EC.visibility_of_element_located((By.XPATH, result_span_xpath))) # url改变作为翻译结束的信号，等待url改变
        return result_span.text.replace("\n", "").replace("\r", "").replace("\r\n", "")
    
        
    def get_translator_name(self):
        return 'Google Translator'
