import PySimpleGUI as sg

sg.change_look_and_feel('Dark Blue 3')

layout = [  [sg.Text('My Window')],
            [sg.Input(key='-IN-'), sg.Text(size=(12,1), key='-OUT-')],
            [sg.Button('Go'), sg.Button('Exit'), sg.Debug()]  ]

window = sg.Window('Window Title', layout)

while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break
    if event == 'Go':
        window['-OUT-'].Update(values['-IN-'])
window.close()