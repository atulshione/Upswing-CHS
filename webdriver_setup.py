from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

def get_driver():
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Edge()

    return driver 