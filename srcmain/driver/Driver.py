import sys
from selenium import webdriver
from srcmain.driver.driver_config import config

class Driver:

    #initialize webdriver
    def initialize_Driver(self):
        self.driver = webdriver.Chrome(config.project_dir + '/resources/driver/chromedriver.exe');
        self.driver.maximize_window();
        self.driver.set_page_load_timeout(10);
        return self.driver;

    #close webdriver
    def close_driver(self):
       self.driver.quit()