# -*- coding: utf-8 -*-
import copy
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager




welcome = [
    # 'Добрый день, меня зовут Артём',
    # 'Добрый день, я Артём',
    # # 'Доброе утро, меня зовут Артём',
    # # 'Доброе утро, я Артём',
    # 'Здравствуйте, меня зовут Артём',
    # 'Здравствуйте, я Артём'
    'Добрый день',
    'Здравствуйте',
    'Приветствую'
]

bye = [
    'Подскажите, актуально ли это для вас?',
    'Подскажите, моё предложение для вас интересно?',
    'Подскажите, вам интересно данное предложение?',
]


# # text = welcome[random.randint(0, len(welcome) - 1)] + "!\n\nМеня зовут Артём и я специализируюсь на увеличении количества заказов для доставок еды с помощью таргетированной рекламы во ВКонтакте\n\nИз последних кейсов могу выделить:\n1) Более 500 заказов по 243р для доставки из столичной сети ресторанов с бюджетом 135.000р (выручка 763.000р)\n2) 147 заказов по 190р для региональной доставки премиум роллов с бюджетом 28.000р (выручка 220.500р)\n\nЧтобы подтвердить свою экспертность, прикрепляю ссылку на мое портфолио с кейсами в данной сфере - https://drive.google.com/file/d/18ETmJTh5ZqKGJw5Ms8QjpcogYULi1GNB/view?usp=sharing\n\nЕсли вас интересует, как сохранить и увеличить число заказов для вашей доставки с помощью таргета во Вконтакте, то я могу составить для вас персональную стратегию и провести бесплатную консультацию с расчётом окупаемости рекламных инвестиций)\n\nХорошего дня!"""
# textSend = welcome[random.randint(0, len(welcome) - 1)] + """
#
# Меня зовут Артём и я специализируюсь на увеличении количества заказов для доставок еды с помощью таргетированной рекламы во ВКонтакте
#
# Из последних кейсов могу выделить:
# 1) Более 500 заказов по 243р для доставки из столичной сети ресторанов с бюджетом 135.000р (выручка 763.000р)
# 2) 147 заказов по 190р для региональной доставки премиум роллов с бюджетом 28.000р (выручка 220.500р)
#
# Чтобы подтвердить свою экспертность, прикрепляю ссылку на мое портфолио с кейсами в данной сфере - https://drive.google.com/file/d/18ETmJTh5ZqKGJw5Ms8QjpcogYULi1GNB/view?usp=sharing
#
# Если вас интересует, как сохранить и увеличить число заказов для вашей доставки с помощью таргета во Вконтакте, то я могу составить для вас персональную стратегию и провести бесплатную консультацию с расчётом окупаемости рекламных инвестиций)
#
# Хорошего дня!
# """


def bot(filename):

    logs = 0
    currentLine = 0
    # with open(f'{filename}.txt', 'r') as file: phones = file.readlines()
    with open(f'delivery/{filename}.txt', 'r', encoding='utf-8') as file: phones = file.readlines()
    phones_new = copy.copy(phones)
    with webdriver.Chrome() as driver:
        driver.get(f"https://web.whatsapp.com/")
        time.sleep(20)
        try:
            for ph in phones:
                currentLine = currentLine+1
                textSend = welcome[random.randint(0,len(welcome) - 1)] + "! Меня зовут Артём и я специализируюсь на увеличении количества заказов для доставок еды с помощью таргетированной рекламы во ВКонтакте. Из последних кейсов могу выделить: более 500 заказов по 243р для доставки из столичной сети ресторанов с бюджетом 135.000р (выручка 763.000р), 147 заказов по 190р для региональной доставки премиум роллов с бюджетом 28.000р (выручка 220.500р). Чтобы подтвердить свою экспертность, прикрепляю ссылку на мое портфолио с кейсами в данной сфере - https://drive.google.com/file/d/18ETmJTh5ZqKGJw5Ms8QjpcogYULi1GNB/view?usp=sharing. Если вас интересует, как сохранить и увеличить число заказов для вашей доставки с помощью таргета во Вконтакте, то я могу составить для вас персональную стратегию и провести бесплатную консультацию с расчётом окупаемости рекламных инвестиций) Хорошего дня!"
                try:
                    phones_new.remove(ph)
                    driver.get(f"https://web.whatsapp.com/send?phone=" + str(ph.replace('\n', '')))
                    time.sleep(7)
                    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]").click()
                    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]").send_keys(textSend)
                    # driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]").send_keys((welcome[random.randint(0, len(welcome) - 1)]+
                    #
                    #     "Меня зовут Артём и я специализируюсь на увеличении количества заказов для доставок еды с помощью таргетированной рекламы во ВКонтакте"
                    #
                    #     "Из последних кейсов могу выделить:"
                    #     "📌Более 500 заказов по 243р для доставки из столичной сети ресторанов с бюджетом 135.000р (выручка 763.000р)"
                    #     "📌147 заказов по 190р для региональной доставки премиум роллов с бюджетом 28.000р (выручка 220.500р)"
                    #
                    #     "Чтобы подтвердить свою экспертность, прикрепляю ссылку на мое портфолио с кейсами в данной сфере - https://drive.google.com/file/d/18ETmJTh5ZqKGJw5Ms8QjpcogYULi1GNB/view?usp=sharing"
                    #
                    #     "Если вас интересует, как сохранить и увеличить число заказов для вашей доставки с помощью таргета во Вконтакте, то я могу составить для вас персональную стратегию и провести бесплатную консультацию с расчётом окупаемости рекламных инвестиций)"
                    #
                    #     "Хорошего дня!"))
                    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]").send_keys(Keys.RETURN)
                    time.sleep(3)
                    print(f'[INFO] Successful phone {ph}')
                    logs=logs+1
                    print(f"count: {logs}")
                    print(f"all: {currentLine}")
                    # logs.append(f'[INFO] Successful phone {ph} \n')
                except Exception as _ex:
                    # print(_ex)
                    print(f'[ALERT] Does not exist phone {ph}')
                    # logs.append(f'[ALERT] Does not exist phone {ph} \n')
                    continue
        except Exception as _ex:
            print(_ex)
            with open(f"logs/{filename}.txt", 'w', encoding='utf-8') as f:
                f.writelines(f"Отправлено:{logs}"
                             f"Всего: {currentLine}")
    print(phones)
    print(phones_new)
    with open(f"logs/{filename}.txt", 'w', encoding='utf-8') as f:
        f.writelines(f"Отправлено:{logs}"
                     f"Всего: {currentLine}")
        # f.writelines(logs)


bot("251 - 500")