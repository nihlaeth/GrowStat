import unittest

# Examples of more tests:
# https://gist.github.com/sontek/1420255
# Especially the integration tests there will be useful when we want to
# test whether we are getting the right page.

class PageTests(unittest.TestCase):
    def setUp(self):
        from growstat import main
        app = main({})
        from webtest import TestApp
        self.testapp = TestApp(app)
        # List of routes taken from growstat/__init__.py
        # Is there a better way to obtain this list
        # FIXME google for `pyramid test list of pages`
        # There must be better pattern, surely.
        self.working_pages = [
            '/',
            '/list',
            '/add/supply',
            '/add/column',
            '/add/slot',
            '/add/plant',
            '/record/watering',
            '/record/water',
            '/record/nutrients',
            '/record/ph',
            '/record/ec',
            '/record/temp',
            '/record/humidity',
            '/record/height',
            '/record/harvest',
            '/record/picture',
            '/record/log']

        # This is where we keep pages that we expect to not work
        # Once the pages is implemented, the test will fail, reminding
        # us to move the page to `self.working_pages`.
        self.nonworking_pages = [
            '/timeline'
            '/edit/supply/{id}',
            '/edit/supply/{id}',
            '/edit/slot/{id}',
            '/edit/plant/{id}',
            '/edit/watering/{id}',
            '/edit/water/{id}',
            '/edit/nutrients/{id}',
            '/edit/ph/{id}',
            '/edit/ec/{id}',
            '/edit/temp/{id}',
            '/edit/humidity/{id}',
            '/edit/length/{id}',
            '/edit/harvest/{id}',
            '/edit/picture/{id}',
            '/edit/log/{id}',
        ]

    # This test fails if any page request gives a response other than
    # `200 OK`
    def test_working_pages(self):
        failed_pages = []
        for page_i in self.working_pages:
            try:
                res = self.testapp.get(page_i, status=200)
            except:
                failed_pages.append(page_i)

        if len(failed_pages) > 0:
            raise Exception("These pages didn't load:\n    " +
                "\n    ".join(failed_pages))

    def test_nonworking_pages(self):
        failed_404s = []
        for page_i in self.nonworking_pages:
            try: 
                res = self.testapp.get(page_i, status=404)
            except:
                failed_404s.append(page_i)

        if len(failed_404s) > 0:
            raise Exception("These pages failed to give a 404:\n    " +
                "\n    ".join(failed_404s))

## Original tests in tests.py
# from pyramid import testing
#
# class ViewTests(unittest.TestCase):
#     def setUp(self):
#         self.config = testing.setUp()
#
#     def tearDown(self):
#         testing.tearDown()
#
#     def test_my_view(self):
#         from .views import my_view
#         request = testing.DummyRequest()
#         info = my_view(request)
#         self.assertEqual(info['project'], 'GrowStat')
