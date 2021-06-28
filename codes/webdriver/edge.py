from msedge.selenium_tools import Edge, EdgeOptions 

def get_web_driver(webdriver_path='./drivers/edgedriver_win64/msedgedriver.exe', 
                    headless=False, without_log=True, edge_path=None, user_agent=None):
    options = EdgeOptions()
    options.use_chromium = True
    options.headless = headless
    if edge_path is not None:
        options.binary_location = edge_path
    if without_log:
        options.add_experimental_option('excludeSwitches', ['enable-logging']) #禁止打印日志 https://blog.csdn.net/wm9028/article/details/107536929
    if user_agent is not None:
        options.add_argument(f'user-agent="{user_agent}"')
        # Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.59

    # options.add_argument("headless")
    # options.add_argument("disable-gpu")
    driver = Edge(executable_path=webdriver_path, options=options)
    driver.implicitly_wait(3)
    return driver