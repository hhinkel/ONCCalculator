'''
Created on May 5, 2017

@author: Heidi Hinkel
'''
import PySimpleGUI as sg
import math
from measurement.measures import Distance, Weight
from screenValues import ScreenValues

menu_def = [['File', ['Exit']],
            ['Help', ['About']], ]


layout = [
    [sg.Menu(menu_def, tearoff=True)],
    [sg.Text('Sex: '), 
     sg.Radio('Male', "SEX", default=False, size=(10,1)), 
     sg.Radio('Female', "SEX", default=False, size=(10,1))],
    [sg.Text('Age: '), sg.InputText('Enter Age in years'), sg.Text('years')],
    [sg.Text('Serum Creatinine Level: '), sg.InputText('Enter Serum Creatinine'), sg.Text('mg/dl')],
    [sg.Text('Weight: '), sg.InputText('Enter pounds'),
     sg.Text('lb '), sg.InputText('Enter ounces'),sg.Text('oz')],
    [sg.Text('Height: '), sg.InputText('Enter feet'),
     sg.Text('ft '), sg.InputText('Enter inches'),sg.Text('in')],
    [sg.Button('Calculate'), sg.Cancel()],
    [sg.Text('_' * 40), sg.Text(' Results '),sg.Text('_' * 40)],
    [sg.Text('Height (cm): '), sg.Text('_' * 5, key='_CM_'), sg.Text('cm')],
    [sg.Text('Weight (kg): '), sg.Text('_' * 5, key="_KG_"), sg.Text('kg')],
    [sg.Text('BMI: '), sg.Text('_' * 5, key="_BMI_"), sg.Text('kg/m2')],
    [sg.Text('BSA: '), sg.Text('_' * 5, key="_BSA_"), sg.Text('m2')],
    [sg.Text('Creatinine Clearance: '), sg.Text('_' * 5, key="_CRCL_"), sg.Text('mg/dl')],
    [sg.Text('Creatinine Clearance (Mod): '), sg.Text('_' * 5, key="_CRCLM_"), sg.Text('mg/dl')],
]

def callAboutScreen():
    pass

def error(values):
    return False

def callErrorScreen():
    pass

window = sg.Window("ONC Body Value Calculator", layout, default_element_size=(40, 1), grab_anywhere=False)

while True:             # Event Loop
    event, values = window.Read()
    if event is "Cancel":
        break
    if values[0] is 'Exit':
        break
    if values[0] is 'About':
        callAboutScreen()
    if error(values) is True:
        callErrorScreen()
    
    screen = ScreenValues(values)

    window.Element('_CM_').Update(screen.heightCm)
    window.Element("_KG_").Update(screen.weightKg)
    window.Element('_BMI_').Update('XX.XX')
    window.Element("_BSA_").Update("X.XX")
    window.Element("_CRCL_").Update("X.X")
    window.Element("_CRCLM_").Update("X.X")

