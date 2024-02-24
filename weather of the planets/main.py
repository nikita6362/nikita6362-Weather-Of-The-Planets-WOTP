import sys
from random import randint, choice
from turtle import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QMessageBox
from PyQt5.QtGui import QFont, QIcon

font = QFont()
font.setFamily("Museo Slab")
font.setPointSize(10)

class WeatherGame(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Weather Of The Planets (WOTP)")
        self.setWindowIcon(QIcon('icon.png'))
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.weather_label = QLabel("Угадайте какая погода на этой планете:")
        self.layout.addWidget(self.weather_label)

        self.button_layout = QVBoxLayout()
        self.layout.addLayout(self.button_layout)

        self.buttons = []
        self.weather_types = ["Солнечно", "Туманно", "Ветрено", "Дождливо", "Снежно"]

        for weather_type in self.weather_types:
            button = QPushButton(weather_type)
            button.clicked.connect(self.check_weather)
            self.buttons.append(button)
            self.button_layout.addWidget(button)

        self.max_attempts = 3  # Максимальное количество попыток
        self.attempts_left = self.max_attempts
        self.correct_weather = None
        self.consecutive_correct_answers = 0
        self.max_consecutive_correct_answers = 0
        self.generate_planet()

        self.next_fact_countdown = randint(2, 5)
        self.next_fact_label = QLabel(f"До следующего факта: {self.next_fact_countdown}")
        self.layout.addWidget(self.next_fact_label)

    def generate_planet(self):
        clear() # turtle
        hideturtle() # turtle
        penup() # turtle
        speed(0) # turtle
        setup(500, 500) # turtle
        x = randint(-150, 150)
        y = randint(-150, 150)
        size = randint(50, 150)
        color = choice(["blue", "red", "green", "yellow", "orange"])
        goto(x, y) # turtle 
        dot(size, color) # turtle

        self.correct_weather = choice(self.weather_types)

    def check_weather(self):
        sender = self.sender()
        selected_weather = sender.text()
        if selected_weather == self.correct_weather:
            self.consecutive_correct_answers += 1
            QMessageBox.about(self, "Результат", "Верно! Поздравляем!")
            self.generate_planet()
            self.attempts_left = self.max_attempts
            if self.consecutive_correct_answers >= self.next_fact_countdown:
                self.show_planet_fact()
                self.consecutive_correct_answers = 0
                self.next_fact_countdown = randint(2, 5)
                self.next_fact_label.setText(f"До следующего факта: {self.next_fact_countdown}")
            else:
                self.next_fact_label.setText(f"До следующего факта: {self.next_fact_countdown - self.consecutive_correct_answers}")
            
        else:
            self.consecutive_correct_answers += 0
            self.attempts_left -= 1
            if self.attempts_left == 0:
                QMessageBox.about(self, "Результат", "Попытки закончились! Попробуйте еще раз.")
                self.generate_planet()
                self.attempts_left = self.max_attempts
            else:
                QMessageBox.about(self, "Результат", f"Неверно! Осталось попыток: {self.attempts_left}")

    def show_planet_fact(self):
        planet_facts = {
            "Меркурий": ["Меркурий является самой близкой планетой к Солнцу и самой маленькой планетой в Солнечной системе.",
                          "Меркурий не имеет атмосферы, и его поверхность покрыта кратерами от метеоритов.",
                          "Меркурий имеет самую эксцентричную орбиту среди всех планет в Солнечной системе."],
            "Венера": ["Венера — самая горячая планета в Солнечной системе. На её поверхности около 900 градусов по Фаренгейту.",
                       "Венера вращается в направлении, противоположном большинству других планет.",
                       "Атмосфера Венеры состоит главным образом из углекислого газа с облаками серной кислоты."],
            "Земля": ["Земля единственная планета в Солнечной системе, на которой есть жизнь.",
                      "Земля имеет единственный естественный спутник — Луну.",
                      "Земля состоит преимущественно из кремния, железа, кислорода и магния."],
            "Марс": ["Марс известен своими красными песчаными дюнами и вулканами, включая самую высокую вулканическую гору в Солнечной системе, Олимп.",
                     "На Марсе есть полярные капы, состоящие из льда и сухого льда.",
                     "Марс имеет атмосферу, состоящую в основном из углекислого газа, но слишком тонкую для поддержания жидкой воды на поверхности."],
            "Юпитер": ["Юпитер — самая большая планета в Солнечной системе. У него есть самая большая в Солнечной системе атмосфера, состоящая в основном из водорода и гелия.",
                       "Юпитер имеет множество спутников, самый большой из которых, Ганимед, является крупнейшим спутником в Солнечной системе.",
                       "Юпитер обладает самой быстрой вращающейся атмосферой среди всех планет."],
            "Сатурн": ["Сатурн известен своими кольцами из льда, пыли и камней, которые окружают планету.",
                       "Сатурн имеет наиболее выраженные кольца среди всех планет в Солнечной системе.",
                       "Сатурн — самая маленькая планета в Солнечной системе, плотность которой меньше плотности воды."],
            "Уран": ["Уран — это планета, которая лежит на боку и вращается вокруг своей оси, как колесо, вместо того чтобы вращаться прямо.",
                     "Уран имеет 27 известных спутников.",
                     "Уран был первоначально назван Георгом Фридрихом Гегелем в честь Гермеса, но позже переименован в Уран."],
            "Нептун": ["Нептун является самой далекой планетой от Солнца в Солнечной системе.",
                        "Нептун имеет самые высокие ветры в Солнечной системе, достигающие скорости до 2 100 км/ч.",
                        "Нептун был первоначально предсказан учеными по математическим расчетам до его физического обнаружения."],
            "Плутон": ["Плутон - это карликовая планета, которая была когда-то признана девятой планетой в Солнечной системе, но теперь считается карликовой планетой.",
                        "Плутон имеет пять спутников, самый крупный из которых, Харон, почти половину его размера.",
                        "Плутон периодически пересекает орбиту Нептуна и является самой эксцентричной орбитой из всех планет в Солнечной системе."]
        }
        current_planet = choice(list(planet_facts.keys()))
        fact = choice(planet_facts[current_planet])
        QMessageBox.about(self, "Интересный факт", f"Интересный факт о планете {current_planet}:\n{fact}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = WeatherGame()
    game.show()
    app.setFont(font)
    Screen().mainloop() # turtle
    sys.exit(app.exec_())