import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import WINDOW_CLOSED

def main():
    layout = [
        [sg.Text('Calculator 1.0 PySimpeGUI')],
        [sg.Button('CE')]
    ]

    window = sg.Window('Calculator', layout, size=(300, 300))

    while True:
        event, values = window.read()
        if event == WINDOW_CLOSED:
            break

        print(event, values)
    
    window.close()


if __name__ == '__main__':
    main()