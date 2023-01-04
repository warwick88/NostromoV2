import PySimpleGUI as sg
import PIL.Image

# best guide is this https://www.pysimplegui.org/en/latest/cookbook/#recipe-printing-24-print-to-output-element
# it is the Pysimegui guide it's at Recipe - Printing persistent window


layout = [[sg.Image(filename="Weyland.png", size=(375, 200), key='-IMAGE-')],
          [sg.Text('Response: '), sg.Multiline(size=(30, 5), key='-OUTPUT-')],
          [sg.Input(key='-IN-')],
          #[sg.Text("Terminal: "), sg.InputText(key="-IN-")],
          #[sg.Text("Output: "), sg.Output(key="-OUT-")],
          #[sg.Text("Output2: "), sg.Output(key='-OUTPUT-')],
          [sg.Button('Enter'), sg.Button("Exit")],
          # [sg.Button("Alien"), sg.Button("Aliens"), sg.Button("Alien 3")],
          # [sg.Exit(), sg.Button("Convert to CSV")]
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
    if event == 'Enter':
        if values['-IN-'] == 'Test':  # So this fails when you added a second if elif probably!
            window['-OUTPUT-'].update('What shall we test?')
        elif values['-IN-'] == 'wea':
            window['-OUTPUT-'].update('Did you want weather?')
        elif str('story') in values['-IN-']:
            window['-OUTPUT-'].update('PRIORITY ONE:'"\n"
                                      'INSURE RETURN OF ORGANISM'"\n"
                                      'FOR ANALYSIS.'"\n"
                                      'ALL OTHER CONSIDERATIONS SECONDARY.'"\n"
                                      'CREW EXPENDABLE.'"\n")
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

