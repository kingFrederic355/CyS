import io
import os
import PySimpleGUI as sg
from PIL import Image
import misc as ms
import Hill as hl

spanishAlphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

file_types = [("JPEG (*.jpg)", "*.jpg"),
              ("All files (*.*)", "*.*")]

def main():
    layout = [
        [
            # Filtros letras simples
            [
                sg.Text('Texto a Cifrar'),
                sg.Input(size=(25, 1), key="-TXTNORMAL-"),
                sg.Text('Clave'),
                sg.Input(size=(25, 1), key="-CKEY-"),
                sg.Button("Cifrar")
            ],

            [sg.Input(size=(25, 1), key='-CIFRADO-')],
            
            # Filtros letras simples
            [
                sg.Text('Texto a Descifrar'),
                sg.Input(size=(25, 1), key="-TXTCIFRADO-"),
                sg.Text('Clave'),
                sg.Input(size=(25, 1), key="-DKEY-"),
                sg.Button("Descifrar")
                ],
            [sg.Input(size=(25, 1), key='-DESCIFRADO-')],
        ]
    ]

    window = sg.Window("Image Viewer", layout)

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

        if event == "Cifrar":
            filename = values["-TXTNORMAL-"]
            key = values["-CKEY-"]
            print('MENSAJE: '+filename+'\nClave: '+key)
            window['-CIFRADO-'].update(hl.cifradoHill(filename,key,spanishAlphabet))
            
        
        if event == "Descifrar":
            filename = values["-TXTCIFRADO-"]
            key = values["-DKEY-"]
            print('MENSAJE: '+filename+'\nClave: '+key)
            window['-DESCIFRADO-'].update(hl.decifradoHill(filename,key,spanishAlphabet))
            

    window.close()


if __name__ == "__main__":
    main()