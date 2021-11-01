import turtle
import pandas

data = pandas.read_csv("50_states.csv")
screen = turtle.Screen()
guessed_states = []
states = data["state"].tolist() 
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

while len(guessed_states) < 50:
    screen.title(f"US States Puzzle")
    user_answer = str(screen.textinput(title=f"Guessed {len(guessed_states)} / {len(states)}", prompt="Enter name of state")).capitalize()
    
    if user_answer == "Q" or user_answer == "End":
        missed_states = pandas.DataFrame([state for state in states if state not in guessed_states]).to_csv("missed_states.csv")

        break
    
    if user_answer in states:
        guessed_states.append(user_answer)
        user_state = data[data.state == user_answer]
        
        name_turtle = turtle.Turtle()
        name_turtle.hideturtle()
        name_turtle.penup()
        name_turtle.setposition(float(user_state.x), float(user_state.y))
        name_turtle.pendown()
      
        name_turtle.write(user_answer, False, align="center")

 

    

screen.exitonclick()
