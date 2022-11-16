import requests
from bs4 import BeautifulSoup
from openpyxl import load_workbook

def categories(url):
    #headers = {'Accept': '*/*',
    #           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64;'
    #                         ' x64) AppleWebKit/537.36 '
    #                         '(KHTML, like Gecko) Chrome/104.0.5112.124 '
    #                         'YaBrowser/22.9.3.888 Yowser/2.5 Safari/537.36'}
#
    #req = requests.get(url, headers=headers)
    #soup = BeautifulSoup(req.text, 'lxml')
    #cat = soup.find_all(class_="CategoryList")
    #with open('Xfile.txt', 'a', encoding='utf-8') as file:
    #    for i in cat[2:]:
    #        i = i.find('a')
    #        Category = i.text
    #        link = i.get('href')
    #        req2 = requests.get(f'https://www.ryp.us/{link}', headers=headers)
    #        soup2 = BeautifulSoup(req2.text, 'lxml')
    #        remains = soup2.find_all('div', class_="Record")
#
    #        for i in remains:
    #            print('++++++++++++++++++++')
    #            card = []
    #            for j in i:
    #                if j.text.isspace():
    #                    continue
    #                elif j.text == '':
    #                    continue
    #                else:
#
    #                    card.append(' +'.join(str(j.text.strip()).split(',')))
#
    #            card.insert(0, Category)
#
    #            file.writelines(','.join(card) + '\n')
    with open('Xfile.txt', 'r', encoding='utf-8') as file:
        listM = file.readlines()
        listState = ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS',
                     'KY', 'LA',
                     'MA', 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY',
                     'OH', 'OK',
                     'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY', 'DC'
                     ]




        for i in range(len(listM)):
            Category = ''
            Name = ''
            tel1 = ''
            cel1 = ''
            tel2 = ''
            cel2 = ''
            web = ''
            email = ''
            Address = ''
            TownCity = ''
            State = ''
            ZIP = ''

            listM[i] = listM[i].split(',')
            Category = listM[i][0]
            Name = listM[i][1]

            del listM[i][0]
            del listM[i][0]






            for j in range(len(listM[i])):
                if 'TEL' in listM[i][j].upper():
                    tel1 = listM[i][j].replace('Tel:', '')
                    listM[i][j] = ''
                    break

            for j in range(len(listM[i])):
                if 'CEL' in listM[i][j].upper():
                    cel1 = listM[i][j].replace('Cell:', '')
                    listM[i][j] = ''
                    break

            for j in range(len(listM[i])):
                if 'TEL' in listM[i][j].upper() or 'T+F' in listM[i][j].upper():
                    tel2 = listM[i][j].replace('Tel:', '')
                    listM[i][j] = ''
                    break

            for j in range(len(listM[i])):
                if 'CEL' in listM[i][j].upper():
                    cel2 = listM[i][j].replace('Cell:', '')
                    listM[i][j] = ''
                    break

            for j in range(len(listM[i])):
                if 'www.' in listM[i][j].lower():
                    web = listM[i][j]
                    listM[i][j] = ''
                    break

            for j in range(len(listM[i])):
                if '@' in listM[i][j]:
                    email = listM[i][j]
                    listM[i][j] = ''
                    break

            for j in range(len(listM[i])):
                if 'TEL' in listM[i][j].upper() or 'FAX' in listM[i][j].upper() or 'Home' in listM[i][j].upper():
                    listM[i][j] = ''




            for j in range(len(listM[i])):
                for l in listState:
                    if l in listM[i][j]:

                        TownCity = listM[i][j].split(' + ')[0].strip().replace('/n', '')
                        if len(listM[i][j].split(' + ')) > 1:

                            State = listM[i][j].split(' + ')[1].split()[0]
                            if len(listM[i][j].split(' + ')[1].split()) > 1:
                                ZIP = listM[i][j].split(' + ')[1].split()[1]

                        listM[i][j] = ''


            for j in range(len(listM[i])):
                if listM[i][j]:
                    Address = Address + listM[i][j]




            fn = 'table.xlsx'
            wb = load_workbook(fn)
            ws = wb['Аркуш1']

            ws.append([Category, Name, tel1, cel1, web, email, Address, TownCity, State, ZIP, tel2, cel2])
            wb.save(fn)
            wb.close()






            #print(Address)

            print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            print(Category, Name, tel1, cel1, tel2, cel2, web, email, Address, TownCity, State, ZIP)
            #print(listM[i])











def main():
    categories('http://www.ryp.us/index.php?CategoryId=88&GroupID=')


if __name__ == '__main__':
    main()

