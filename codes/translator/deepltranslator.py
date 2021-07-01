import time
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.by import By

from .translator import Translator

class ATranslator(Translator):
    def __init__(self, web_driver, source_language='zh', to_language='en') -> None:
        self.url = 'https://www.deepl.com/en/translator#[1]/[2]/'
        self.supprt_source_language_list = ['en', 'zh']
        self.to_language_list = ['en', 'zh']
        
        super().__init__(web_driver, self.url, 
                        self.supprt_source_language_list, self.to_language_list, 
                        source_language, to_language)
        
    def translate(self, text):
        # 切换到翻译页面
        self.web_driver.switch_to.window(self.window_handle)

        # 清空输入框
        textarea = self.web_driver.find_element_by_tag_name("textarea")
        clear_btn_xpath = '/html/body/div[2]/div[1]/div[5]/div[4]/div[1]/button'
        clear_btn = self.web_driver.find_element_by_xpath(clear_btn_xpath)
        if clear_btn.is_displayed():
            clear_btn.click()

        # 输入待翻译内容
        textarea.send_keys(text)

        # 获取翻译结果
        mobile_share_xpath = '/html/body/div[2]/div[1]/div[5]/div[4]/div[3]/div[5]'
        mobile_share = self.web_driver.find_element_by_xpath(mobile_share_xpath)
        xpath = '/html/body/div[2]/div[1]/div[5]/div[4]/div[3]/div[3]/div[1]/div[1]'
        e = self.web_driver.find_element_by_xpath(xpath)
        # 当使用无头浏览器时，mobile_share会被隐藏，这里改用循环获取翻译结果，并判断五次结果一致
        if "lmt--mobile-hidden" in mobile_share.get_attribute('class'):
            # WebDriverWait(self.web_driver, timeout=10).until(EC.url_changes((self.web_driver.current_url)))
            loader_indicator = '/html/body/div[2]/div[1]/div[5]/div[4]/div[3]/div[3]/div[3]/div'
            WebDriverWait(self.web_driver, timeout=10).until(EC.invisibility_of_element_located((By.XPATH, loader_indicator)))
            result = e.get_property('innerHTML').strip()
            times = 0
            while True:
                if times >= 5:
                    break
                if result == e.get_property('innerHTML').strip() and result != "" and "..." not in result:
                    time.sleep(0.1)
                    times += 1
                result = e.get_property('innerHTML').strip()
        else:
            WebDriverWait(self.web_driver, timeout=10).until(
                lambda d: d.find_element_by_xpath(mobile_share_xpath).get_attribute('class') == 'lmt__mobile_share_container')

        return e.get_property('innerHTML').strip()
        
    def get_translator_name(self):
        return 'DeepL Translator'
