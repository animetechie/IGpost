import time
from selenium import webdriver

# Replace USERNAME and PASSWORD with your Instagram login credentials
USERNAME = 'YOUR_USERNAME'
PASSWORD = 'YOUR_PASSWORD'

# Replace POST_URL with the URL of the post you want to comment on
POST_URL = 'https://www.instagram.com/p/POST_ID/'

# Replace COMMENT_TEXT with the text of the comment you want to leave
COMMENT_TEXT = 'This is an automated comment!'

# Set the path to the webdriver executable
DRIVER_PATH = '/path/to/webdriver'

# Create a webdriver object
driver = webdriver.Chrome(DRIVER_PATH)

# Navigate to the Instagram login page
driver.get('https://www.instagram.com/accounts/login/')

# Wait for the page to load
time.sleep(2)

# Enter the login credentials
driver.find_element_by_name('username').send_keys(USERNAME)
driver.find_element_by_name('password').send_keys(PASSWORD)

# Click the login button
driver.find_element_by_css_selector('button[type="submit"]').click()

# Wait for the page to load
time.sleep(2)

# Navigate to the post URL
driver.get(POST_URL)

# Wait for the page to load
time.sleep(2)

# Click the comment button
driver.find_element_by_css_selector('button[aria-label="Comment"]').click()

# Wait for the comment field to appear
time.sleep(1)

# Enter the comment text
driver.find_element_by_css_selector('textarea[aria-label="Add a comment…"]').send_keys(COMMENT_TEXT)

# Click the post button
driver.find_element_by_css_selector('button[type="submit"]').click()

# Wait for the comment to be posted
time.sleep(1)

# Click the like button
driver.find_element_by_css_selector('button[aria-label="Like"]').click()

# Close the webdriver
driver.close()
