import time
import csv
from pathlib import  Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL ='https://airquality.cpcb.gov.in/AQI_India/'

OUT_CSV = "cpcb_repository_table.csv"
PROFILE_DIR = str(Path.cwd()/"chrome_profie_cpcb")


def start_driver():
    options = Options()
    options.add_argument("--window-size=1400,900")
    options.add_argument(f"--user-data={PROFILE_DIR}")
    options.add_argument("--disable-gpu")
    options.add_argument("--log-level=3")
    return webdriver.Chrome(options=options)

def extract_largest_table(driver):
    # wait until at least one table is present (dynamic page)
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.TAG_NAME, "table"))
    )

    tables = driver.find_elements(By.TAG_NAME, "table")
    best = None
    best_rows = 0

    for t in tables:
        rows = t.find_elements(By.CSS_SELECTOR, "tr")
        if len(rows) > best_rows:
            best = t
            best_rows = len(rows)

    if not best or best_rows < 2:
        raise RuntimeError("No usable table was found")

    data = []
    for row in best.find_elements(By.CSS_SELECTOR, "tr"):
        cells = row.find_elements(By.CSS_SELECTOR, "th,td")
        data.append([c.text.strip() for c in cells])

    return data


def save_to_csv(data, filename):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(data)


if __name__ == "__main__":
    driver = start_driver()
    driver.get(URL)

    table_data = extract_largest_table(driver)
    save_to_csv(table_data, OUT_CSV)

    driver.quit()
