import turtle
import pandas as pd

FONT = ("Arial", 8, "normal")

screen = turtle.Screen()
screen.title("U.S. States Game")

# can set turtle shape to image -> must be .gif
image = "blank_states_img.gif"
screen.addshape(image)

# once shape added, it's now available to be used by turtle
# change turtle shape to image
turtle.shape(image)

# don't need this code b/c in 50_states.csv file
# get coordinates for state locations on image:
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# # event listener: listen for click -> call get_mouse_click function and pass over x and y coordinates of click location
# turtle.onscreenclick(get_mouse_click_coor)
#
# # alternative way of keeping screen open even though code has finished running (alternative to exitonclick)
# # don't want to exit on click
# turtle.mainloop()

states = pd.read_csv("50_states.csv")
answers = []
score = 0
text = turtle.Turtle()
text.hideturtle()
text.penup()

# can use len of guessed state instead of even having a score variable
while score < 50:
    # create popup box
    # convert to title case
    answer_state = screen.textinput(title=f"{score}/50 States Correct",
                                    prompt="What's a state name?").title()

    # because answer_state in title case
    if answer_state == "Exit":
        # generate new file of states that haven't been guessed by user.
        all_states = states.state.to_list()
        for answer in answers:
            if answer in all_states:
                all_states.remove(answer)

        states_not_guessed = pd.DataFrame(all_states)
        states_not_guessed.to_csv("states_not_guessed.csv")
        # break out of while loop
        break

    if answer_state in states.values and answer_state not in answers:
        answers.append(answer_state)
        score += 1
        # extract info of state where it's the same as the answer
        state_info = states[states["state"] == answer_state]
        # get x and y coordinate of state
        x_cor = int(state_info["x"])
        y_cor = int(state_info["y"])
        # write state in its location
        text.goto(x_cor, y_cor)
        text.write(answer_state, align="center", font=FONT)
        # can also use use states.state.item() instead of answer_state
        # grabs 1st element pf underlying data



screen.exitonclick()
