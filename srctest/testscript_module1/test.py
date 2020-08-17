import sys

from selenium import webdriver
from srcmain.driver.Driver import Driver

class driverclass:

    driver = Driver.initialize_Driver(Driver);
    driver.get('https://www.google.com/');
    driver.find_element_by_name("q").send_keys("python tutorial");
    #driver.find_element_by_id("btnk").click();
    Driver.close_driver(Driver);




