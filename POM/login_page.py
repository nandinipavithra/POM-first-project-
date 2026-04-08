from object_repository.loginpage_locators import LoginPageLocators
loc=LoginPageLocators()

class LoginPage:
    def enter_email(self,driver,email_id):
        driver.find_element(*loc.email).send_keys(email_id)


    def enter_pwd(self,driver,email_id,pwd):
        driver.find_element(*loc.password).send_keys(pwd)


    def click_on_login_button(self,driver,email_id):
        driver.find_element(*loc.login_btn).click()
