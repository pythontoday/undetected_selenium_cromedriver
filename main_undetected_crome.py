import undetected_chromedriver
import time

try:
    driver = undetected_chromedriver.Chrome()
    # driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
    driver.get("https://www.vindecoderz.com/EN/check-lookup/ZDMMADBMXHB001652")
    time.sleep(15)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
