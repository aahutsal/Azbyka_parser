import requests
from bs4 import BeautifulSoup
url = 'https://azbyka.ru/molitvoslov/akafist-slava-bogu-za-vsyo.html'
r = requests.get(url)
titles_list = []
text_list = []
soup = BeautifulSoup(r.text, 'html.parser')
main_title = soup.h1.text
main_title = list(main_title)
for i in main_title:
    if i == '\xa0' or i == '\xad':
        main_title.insert(main_title.index(i), ' ')
        main_title.remove(i)
        main_title = ''.join(main_title)
first_dict = {'Title' : None,
              'Audio' : None
              }
first_dict['Title'] = main_title
first_dict['Audio'] = soup.audio.get('src')
for i in soup.find_all('h3'):
    if i.text.startswith('Кондак') or i.text.startswith('Икос'):
        titles_list.append(i.text)

all_p = soup.find_all('p', {'class' : 'paint'})
for i in all_p:
    text_list.append([i.text])
clean_text = []

for i in range(len(text_list)):
    for j in text_list[i]:
        s = list(j)
        for xad in s:
            if xad == '\xad' or xad == '\xa0':
                s.remove(xad)
            n = ''.join(s)
        clean_text.append([n])

n = len(clean_text)
i = 0
while i < n:
    for j in clean_text[i]:
        if j.startswith('Слава'):
            clean_text[i-1].extend(clean_text[i])
            clean_text.remove(clean_text[i])
            n -= 1
        else:
            i += 1

final_dict = dict.fromkeys(titles_list)
i = 0
while i < len(final_dict):
    for j in final_dict:
        final_dict[j] = clean_text[i]
        i += 1

final_tuple = (first_dict, final_dict)
print(final_tuple)