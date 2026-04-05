from playwright.sync_api import sync_playwright
import time

def take_screenshot():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        page.goto('http://localhost:8000')
        time.sleep(2)  # wait for GSAP to load
        page.screenshot(path='/Users/etosegun/Documents/websites /kliques homepage/screenshot_hero.png')
        
        # scroll to end
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(2)
        page.screenshot(path='/Users/etosegun/Documents/websites /kliques homepage/screenshot_end.png')
        
        browser.close()

take_screenshot()
