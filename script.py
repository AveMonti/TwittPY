import config
from selenium import webdriver

driver = webdriver.Chrome("/Users/mateuszchojnacki/Applications/chromedriver")
def login_twitter(username, password):
    driver.get("https://twitter.com/login")

    username_field = driver.find_element_by_class_name("js-username-field")
    password_field = driver.find_element_by_class_name("js-password-field")

    username_field.send_keys(username)
    driver.implicitly_wait(1)

    password_field.send_keys(password)
    driver.implicitly_wait(1)

    driver.find_element_by_class_name("EdgeButtom--medium").click()

def sendTwitt(twitt):
    inputElement = driver.find_element_by_id("tweet-box-home-timeline")
    inputElement.send_keys(twitt)

    driver.implicitly_wait(1)
    driver.find_element_by_class_name("tweeting-text").click()
def openHashtag(hashtag):
    inputElement = driver.find_element_by_id("search-query")
    inputElement.send_keys(hashtag)
    driver.find_element_by_class_name("nav-search").click()
    # wait here

    driver.implicitly_wait(120)
    manyElements = driver.find_elements_by_class_name("HeartAnimation")
    for element in manyElements:
        element.click()
    driver.implicitly_wait(10)


if __name__ == "__main__":
    username = config.DATACOUP_USERNAME
    password = config.DATACOUP_PASSWORD
    twitt = "Test tweet"
    login_twitter(username, password)
    # sendTwitt(twitt)
    openHashtag("#F4F")
