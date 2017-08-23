from selenium import webdriver

# Starting a Selenium "webdriver" to pop up a real Firefox browser window
browser = webdriver.Firefox()

#browser.accept_untrusted_certs = True
#browser.assume_untrusted_cert_issuer=True
#browser.accept_next_alert = True

# Using it to open up a web page we're expecting to be served from local PC
browser.get('http://localhost:8000')

# This is our first functional test (FT)
# Checking (making a test assertion) that page has the word "Django" in title
# Note: assert raises an exception if a given condition isn't true

assert 'Django' in browser.title
