from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_stealth import stealth
from webdriver_manager.chrome import ChromeDriverManager
# from fake_useragent import UserAgent
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
import time
# import solver


# Set up the Selenium WebDriver (e.g., Chrome)
options = webdriver.ChromeOptions()
# options.add_argument('--headless')  # Run in headless mode
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')
# options.add_argument("--disable-javascript")
# options.add_argument("user-agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'")
# options.add_argument("--start-maximized")  # Start maximized
# options.add_argument("--disable-blink-features=AutomationControlled")  # Disable automation flags
# # options.add_experimental_option("excludeSwitches", ["enable-automation"])  # Exclude automation switch
# options.add_experimental_option('useAutomationExtension', False)  # Disable automation extension

# service = Service(r'C:\Users\h\.wdm\drivers\chromedriver\win64\127.0.6533.99\chromedriver-win32\chromedriver.exe')  # Replace with your path to ChromeDriver
# driver = webdriver.Chrome(service=service, options=options)

proxy = "20.235.159.154:80"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
#chrome_options.add_argument('--headless=new')
#chrome_options.add_argument('--disable-extensions')
options.add_argument(f"--proxy-server={proxy}")

chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-infobars')
chrome_options.add_argument('--log-level=3')
#chrome_options.add_argument('--incognito')
chrome_options.add_argument('--disable-popup-blocking')
chrome_options.add_argument('--extensions-on-chrome-urls')
chrome_options.add_argument('--test-type')
chrome_options.add_argument('--start-minimized')
# chrome_options.add_argument("--window-position=-2000,-1100")
chrome_options.add_argument("window-size=1920,1080")
chrome_options.add_argument('--disable-cache')
chrome_options.add_argument('--delete-cookies')
chrome_options.add_argument('--ignore-certificate-errors')
# chrome_options.add_extension('AdBlock.crx')
# chrome_options.add_extension('captcha.crx')

# chrome_options.add_experimental_option("excludeSwitches", ['enable-automation','enable-logging' ])
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
wait = WebDriverWait(driver, 10)


# Initialize the WebDriver
# driver = webdriver.Chrome(options=options)

# Use selenium-stealth to help avoid detection
stealth(driver,
    languages=["en-US", "en"],
    vendor="Google Inc.",
    platform="Win32",
    webgl_vendor="Intel Inc.",
    renderer="Intel Iris OpenGL Engine",
    fix_hairline=True,
)

# Target URL to scrape
url = "https://mygift.giftcardmall.com/"  # Replace with the target URL
driver.get(url)


time.sleep(10)

# solver.capsolver()

# credit_card_number = "4358808146018136"
# input_field = driver.find_element(By.ID, "credit-card-number")
# input_field.send_keys(credit_card_number)

# time.sleep(2)

# expiration_month = "12"
# input_field = driver.find_element(By.ID, "expiration_month")
# input_field.send_keys(expiration_month)

# time.sleep(1)

# expiration_year = "30"
# input_field = driver.find_element(By.ID, "expiration_year")
# input_field.send_keys(expiration_year)

# time.sleep(1)

# credit_card_code = "845"
# input_field = driver.find_element(By.ID, "credit-card-code")
# input_field.send_keys(credit_card_code)

# time.sleep(1)

# button = driver.find_element(By.CSS_SELECTOR, ".btn.ml-2.submit-btn")
# button.click()

# time.sleep(3)

# paragraphs = driver.find_elements(By.TAG_NAME, 'p')
# for paragraph in paragraphs:
#     print(paragraph.text)

# Close the driver

input("Press Enter to close the browser...")
driver.quit()





        