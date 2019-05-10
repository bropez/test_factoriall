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
    # TODO: fix this
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


def choice_4(dr):
    # TODO: figure out how to find the API being called
    """
    This figures out the API call that is being made with the headers and parameters sent
    :param dr: the webdriver used
    :return: no return value
    """
    print("Choice 4 chosen. This will be done later")


def choice_5():
    """
    This writes a bug report
    :return: no return value
    """
    print("Choice 5 chosen. This will be done later")


def choice_6():
    """
    This documents a test case
    :return: no return value
    """
    print("Choice 6 chosen. This will be done later")


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
          "6. document a test case\n"
          "7. Quit")
    choice = int(input("Which would you like to choose? "))
    while choice != 7:
        if choice not in range(1,7):
            choice = int(input("Please enter a number between 1 and 7: "))
        elif choice == 1:
            choice_1(dr)
        elif choice == 2:
            choice_2(dr)
        elif choice == 3:
            choice_3(dr)
        elif choice == 4(dr):
            choice_4(dr)
        elif choice == 5:
            choice_5()
        elif choice == 6:
            choice_6()
    close_interview()


if __name__ == '__main__':
    driver = webdriver.Firefox()
    open_interview(driver)
    choice(driver)
