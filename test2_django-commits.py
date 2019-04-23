import staticNames
import workFlow

from selenium import webdriver

workWithClassName = workFlow.workWithSelenium(webdriver.Chrome())
workWithXpath = workFlow.workWithSelenium(webdriver.Chrome())

workWithClassName.getDriver(staticNames.staticReference.commitReference)
commit = workWithClassName.findByClassName(staticNames.staticClassName.allCommits)

workWithXpath.getDriver(staticNames.staticReference.lastCommitRefernce)
commit01 = workWithXpath.findByXpath(staticNames.staticXpath.lastCommit)

if commit[0].text == commit01[0].text:
    print("%(expected)s equals %(actual)s" % {"expected":commit01[0].text, "actual": commit[0].text})
else:
    print("%(expected)s not equals %(actual)s" % {"expected": commit01[0].text, "actual": commit[0].text})

workWithClassName.closeDriver()
workWithXpath.closeDriver()