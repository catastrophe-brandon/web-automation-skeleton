

class PageObject(object):
    """ Base PageObject class from which specific page objects should be derived. """

    def __init__(self, webdriver):
        self.webdriver = webdriver

