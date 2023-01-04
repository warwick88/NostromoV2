import PySimpleGUI as sg
import MovieInfoTerminalResponses as mr
import EngineerGame as eg

# best guide is this https://www.pysimplegui.org/en/latest/cookbook/#recipe-printing-24-print-to-output-element
# it is the Pysimegui guide it's at Recipe - Printing persistent window


# First the window layout in 2 columns
file_list_column = [
    [sg.Image(filename="Weyland.png", size=(375, 200), key='-IMAGE-')],
    [sg.Text('Movie Selection', font=('Arial', 10, 'bold'), background_color='black', justification='center',
             text_color='green', size=(20, 1))],
    [sg.Button("Alien"), sg.Button("Aliens"), sg.Button("Alien 3"), sg.Button("Engineer Game")],
]

# For now will only show the name of the file that was chosen
image_viewer_column = [
    [sg.Text('Input: '), sg.Input(key='-IN-')],
    [sg.Text('Response: '), sg.Multiline(size=(40, 8), background_color='grey', key='-OUTPUT-')],
    [sg.Button('Enter', bind_return_key=True), sg.Button("Exit")],
]
image_viewer_column2 = [
    [sg.Image(filename="Galaxy.png", size=(375, 200), key='-IMAGE-')],
    [sg.Text('Input: '), sg.Input(key='-IN2-')],
    [sg.Text('Output: '), sg.Multiline(size=(40, 8), background_color='grey', key='-OUTPUT2-')],
    [sg.Button('Exit Game', bind_return_key=True)],
    # [sg.Text('Input2: '), sg.Input(key='-IN-')],
    # [sg.Text('Response2: '), sg.Multiline(size=(40, 8), background_color='grey', key='-OUTPUT2-')],
    # [sg.Button('Enter2', bind_return_key=True), sg.Button("Exit2")],
]
# ----- Full layout -----
layout = [
    [sg.Column(file_list_column, background_color='black'),
     sg.VSeperator(),
     sg.Column(image_viewer_column, background_color='black', key='-COL2-', visible=True),
     sg.Column(image_viewer_column2, background_color='black', key='-COL3-', visible=False)],
]

# So this window controls how the window of the application feels.
window = sg.Window('Nostromo_v1', layout, size=(800, 425),  # was 350 adjusting a little.
                   background_color='black', button_color='green',
                   titlebar_text_color='orange',
                   )

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
        elif (str('Story') in values['-IN-']) or (str('story') in values['-IN-']):
            list_mother_responses = list(mr.mother_responses.values())
            window['-OUTPUT-'].update(list_mother_responses[0])
        elif (str('Mother') in values['-IN-']) or (str('mother') in values['-IN-']):
            list_mother_values = list(mr.mother_info.values())
            window['-OUTPUT-'].update(list_mother_values[0])
        elif (str('Dallas') in values['-IN-']) or (str('dallas') in values['-IN-']):
            list_dallas_values = list(mr.dallas_info.values())
            window['-OUTPUT-'].update(list_dallas_values[0] + '\n' + list_dallas_values[1] + '\n'
                                      + list_dallas_values[2])
    if event == "Alien":
        window['-OUTPUT-'].update('Now starting Alien Directors cut')
    if event == "Engineer Game":
        # So this code works. It updates the windows as expected.
        window['-COL2-'].update(visible=False)
        window['-COL3-'].update(visible=True)
        list_game_values = list(eg.game_responses.values())
        #print(eg.game_responses)
        #print(eg.game_responses[0])
        # Put a delay here so it looks cooler
        window['-OUTPUT2-'].update(list_game_values[0])
        # window['-OUTPUT2-'].update(eg.game_responses[0])

    if event == "Aliens":
        window['-OUTPUT-'].update("Now starting Aliens Directors cut")
        window['-OUTPUT2-'].update("Now starting Aliens Directors cut")
    if event == "Alien 3":
        window['-OUTPUT-'].update("Now playing Aliens 3 Director cut")
    if event == "Exit2":
        break
    if event == "Exit Game":
        window['-COL2-'].update(visible=True)
        window['-COL3-'].update(visible=False)

window.close()
