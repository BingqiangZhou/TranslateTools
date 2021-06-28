from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .translator import Translator

class ATranslator(Translator):
    def __init__(self, web_driver, source_language='zh-CN', to_language='en') -> None:
        self.url = 'https://fanyi.youdao.com'
        self.supprt_source_language_list = ['en', 'zh-CN']
        self.to_language_list = ['en', 'zh-CN']
        
        super().__init__(web_driver, self.url, 
                        self.supprt_source_language_list, self.to_language_list, 
                        source_language, to_language)
        
        # 刷新 去掉多余的div
        self.web_driver.refresh()
        # 关闭指导页
        guide_close_xpath = '/html/body/div[7]/div/span'
        close_btn = self.web_driver.find_element_by_xpath(guide_close_xpath)
        if close_btn.is_displayed():
            close_btn.click()
    
    # 让翻译网站自己判断语言，重写父类Translator获取url的方法
    def get_url(self, source_language=None, to_language=None):
        return self.url

    def translate(self, text):
        # 切换到翻译页面
        self.web_driver.switch_to.window(self.window_handle) 
        
        # 清空输入框
        clear_btn_xpath = '/html/body/div[2]/div[2]/div[1]/div[1]/a'
        clear_btn = self.web_driver.find_element_by_xpath(clear_btn_xpath)
        if clear_btn.is_displayed():
            # clear_btn = WebDriverWait(self.web_driver, timeout=10).until(EC.element_to_be_clickable((By.XPATH, clear_btn_xpath)))
            clear_btn.click()

        # 输入待翻译内容
        textarea_xpath = '/html/body/div[2]/div[2]/div[1]/div[1]/textarea'
        textarea = self.web_driver.find_element_by_xpath(textarea_xpath)
        # textarea.clear()
        textarea.send_keys(text)

        # 当翻译结果所在元素可见时，获取翻译结果
        result_span_xpath = '/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/p'
        result_span = WebDriverWait(self.web_driver, timeout=10).until(EC.visibility_of_element_located((By.XPATH, result_span_xpath)))

        return result_span.text
    
    def get_translator_name(self):
        return 'YouDao Translator'