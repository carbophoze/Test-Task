del report /q
del allure-report /q
cls
pytest tests/ --alluredir=report 
allure serve report/ 

