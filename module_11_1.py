
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageFilter


class Requests:
    print('-----------------------------------------------------------------------')
    url = ''

    response = requests.get(url)

    if response.status_code == 200:

        data = response.url
        print(f'Статус ответа: OK [код 200]')

    else:
        print('Ошибка при выполнении запроса')

print('-----------------------------------------------------------------------')

class Matplotlib:
    x = [5, 4, 3, 2, 1]
    y = [10, 20, 15, 25, 30]
    plt.plot(x, y)
    plt.xlabel('ось X')
    plt.ylabel('ось Y')
    plt.title('Пример линейного графика')
    plt.show()
