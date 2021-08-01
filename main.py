from tkinter.constants import RIGHT
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import WINDOW_CLOSED

class Calculator:
    stored_value: str
    value: str

    def __init__(self) -> None:
        self.value = '0'

    def __str__(self) -> str:
        return self.value

    def button_press(self, event):
        if event in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.',):
            if self.value == '0':
                self.value = event
            else:
                self.value += event
        elif event == 'CE':
            self.value = '0'

def main():
    calculator = Calculator()

    layout = [
        [sg.Text('Calculator 1.0 PySimpeGUI')],
        [sg.Column([[sg.Text(calculator, key='-INPUT-', size=(23, 1), background_color='#FFF', text_color='#000', justification=RIGHT)]])],
        [sg.Column([[sg.Button('CE', size=(4, 2)), sg.Button('+/-', size=(4, 2)), sg.Button('%', size=(4, 2)), sg.Button('/', size=(4, 2))]])],
        [sg.Column([[sg.Button('7', size=(4, 2)), sg.Button('8', size=(4, 2)), sg.Button('9', size=(4, 2)), sg.Button('*', size=(4, 2))]])],
        [sg.Column([[sg.Button('4', size=(4, 2)), sg.Button('5', size=(4, 2)), sg.Button('6', size=(4, 2)), sg.Button('-', size=(4, 2))]])],
        [sg.Column([[sg.Button('1', size=(4, 2)), sg.Button('2', size=(4, 2)), sg.Button('3', size=(4, 2)), sg.Button('+', size=(4, 2))]])],
        [sg.Column([[sg.Button('0', size=(4, 2)), sg.Button('.', size=(4, 2)), sg.Button('=', size=(4, 2))]], element_justification=RIGHT)]
    ]

    window = sg.Window('Calculator', layout, size=(250, 400))

    while True:
        event, values = window.read()
        if event == WINDOW_CLOSED:
            break
                
        calculator.button_press(event)
        window['-INPUT-'].update(calculator)

    window.close()


if __name__ == '__main__':
    main()