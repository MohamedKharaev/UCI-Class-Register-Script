import tkinter as tk
from tkinter import messagebox
import re
import urllib.request


def _get_verified_set() -> set:
    '''returns a set with the ucinetids that have been authenticated'''
    website = urllib.request.urlopen('https://uci-class-bot.000webhostapp.com/')
    data = website.read()
    website.close()
    data = data.decode(encoding = 'utf-8')
    return set(data.split('\n'))
        

class GUI:
    def __init__(self):

        self._root_window = tk.Tk()


## Main Banner

        self._mainbanner = tk.Label(
            master = self._root_window, text = 'UCI CLASS BOT',
            font = ('Arial', 30))
        self._subbanner = tk.Label(
            master = self._root_window, text = '''*CHROME MUST BE INSTALLED FOR THIS BOT TO WORK*
*Input class codes*''', font = ('Courier', 8))
        
        self._mainbanner.grid(
            row = 0, columnspan = 6)
        self._subbanner.grid(
            row = 1, columnspan = 6)




## Default variables
        self.submit_pressed = False
        self.login = ''
        self.passw = ''
        self.rtime = ''
        self.c1 = ['','','']
        self.c2 = ['','','']
        self.c3 = ['','','']
        self.c4 = ['','','']
        self.c5 = ['','','']
        self.classes = []
        self.aclasses = []



##Account Login
        self._login_label = tk.Label(
            master = self._root_window, text = "UCInetID")
        self._login_entry = tk.Entry(
            master = self._root_window, width = 15,
            textvariable = tk.StringVar())
        self._password_label = tk.Label(
            master = self._root_window, text = "Password: ")
        self._password_entry = tk.Entry(
            master = self._root_window, width = 15,
            textvariable = tk.StringVar())
        

        self._login_label.grid(
            row = 2, column = 1, columnspan = 2)
        self._login_entry.grid(
            row = 3, column = 1, columnspan = 2)
        self._password_label.grid(
            row = 2, column = 3, columnspan = 2)
        self._password_entry.grid(
            row = 3, column = 3, columnspan = 2)
            
        

## Registration Time
        self._registration_label = tk.Label(
            master = self._root_window, text = '''Registration Time
(EX: Jun 24 2017 12:15PM)''')
        self._registration_entry = tk.Entry(
            master = self._root_window, width = 20,
            textvariable = tk.StringVar())

        self._registration_label.grid(
            row = 4, column = 0, columnspan = 6)
        self._registration_entry.grid(
            row = 5, column = 0, columnspan = 6, pady = (0, 10))


## Class 1
        self._class1Label = tk.Label(
            master = self._root_window, text = 'Lecture 1: ')
        self._class1Entry = tk.Entry(
            master = self._root_window, width = 10,
            textvariable = tk.StringVar())
        self._Lab1Label = tk.Label(
            master = self._root_window, text = 'Lab 1: ')
        self._Lab1Entry = tk.Entry(
            master = self._root_window, width = 10,
            textvariable = tk.StringVar())
        self._Dis1Label = tk.Label(
            master = self._root_window, text = 'Dis 1: ')
        self._Dis1Entry = tk.Entry(
            master = self._root_window, width = 10,
            textvariable = tk.StringVar())

        
        self._class1Label.grid(
            row = 6, column = 0, padx = (0, 10), pady = 3,
            sticky = tk.E)
        self._class1Entry.grid(
            row = 6, column = 1, pady = 3,
            sticky = tk.W)
        self._Lab1Label.grid(
            row = 6, column = 2, padx = (0, 10), pady = 3,
            sticky = tk.E)
        self._Lab1Entry.grid(
            row = 6, column = 3, pady = 3,
            stick = tk.W)
        self._Dis1Label.grid(
            row = 6, column = 4, padx = (0, 10), pady = 3,
            sticky = tk.E)
        self._Dis1Entry.grid(
            row = 6, column = 5, padx = (0, 10), pady = 3,
            stick = tk.W) 


