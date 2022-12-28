import PySimpleGUI as sg
import PIL.Image





# Info on colors https://stackoverflow.com/questions/69151062/how-do-i-change-background-color-in-pysimplegui
# Video guide: https://www.youtube.com/watch?v=LzCfNanQ_9c&t=277s
# Guide on images for layout? https://stackoverflow.com/questions/67079155/displaying-an-image-using-pysimplegui-without-having-to-use-an-event-listener
# Guide on images etc.best free
# This is how many rows are within your application and what they do
layout = [[sg.Image(size=(200, 200), key='-IMAGE-')],
          [sg.Text("Input File:"), sg.Input(key="-IN-"), sg.FileBrowse()],
          [sg.Text("    Output:"), sg.Input(key="-OUT-"), sg.FileBrowse()],
          [sg.Button("Alien"), sg.Button("Aliens"), sg.Button("Alien 3")],
          [sg.Exit(), sg.Button("Convert to CSV")]
          ]

# So this window controls how the window of the application feels.
window = sg.Window('Nostromo_v1', layout, size=(700, 400),
                   background_color='black', button_color='green',
                   titlebar_text_color='orange',
                   )

fp = open("Weyland.png", "rb")
img = PIL.Image.open(fp)





# Loop that maintains that the application stays open. Without this it would close
# When you completed your action.
while True:  # Event Loop
    event, values = window.read()
    # print(event, values) this was annoying it kept printing rubbish
    if event in (None, 'Exit'):
        break
    if event == "Alien":
        print("Excellent choice, now starting Alien Directors cut")
    if event == "Aliens":
        print("Now starting Aliens Directors cut")
    if event == "Alien 3":
        print("Now playing Aliens 3 Director cut")
    if event == 'Convert to CSV':
        # So this is pretty cool, this let's you display the loaded image.
        img.show()
        break
window.close()
