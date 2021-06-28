import time
import traceback
from codes.config import Config

config = Config("./config/config.json")
webdriver = config.config_webdriver()
translator_list = config.config_translators()

try:
    while True:
        print(f"\r\n{'='*80}\r\nPlease enter the Chinese you want to translate: [enter 'exit' to quit]")
        text = input()
        if text.lower() == 'exit':
            break
        for translator in translator_list:
            s = time.time()
            translate_result = translator.translate(text)
            print("\r\n"+ translate_result)
            print(f"{'='*80}\r\n{translator.get_translator_name()}, {time.time() - s}s")
except Exception:
    print(traceback.format_exc())
finally:
    if webdriver is not None:
        webdriver.quit()

