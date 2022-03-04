class SignIn():
    def __init__(self, driver):
        self.driver = driver

        self.login_xpath = '//*[@id="nav-signin-tooltip"]/a'
        self.email_id    = 'ap_email'
        self.next_id     = 'continue'
        self.password_id = 'ap_password'
        self.submit_id   = 'signInSubmit'

    def login(self):
        self.driver.find_element_by_xpath(self.login_xpath).click()

    def fill_email(self, email):
        self.driver.find_element_by_id(self.email_id).send_keys(email)

    def next_step(self):
        self.driver.find_element_by_id(self.next_id).click()

    def fill_password(self, password):
        self.driver.find_element_by_id(self.password_id).send_keys(password) 

    def submit(self):
        self.driver.find_element_by_xpath(self.submit_id).click()