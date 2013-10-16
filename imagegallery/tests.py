from django.contrib.auth import get_user_model
from django.core import mail
from django.test import LiveServerTestCase, TestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from imagegallery.forms import ContactForm


class ContactFormTest(TestCase):
    fixtures = ['admin_user']

    @classmethod
    def setUpClass(cls):
        cls.data = {'name': 'Batou',
                    'email': 'batou@example.com',
                    'subject': 'hello',
                    'message': 'msg'}
        super(ContactFormTest, cls).setUpClass()

    def setUp(self):
        self.form = ContactForm(self.data)
        super(ContactFormTest, self).setUp()

    def test_validate_contact_form(self):
        self.assertTrue(self.form.is_valid(), 'Invalid contact form data')

    def test_send_email(self):
        self.form.is_valid()
        self.form.send_email()

        self.assertEqual(1, len(mail.outbox),
                         'Only 1 email should have been sent')

        email = mail.outbox[0]

        self.assertEqual(self.data['subject'], email.subject)
        self.assertEqual(self.data['message'], email.body)
        to = get_user_model().objects.get(pk=1).email
        self.assertEqual(to, email.to[0])
        from_email = '{name} {email}'.format(name=self.data['name'],
                                             email=self.data['email'])
        self.assertEqual(from_email, email.from_email)


class SeleniumTestCase(LiveServerTestCase):
    fixtures = ['admin_user']

    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        super(SeleniumTestCase, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(SeleniumTestCase, cls).tearDownClass()

    def test_contact(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/contact'))

        name_input = self.selenium.find_element_by_name('name')
        name_input.send_keys('name')
        email_input = self.selenium.find_element_by_name('email')
        email_input.send_keys('me@example.com')
        subject_input = self.selenium.find_element_by_name('subject')
        subject_input.send_keys('email')
        message_input = self.selenium.find_element_by_name('message')
        message_input.send_keys('email')

        self.selenium.find_element_by_xpath('//input[@value="Send"]').click()

        self.assertEqual(
            'The email was successfully sent.',
            self.selenium.find_element_by_class_name('alert-success').text)
