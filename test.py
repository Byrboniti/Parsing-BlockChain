# x = '<span class="sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC sc-85fclk-0 fhjukF" opacity="1">'
# y = '<span class="sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC sc-85fclk-0 fhjukF" opacity="1">'
# <div class="sc-1rk8jst-1 bFopoh"><span class="sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC sc-85fclk-0 fhjukF" opacity="1">-0.00000000 ETH</span></div>
# <span class="sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC sc-85fclk-0 fhjukF" opacity="1">-0.00000000 ETH</span>
# <span class="sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC" opacity="1">2021-05-21 13:22</span>

"""https://www.youtube.com/watch?v=gM9uu9xf4SQ"""
from selenium import webdriver
from selenium.webdriver.common.by import By

wallet = ['0x50948da90df3f676241fd4e9b83a55343d88ee66',
     '0xd0Dd94f50A15d07b0FFf2E20641Dced97E4e9399',
     ]

def main(html):
    driver = webdriver.Chrome()
    driver.get(f'https://www.blockchain.com/eth/address/{html}')
    title = driver.find_elements(By.CLASS_NAME, 'fhjukF') # html значения отправленные
    x = 1 # счетчик
    schet = driver.find_elements(By.CLASS_NAME, 'vXYMB') # ХТМЛ значения полученных
    for i in title:
        Kogda = driver.find_elements(By.XPATH,f'/html/body/div[1]/div[4]/div[2]/div/div/div[2]/div/div[2]/div/div[3]/div[{x}]/div[1]/div[2]/div[2]/div/span')
        for e in Kogda:
            when_text = e.text
        x = x + 1
        string_text = i.text
        minus = string_text.split('-')[1]
        no_eth = minus.rsplit(' ETH')[0]
        float_text = float(no_eth)
        print(when_text)
        print(float_text)

        # print(type(float_text))
    # for e in Kogda:
    #     when_text = e.text
    #     print(when_text)

for html in wallet:
    main(html)




#
# if __name__ == "__main__":
#     main()










# class blockchainParser(object):
#
#     def __init__(self):