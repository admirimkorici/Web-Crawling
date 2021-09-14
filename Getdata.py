from bs4 import BeautifulSoup

with open("C:/Users/user/OneDrive/Documents/Visual Studio Code/Python/Grid Coding/Web Crawling/home.html", 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    course_carts = soup.find_all('div', class_='card')
    for course in course_carts:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]

        print(f'{course_name} costs {course_price}')