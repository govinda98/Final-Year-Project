from guizero import App, Text, PushButton 

def say_my_name():
    welcome_message.value = exec(open("dummy.py").read())
     

app = App(title="ALS Comms")
#insert widget code here
spacer= Text(app, text=" ")
spacer= Text(app, text=" ")
spacer= Text(app, text=" ")
spacer= Text(app, text=" ")
welcome_message = Text(app, text="WELCOME TO THE ASSISTIVE COMMUNICATION APP", size=34, font="Arial Bold", color='blue')
spacer= Text(app, text=" ")
spacer= Text(app, text=" ")
spacer= Text(app, text=" ")
message = Text(app, text="Click the button below to begin.", size=25, font="Arial Bold", color='black')
spacer= Text(app, text=" ")
spacer= Text(app, text=" ")
spacer= Text(app, text=" ")
spacer= Text(app, text=" ")
spacer= Text(app, text=" ")
spacer= Text(app, text=" ")
update_text = PushButton(app, command=say_my_name, text="Begin Sign Language Communication")
#end of code
app.display()