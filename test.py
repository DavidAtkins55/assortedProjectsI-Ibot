from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
options = Options()
options.binary_location = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(chrome_options=options, executable_path=r'/usr/local/bin/chromedriver')
d = webdriver.Chrome('/home/<user>/chromedriver',chrome_options=chrome_options)
d.get('https://www.google.nl/')