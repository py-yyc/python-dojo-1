from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

def main():
	driver = webdriver.Chrome()
	
	# Selenium navigates to the open data page
	driver.get("https://cityonline.calgary.ca/Pages/Category.aspx?cat=CITYonlineDefault&category=PublicData&publicdata")
	
	# get each open data url on the page
	urls = ["test"]
	
	# Go into each page and add items to the cart
	for url in urls:
		link = driver.find_element_by_tag_name("a")
		print link
		
	# Go to the cart page and check everything out
	driver.get("https://cityonline.calgary.ca/Pages/Cart.aspx")
	
	
	

if __name__ == "__main__":
    main()
