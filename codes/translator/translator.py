
class Translator:
    def __init__(self, web_driver, url, supprt_source_language_list, to_language_list, 
                source_language='zh-CN', to_language='en') -> None:
        self.supprt_source_language_list = supprt_source_language_list
        self.to_language_list = to_language_list
        self.url = url # such as: 'https://translate.google.cn/?sl=[1]&tl=[2]'
        
        to_url = self.get_url(source_language, to_language)
        self.web_driver = web_driver

        # 打开并切换到新的标签页
        if "http" in self.web_driver.current_url: # whether frist time to visit.
            js = f'window.open("{to_url}","_blank");'
            self.web_driver.execute_script(js)
            self.web_driver.implicitly_wait(5)
            self.web_driver.switch_to.window(self.web_driver.window_handles[-1])
        
        # 访问to_url，并记录当前标签页句柄
        self.web_driver.get(to_url)
        self.web_driver.implicitly_wait(5)
        self.window_handle = self.web_driver.current_window_handle
    
    def set_language(self, source_language='zh-CN', to_language='en'):
        assert source_language in self.supprt_source_language_list, f'source language [{source_language}] is not support.'
        assert to_language in self.to_language_list, f'to language [{to_language}] is not support.'
        self.source_language = source_language
        self.to_language = to_language
    
    def get_url(self, source_language='zh-CN', to_language='en'):

        self.set_language(source_language, to_language)

        url = self.url.replace('[1]', self.source_language)
        url = url.replace('[2]', self.to_language)
        return url

    # to be overload
    def translate(self, text):
        # self.web_driver.switch_to.window(self.window_handle)
        return text
    
    def translate(self, text, source_language, to_language):
        self.web_driver.switch_to.window(self.window_handle)
        to_url = self.get_url(source_language, to_language)
        self.web_driver.get(to_url)
        # js = f'window.open("{to_url}");'
        # self.web_driver.execute_script(js)
        self.web_driver.driver.implicitly_wait(5)
        return self.translate(text)
    
    def get_translator_name(self):
        return 'Translator'