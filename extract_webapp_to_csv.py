
# table = wait.until(EC.presence_of_element_located((By.XPATH, "//table[contains(@class, 'table table-bordered background-white shares-table fixedHeader')]")))

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import pandas as pd

# # Setup Chrome driver
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# # Open the page
# url = "https://www.dsebd.org/latest_share_price_scroll_by_value.php"
# driver.get(url)

# # Wait until the table is visible
# wait = WebDriverWait(driver, 20)
# table = wait.until(EC.presence_of_element_located((By.XPATH, "//table[@class='table table-bordered background-white shares-table fixedHeader']")))

# # Extract headers (th)
# headers = [th.text.strip() for th in table.find_elements(By.TAG_NAME, "th")]

# # Extract rows (td)
# rows = []
# for tr in table.find_elements(By.TAG_NAME, "tr"):
#     cols = [td.text.strip() for td in tr.find_elements(By.TAG_NAME, "td")]
#     if cols:  # Avoid adding empty rows
#         rows.append(cols)

# # Convert to DataFrame
# df = pd.DataFrame(rows, columns=headers)

# # Save to CSV
# df.to_csv("stock_data.csv", index=False)

# print("Scraping complete! CSV saved.")

# # Close the driver
# driver.quit()



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# Setup Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the page
# url = "https://www.dsebd.org/latest_share_price_scroll_by_value.php"
url = "https://www.dsebd.org/latest_share_price_scroll_l.php"

driver.get(url)

# Wait until the table is visible
wait = WebDriverWait(driver, 20)
table = wait.until(EC.presence_of_element_located((By.XPATH, "//table[@class='table table-bordered background-white shares-table fixedHeader']")))

# Extract headers with aria-label from thead > tr > th
thead = table.find_element(By.TAG_NAME, "thead")
tr = thead.find_element(By.TAG_NAME, "tr")
headers = [th.get_attribute("aria-label").strip() for th in tr.find_elements(By.TAG_NAME, "th")]

# Extract rows (td)
rows = []
for tr in table.find_elements(By.TAG_NAME, "tr"):
    cols = [td.text.strip() for td in tr.find_elements(By.TAG_NAME, "td")]
    if cols:  # Avoid adding empty rows
        rows.append(cols)

# Convert to DataFrame
df = pd.DataFrame(rows, columns=headers)

# Save to CSV
df.to_csv("stock_data.csv", index=False)

print("Scraping complete! CSV saved.")

# Close the driver
driver.quit()



