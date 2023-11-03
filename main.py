import PySimpleGUI as sg
import csv

def verify_credentials(acc_no, pin):
  # open the file in read mode
  filename = open('credentials.csv', 'r')
  # create dictreader object to read the data from file
  file = csv.DictReader(filename) 
  # iterate over each row and append values to empty list
  for col in file:
    if col['Account number'] == acc_no and col['PIN'] == pin :
        return True     
  return False

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
    if event == "Sign in":
      acc_number = values['acc_number']
      pin = values['pin']            

      if verify_credentials(acc_number,pin):                                  
        window.close()
        # call the function to display main screen
      else:
        sg.popup("Check your account number and PIN", background_color='grey', title='Error')
        window['acc_number'].update("")
        window['pin'].update("")
        window['acc_number'].Widget.focus()           
  window.close()

login_screen()
