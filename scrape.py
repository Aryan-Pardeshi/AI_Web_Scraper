import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time
import random
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

# from dotenv import load_dotenv
# import os

# load_dotenv()
ua = UserAgent()


# proxy_host = os.getenv("PROXY_HOST")
# proxy_port = os.getenv("PROXY_PORT")
# proxy_user = os.getenv("PROXY_USER")
# proxy_pass = os.getenv("PROXY_PASS")

def load_proxies(file_path):
    """Read proxies from the text file and return a list of dictionaries."""
    proxies = []
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():  # Skip empty lines
                ip, port, username, password = line.strip().split(':')
                proxies.append({
                    'host': ip,
                    'port': port,
                    'user': username,
                    'pass': password
                })
    return proxies

def scrape_website(website):
    print("launching chrome browser")
    
    chrome_driver_path = "./chromedriver.exe"
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={ua.chrome}")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument("--enable-javascript")
    options.add_argument("window-size=1920,1080")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-notifications")
    options.add_argument("user-data-dir=/path/to/your/chrome/profile")
    options.add_argument("--no-sandbox")
    options.add_argument("accept-language=en-US,en;q=0.9")
    options.add_argument("accept=application/json, text/plain, */*")
    options.add_argument("--disable-geolocation")
    options.add_experimental_option("prefs", {"profile.default_content_setting_values.geolocation": 2})
    options.add_argument("--incognito")


    # options.add_argument("--disable-dev-shm-usage")  # For headless if used
    # options.add_argument("--headless=new")
    

    # proxies = load_proxies("proxies.txt")
    # if not proxies:
    #     print("No proxies found in the file!")
    #     return None
    # selected_proxy = random.choice(proxies)
    # proxy_host = selected_proxy['host']
    # proxy_port = selected_proxy['port']
    # proxy_user = selected_proxy['user']
    # proxy_pass = selected_proxy['pass']
    # proxy = f"http://{proxy_user}:{proxy_pass}@{proxy_host}:{proxy_port}"
    # options.add_argument(f"--proxy-server={proxy}")
    #Uncomment the above lines to use a proxy from the file
    
    
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
        
        
        
def extract_body(html):
    soup = BeautifulSoup(html, 'html.parser')
    body_content = soup.body
    if body_content:
        return body_content.get_text(strip=True)
    return ""
def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, 'html.parser')
    
    for script_or_style in soup(['script', 'style']):
        script_or_style.extract() # Remove script and style elements coz they are not needed
        
    # Clean up the text by removing extra spaces and newlines
    cleaned_content = soup.get_text(separator='\n')
    cleaned_content = "\n".join(line.strip() for line in cleaned_content.splitlines() if line.strip())
    
    return cleaned_content

def split_dom_content(dom_content, max_length=6000):
    return [
        dom_content[i:i + max_length] for i in range(0, len(dom_content), max_length)
    ]