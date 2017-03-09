

class PageComponent(object):
    """ PageComponent is a base class that should be extended to represent a UI widget that is used across multiple
    pages. """

    def __init__(self, parent_page_object):
        self.parent_page = parent_page_object