## Class 2
        self._class2Label = tk.Label(
            master = self._root_window, text = 'Lecture 2: ')
        self._class2Entry = tk.Entry(
            master = self._root_window, width = 10,
            textvariable = tk.StringVar())
        self._Lab2Label = tk.Label(
            master = self._root_window, text = 'Lab 2: ')
        self._Lab2Entry = tk.Entry(
            master = self._root_window, width = 10,
            textvariable = tk.StringVar())
        self._Dis2Label = tk.Label(
            master = self._root_window, text = 'Dis 2: ')
        self._Dis2Entry = tk.Entry(
            master = self._root_window, width = 10,
            textvariable = tk.StringVar())

        
        self._class2Label.grid(
            row = 7, column = 0, padx = (0, 10), pady = 3,
            sticky = tk.E)
        self._class2Entry.grid(
            row = 7, column = 1, pady = 3,
            sticky = tk.W)
        self._Lab2Label.grid(
            row = 7, column = 2, padx = (0, 10), pady = 3,
            sticky = tk.E)
        self._Lab2Entry.grid(
            row = 7, column = 3, pady = 3,
            stick = tk.W)
        self._Dis2Label.grid(
            row = 7, column = 4, padx = (0, 10), pady = 3,
            sticky = tk.E)
        self._Dis2Entry.grid(
            row = 7, column = 5, pady = 3,
            stick = tk.W) 


## Class 3
        self._class3Label = tk.Label(
            master = self._root_window, text = 'Lecture 3: ')
        self._class3Entry = tk.Entry(
            master = self._root_window, width = 10,
            textvariable = tk.StringVar())
        self._Lab3Label = tk.Label(
            master = self._root_window, text = 'Lab 3: ')
        self._Lab3Entry = tk.Entry(
            master = self._root_window, width = 10,
            textvariable = tk.StringVar())
        self._Dis3Label = tk.Label(
            master = self._root_window, text = 'Dis 3: ')
        self._Dis3Entry = tk.Entry(
            master = self._root_window, width = 10,
            textvariable = tk.StringVar())

        
        self._class3Label.grid(
            row = 8, column = 0, padx = (0, 10), pady = 3,
            sticky = tk.E)
        self._class3Entry.grid(
            row = 8, column = 1, pady = 3,
            sticky = tk.W)
        self._Lab3Label.grid(
            row = 8, column = 2, padx = (0, 10), pady = 3,
            sticky = tk.E)
        self._Lab3Entry.grid(
            row = 8, column = 3, pady = 3,
            stick = tk.W)
        self._Dis3Label.grid(
            row = 8, column = 4, padx = (0, 10), pady = 3,
            sticky = tk.E)
        self._Dis3Entry.grid(
            row = 8, column = 5, pady = 3,
            stick = tk.W) 


## Class 4
        self._class4Label = tk.Label(
            master = self._root_window, text = 'Lecture 4: ')
        self._class4Entry = tk.Entry(
            master = self._root_window, width = 10,
            textvariable = tk.StringVar())
        self._Lab4Label = tk.Label(
            master = self._root_window, text = 'Lab 4: ')
        self._Lab4Entry = tk.Entry(
            master = self._root_window, width = 10,
            textvariable = tk.StringVar())
        self._Dis4Label = tk.Label(
            master = self._root_window, text = 'Dis 4: ')
        self._Dis4Entry = tk.Entry(
            master = self._root_window, width = 10,
            textvariable = tk.StringVar())

        
        self._class4Label.grid(
            row = 9, column = 0, padx = (0, 10), pady = 3,
            sticky = tk.E)
        self._class4Entry.grid(
            row = 9, column = 1, pady = 3,
            sticky = tk.W)
        self._Lab4Label.grid(
            row = 9, column = 2, padx = (0, 10), pady = 3,
            sticky = tk.E)
        self._Lab4Entry.grid(
            row = 9, column = 3, pady = 3,
            stick = tk.W)
        self._Dis4Label.grid(
            row = 9, column = 4, padx = (0, 10), pady = 3,
            sticky = tk.E)
        self._Dis4Entry.grid(
            row = 9, column = 5, pady = 3,
            stick = tk.W) 

