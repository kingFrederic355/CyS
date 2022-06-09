import io
from nis import cat
import os
import PySimpleGUI as sg
import ecies as ec



spanishAlphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

file_types = [("JPEG (*.jpg)", "*.jpg"),
              ("All files (*.*)", "*.*")]

def main():
    sg.theme('DarkAmber')   # Add a touch of color
    
    layout = [
                [sg.Text('Curva      y^2 = x^3 + Ax + B, en Zp')],
                [
                    sg.Text('A: '),sg.Input(size=(10, 1), key='avalue'),
                    sg.Text('B: '),sg.Input(size=(10, 1), key='bvalue'),
                    sg.Text('Zp: '),sg.Input(size=(10, 1), key='zpvalue'),
                    sg.Button('Clear',key = 'clear curve')
                ],
                [
                    sg.Text('Punto P = (x1,y1)  x1:'), 
                    sg.Input(size=(5, 1), key='xval1'),sg.Text('y1:'),sg.Input(size=(5, 1), key='yval1'),
                    sg.Button('Clear', key='clear ppoint')
                ],
                [
                    sg.Text('Punto Q = mP = (x2,y2)  x2:'), 
                    sg.Input(size=(5, 1), key='xval2'),sg.Text('y2:'),sg.Input(size=(5, 1), key='yval2'),
                    sg.Text('m:'),sg.Input(size=(5, 1), key='m'),
                    sg.Button('Calcula Q', key='calcula'),
                    sg.Button('Clear', key='clear qpoint')
                ],
                [sg.Text('Mensaje sin cifrar')],
                [sg.Multiline(size=(100, 2), key='dmsg')],
                [sg.Text('Mensaje cifrado')],
                [sg.Button('Encrypta'),sg.Button('Clear', key='clear nocode')],
                [sg.Multiline(size=(100, 10), key='emsg')],
                [sg.Button('Clear',key='clear coded')]
            ]

    window = sg.Window("ECIES", layout)

    while True:
        
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

        if event == 'clear curve':
            window['avalue'].update('')
            window['bvalue'].update('')
            window['zpvalue'].update('')
        
        if event == 'clear ppoint':
            window['xval1'].update('')
            window['yval1'].update('')
        
        if event == 'clear qpoint':
            window['xval2'].update('')
            window['yval2'].update('')
            window['m'].update('')

        if event == 'clear nocode':
            window['dmsg'].update('')

        if event == 'clear coded':
            window['emsg'].update('')
        
        if event == 'calcula':
            try:
                x1 = int(values['xval1'])
                y1 = int(values['yval1'])
                mval = int(values['m'])
                a = int(values['avalue'])
                mod = int(values['zpvalue'])
            except:
                print('Datos no validos')
                break
            q = ec.getSuma(x1,y1,mod,a,mval)
            window['xval2'].update(str(q[0]))
            window['yval2'].update(str(q[1]))
        
        if event == 'Encrypta':
            try:
                a = int(values['avalue'])
                b = int(values['bvalue'])
                zp = int(values['zpvalue'])
                curve = [a,b,zp]
                x1 = int(values['xval1'])
                y1 = int(values['yval1'])
                p = [x1,y1]
                x2 = int(values['xval2'])
                y2 = int(values['yval2'])                
                q = [x2,y2]
            except:
                print('Algo salio mal')
                break
            
            print('Curva: y^2 = x^3 + ',a,'*x + ',b,' mod (',zp,')')
            
            p = [8,21]           
            msg = values['dmsg']
            encoded = ec.encode(curve,p,q,30,msg)
            print('Mensaje encriptado: ' + str(encoded))
            window['emsg'].update(str(encoded))
        
        if event == 'Desencrypta':
            print('-1')
            '''
            window['dmsg'].update(str(mensaje))'''
    
    window.close()

if __name__ == "__main__":
    main()