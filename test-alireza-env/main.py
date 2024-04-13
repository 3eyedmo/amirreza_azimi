import requests
from bs4 import BeautifulSoup

from file_handlers import write_lines


# response = requests.get("https://maktabkhooneh.org/")

# soup = BeautifulSoup(response.text)


# courses = soup.select(selector=".base-course-card__title")

# f = open('course.txt', 'w', encoding='utf-8')

# for c in courses:
#     f.write(c.text.strip())
#     f.write('\n')

names = ['amirreza', 'ali', 'mohammad']

write_lines(string_list=names, filename='names.txt')
write_lines(string_list=['ahmad', 'reza', 'hosein'], filename='names2.txt')
# write_lines(string_list=['ahmad', 'reza', 'hosein'], filename='names3.txt')
# write_lines(string_list=['ahmad', 'reza', 'hosein'], filename='names4.txt')
# write_lines(string_list=['ahmad', 'reza', 'hosein'], filename='names5.txt')
# write_lines(string_list=['ahmad', 'reza', 'hosein'], filename='names6.txt')
# write_lines(string_list=['ahmad', 'reza', 'hosein'], filename='names7.txt')
