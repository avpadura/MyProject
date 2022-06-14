from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import \
    (NumericProperty, ReferenceListProperty, ObjectProperty)
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint

"""Scores player"""
class PongPaddle(Widget):
    score = NumericProperty(0)


    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1 * vx, vy)
            vel = bounced * 1.1
            ball.velocity = vel.x, vel.y + offset


"""Speed move ball"""
class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    """Create a vector"""
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self): # Move ball
        self.pos = Vector(*self.velocity) + self.pos

class PongGame(Widget):
    ball = ObjectProperty(None) #Communication of the ball with the object
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)

    def serve_ball(self, vel=(4, 0)):
        self.ball.center = self.center
        self.ball.velocity = vel

    def update(self, dt):
        self.ball.move() #Move the ball after each screen update

        # Check the reflection of the ball from the players panel
        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)

        # Reflection of the ball on Y
        if (self.ball.y < self.y) or (self.ball.top > self.top):
            self.ball.velocity_y *= -1 # increase the current speed by Y

        # Reflection of the ball on X.
        # If the ball was able to go beyond the player's trap,
        # then add 1 point to the opponent
        if self.ball.x < self.x:
            self.player2.score += 1
            self.serve_ball(vel=(4, 0)) # throws the ball to the center again
        if self.ball.right > self.width:
            self.player1.score += 1
            self.serve_ball(vel=(-4, 0)) # throws the ball to the center again


#Parf of touch screen

    def on_touch_move(self, touch):
        # player1 can only touch the left side of the screen
        if touch.x < self.width / 3:
            self.player1.center_y = touch.y
        #player2 can only touch the right side of the screen
        if touch.x > self.width - self.width / 3:
            self.player2.center_y = touch.y

class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0/60)
        return game


if __name__ == '__main__':
    PongApp().run()