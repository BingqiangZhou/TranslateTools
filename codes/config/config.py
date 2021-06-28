import os
import json
import importlib

class Config:
    def __init__(self, config_file) -> None:
        assert os.path.exists(config_file), "file is not exist."
        f = open(config_file, 'r')
        self.config_dict = json.load(f)
        f.close()
        
    def config_webdriver(self):
        webdriver_config_dict = self.config_dict.get('browser')
        browser_name = webdriver_config_dict.get('name').lower()

        browser = importlib.import_module(f".webdriver.{browser_name}", "codes")
        if browser_name == 'safair':
            self.webdriver = browser.get_web_driver()
        else:
            self.webdriver = browser.get_web_driver(webdriver_config_dict.get("webdriver_path"), webdriver_config_dict.get("headless"), 
                                    webdriver_config_dict.get("without_log"), webdriver_config_dict.get("edge_path"), 
                                    webdriver_config_dict.get("user_agent"))
        print("webdriver is prepared.")
        return self.webdriver
    
    def config_translators(self):
        self.translators_list = []
        translators_config_dict = self.config_dict.get('translators')
        for name in translators_config_dict.get('names'):
            translator = importlib.import_module(f".translator.{name.lower()}translator", "codes").ATranslator(self.webdriver)
            print(f"{translator.get_translator_name()} is loaded successfully.")
            self.translators_list.append(translator)
        print("translators is prepared.")
        return self.translators_list

    def get_translators(self):
        return self.translators_list

    def get_webdriver(self):
        return self.webdriver
