#! /usr/bin/env python3
"""
To download student journals into a csv file.
As Firefox downloads only to Desktop, the `ls_desktop()` and `mv_csv()`
functions are necessary to have the data in the current directory.

This module is part of a program that will 'read' students' reflective
journal blogs and investigate them for any words that might be signs
of distress, or unhappiness.
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # For typing the login.
from selenium.webdriver.firefox.options import Options  # To block pop-ups.
from selenium.webdriver.support.select import Select  # For dropdown menu.
import os
import shutil

url = 'https://ble.soas.ac.uk/mod/hsuforum/route.php?contextid=4648522&action=export'  # Export blog


def save_blog_to_desktop():  # main()
    desktop = ls_desktop()
    driver = get_browser()
    find_data(driver, url)
    driver.close()
    mv_csv(desktop)


def ls_desktop():
    desktop = os.listdir('/home/sam/Desktop/')
    return desktop


def mv_csv(desktop):
    new_desktop = os.listdir('/home/sam/Desktop/')
    dif_desktop = [item for item in new_desktop if item not in desktop]
    if len(dif_desktop) != 1:
        raise Exception('Unique new download not found')
    elif 'downloads' not in os.listdir():
        raise Exception('downloads directory not found. Downloaded file remains on Desktop.')
    else:
        journal_export = '/home/sam/Desktop/' + dif_desktop[0]
        downloads_path = os.getcwd() + '/downloads'
        shutil.move(journal_export, downloads_path)


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
