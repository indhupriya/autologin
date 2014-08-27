from selenium import webdriver

webpage = "http://www.gmail.com" 

un = "example@gmail.com"                //your email-id
pass1="password"                       //your password
driver = webdriver.Firefox()
driver.get(webpage)

ubox = driver.find_element_by_id("Email")
ubox.send_keys(un)

pbox=driver.find_element_by_id("Passwd")
pbox.send_keys(pass1)

submit=driver.find_element_by_id("signIn")
submit.click()

