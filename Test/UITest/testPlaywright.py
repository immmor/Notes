from playwright.sync_api import sync_playwright

def run_playwright_demo():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page()

        # Navigate to a website
        page.goto('https://www.example.com')

        # Perform actions on the page
        # page.click('a')
        # page.fill('input[name="username"]', 'myusername')
        # page.fill('input[name="password"]', 'mypassword')
        # page.click('input[type="submit"]')

        # # Wait for navigation to complete
        # page.wait_for_load_state('networkidle')

        # # Extract information from the page
        # title = page.title()
        # content = page.inner_text('body')

        # # Display the results
        # print(f'Title: {title}')
        # print(f'Content: {content}')

        # # Close the browser
        # browser.close()

# Run the Playwright demo
run_playwright_demo()