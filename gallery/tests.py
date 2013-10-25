from os.path import realpath, dirname, join
from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver


class SeleniumTestCase(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        super(SeleniumTestCase, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(SeleniumTestCase, cls).tearDownClass()

    def fill_form(self):
        title_input = self.selenium.find_element_by_name('title')
        title_input.send_keys('Title')
        pub_date_input = self.selenium.find_element_by_name('pub_date')
        pub_date_input.send_keys('2013-12-20')
        caption_input = self.selenium.find_element_by_name('caption')
        caption_input.send_keys('Text')
        img_path = join(dirname(dirname(realpath(__file__))),
                        'imagegallery/static/imagegallery/img/day268.jpg')
        image_input = self.selenium.find_element_by_name('image')
        image_input.send_keys(img_path)

    def test_upload_one_image(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/gallery/upload'))

        self.fill_form()

        self.selenium.find_element_by_xpath('//input[@type="submit"]').click()

        self.assertEqual(
            'The image was successfully uploaded.',
            self.selenium.find_element_by_class_name('alert-success').text)

        self.selenium.get('%s%s' % (self.live_server_url, '/gallery'))

        self.assertEqual(
            1,
            len(self.selenium.find_elements_by_class_name('thumbnail')),
            'One image should be uploaded.')

    def test_upload_two_images(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/gallery/upload'))

        self.fill_form()

        self.selenium.find_element_by_xpath('//input[@type="submit"]').click()

        self.assertEqual(
            'The image was successfully uploaded.',
            self.selenium.find_element_by_class_name('alert-success').text)

        self.fill_form()

        self.selenium.find_element_by_xpath('//input[@type="submit"]').click()

        self.assertEqual(
            'The image was successfully uploaded.',
            self.selenium.find_element_by_class_name('alert-success').text)

        self.selenium.get('%s%s' % (self.live_server_url, '/gallery'))

        self.assertEqual(
            2,
            len(self.selenium.find_elements_by_class_name('thumbnail')),
            'Two images should be uploaded.')
