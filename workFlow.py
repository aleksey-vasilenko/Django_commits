from selenium import webdriver

class workWithSelenium:
    driver = webdriver

    def __init__(self, driver):
        self.driver = driver

    def findByClassName(self, className):
        print('find by class name, class name = %(class_name)s' % {"class_name": className})
        return self.driver.find_elements_by_class_name(className)

    def findByXpath(self, path):
        print('find by xpath, xpath = %(xpath)s' % {"xpath": path})
        return self.driver.find_elements_by_xpath(path)

    def closeDriver(self):
        self.driver.close()

    def getDriver(self, reference):
        self.driver.get(reference)