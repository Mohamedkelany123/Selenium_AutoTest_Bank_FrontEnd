# Selenium_AutoTest_Bank_FrontEnd
 Automation test for the Bank-FronEnd and Bank-Loans_Django_backend project

# Open The Terminal(Make sure Bank-FronEnd and Bank-Loans_Django_backend project are opened and running):
1-  venv\Scripts\activate
2-  cd .\selenium_project\
Run: 
3-  python my_test.py

# The Scenario Covered:
Loan Management System Workflow:
1.	Bank Personnel's Role:
•	Log into the system with authorized credentials.
•	Create Loan Funds: Bank Personnel can create new loan funds, specifying fund names (e.g., "Cars"), maximum and minimum loan amounts, interest rates, and loan durations.
•	Manage Loan Funds: Bank Personnel can view, or delete existing loan funds.
2.	Loan Provider's Role:
•	Log into the system with valid credentials.
•	View Loan Funds: Loan Providers can access the list of available loan funds, including fund details like fund names, maximum and minimum loan amounts, interest rates, and loan durations.
•	Provide Loan Amount: Loan Providers can select a loan fund by its unique ID and add the amount they are willing to offer as a loan.
3.	Customer's Role:
•	Register Account
•	Log into the system using authorized login details.
•	Browse Available Funds: Customers can view a list of available loan funds, showcasing information about each fund, such as fund names, maximum and minimum loan amounts, interest rates, and loan durations.
•	Apply for a Loan: Customers can select a specific loan fund by its unique ID and enter the desired loan amount they require.
•	Loan Creation: Upon submission, a loan will be generated, capturing all relevant loan details, including the calculated monthly installments based on the provided interest rate. The loan status is automatically set as "Requested."
4.	Bank Personnel's Approval/Rejection Process:
•	Bank Personnel can view all loan requests with their respective details.
•	Loan Approval: Bank Personnel can approve a customer's loan request, indicating acceptance.
•	Loan Rejection: In the event of rejecting a loan request, the status will be updated accordingly.
