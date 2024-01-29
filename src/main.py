import time
import pandas as pd

from selenium.webdriver.common.by import By

from browser.webdriver import set_driver_options
from log_conf import logger


def get_challenge():
    excel_file_path = "../statics/challenge.xlsx"
    df = pd.read_excel(excel_file_path)
    driver = set_driver_options()

    try:
        driver.get("https://rpachallenge.com/?lang=EN")
        start_button = driver.find_element(
            By.XPATH, "/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button"
        )
        start_button.click()
        logger.info("Started!")
        time.sleep(5)
        for index, row in df.iterrows():
            for column, value in row.items():
                input_field_xpath = (
                    f"//*[@ng-reflect-name="
                    f"'label{str(column).strip().replace(' ', '')}']"
                )
                if column == "Role in Company" or column == "Phone Number":
                    input_field_xpath = (
                        f"//*[@ng-reflect-name='label{str(column).split()[0]}']"
                    )
                input_field = driver.find_element(By.XPATH, input_field_xpath)
                input_field.clear()
                input_field.send_keys(str(value))
                time.sleep(2)
            submit_button = driver.find_element(
                By.XPATH, "/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input"
            )
            submit_button.click()
            time.sleep(2)
            logger.info("Done!")
    except KeyboardInterrupt:
        logger.info("Bye!")
    except Exception as e:
        logger.error(e)
    finally:
        driver.quit()


if __name__ == "__main__":
    get_challenge()
