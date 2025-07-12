import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time
import random

def scrape_website(website):
    print("launching chrome browser")
    
    chrome_driver_path = "./chromedriver.exe"
    options = webdriver.ChromeOptions()
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                            "AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/126.0.0.0 Safari/537.36")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument("--enable-javascript")
    options.add_argument("window-size=1920,1080")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-notifications")
    options.add_argument("user-data-dir=/path/to/your/chrome/profile")
    # options.add_argument("--headless=new")
    
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        })
    """
    })
    
    
    
    
    try:
        driver.get(website)
        print(f"Successfully opened {website}")
        
        time.sleep(random.uniform(2, 5))
        html = driver.page_source
        return html
    finally:
        driver.quit()
        print("Closed the browser")