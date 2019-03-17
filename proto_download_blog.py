#! /usr/bin/env python3
"""
This is prototype for a program that will 'read' students' reflective
journal blogs and investigate them for any words that might be signs
of distress, or unhappiness.
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # For typing the login.
from selenium.webdriver.firefox.options import Options  # To block pop-ups.
from selenium.webdriver.support.select import Select  # For dropdown menu.

url = 'https://ble.soas.ac.uk/mod/hsuforum/route.php?contextid=4648522&action=export'  # Export blog


def save_blog_to_desktop():
    driver = get_browser()
    find_data(driver, url)
    driver.close()


def find_data(driver, url):
    """
    Downloads the entire blog record as a csv file.
    (csv is selected from the dropdown menu, and then downloaded.
    """
    driver.get(url)
    # Manage dropdown menu to select csv.
    dropdown = driver.find_element_by_id('id_format')
    select_box = Select(dropdown)
    select_box.select_by_value('csv')

    driver.find_element_by_id('id_submitbutton').click()


def get_browser():
    """Returns selenium browser, logged in to Moodle."""
    import credentials
    options = Options();

    # Set up firefox to use special profile for selenium_browser.
    # This profile has been configured to avoid dialogues, using the following
    # 'firefox -P selenium_browser' and using 'about:config' (see
    # https://www.lifewire.com/modifying-download-settings-in-firefox-445716)
    # Setting it using selinium 'options' has not worked for this.
    options.profile = "/home/sam/.mozilla/firefox/jtpgrbkl.selenium_browser//"

    login = 'https://ble.soas.ac.uk/login/index.php'
    driver = webdriver.Firefox(firefox_options=options);
    driver.get(login)
    driver.find_element_by_id("username").send_keys(credentials.username)
    driver.find_element_by_id("password").send_keys(credentials.password)
    driver.find_element_by_id("loginbtn").click()
    return driver


if __name__ == '__main__':
    save_blog_to_desktop()
