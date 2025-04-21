import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S States Game')

image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

states_data = pandas.read_csv('50_states.csv')

turtle = turtle.Turtle()
turtle.hideturtle()
turtle.penup()

states_correct = []

while len(states_correct) < 50:
    if len(states_correct) == 0:
        answer_state = screen.textinput(title='Guess the State', prompt="Can you name a State?").title()
    else:
        answer_state = screen.textinput(title=f'{len(states_correct)}/50 States Correct',
        prompt="What's another State's Name?").title()
    if answer_state == "Exit".title():
        missing_states =[state for state in states_data.state if state not in states_correct]
        pandas.DataFrame(missing_states).to_csv('States to Learn.csv')
        break
    for state in states_data.state:
        if state == answer_state and state not in states_correct:
                    state_record = (states_data[states_data.state == answer_state])
                    state_xcor = state_record['x']
                    state_ycor = state_record['y']
                    turtle.goto(int(state_xcor.iloc[0]),int(state_ycor.iloc[0]))
                    turtle.write(arg=state)
                    states_correct.append(answer_state)
            
screen.mainloop()
