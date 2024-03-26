import time

from easygui import msgbox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from apscheduler.schedulers.blocking import BlockingScheduler


def web_server(browser):
    try:
        browser.get("https://jx3.seasunwbl.com/buyer?t=skin")
        wait = WebDriverWait(browser, 10)

        text_input = browser.find_element(By.XPATH, '//*[@id="#appearance_input_role"]')
        text_input.clear()
        text_input.send_keys('海阔天空白发')

        wait.until(EC.element_to_be_clickable((
            By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div[1]/div[1]/div[2]/div[3]'
        ))).click()
        # browser.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div[1]/div[1]/div[2]/div[3]').click()
        # time.sleep(2)
        wait.until(EC.presence_of_element_located((
            By.XPATH, '//*[@id="#appearance_result_item_role"]'
        ))).click()
        # browser.find_element(By.XPATH, '//*[@id="#appearance_result_item_role"]').click()
        overlay = wait.until(EC.presence_of_element_located((
            By.XPATH, '//*[@id="app"]/div/div[4]'
        )))
        driver.execute_script("arguments[0].style.display = 'none';", overlay)
        # 点击查询
        wait.until(EC.presence_of_element_located((
            By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div[3]/div[2]'
        ))).click()
        # browser.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div[3]/div[2]').click()
        # 价格逆序
        wait.until(EC.presence_of_element_located((
            By.XPATH, '//*[@id="app"]/div/div[3]/div/div[3]/div[1]/div[3]'
        ))).click()
        # browser.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div[3]/div[1]/div[3]').click()
        time.sleep(1)
        price = browser.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div[3]/div[2]/div[1]/div[3]/div/span').text
        # time.sleep(5)
        if float(price) < 175:
            task('买买买！！！', '白发价格掉到'+price+'啦！')
    except Exception as e:
        print(format(e))


def task(title: str, content: str):
    msgbox(content, title, '关闭')


def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    return webdriver.Chrome(executable_path="/home/java/chromedriver", chrome_options=options)


if __name__ == '__main__':
    driver = get_driver()
    session_id = driver.session_id
    scheduler = BlockingScheduler()
    try:
        scheduler.add_job(web_server, 'interval', seconds=60, args=[driver])
        scheduler.start()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(format(e))
