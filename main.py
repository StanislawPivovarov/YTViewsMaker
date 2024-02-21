import undetected_chromedriver as uc
import ssl
import json
import random
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import requests
from random import randint
import argparse

def main(num_runs, num_browsers):
    ssl._create_default_https_context = ssl._create_unverified_context
    
    for _ in range(num_runs):
        for _ in range(num_browsers):
            driver = uc.Chrome()
            driver.get('https://youtu.be/5UOQEU9w9_U')
            time.sleep(randint(10,30))
            driver.close()
            driver.quit()
            time.sleep(5)  # Опциональная пауза между запусками браузеров

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run multiple instances of Chrome browser.")
    parser.add_argument("--runs", type=int, default=1, help="Number of runs.")
    parser.add_argument("--browsers", type=int, default=1, help="Number of simultaneous browsers to open.")
    args = parser.parse_args()
    main(args.runs, args.browsers)