## Class 5
        self._class5Label = tk.Label(
            master = self._root_window, text = 'Lecture 5: ')
        self._class5Entry = tk.Entry(
            master = self._root_window, width = 10,
            textvariable = tk.StringVar())
        self._Lab5Label = tk.Label(
            master = self._root_window, text = 'Lab 5: ')
        self._Lab5Entry = tk.Entry(
            master = self._root_window, width = 10,
            textvariable = tk.StringVar())
        self._Dis5Label = tk.Label(
            master = self._root_window, text = 'Dis 5: ')
        self._Dis5Entry = tk.Entry(
            master = self._root_window, width = 10,
            textvariable = tk.StringVar())

        
        self._class5Label.grid(
            row = 10, column = 0, padx = (0, 10), pady = 3,
            sticky = tk.E)
        self._class5Entry.grid(
            row = 10, column = 1, pady = 3,
            sticky = tk.W)
        self._Lab5Label.grid(
            row = 10, column = 2, padx = (0, 10), pady = 3,
            sticky = tk.E)
        self._Lab5Entry.grid(
            row = 10, column = 3, pady = 3,
            stick = tk.W)
        self._Dis5Label.grid(
            row = 10, column = 4, padx = (0, 10), pady = 3,
            sticky = tk.E)
        self._Dis5Entry.grid(
            row = 10, column = 5, pady = 3,
            stick = tk.W) 

## Class 6
        self._class6Label = tk.Label(
            master = self._root_window, text = 'Lecture 6: ')
        self._class6Entry = tk.Entry(
            master = self._root_window, width = 10,
            textvariable = tk.StringVar())
        self._Lab6Label = tk.Label(
            master = self._root_window, text = 'Lab 6: ')
        self._Lab6Entry = tk.Entry(
            master = self._root_window, width = 10,
            textvariable = tk.StringVar())
        self._Dis6Label = tk.Label(
            master = self._root_window, text = 'Dis 6: ')
        self._Dis6Entry = tk.Entry(
            master = self._root_window, width = 10,
            textvariable = tk.StringVar())

        
        self._class6Label.grid(
            row = 11, column = 0, padx = (0, 10), pady = 3,
            sticky = tk.E)
        self._class6Entry.grid(
            row = 11, column = 1, pady = 3,
            sticky = tk.W)
        self._Lab6Label.grid(
            row = 11, column = 2, padx = (0, 10), pady = 3,
            sticky = tk.E)
        self._Lab6Entry.grid(
            row = 11, column = 3, pady = 3,
            stick = tk.W)
        self._Dis6Label.grid(
            row = 11, column = 4, padx = (0, 10), pady = 3,
            sticky = tk.E)
        self._Dis6Entry.grid(
            row = 11, column = 5, pady = 3,
            stick = tk.W) 


## Alternate Classes Banner

        self._alternateL = tk.Label(
            master = self._root_window, text = 'Alternate Classes',
            font = ('Helvetica', 20))

        self._alternateL.grid(
            row = 12, columnspan = 6)


##Alternate Class Labels
        
        self._aClassLabel = tk.Label(
            master = self._root_window, text = 'Lecture')
        self._aLabLabel = tk.Label(
            master = self._root_window, text = 'Lab')
        self._aDisLabel = tk.Label(
            master = self._root_window, text = 'Dis')

        self._aClassLabel.grid(
            row = 13, column = 0, columnspan = 2)
        self._aLabLabel.grid(
            row = 13, column = 2, columnspan = 2)
        self._aDisLabel.grid(
            row = 13, column = 4, columnspan = 2)

