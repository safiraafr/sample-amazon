class SignUp():
    def __init__(self, driver):
        self.driver = driver

        self.start_link    = 'Start here.'
        self.name_id       = 'ap_customer_name'
        self.email_id      = 'ap_email' 
        self.password_id   = 'ap_password'
        self.repassword_id = 'ap_password_check'
        self.next_id       = 'continue'

    def signup(self):
        self.driver.find_element_by_link_text(self.start_link).click()

    def fill_name(self, name):
        self.driver.find_element_by_id(self.name_id).send_keys(name)
        
    def fill_email(self, email):
        self.driver.find_element_by_id(self.email_id).send_keys(email)

    def fill_password(self, password):
        self.driver.find_element_by_id(self.password_id).send_keys(password)
    
    def fill_repassword(self, repassword):
        self.driver.find_element_by_id(self.repassword_id).send_keys(repassword)

    def next_step(self):
        self.driver.find_element_by_id(self.next_id).click()