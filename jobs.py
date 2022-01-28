
from os import path
from tkinter import BROWSE
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    page= browser.new_page()
    page.goto('https://www.jobsite.co.uk/')

    browser.close()