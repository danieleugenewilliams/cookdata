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

url = "http://162.217.184.82/i2/default.aspx"

driver = webdriver.Firefox()
driver.get(url)

search_menu = driver.find_element_by_id("Navigator1_SearchCriteria1_menuLabel")
search_menu_hover = ActionChains(driver).move_to_element(search_menu)
search_menu_hover.perform()
search_criteria = driver.find_element_by_id("Navigator1_SearchCriteria1_LinkButton04")
search_criteria.click()

#TODO: Cycle through #SearchFormEx1_ACSDropDownList_DocumentType to get LIS PENDENS
driver.find_element_by_xpath("//select[@name='SearchFormEx1$ACSDropDownList_DocumentType']/option[text()='LIS PENDENS']").click()
search_button = driver.find_element_by_id("SearchFormEx1_btnSearch")
search_button.click()

doc_list = driver.find_element_by_id("DocList1_WidgetContainer")

# get row count and loop through
row_count = len(doc_list.find_elements_by_xpath('//*[@id="DocList1_ContentContainer1"]/table/tbody/tr[1]/td/div/div[2]/table/tbody/tr')) 

# for each row, go to the #DocDetails1_ContentContainer1 -> #DocDetails1_Table_Details
doc_list = driver.find_element_by_id("DocList1_WidgetContainer")
for row in range(1,row_count+1):
    doc_list.find_elements_by_xpath('//*[@id="DocList1_ContentContainer1"]/table/tbody/tr[1]/td/div/div[2]/table/tbody/tr['+str(row)+']/td[2]/a')[0].click()
	#TODO: logic to save data goes here
    doc_list = driver.find_element_by_id("DocList1_WidgetContainer")


#TODO: each dropdown list item of interest will be in its own function below
#TODO: LIS PENDENS function
#TODO: #DocDetails1_Table_Details data function
#TODO: #DocDetails1_Panel_GrantorGrantee data function
