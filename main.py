from urllib.request import urlopen
import requests
from lxml import etree
wallet = ['0x50948da90df3f676241fd4e9b83a55343d88ee66',
     '0xd0Dd94f50A15d07b0FFf2E20641Dced97E4e9399',
     ]
for html in wallet:
    x = urlopen(f'https://www.blockchain.com/eth/address/{html}').read()
    y = str(x)
    '''все получила'''
    # q = y.split('Ethereum blockchain. It has received a total of ')[1]
    # z = q.rsplit(' ETH')[0]
    # print(z)
    '''всего отправила'''
    # q = y.split(') and has sent a total of ')[1]
    # z = q.rsplit(' ETH')[0]
    # print(z)
    print(y)









    ## print(y.find('Ethereum blockchain. It has received a total of '))
    ## print(y.partition("Ethereum blockchain. It has received a total of ")[0])
    # y = etree.XPath('//<span class="sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC" opacity="1">/$) и всего отправила /text()')
    # print(y)
"""

(Ethereum blockchain. It has received a total of )( ETH) не то **
$) и всего отправила 
<span class="sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC" opacity="1">
0.00105
'1H3yFtTD2f4doKeSQkYyiuh16bY7rVUBZ4'



This address has transacted 3 times on the Ethereum blockchain. 
It has received a total of 0.00525 ETH ($5.60) and has sent a total of 0.002488345 ETH ($2.65). 
The current value of this address is 0.000000000000000000 ETH ($0.00).
"""
    # y = str(x)
    # print(type(y))
# url = 'https://www.starwars.com/news/15-star-wars-quotes-to-use-in-everyday-life'
# headers = {'Content-Type': 'text/html',}
# response = requests.get(url, headers=headers)
# html = response.text
# with open ('star_wars_html', 'w') as f:
#     f.write(html)
#
# local = 'insert_browser_file_path_here'
# response = urlopen(local)
# htmlparser = etree.HTMLParser()
# tree = etree.parse(response, htmlparser)

# html = urlopen("http://www.google.com/").read()
# print(html)