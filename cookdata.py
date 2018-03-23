# cook_data_scraper.py
# Contributors:
#	@dewilliams
#########################################################
# web service to analyze real estate trends using publicly available docs
# Test scenario for Cook County, Illinois. 
# 1. http://cookrecorder.com/
# 2. Left nav -> Search Public Records
# 3. http://162.217.184.82/i2/default.aspx
# 4. In top nav, Search Criteria -> Recorded Date Search -> Select date range, all doc types, search
# 5. Click record in left pane, scrape data in right pane.
# 6. Click next page button in bottom of left pane.
# 7. Repeat steps 5 & 6
# One Doc Type of interest: Mortgage. Gives current mortgage value. Warranty Deed.
#########################################################
# import libs
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

url = "http://162.217.184.82/i2/default.aspx"

driver = webdriver.Firefox()
driver.get(url)
print("url finished")

action = ActionChains(driver)
time.sleep(5)
search_menu = driver.find_element_by_id("Navigator1_SearchCriteria1_menuLabel")
action.move_to_element(search_menu)
action.perform()
print("search_menu finished")
search_criteria = driver.find_element_by_id("Navigator1_SearchCriteria1_LinkButton04")
action.move_to_element(search_criteria)
search_criteria.click()
print("search_crit finished")
time.sleep(3)
#TODO: Cycle through #SearchFormEx1_ACSDropDownList_DocumentType to get LIS PENDENS
driver.find_element_by_xpath("//select[@name='SearchFormEx1$ACSDropDownList_DocumentType']/option[text()='LIS PENDENS']").click()
search_button = driver.find_element_by_id("SearchFormEx1_btnSearch")
search_button.click()
time.sleep(3)
print("search_btn finished")
doc_list = driver.find_element_by_id("DocList1_WidgetContainer")
print("doc_list1 finished")
# get row count and loop through
row_count = len(doc_list.find_elements_by_xpath('//*[@id="DocList1_ContentContainer1"]/table/tbody/tr[1]/td/div/div[2]/table/tbody/tr')) 
print("row_count finished")
time.sleep(1.5)
# for each row, go to the #DocDetails1_ContentContainer1 -> #DocDetails1_Table_Details
doc_list = driver.find_element_by_id("DocList1_WidgetContainer")
print("doc_list2 finished")
for row in range(1,row_count+1):
    print("in loop "+str(row))
    time.sleep(3)
    doc_list = driver.find_element_by_id("DocList1_WidgetContainer")	
    doc_list.find_element_by_xpath('//*[@id="DocList1_ContentContainer1"]/table/tbody/tr[1]/td/div/div[2]/table/tbody/tr['+str(row)+']/td[2]/a').click()
	#TODO: logic to save data goes here
    doc_list = driver.find_element_by_id("DocList1_WidgetContainer")


#TODO: each dropdown list item of interest will be in its own function below
#TODO: LIS PENDENS function
#TODO: #DocDetails1_Table_Details data function
#TODO: #DocDetails1_Panel_GrantorGrantee data function
