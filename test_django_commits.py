from selenium import webdriver

driver = webdriver.Chrome()
driver2 = webdriver.Chrome()

driver.get('https://github.com/django/django/commits/master')
commit = driver.find_elements_by_class_name('BtnGroup')

driver2.get('https://github.com/django/django')
commit01 = driver2.find_elements_by_xpath('//*[@id="js-repo-pjax-container"]/div[2]/div[1]/div[6]/div[3]/a')

if commit[0].text == commit01[0].text:
    print("%(expected)s equals %(actual)s" % {"expected": commit01[0].text, "actual": commit[0].text})
else:
    print("%(expected)s not equals %(actual)s" % {"expected": commit01[0].text, "actual": commit[0].text})

driver.quit()
driver2.quit()
