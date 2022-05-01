import io
import os
import PySimpleGUI as sg
from PIL import Image
import rsa

spanishAlphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

file_types = [("JPEG (*.jpg)", "*.jpg"),
              ("All files (*.*)", "*.*")]

def main():
    sg.theme('DarkAmber')   # Add a touch of color
    
    layout = [  
        
                [sg.Button('Genera claves'),sg.Button('Limpia claves')],
                [sg.Text('Encryptado')],
                [sg.Text('Valor n'),sg.Multiline(size=(100, 3), key='nkey')],
                [sg.Text('Valor e'),sg.Multiline(size=(100, 3), key='ekey')],
                [sg.Text('Valor d'),sg.Multiline(size=(100, 3), key='dkey')],
                [sg.Text('Mensaje sin cifrar')],
                [sg.Multiline(size=(100, 2), key='dmsg')],
                [sg.Text('Mensaje cifrado')],
                [sg.Multiline(size=(100, 10), key='emsg')],
                [sg.Button('Encrypta'),sg.Button('Desencrypta'),sg.Button('Limpia')],
            ]  # identify the multiline via key option

    window = sg.Window("RSA", layout)

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

        if event == "Genera claves":
            keys = rsa.generaClaves()                       
            window['nkey'].update(str(keys[0]))
            window['ekey'].update(str(keys[1]))
            window['dkey'].update(str(keys[2]))            

        if event == "Encrypta":
            try:
                msg = values['dmsg']
                n = int(values['nkey'])
                e = int(values['ekey'])
                window['emsg'].update(str(rsa.encrypt(msg,e,n)))
            except:
                print('Faltan elementos')         
                

        if event == "Desencrypta":
                        
            try:
                msg = values['emsg']
                n = int(values['nkey'])
                d = int(values['dkey'])
                window['dmsg'].update(str(rsa.decrypt(msg,d,n)))
            except:
                print('Faltan elementos')
                       
        if event == "Limpia":
            window['emsg'].update('')
            window['dmsg'].update('')

        if event == "Limpia claves":
            window['nkey'].update('')
            window['ekey'].update('')
            window['dkey'].update('')
            

    window.close()


if __name__ == "__main__":
    main()