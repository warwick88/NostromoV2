import PySimpleGUI as sg
import PIL.Image

# best guide is this https://www.pysimplegui.org/en/latest/cookbook/#recipe-printing-24-print-to-output-element
# it is the Pysimegui guide it's at Recipe - Printing persistent window


# First the window layout in 2 columns
file_list_column = [
    [sg.Image(filename="Weyland.png", size=(375, 200), key='-IMAGE-')],
    [sg.Text('Movie Selection', font=('Arial', 10, 'bold'), background_color='black', justification='center', text_color='green', size=(20, 1))],
    [sg.Button("Alien"), sg.Button("Aliens"), sg.Button("Alien 3")],
     ]

# For now will only show the name of the file that was chosen
image_viewer_column = [
    [sg.Text('Input: '), sg.Input(key='-IN-')],
    [sg.Text('Response: '), sg.Multiline(size=(40, 8),background_color='grey', key='-OUTPUT-')],
    [sg.Button('Enter', bind_return_key=True), sg.Button("Exit")],
     ]

# ----- Full layout -----
layout = [
    [sg.Column(file_list_column, background_color='black'),
     sg.VSeperator(),
     sg.Column(image_viewer_column, background_color='black')],
]
#window = sg.Window("Column Demo", layout)




#layout = [[sg.Image(filename="Weyland.png", size=(375, 200), key='-IMAGE-'), sg.Text('Input: '), sg.Input(key='-IN-')],
         # [sg.Button('Enter', bind_return_key=True), sg.Button("Exit"), sg.Text('Response: '), sg.Multiline(size=(30, 5),background_color='grey', key='-OUTPUT-')],
          #[sg.Text("Terminal: "), sg.InputText(key="-IN-")],
          #[sg.Text("Output: "), sg.Output(key="-OUT-")],
          #[sg.Text("Output2: "), sg.Output(key='-OUTPUT-')],
          #[sg.Button('Enter')bind_return_key=True), sg.Button("Exit")],
          # [sg.Button("Alien"), sg.Button("Aliens"), sg.Button("Alien 3")],
          # [sg.Exit(), sg.Button("Convert to CSV")]
#          ]

# So this window controls how the window of the application feels.
window = sg.Window('Nostromo_v1', layout, size=(800, 350),
                   background_color='black', button_color='green',
                   titlebar_text_color='orange',
                   )

#fp = open("Weyland.png", "rb")
#img = PIL.Image.open(fp)





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
        window['-OUTPUT-'].update('Now starting Alien Directors cut')
    if event == "Aliens":
        window['-OUTPUT-'].update("Now starting Aliens Directors cut")
    if event == "Alien 3":
        window['-OUTPUT-'].update("Now playing Aliens 3 Director cut")

window.close()


