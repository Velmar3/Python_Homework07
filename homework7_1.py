"""
Задание 1.
Создать класс TrafficLight (светофор)
и определить у него один приватный атрибут цвет (цвет) и публичный метод запуска (запуск).
В рамках используемой реализации реализации переключения светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьей (зеленый) —
на ваше усмотрение.
Для имитации "горения" каждого цвета испольщуйте ф-цию модуляции сна
Переключение между режимами передачи должно быть только
в указанном порядке (красный, желтый, зеленый).
Проверьте работу примера, создав экземпляр и вызвав описанный метод.
"""

from time import sleep
from datetime import datetime as dt


class TrafficLight:
    """ Класс светофора, реализующий свое переключение при запуске running( """
    _states = {'red': 7, 'yellow': 2, 'green': 7}
    _color = ''

    def running(self):
        """ Метод запуска светофора """
        for color, sw_time in self._states.items():
            self._color = color
            start_state_time = dt.now()

            print(f"TrafficLight switched to state '{self._color}' "
                  f"on {sw_time} seconds")

            sleep(sw_time)

            print(f"TrafficLight leave state '{self._color}' after"
                  f"{(dt.now() - start_state_time).seconds} seconds")


if __name__ == '__main__':
    tl = TrafficLight()
    tl.running()
