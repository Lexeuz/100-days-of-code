# Project - Quizz Game (List of U.S. States).
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game. - Alexander Eraso Adarme")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

def get_mouse_click_cor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_cor)
turtle.mainloop()
