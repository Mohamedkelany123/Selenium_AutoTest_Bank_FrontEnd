from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the WebDriver (in this case, Chrome)
driver = webdriver.Chrome()

#Loan Management System Workflow:

# Navigate to a website
driver.get("http://localhost:8080/login")
time.sleep(1)

# 1.Bank Personnel's Role: ----------------------------------------------------------------------------------#

# Enter username "bankPersonnel"
# username_field = driver.find_element(By.XPATH, "//label[text()='Username']/following-sibling::div/input")
username_field= driver.find_element(By.ID, "Username")
username_field.send_keys("bankPersonnel")

time.sleep(1)

# Enter Password
password_field = driver.find_element(By.ID, "Password")
password_field.send_keys("bankPersonnel")

time.sleep(2)

# Find and click the "Login" button
login_button = driver.find_element(By.CSS_SELECTOR, ".submit-button")
login_button.click()

time.sleep(2)

#Create Loan Fund Button
button = driver.find_element(By.ID, "createLoanFunds")
button.click()

time.sleep(2)

#Enter LoanFund name "testFund"
loanFund_name_field = driver.find_element(By.ID, "Name")
loanFund_name_field.send_keys("testFund")

time.sleep(1)

#Enter Max Loan Amount "10,000"
loanFund_maxAmount_field = driver.find_element(By.ID, "Max Loan Amount")
loanFund_maxAmount_field.send_keys("10000")

time.sleep(1)

#Enter Min Loan Amount "10,000"
loanFund_minAmount_field = driver.find_element(By.ID, "Min Loan Amount")
loanFund_minAmount_field.send_keys("100")

time.sleep(1)

#Enter Interest Rate  "2.5%"
loanFund_interest_rate_field = driver.find_element(By.ID, "Interest Rate")
loanFund_interest_rate_field.send_keys("2.5")

time.sleep(1)

#Enter Loan Duration "12"
loanFund_loan_duration_field = driver.find_element(By.ID, "Loan Duration")
loanFund_loan_duration_field.send_keys("12")

time.sleep(3)

#Create Loan Fund
button = driver.find_element(By.ID, "submitLoanFund")
button.click()

time.sleep(3)

#Logout
button = driver.find_element(By.ID, "logOut")
button.click()


time.sleep(2)

#-----------------------------------------------------------------------------------------------#

#2.	Loan Provider's Role: ----------------------------------------------------------------------#

# Enter username "loanProvider"
username_field = driver.find_element(By.ID, "Username")
username_field.send_keys("loanProvider")

time.sleep(1)

# Enter Password "loanProvider"
password_field = driver.find_element(By.ID, "Password")
password_field.send_keys("loanProvider")

time.sleep(2)

# Find and click the "Login" button
login_button = driver.find_element(By.CSS_SELECTOR, ".submit-button")
login_button.click()

time.sleep(3)

# Find all elements with id="fundID"
fund_id_elements = driver.find_elements(By.ID, "fundID")

# Find all elements with id="fundTitle"
fund_title_elements = driver.find_elements(By.ID, "fundTitle")

idTemp = 0
# Loop through the indices and print their text
for i in range(len(fund_title_elements)):
    element = fund_title_elements[i]
    elementId = fund_id_elements[i]
    fund_input_id = f"fundInput{elementId.text}"
    add_fund_btn_id = f"addFund{elementId.text}"
    idTemp = elementId.text
    
    
    if element.text == "testFund":
        fund_field = driver.find_element(By.ID, fund_input_id)
        fund_field.send_keys("10000")
        time.sleep(3)  

        # Find the "addFund+id" button by ID and click it
        add_fund_btn = driver.find_element(By.ID, add_fund_btn_id)
        add_fund_btn.click()

time.sleep(3)

#Logout
button = driver.find_element(By.ID, "logOut")
button.click()


time.sleep(3)








#3.	Customer's Role:---------------------------------------------------------------------------------#

#REGISTER A NEW CUSTOMER
wait = WebDriverWait(driver, 4)
register_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".register-link")))
register_button.click()

time.sleep(3)


username_field = driver.find_element(By.ID, "Username")
username_field.send_keys("testUser")

time.sleep(1)

password_field = driver.find_element(By.ID, "Password")
password_field.send_keys("testUser123")

time.sleep(1)

email_field = driver.find_element(By.ID, "Email")
email_field.send_keys("testUser@gmail.com")

time.sleep(3)

button = driver.find_element(By.ID, "submit")
button.click()

time.sleep(3)

#LOGIN
username_field = driver.find_element(By.ID, "Username")
username_field.send_keys("testUser")

time.sleep(1)

password_field = driver.find_element(By.ID, "Password")
password_field.send_keys("testUser123")

time.sleep(1)

# Find and click the "Login" button
login_button = driver.find_element(By.CSS_SELECTOR, ".submit-button")
login_button.click()

time.sleep(2)

#Create Loan Fund Button To See the id of the testLoanFund
button = driver.find_element(By.ID, "viewLoanFunds")
button.click()

time.sleep(3)

#Create Loan Fund Button To See the id of the testLoanFund
button = driver.find_element(By.ID, "createLoan")
button.click()

time.sleep(3)

#Enter LoanFund ID 
loanFund_name_field = driver.find_element(By.ID, "Loan Fund ID")
loanFund_name_field.send_keys({idTemp})

time.sleep(1)

#Enter Loan Amount
loanFund_name_field = driver.find_element(By.ID, "Amount")
loanFund_name_field.send_keys('5000')

time.sleep(1)

#Create Loan Fund Button To See the id of the testLoanFund
button = driver.find_element(By.ID, "createLoanButton")
button.click()



time.sleep(3)

#Logout
button = driver.find_element(By.ID, "logOut")
button.click()

#4.	Bank Personnel's Approval/Rejection Process:------------------------------------------------#

time.sleep(2)

# Enter username "bankPersonnel"
username_field = driver.find_element(By.ID, "Username")
username_field.send_keys("bankPersonnel")

time.sleep(1)

# Enter Password
password_field = driver.find_element(By.ID, "Password")
password_field.send_keys("bankPersonnel")

time.sleep(1)

# Find and click the "Login" button
login_button = driver.find_element(By.CSS_SELECTOR, ".submit-button")
login_button.click()

time.sleep(1)

#View Loan Fund Button
button = driver.find_element(By.ID, "viewLoans")
button.click()

time.sleep(3)

result_string = "acceptLoan" + str(idTemp)
print(result_string)

#Accept Test Loan Loan Fund Button
button = driver.find_element(By.ID, result_string)
button.click()

time.sleep(3)

#Logout
button = driver.find_element(By.ID, "logOut")
button.click()

time.sleep(1)

#5- User Login to see the approved loan----------------------------------------------------------#

#LOGIN
username_field = driver.find_element(By.ID, "Username")
username_field.send_keys("testUser")

time.sleep(1)

password_field = driver.find_element(By.ID, "Password")
password_field.send_keys("testUser123")

time.sleep(1)

# Find and click the "Login" button
login_button = driver.find_element(By.ID, "submit")
login_button.click()

time.sleep(2)

#View Loan Button
button = driver.find_element(By.ID, "viewLoansCustomer")
button.click()

time.sleep(4)


#---------------------------------------------------------------------------------------------#

# Close the browser
driver.quit()