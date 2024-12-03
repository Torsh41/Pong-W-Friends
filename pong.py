import turtle



class Racket:
    def __init__(self, x, y):
        position_x: int = x
        position_y: int = y

        # size_x: int  = ...
        # size_y: int  = ...


class Ball:
    def __init__(self, x, y):
        position_x: int = x
        position_y: int = y
        # size_x: int  = ...
        # size_y: int  = ...
        # velocity_x: int = ...
        # velocity_y: int = ...


class Pong:
    def __init__(self):
        # racket_left = Racket(...)
        # racket_right = Racket(...)
        score_left: int = 0
        score_right: int = 0
        dt = 16.6666 # ms # 60 fps
        pass

    def draw_frame(self):
        # Draw the rackets
        # Draw the ball
        # Draw the score
        pass

    def time_shift(self):
        # dt = ... # === (1 / fps)

        # Move the rackets
        # Move the ball
        pass

    def sleep(self):
        # wait dt amount of time
        pass

# MAIN CODE GOES HERE
pong = Pong()
while True:
    pong.draw_frame()
    pong.time_shift()
    pong.sleep()

