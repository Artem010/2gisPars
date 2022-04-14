import copy
import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import bot


def main(query):
    url = f'https://2gis.ru/perm/search/{query}/page/10/'
    driver = webdriver.Chrome()
    phones_mas = []
    try:
        card = 1
        driver.get(url)
        time.sleep(10)
        maxCard = int(driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/div[1]/header/div[3]/div/div[1]/div/div/a/span').text)
        while True:
            cards = driver.find_elements(By.XPATH, '/html/body/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div')
            for i in range(12):
                try:
                    cards[0].find_element(By.XPATH, f'div[{i+1}]/div/div[2]').click()
                    time.sleep(0.5)
                    webdriver.ActionChains(driver).move_to_element(driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div')).perform()
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    driver.find_element(By.CLASS_NAME, '_1ns0i7c').click()
                    time.sleep(0.2)
                    phones_mas.append(str(cards[0].find_element(By.XPATH, f'div[{i+1}]/div/div[2]/a/span').text  + " : " + driver.find_element(By.TAG_NAME, 'bdo').text) + '\n')
                    print(f"[+] Processed: {card}/{maxCard}")
                    card += 1
                    webdriver.ActionChains(driver).move_to_element(cards[0]).perform()
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                except:
                    print(f"[-] Does not exist phone: {card}/{maxCard}")
            driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div[1]/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[3]/div[2]/div[2]').click()
            time.sleep(1)
    except Exception as _ex:
        print(f"total page: {round(card/12)}")
        filename = f"{query}_{datetime.datetime.now().strftime('%H-%M')}"
        with open(f'organizations/{filename}.txt', 'w', encoding='utf-8') as f:
            f.writelines(phones_mas)
        print("Pars end")

        convertToPhoneList(filename)
        filename = filename + "_converted"
        delDoubles(filename)
        bot.bot(filename)

        print('EXIT')

    finally:
        print(f"total page: {round(card/12)}")
        with open(f"organizations/{query}_{datetime.datetime.now().strftime('%H-%M')}.txt", 'w', encoding='utf-8') as f:
            f.writelines(phones_mas)
        driver.close()
        driver.quit()



def convertToPhoneList(filename):
    s = []
    s_new = []
    with open(f"organizations/{filename}.txt", 'r', encoding='utf-8') as f:
        s = f.readlines()

    for line in s:
        line = (line.split(':'))[1]
        line= line.replace(' ','')
        line= line.replace('+','')
        line= line.replace('(','')
        line= line.replace(')','')
        line= line.replace('-','')
        line= line.replace('‒','')
        if('342' not in line):
            s_new.append(str(line))
            print(line)

    with open(f"organizations/{filename}_converted.txt", 'w', encoding='utf-8') as f:
        f.writelines(s_new)

def delDoubles(filename):
    s = []
    temp = []
    with open(f"organizations/{filename}_converted.txt", 'r', encoding='utf-8') as f:
        s = f.readlines()

    for x in s:
        if x not in temp:
            temp.append(x)

    with open(f"organizations/{filename}_converted.txt", 'w', encoding='utf-8') as f:
        f.writelines(temp)

    print(f"doubles: {len(s)-len(temp)}")

if __name__ == '__main__':
    query='студия растяжки нижний новгород_17-43'
    main(query)


    # convertToPhoneList(query)
    #
    # delDoubles(query)

    # bot.bot(query)
