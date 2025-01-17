import conftest
from selenium.webdriver.common.by import By

class TrianglePage:
    def __init__(self):
        self.driver = conftest.driver

    # Page elements
    def get_input_vertice1(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[name*='V1']")

    def get_input_vertice2(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[name*='V2']")

    def get_input_vertice3(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[name*='V3']")

    def get_submit_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[value*='Identificar']")

    def get_result_text(self):
        return self.driver.find_element(By.XPATH, "/html/body/div[4]").text

    # Page Actions
    def fill_vertices(self, vertice1, vertice2, vertice3):
        self.get_input_vertice1().clear()
        self.get_input_vertice1().send_keys(str(vertice1))
        self.get_input_vertice2().clear()
        self.get_input_vertice2().send_keys(str(vertice2))
        self.get_input_vertice3().clear()
        self.get_input_vertice3().send_keys(str(vertice3))

    def click_indetify_button(self):
        self.get_submit_button().click()

    def get_result(self):
        return self.get_result_text()
