from turtle import Turtle

ALIGMENT = "center"
FONT = ("Arial", 20, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=270)
        self.score = 0

        with open("data.txt") as file:
            self.highscore = int(file.read())

        self.update_score()

    def update_score(self):
        self.clear()
        self.write(
            f"Scoreboard: {self.score} High Score: {self.highscore}",
            move=False,
            align=ALIGMENT,
            font=FONT,
        )

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score

            with open("data.txt", mode="w") as file:
                file.write(f"{self.highscore}")

        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGMENT, font=FONT)
