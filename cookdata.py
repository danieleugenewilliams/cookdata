# cook_data_scraper.py
# Contributors:
#	DanielEugeneWilliams@gmail.com
# 	Martin.J.Adamczyk@gmail.com
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

#web_r = requests.get(url)
web_soup = BeautifulSoup(web_r.text, 'html.parser')

print(web_soup.findAll("#DocList1_WidgetContainer"))

driver = webdriver.Firefox()
driver.get(url)
search_menu = driver.find_element_by_id("Navigator1_SearchCriteria1_menuLabel")
search_menu_hover = ActionChains(firefox).move_to_element(search_menu)
search_menu_hover.perform()

search_criteria = driver.find_element_by_id("Navigator1_SearchCriteria1_LinkButton04")
search_criteria.click()

#TODO: Cycle through #SearchFormEx1_ACSDropDownList_DocumentType
driver.find_element_by_xpath("//select[@name='SearchFormEx1$ACSDropDownList_DocumentType']/option[text()='ABANDONMENT']").click()

search_button = driver.find_element_by_id("SearchFormEx1_btnSearch")
search_button.click()

doclist = driver.find_element_by_id("DocList1_ContentContainer1")

#TODO: Need to get row count and loop through
# for each row, go to the #DocDetails1_ContentContainer1 -> #DocDetails1_Table_Details
# check to see if #DocDetails1_ContentContainer1 -> #DocDetails1_GridView_Grantor exists for TRUSTEES DEED
# check to see if #DocDetails1_ContentContainer1 -> #DocDetails1_Panel_GrantorGrantee exists for POWER OF ATTORNEY

doclist.find_elements_by_xpath('//*[@id="DocList1_ContentContainer1"]/table/tbody/tr/td/div/div/table/tbody/tr[@class="DataGridAlternatingRow"]/td/a[@href]')[1].click()


