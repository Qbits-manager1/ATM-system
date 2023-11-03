import PySimpleGUI as sg

def login_screen():
  sg.theme('DarkTeal12') 
  # add the components inside the window
  layout = [  
    [sg.Text('ATM system',size=(15,2),font=('Arial',25),justification='center')],
    [sg.Text('Enter account number:',size=(20,2)), sg.Input(key='acc_number', size=(10, 2), font=('Arial', 16))],
    [sg.Text('Enter PIN:',size=(20,2)), sg.Input(key='pin',password_char="*", size=(10, 2), font=('Arial', 16))],
    [sg.Text('',size=(10,2)),sg.Button('Sign in'), sg.Button('Cancel') ]
  ]  

  # create the Window
  window = sg.Window('Login', layout)  

 # event loop to keep the GUI window active
  while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break           
  window.close()

login_screen()
