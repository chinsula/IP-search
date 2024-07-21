import requests
from dadata import Dadata
import re
from config import adress_token


# with open("vopros.txt", "r",encoding='UTF-8') as file1:
#     # итерация по строкам
#     for line in file1:
#         print(line.strip())


def get_info_by_ip(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        # pprint(response)

        data = {
            'IP': response.get('query'),  # ip
            'провайдер': response.get('isp'),  # интернет провайдер
            'организация': response.get('org'),  # организация
            'страна': response.get('country'),  # страна
            'регион': response.get('regionName'),  # регион
            'город': response.get('city'),  # город
            'индекс': response.get('zip'),  # почт код
            'широта': response.get('lat'),  # широта
            'долгота': response.get('lon'),  # долгота
        }

        # запись данных об IP-адресе в файл

        f = open('report.txt', 'a', encoding='UTF-8')
        for k, v in data.items():
            f.write(f"{k}: {v} \n")
        dadata = Dadata(adress_token)
        result = dadata.geolocate(name="address", lat=data['широта'], lon=data['долгота'], radius_meters=50)
        # pprint(result)
        for i in range(len(result)):
            # print(f"адрес: {result[i]['value']}")
            f = open('report.txt', 'a', encoding='UTF-8')
            f.write(f"адрес: {result[i]['value']} \n")

        # area = folium.Map(location=[response.get('lat'), response.get('lon')])
        # area.save(f'{response.get("query")}_{response.get("city")}.html')

    except requests.exceptions.ConnectionError:
        print('[!] Please check your connection!')


def main():
    with open('report.txt', 'w', encoding='UTF-8') as f:
        with open("vopros.txt", "r", encoding='UTF-8') as file:
            for ip in file:
                get_info_by_ip(ip=ip.strip())
                open('report.txt', 'a', encoding='UTF-8').write("_____________________________ \n")
    f.close()


if __name__ == "__main__":
    main()
