#!/usr/bin/python3
import threading
import time
import PySimpleGUI as sg



def long_operation_thread(seconds, window):
    progress = 0
    print('Thread started - will sleep for {} seconds'.format(seconds))
    for i in range(int(seconds * 10)):
        time.sleep(.1)  # sleep for a while
        progress += 100 / (seconds * 10)
        window.write_event_value('-PROGRESS-', progress)
    window.write_event_value('-THREAD-','Finished')
    
def long_operation_thread2(seconds, window):
    progress = 0
    print('Thread started - will sleep for {} seconds'.format(seconds))
    for i in range(int(seconds * 10)):
        time.sleep(.1)  # sleep for a while
        progress += 100 / (seconds * 10)
        window.write_event_value('-PROGRESS2-', progress)
    window.write_event_value('-THREAD2-','Finished') 

          #Empiezan los experimentos con el codigo
  
def long_operation_thread3(seconds, window):        #CAMBIAMOS EL NOMBRE DEL THREAD
    progress = 0                                    # Progres inicia en 0
    print('Thread started - will sleep for {} seconds'.format(seconds))
    for i in range(int(seconds * 10)):
        time.sleep(.1)  # sleep for a while
        progress += 100 / (seconds * 10)
        window.write_event_value('-PROGRESS3-', progress) #Ajustamos nombre de la varialble PROGRESS
    window.write_event_value('-THREAD3-','Finished')     #ajustamos nombre de la variable THREAD
  

def long_operation_thread4(seconds, window):  #CAMBIAMOS EL NOMBRE DEL THREAD
    progress = 0  # Progres inicia en 0
    print('Thread started - will sleep for {} seconds'.format(seconds))
    for i in range(int(seconds * 10)):
        time.sleep(.1)  # sleep for a while
        progress += 100 / (seconds * 10)
        window.write_event_value('-PROGRESS4-', progress) #Ajustamos nombre de la varialble PROGRESS
    window.write_event_value('-THREAD4-','Finished') #ajustamos nombre de la variable THREAD

    
def long_operation_thread5(seconds, window):  #CAMBIAMOS EL NOMBRE DEL THREAD
    progress = 0  # Progres inicia en 0
    print('Thread started - will sleep for {} seconds'.format(seconds))
    for i in range(int(seconds * 10)):
        time.sleep(.1)  # sleep for a while
        progress += 100 / (seconds * 10)
        window.write_event_value('-PROGRESS5-', progress) #Ajustamos nombre de la varialble PROGRESS
    window.write_event_value('-THREAD5-','Finished') #ajustamos nombre de la variable THREAD


def the_gui():
    #sg.theme('Light Brown 3')
    layout = [[sg.B('Boton1'),
               sg.ProgressBar(100, size=(20, 20),orientation='h', key='-PROG1-'),
               sg.Input(key='-SECONDS-', focus=True, size=(5, 1))],
              [sg.B('Boton2'),sg.ProgressBar(100, size=(20, 20),
                              orientation='h', key='-PROG2-'),
               sg.Input(key='-SECONDS2-', focus=True, size=(5, 1))],
              [sg.B('Boton3'),sg.ProgressBar(100, size=(20, 20),
                              orientation='h', key='-PROG3-'),
               sg.Input(key='-SECONDS3-', focus=True, size=(5, 1))],
              [sg.B('Boton4'),sg.ProgressBar(100, size=(20, 20),
                              orientation='h', key='-PROG4-'),
               sg.Input(key='-SECONDS4-', focus=True, size=(5, 1))],
              [sg.B('Boton5'),sg.ProgressBar(100, size=(20, 20),
                              orientation='h', key='-PROG5-'),
               sg.Input(key='-SECONDS5-', focus=True, size=(5, 1))],
              [sg.Button('Exit') ]]
    window = sg.Window('Ventana Multihilo', layout)

  
    # --------------------- EVENT LOOP ---------------------
    work_id = 0
    
    timeout = thread = None
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if event == 'Boton1':
            if values['-SECONDS-']!= '' and float(values['-SECONDS-'])>=0: 
                thread = threading.Thread(target=long_operation_thread,
                                      args=(float(values['-SECONDS-']),
                                            window), daemon=True)
                thread.start()
        if values['-SECONDS2-']!= '' and float(values['-SECONDS2-'])>=0:
            if event == 'Boton2':
                thread2 = threading.Thread(target=long_operation_thread2,
                                      args=(float(values['-SECONDS2-']),
                                            window), daemon=True)
                thread2.start()
        if event =='-PROGRESS-':
            window['-PROG1-'].update_bar(values[event], 100)
        if event =='-PROGRESS2-':
            window['-PROG2-'].update_bar(values[event], 100)
        if event == '-THREAD-':
            window['-PROG1-'].update_bar(0,0)
        if event == '-THREAD2-':
            window['-PROG2-'].update_bar(0,0)

          #COMIEZA SEGUNDO EXPERIMENTO

        if event == 'Boton3': #CAMBIO
            if values['-SECONDS3-']!= '' and float(values['-SECONDS3-'])>=0: 
                thread3 = threading.Thread(target=long_operation_thread3,
                                      args=(float(values['-SECONDS3-']),
                                            window), daemon=True)
                thread3.start()#CAMBIO
        if event =='-PROGRESS3-':#CAMBIO
            window['-PROG3-'].update_bar(values[event], 100)       #CAMBIO
        if event == '-THREAD3-':#CAMBIO
            window['-PROG3-'].update_bar(0,0)#CAMBIO


        if event == 'Boton4': #CAMBIO   
            if values['-SECONDS4-']!= '' and float(values['-SECONDS4-'])>=0: 
                thread4 = threading.Thread(target=long_operation_thread4,
                                      args=(float(values['-SECONDS4-']),
                                            window), daemon=True)
                thread4.start()#CAMBIO
        if event =='-PROGRESS4-':#CAMBIO
            window['-PROG4-'].update_bar(values[event], 100)       #CAMBIO
        if event == '-THREAD4-':#CAMBIO
            window['-PROG4-'].update_bar(0,0)#CAMBIO

          
        
        if event == 'Boton5': #CAMBIO
            if values['-SECONDS5-']!= '' and float(values['-SECONDS5-'])>=0: 
                thread5 = threading.Thread(target=long_operation_thread5,
                                      args=(float(values['-SECONDS5-']),
                                            window), daemon=True)
                thread5.start()#CAMBIO
        if event =='-PROGRESS5-':#CAMBIO
            window['-PROG5-'].update_bar(values[event], 100)       #CAMBIO
        if event == '-THREAD5-':#CAMBIO
            window['-PROG5-'].update_bar(0,0)#CAMBIO

                
    window.close()

#if __name__ == '__main__':
the_gui()
print('Exiting Program')
