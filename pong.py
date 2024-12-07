import sys, pygame


class Point2D:
    def __init__(self, x, y):
        self.x: int = x
        self.y: int = y


class Racket:
    def __init__(self, initial_position: Point2D):
        self.pos: Point2D = initial_position

        # size_x: int  = ...
        # size_y: int  = ...


class Ball:
    def __init__(self, initial_position: Point2D):
        self.pos: Point2D = initial_position
        # self.size_x: int  = ...
        # self.size_y: int  = ...
        # self.velocity_x: int = ...
        # self.velocity_y: int = ...


class Pong:
    def __init__(self):
        # self.racket_left = Racket(...)
        # self.racket_right = Racket(...)
        # self.ball = Ball(...)
        self.score_left: int = 0
        self.score_right: int = 0
        self.dt = 16.6666 # ms # 60 fps
        pass

    def draw_frame(self):
        """Метод, для вывода состояния системы на экран.
        Или, по человечески, для рисования.
        По очереди рисует все объекты, которые есть на экране."""
        # Draw the rackets
        # Draw the ball
        # Draw the score
        pass

    def time_shift(self):
        """Метод, для расчета следующего состояния системы, по прошествии
        некоторого времени.
        По сути - расчитываем куда сдвинется мяч и ракетки. Также,
        проверяем на столкновение мяча с краем экрана, и мяча с ракетками."""
        # dt = ... # === (1 / fps)

        # Move the rackets (User Input)
        # Move the ball
        # Check collision
        pass

    def sleep(self):
        """Метод, для выполнения задержки.
        Все вычисления и расчеты происходят очень быстро, следовательно нужно
        ограничить количество FPS."""
        # wait dt amount of time
        pass

# MAIN CODE GOES HERE
if __name__ == "__main__":
    # Инициализация окна
    pong = Pong()
    while True:
        pong.draw_frame()
        pong.time_shift()
        pong.sleep()
