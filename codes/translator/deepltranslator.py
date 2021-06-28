from selenium.webdriver.support.ui import WebDriverWait

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
        clear_btn_xpath = '/html/body/div[2]/div[1]/div[5]/div[3]/div[1]/button'
        clear_btn = self.web_driver.find_element_by_xpath(clear_btn_xpath)
        if clear_btn.is_displayed():
            clear_btn.click()
        # textarea.clear()

        # 输入待翻译内容
        textarea.send_keys(text)

        # 分享图标可用的时候，获取翻译结果
        mobile_share_xpath = '/html/body/div[2]/div[1]/div[5]/div[3]/div[3]/div[5]'
        WebDriverWait(self.web_driver, timeout=10).until(
            lambda d: d.find_element_by_xpath(mobile_share_xpath).get_attribute('class') == 'lmt__mobile_share_container')
        xpath = f'/html/body/div[2]/div[1]/div[5]/div[3]/div[3]/div[3]/div[1]/div[1]'
        e = self.web_driver.find_element_by_xpath(xpath)

        return e.get_property('innerHTML').strip()
        
    def get_translator_name(self):
        return 'DeepL Translator'
