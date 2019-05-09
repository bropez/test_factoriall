from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def open_interview(driver):
    driver.get('http://qainterview.pythonanywhere.com/')


def close_interview(dr):
    dr.close()


def text_and_click(dr, integer):
    """
    This clears any text in the input box, enters the input, and clicks the submit button
    :param integer: param to be entered into the text box
    :return: no return value
    """
    dr.find_element_by_id("number").clear()
    dr.find_element_by_id("number").send_keys(integer)
    dr.find_element_by_id("getFactorial").click()


def choice_1(dr):
    """
    This choice grabs a hold of the red form validation styling
    :param dr: the webdriver used
    :return: the red form validation styling
    """
    text_and_click(dr, "five")
    elem_attr = dr.find_element_by_id("resultDiv").get_attribute("style")
    print("The element attribute is", "'" + elem_attr + "'")
    return elem_attr


def choice_2(dr):
    """
    this choice finds the console message printed out once the factorial is calculated
    :param dr: the webdriver used
    :return: the console output
    """
    text_and_click(dr, 5)
    log = dr.get_log("browser")
    for entry in log:
        print(entry)


def choice_3(dr):
    """
    this choice tests if the factorial of 5 is 120
    :param dr: the webdriver used
    :return: boolean, if True then it is correct, False if not
    """
    text_and_click(dr, 5)
    output = dr.find_element_by_id("resultDiv").text.split(" ")
    print(120 == int(output[-1]))


def choice(dr):
    # TODO:
    # 2. find teh console message printed
    # 4. figure out the API call being made along with the headers and parameters sent
    # 5. write a bug report
    # 6. document a test case
    print("# 1. write a locator (CSS selector/XPath) for the red form validation styling\n"
          "2. find the console message printed\n"
          "3. write a Selenium script to test that the factorial of 5 is 120\n"
          "4. figure out the API call being made along with the headers and parameters sent\n"
          "5. write a bug report\n"
          "6. document a test case")
    print("Which would you like to run? ")
    # elem_attr = choice_1(dr)
    # choice_2(dr)
    choice_3(dr)

    # close_interview(driver)


if __name__ == '__main__':
    driver = webdriver.Firefox()
    open_interview(driver)
    choice(driver)
