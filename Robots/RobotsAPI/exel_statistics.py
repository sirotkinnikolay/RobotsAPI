from io import BytesIO
import xlsxwriter
from urllib.request import urlopen

works = [
    {
    'id' : 1,
    'name': 'Work 1',
    'image_url': 'https://dagstyazhka.ru/static/img/content/tPOXB2KXhck.jpg',
    },
    {
    'id' : 2,
    'name': 'Work 2',
    'image_url': 'https://dagstyazhka.ru/static/img/content/-iNioTY6Mw.jpg',
    },
    {
    'id' : 3,
    'name': 'Work 3',
    'image_url': 'https://dagstyazhka.ru/static/img/content/-iNioTY6Mw.jpg',
    },
]
workbook = xlsxwriter.Workbook('example.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write(0, 0, 'ID')
worksheet.write(0, 1, 'Name')
worksheet.write(0, 2, 'Image_url')
i = 1
for work in works:
    worksheet.write(i, 0, work.get('id'))
    worksheet.write(i, 1, work.get('name'))
    image_url = work.get('image_url')
    image_data = BytesIO(urlopen(image_url).read())
    worksheet.insert_image(i,2, image_url, {'image_data': image_data})
    i +=1

workbook.close()