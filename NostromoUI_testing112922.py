import PySimpleGUI as sg
import PIL.Image


# Guides : https://stackoverflow.com/questions/66537095/how-can-i-make-pysimplegui-read-my-input-and-update-my-window


# Info on colors https://stackoverflow.com/questions/69151062/how-do-i-change-background-color-in-pysimplegui
# Video guide: https://www.youtube.com/watch?v=LzCfNanQ_9c&t=277s
# Guide on images for layout? https://stackoverflow.com/questions/67079155/displaying-an-image-using-pysimplegui-without-having-to-use-an-event-listener
# Guide on images etc.best free
# This is how many rows are within your application and what they do
layout = [[sg.Text('Your typed chars appear here:'), sg.Text(size=(15,1), key='-OUTPUT-')],
          [sg.Input(key='-IN-')],
          [sg.Button('Show'), sg.Button('Exit')]]

# So this window controls how the window of the application feels.
window = sg.Window('Nostromo_v1', layout, size=(700, 500),
                   background_color='black', button_color='green',
                   titlebar_text_color='orange',
                   )

fp = open("Weyland.png", "rb")
img = PIL.Image.open(fp)





# Loop that maintains that the application stays open. Without this it would close
# When you completed your action.
while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Show':
        if values['-IN-'] == 'Test':  # So this fails when you added a second if elif probably!
            window['-OUTPUT-'].update('What shall we test?')
        elif 'wea' in values['-IN-']:
            window['-OUTPUT-'].update('Did you want weather?')
        else:
            window['-OUTPUT-'].update(values['-IN-'])
        print(values['-IN-'])



window.close()