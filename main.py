import requests
from bs4 import BeautifulSoup


def categories(url):
    headers = {'Accept': '*/*',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64;'
                             ' x64) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/104.0.5112.124 '
                             'YaBrowser/22.9.3.888 Yowser/2.5 Safari/537.36'}

    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.text, 'lxml')
    cat = soup.find_all(class_="CategoryList")
    with open('Xfile.txt', 'a', encoding='utf-8') as file:
        for i in cat[2:]:
            i = i.find('a')
            Category = i.text
            link = i.get('href')
            req2 = requests.get(f'https://www.ryp.us/{link}', headers=headers)
            soup2 = BeautifulSoup(req2.text, 'lxml')
            remains = soup2.find_all('div', class_="Record")

            for i in remains:
                print('++++++++++++++++++++')
                card = []
                for j in i:
                    if j.text.isspace():
                        continue
                    elif j.text == '':
                        continue
                    else:

                        card.append(' +'.join(str(j.text.strip()).split(',')))

                card.insert(0, Category)

                file.writelines(','.join(card) + '\n')



def main():
    categories('http://www.ryp.us/index.php?CategoryId=88&GroupID=')


if __name__ == '__main__':
    main()
