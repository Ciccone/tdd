from selenium import webdriver

browser = webdriver.Firefox()
browser.accept_untrusted_certs = True
browser.assume_untrusted_cert_issuer=True
browser.accept_next_alert = True
browser.get('http://localhost:8000')


# assert - raise an exception if a given condition isn't true
assert 'Django' in browser.title
# This is our first functional test (FT)
