from selenium import webdriver

GECKODRIVER = "/home/ebris/drivers/selenium/geckodriver"

browser = webdriver.Firefox(executable_path=GECKODRIVER)
browser.get("http://localhost:9000")

print(browser.title)
print(browser.name)
print(browser.current_url)

assert "Django" in browser.title
