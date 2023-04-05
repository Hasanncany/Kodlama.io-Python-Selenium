#Burada wait_for_element_visible() Fonksiyonu yerime sleep fonksiyonunu kullanmamın sebebi About sayfasının tamamlanmasını beklemek ve ekran görüntüsünü daha güzel alabilmek.

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from pathlib import Path
from datetime import date
import pytest
import time

class Test_Sauce():

    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok = True)

    def teardown_method(self):
        self.driver.quit()

    def wait_for_element_visible(self,locator):
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located(locator))

    # Başarılı giriş
    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_get_login(self,username,password):
        self.wait_for_element_visible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")

        self.wait_for_element_visible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")

        action = ActionChains(self.driver)
        action.send_keys_to_element(usernameInput,username)
        action.send_keys_to_element(passwordInput,password)
        action.perform()

        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()      
        self.driver.save_screenshot(f"{self.folderPath}/test-get-login-{username}-{password}.png") 
    
    # Başarısız giriş
    @pytest.mark.parametrize("username,password",[("1","1"),("hasancan","yıldırım"),("kodlamaio","12345")])
    def test_invalid_login(self,username,password):
        self.wait_for_element_visible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")

        self.wait_for_element_visible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")

        action = ActionChains(self.driver)
        action.send_keys_to_element(usernameInput, username)
        action.send_keys_to_element(passwordInput,password)
        action.perform()

        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()

        errorMesage = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-invalid-login-{username}-{password}.png") 
        assert errorMesage.text == 'Epic sadface: Username and password do not match any user in this service'

    # Boş giriş
    @pytest.mark.parametrize("username,password",[("", "")])
    def test_empty_login(self,username,password):
        self.wait_for_element_visible((By.ID, "user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        
        self.wait_for_element_visible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID, "password")

        action = ActionChains(self.driver)
        action.send_keys_to_element(usernameInput,username)
        action.send_keys_to_element(passwordInput,password)
        action.perform()

        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()

        errorMessage = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-empty-login-{username}-{password}.png")
        assert errorMessage.text == 'Epic sadface: Username is required'      

    # Şifre boş giriş
    @pytest.mark.parametrize("username,password",[("hasancan","")])
    def test_empty_password(self,username,password):
        self.wait_for_element_visible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")

        self.wait_for_element_visible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")

        action = ActionChains(self.driver)
        action.send_keys_to_element(usernameInput,username)
        action.send_keys_to_element(passwordInput,password)
        action.perform()

        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()

        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-empty-password-login-{username}-{password}.png")
        assert errorMessage.text == 'Epic sadface: Password is required'

    # Locked out
    @pytest.mark.parametrize("username,password",[("locked_out_user","secret_sauce")])
    def test_locked_out(self,username,password):
        self.wait_for_element_visible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")

        self.wait_for_element_visible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")

        action = ActionChains(self.driver)
        action.send_keys_to_element(usernameInput,username)
        action.send_keys_to_element(passwordInput,password)
        action.perform()

        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()

        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-locked-out-login-{username}-{password}.png")
        assert errorMessage.text == 'Epic sadface: Sorry, this user has been locked out.'

    # Problemli Giriş
    @pytest.mark.parametrize("username,password",[("problem_user","secret_sauce")])
    def test_problem_user(self,username,password):
        self.wait_for_element_visible((By.ID, "user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")

        self.wait_for_element_visible((By.ID, "password"))
        passwordInput = self.driver.find_element(By.ID, "password")

        action = ActionChains(self.driver)
        action.send_keys_to_element(usernameInput,username)
        action.send_keys_to_element(passwordInput,password)
        action.perform()

        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        self.driver.save_screenshot(f"{self.folderPath}/test-problem-user-{username}-{password}.png")
        
    # İcon testi
    @pytest.mark.parametrize("username,password",[("hasancan","yıldırım")])
    def test_x_icon(self,username,password):
        self.wait_for_element_visible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")

        self.wait_for_element_visible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")

        action = ActionChains(self.driver)
        action.send_keys_to_element(usernameInput,username)
        action.send_keys_to_element(passwordInput,password)
        action.perform()

        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()

        self.driver.save_screenshot(f"{self.folderPath}/test-icon-{username}-{password}.png")

        xBtn = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3/button")
        xBtn.click()

    # Ürün listesi
    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_inventory(self,username,password):
        self.wait_for_element_visible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")

        self.wait_for_element_visible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")

        action = ActionChains(self.driver)
        action.send_keys_to_element(usernameInput,username)
        action.send_keys_to_element(passwordInput,password)
        action.perform()
        
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()

        self.driver.get("https://www.saucedemo.com/inventory.html")
        self.driver.save_screenshot(f"{self.folderPath}/test-product-list-{username}-{password}.png")
   
   # Ürün sayısı
    @pytest.mark.parametrize("username,password", [("standard_user", "secret_sauce")])
    def test_item_number(self, username, password):
        self.wait_for_element_visible((By.ID, "user-name"))
        userNameInput = self.driver.find_element(By.ID, "user-name")
       
        self.wait_for_element_visible((By.ID, "password"))
        passwordInput = self.driver.find_element(By.ID, "password")

        action = ActionChains(self.driver)
        action.send_keys_to_element(userNameInput, username)
        action.send_keys_to_element(passwordInput, password)
        action.perform()
       
        logIn = self.driver.find_element(By.ID, "login-button")
        logIn.click()
       
        itemNumber = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        self.driver.save_screenshot(f"{self.folderPath}/test-item-number-{username}-{password}.png")
        assert len(itemNumber) == 6

    # Ürün Ekle ve Sepete Git
    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_add_product(self,username,password):
        self.wait_for_element_visible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")

        self.wait_for_element_visible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")

        action = ActionChains(self.driver)
        action.send_keys_to_element(usernameInput,username)
        action.send_keys_to_element(passwordInput,password)
        action.perform()

        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()

        add_button = self.driver.find_element(By.XPATH,"//*[@id='add-to-cart-sauce-labs-bike-light']")
        add_button.click()
        time.sleep(1)
        self.driver.save_screenshot(f"{self.folderPath}/test-add-cart-{username}-{password}.png")

        products_button = self.driver.find_element(By.XPATH,"//*[@id='shopping_cart_container']/a")
        products_button.click()
        self.driver.save_screenshot(f"{self.folderPath}/test-show-carts-{username}-{password}.png")

    # Ürün Satın Alma
    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_buy(self,username,password):
        self.wait_for_element_visible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")

        self.wait_for_element_visible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")

        action = ActionChains(self.driver)
        action.send_keys_to_element(usernameInput,username)
        action.send_keys_to_element(passwordInput,password)
        action.perform()

        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()

        add_button = self.driver.find_element(By.XPATH,"//*[@id='add-to-cart-sauce-labs-bike-light']")
        add_button.click()
        time.sleep(1)

        products_button = self.driver.find_element(By.XPATH,"//*[@id='shopping_cart_container']/a")
        products_button.click()

        checkoutBtn = self.driver.find_element(By.XPATH,"//*[@id='checkout']")
        checkoutBtn.click()

        self.wait_for_element_visible((By.ID, "first-name"))
        firstNameInput = self.driver.find_element(By.ID, "first-name")
        firstNameInput.send_keys("Hasancan")

        self.wait_for_element_visible((By.ID, "last-name"))
        lastNameInput = self.driver.find_element(By.ID, "last-name")
        lastNameInput.send_keys("Yıldırım")

        self.wait_for_element_visible((By.ID, "postal-code"))
        postalCodeInput = self.driver.find_element(By.ID, "postal-code")
        postalCodeInput.send_keys("34000")
        time.sleep(1)
        self.driver.save_screenshot(f"{self.folderPath}/test-buy-WritingPersonalDetails-{username}-{password}.png")

        continueBtn = self.driver.find_element(By.ID, "continue")
        continueBtn.click()
        time.sleep(2)
        self.driver.save_screenshot(f"{self.folderPath}/test-buy-invoiceScreen-{username}-{password}.png")

        finishBtn = self.driver.find_element(By.XPATH, "//*[@id='finish']")
        finishBtn.click()
        time.sleep(2)
        self.driver.save_screenshot(f"{self.folderPath}/test-buy-finishScreen-{username}-{password}.png")

        backHomeBtn = self.driver.find_element(By.ID, "back-to-products")
        backHomeBtn.click()
        time.sleep(2)
        self.driver.save_screenshot(f"{self.folderPath}/test-buy-backHome-{username}-{password}.png")

    # Filtreler
    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_product_sort(self,username,password):
        self.wait_for_element_visible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")

        self.wait_for_element_visible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")

        action = ActionChains(self.driver)
        action.send_keys_to_element(usernameInput,username)
        action.send_keys_to_element(passwordInput,password)
        action.perform()

        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()

        filterBtn = self.driver.find_element(By.CLASS_NAME,"product_sort_container")
        filterBtn.click()
        self.driver.save_screenshot(f"{self.folderPath}/test-product-sort-{username}-{password}.png")

    # About
    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_about(self,username,password):
        self.wait_for_element_visible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")

        self.wait_for_element_visible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")

        action = ActionChains(self.driver)
        action.send_keys_to_element(usernameInput,username)
        action.send_keys_to_element(passwordInput,password)
        action.perform()

        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()

        menuBtn = self.driver.find_element(By.ID,"react-burger-menu-btn")
        menuBtn.click()
        time.sleep(1)

        aboutBtn = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[1]/div/div[2]/div[1]/nav/a[2]")
        aboutBtn.click()
        time.sleep(10)
        self.driver.save_screenshot(f"{self.folderPath}/test-about-{username}-{password}.png")
    
    # Çıkış yap
    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_log_out(self,username,password):
        self.wait_for_element_visible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")

        self.wait_for_element_visible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")

        action = ActionChains(self.driver)
        action.send_keys_to_element(usernameInput,username)
        action.send_keys_to_element(passwordInput,password)
        action.perform()
        
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()

        menuBtn = self.driver.find_element(By.ID,"react-burger-menu-btn")
        menuBtn.click()
        time.sleep(2)

        logoutBtn = self.driver.find_element(By.XPATH,"//*[@id='logout_sidebar_link']")
        self.driver.save_screenshot(f"{self.folderPath}/test-log-out-{username}-{password}.png")
        logoutBtn.click()