##Alternate Class Codes
        self.aClassCodesStr = tk.StringVar()
        self.aLabCodesStr = tk.StringVar()
        self.aDisCodesStr = tk.StringVar()
        self.aClassCodeNumsStr = tk.StringVar()

        self.aClassCodesStr.set('\n')
        self.aLabCodesStr.set('\n')
        self.aDisCodesStr.set('\n')

        self._aClassCodes = tk.Label(
            master = self._root_window, textvariable = self.aClassCodesStr)
        self._aLabCodes = tk.Label(
            master = self._root_window, textvariable = self.aLabCodesStr)
        self._aDisCodes = tk.Label(
            master = self._root_window, textvariable = self.aDisCodesStr)
        self._aClassCodeNums = tk.Label(
            master = self._root_window, textvariable = self.aClassCodeNumsStr)


        self._aClassCodeNums.grid(
            row = 14, column = 0)
        self._aClassCodes.grid(
            row = 14, column = 0, columnspan = 2)
        self._aLabCodes.grid(
            row = 14, column = 2, columnspan = 2)
        self._aDisCodes.grid(
            row = 14, column = 4, columnspan = 2)

        self.alectures = []
        self.alab = []
        self.adis = []

        def update_code_nums():
            '''Updates the alternate class code index numbers'''
            if len(self.alectures) == 0:
                self.aClassCodeNumsStr.set('')
            elif len(self.alectures) == 1:
                self.aClassCodeNumsStr.set('1')
            else:
                self.aClassCodeNumsStr.set(('\n'.join([str(i) for i in range(1, len(self.alectures) + 1)])))
            
##Add Alternate Class Button

        def plus_pressed():
            addmenu = tk.Toplevel()
            lecturel = tk.Label(
                master = addmenu, text = 'Lecture: ')
            lecturee = tk.Entry(
                master = addmenu, width = 10,
                textvariable = tk.StringVar())

            labl = tk.Label(
                master = addmenu, text = 'Lab: ')
            labe = tk.Entry(
                master = addmenu, width = 10,
                textvariable = tk.StringVar())

            disl = tk.Label(
                master = addmenu, text = 'Dis: ')
            dise = tk.Entry(
                master = addmenu, width = 10,
                textvariable = tk.StringVar())


            lecturel.grid(row = 0, column = 0, padx = 5)
            lecturee.grid(row = 0, column = 1, padx = 5)
            labl.grid(row = 0, column = 2, padx = 5)
            labe.grid(row = 0, column = 3, padx = 5)
            disl.grid(row = 0, column = 4, padx = 5)
            dise.grid(row = 0, column = 5, padx = 5)

            def add_pressed():
                self.alectures.append(lecturee.get())
                self.aClassCodesStr.set(self.aClassCodesStr.get() + lecturee.get() + '\n')
                self.alab.append(labe.get())
                self.aLabCodesStr.set(self.aLabCodesStr.get() + labe.get() + '\n')
                self.adis.append(dise.get())
                self.aDisCodesStr.set(self.aDisCodesStr.get() + dise.get() + '\n')
                update_code_nums()
                addmenu.destroy()

            addbutton = tk.Button(
                master = addmenu, text = 'Add',
                command = add_pressed)
            addbutton.grid(row = 0, column = 6, padx = 5)
                    
        self.plusButton = tk.Button(
            master = self._root_window, text = ' + ',
            command = plus_pressed)

        self.plusButton.grid(row = 13, column = 0,
                            padx = (5, 0), sticky = tk.W)

##Remove Alternate Class Button
        def minus_pressed():
            minusmenu = tk.Toplevel()
            instructions = tk.Label(
                master = minusmenu, text = 'Which number class should be removed')
            minuse = tk.Entry(
                master = minusmenu, width = 10,
                textvariable = tk.StringVar())

            instructions.grid(row = 0, column = 0, padx = 3)
            minuse.grid(row = 1, column = 0, pady = 2)

            def remove_pressed():
                class_index = minuse.get()
                if class_index.isdigit():
                    class_index = int(class_index) - 1
                    if len(self.alectures) >= (class_index + 1) and class_index + 1 > 0:
                        self.alectures.pop(class_index)
                        self.alab.pop(class_index)
                        self.adis.pop(class_index)

                        
                        for aCodeStr in [self.aClassCodesStr, self.aLabCodesStr, self.aDisCodesStr]:
                            temp = aCodeStr.get().split('\n')
                            temp.pop(class_index + 1)
                            aCodeStr.set('\n'.join(temp))
                        update_code_nums()

                minusmenu.destroy()


            removeButton = tk.Button(
                master = minusmenu, text = 'Remove',
                command = remove_pressed)

            removeButton.grid(row = 2, pady = (0, 2))

        self.minusButton = tk.Button(
            master = self._root_window, text = ' - ',
            command = minus_pressed)

        self.minusButton.grid(row = 13, column = 5,
                              padx = (0, 5), sticky = tk.E)


