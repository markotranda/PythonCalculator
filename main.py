from tkinter.constants import RIGHT
from typing import List
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import WINDOW_CLOSED

class Calculator:
    value: str
    value_stack: List
    for_reset: bool

    def __init__(self) -> None:
        self.__button_reset()

    def __str__(self) -> str:
        return self.value

    def button_press(self, event):
        if event in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            self.__button_digit(event)
        elif event == '.':
            self.__button_comma()
        elif event == 'CE':
            self.__button_reset()
        elif event == '+/-':
            self.__button_sign()
        elif event in ('+', '-', '*', '/', '%'):
            self.__button_operator(event)
        elif event == '=':
            self.__calculate_value_stack()

    def __button_comma(self):
        if not '.' in self.value:
            self.value += '.'
            
    def __button_digit(self, input):
        if self.value == '0' or self.for_reset:
            self.value = input
        else:
            self.value += input
        self.for_reset = False
    
    def __button_sign(self):
        if float(self.value) > 0:
            self.value = '-' + self.value
        else:
            self.value = self.value[1:]

    def __button_operator(self, operator):
        self.__calculate_value_stack()
        self.value_stack.append(self.value)
        self.value_stack.append(operator)
        self.for_reset = True
        
    def __calculate_value_stack(self):
        self.value_stack.append(self.value)
        if len(self.value_stack) >= 3:
            value2 = self.value_stack.pop()
            operator = self.value_stack.pop()
            value1 = self.value_stack.pop()

            if operator == '+':
                self.value_stack.append(f'{float(value1) + float(value2)}')
            elif operator == '-':
                self.value_stack.append(f'{float(value1) - float(value2)}')
            elif operator == '*':
                self.value_stack.append(f'{float(value1) * float(value2)}')
            elif operator == '/':
                self.value_stack.append(f'{float(value1) / float(value2)}')
            elif operator == '%':
                self.value_stack.append(f'{(float(value1)/100) * float(value2)}')
                
        self.value = self.value_stack.pop()
    
    def __button_reset(self):
        self.value = '0'
        self.value_stack = []
        self.for_reset = False

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

    window = sg.Window('Calculator', layout, size=(235, 350))

    while True:
        event, values = window.read()
        if event == WINDOW_CLOSED:
            break
                
        calculator.button_press(event)
        window['-INPUT-'].update(calculator)

    window.close()

if __name__ == '__main__':
    main()