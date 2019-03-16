from selenium import webdriver


class Application:


    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(5)

    def get_value_age(self):
        wd = self.wd
        return wd.find_element_by_id("old").text

    def click_button(self):
        wd = self.wd
        wd.find_element_by_css_selector("button.btn.btn-default").click()

    def fill_date(self, date):
        wd = self.wd
        wd.find_element_by_id("date").clear()
        wd.find_element_by_id("date").send_keys(date)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://tutu-ru.github.io/")

    def destroy(self):
        self.wd.quit()