## Submit Button
        def submit_pressed() -> None:
            '''Checks that all the values input are valid and then saves them'''
            rtime_re = '^((Jan)|(Feb)|(Mar)|(Apr)|(May)|(Jun)|(Jul)|(Aug)|(Sep)|(Oct)|(Nov)|(Dec)) [0-9]{1,2} [0-9]{4} [0-9]{1,2}:[0-9]{1,2}((PM)|(AM))$'
            c_re = re.compile('[0-9]{5}')

            self.login = self._login_entry.get()                
            self.passw = self._password_entry.get()
            self.rtime = self._registration_entry.get()
            
            self.c1 = [self._Lab1Entry.get(), self._Dis1Entry.get(), self._class1Entry.get()]
            self.c2 = [self._Lab2Entry.get(), self._Dis2Entry.get(), self._class2Entry.get()]
            self.c3 = [self._Lab3Entry.get(), self._Dis3Entry.get(), self._class3Entry.get()]
            self.c4 = [self._Lab4Entry.get(), self._Dis4Entry.get(), self._class4Entry.get()]
            self.c5 = [self._Lab5Entry.get(), self._Dis5Entry.get(), self._class5Entry.get()]
            
            self.classes = (self.c1, self.c2, self.c3, self.c4, self.c5)
            self.aclasses = list(zip(self.alectures, self.alab, self.adis))

            incorrect_fields = []

            if self.login not in _get_verified_set():
                messagebox.showwarning('ID Not found', 'Your ID has not been authenticated. Please contact mkharaev@uci.edu')
            
            else:
                if re.match(rtime_re, self.rtime) == None:
                    incorrect_fields.append('Registration Time')
                for i in range(4):
                    for code in self.classes[i]:
                        if code != '' and c_re.fullmatch(code) == None:
                            incorrect_fields.append('Class {}'.format(i + 1))
                for i in range(len(self.aclasses)):
                    for acode in self.aclasses[i]:
                        if acode != '' and c_re.fullmatch(acode) == None:
                            incorrect_fields.append('Alternate Class {}'.format(i + 1))
                            break

                if incorrect_fields == []:
                    if self.confirm():
                        self.submit_pressed = True
                        self._root_window.destroy()
                        
                else:
                    messagebox.showwarning('Fields Invalid', 'These fields have invald values.\n{}'.format(', '.join(incorrect_fields)))
                    incorrect_fields = []

        self._submit = tk.Button(
            master = self._root_window, text = 'Submit', font = ('Arial', 15),
            command = submit_pressed)
        self._submit.grid(
            row = 15, pady = 10, columnspan = 6)

    def run(self) -> None:
        self._root_window.mainloop()

    def get_values(self):
        '''Returns all the values that were input to the bot'''
        return self.submit_pressed,\
               self.login,\
               self.passw,\
               self.rtime,\
               self.classes,\
               self.aclasses

    def confirm(self) -> str:
        '''Creates a messagebox that asks the user to confirm the information they input into the bot'''
        confirm_message = '''Is this information correct?

Login: {}
Password: {}

Registration Time: {}


Classes: '''.format(self.login, self.passw, self.rtime)

        for c in self.classes:
            for code in c:
                if code != '':
                    confirm_message += (code + ' ')

        confirm_message += '\n\nAlternate Classes: '

        for ac in self.aclasses:
            for code in ac:
                if code != '':
                    confirm_message += (code + ' ')

        return messagebox.askyesno('Confirm', confirm_message)


