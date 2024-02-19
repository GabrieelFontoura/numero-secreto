from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


servico = Service(ChromeDriverManager().install())
navegaddor = webdriver.Chrome(service = servico)

