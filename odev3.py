from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep


class Test():
    
    #Kullanıcı adı ve şifreyi boş test etme
    def test_username_password(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")

        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        sleep(3)

        usernameInput.send_keys("")
        passwordInput.send_keys("")
        sleep(3)

        loginBtn = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/input")
        loginBtn.click()
        sleep(3)

        errorMessage = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        print(errorMessage.text == "Epic sadface: Username is required")
        sleep(10)
    
    #Şifreyi boş test etme
    def test_empty_password(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")

        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        sleep(3)
        
        usernameInput.send_keys("hasan")
        passwordInput.send_keys("")
        sleep(3)

        loginBtn = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/input")
        loginBtn.click()
        sleep(3)

        errorMessage = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        print(errorMessage.text == "Epic sadface: Password is required")
        sleep(10)

    #Locked out testi
    def test_locked_out(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")

        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        sleep(3)

        usernameInput.send_keys("locked_out_user")
        passwordInput.send_keys("secret_sauce")
        sleep(3)

        loginBtn = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/input")
        loginBtn.click()
        sleep(3)

        errorMessage = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        print(errorMessage.text == "Epic sadface: Sorry, this user has been locked out.")
        sleep(10)

    #Hata mesajında X butonuna tıklama testi
    def close_x_button(self):     
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")

        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        sleep(3)

        usernameInput.send_keys("")
        passwordInput.send_keys("")
        sleep(3)

        loginBtn = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/input")
        loginBtn.click()
        sleep(3)

        xButton = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button")
        xButton.click()
        sleep(10)
    
    #Başarılı giriş yapma testi
    def test_get_login(self):       
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")

        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        sleep(3)

        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        sleep(3)

        loginBtn = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/input")
        loginBtn.click()
        sleep(10)

    #Ürün listesinin testi
    def test_list_products(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        
        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        sleep(3)

        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        sleep(3)

        loginBtn = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/input")
        loginBtn.click()
        sleep(5)

        product_list = driver.find_elements(By.CLASS_NAME, "inventory_item")
        print("Bu sayfada şu an {} adet ürün var.".format(len(product_list)))
        sleep(10)




testClass = Test()
testClass.test_username_password()
testClass.test_empty_password()
testClass.test_locked_out()
testClass.close_x_button()
testClass.test_get_login()
testClass.test_list_products()