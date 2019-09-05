from tkinter import *
from tkinter import messagebox
import os.path


class View:
    '''We create all necessary windows for user interaction.'''
    def __init__(self):
        self.view_sel = None
        # Tk window for user to select the view they want
        self.Menu = None
        # Tk window for user to input the title of series
        self.Selection = None
        # Tk window for user selection
        self.user_inp = ''
        # string of user's series title
        self.select = []
        # list of episodes that user selected
        self.view_1 = None

    def view_selection(self):
        '''Function that create Tk window for user to select the type
        of GUI that they want'''
        self.view_sel = Tk()

        Label(self.view_sel, text='Select your prefer type '
                                  'of GUI:').pack()

        Button(self.view_sel, text='GUI 1',
               command=self.gui_1).pack()
        Button(self.view_sel, text='GUI 2',
               command=self.gui_2).pack()
        # Button for GUI selection with will run the two function
        # down below

        self.view_sel.mainloop()

        return self.view_1

    def gui_1(self):
        self.view_1 = False
        self.view_sel.destroy()

    def gui_2(self):
        self.view_1 = True
        self.view_sel.destroy()

    def menu(self):
        '''Function create the Tk window for user to input their series
        title'''
        self.Menu = Tk()
        self.Menu.title('TV Show Search')
        message = Label(self.Menu, text='Enter the title of series:')
        self.user_inp = Entry(self.Menu)
        search_button = Button(self.Menu, text='Search', command=self.search)
        # Create button that run the function search() (function below) when
        # press

        message.grid(row=0, column=0)
        self.user_inp.grid(row=0, column=1)
        search_button.grid(row=1, column=0)
        # layout of Tk window

        self.Menu.mainloop()

        return self.user_inp
        # return user input title so control can pass it to model

    def search(self):
        '''Function for search button in Tk window menu'''
        self.user_inp = self.user_inp.get()
        self.Menu.destroy()

    def scrollbar(self, List_of_epi):
        '''Function create a Tk window for episodes selection'''
        self.Selection = Tk()

        scrollbar = Scrollbar(self.Selection)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.select = Listbox(self.Selection, selectmode=MULTIPLE,
                              yscrollcommand=scrollbar.set, width=70)
        # create a listbox for all episodes

        for i in List_of_epi:
            # put all the episodes that is found, which in a list
            # call List_of_epi, into the listbox
            string = 'Season: %s, Episodes: %s, Title: %s' \
                     % (i['Season'], i['Episodes'], i['Title'])
            self.select.insert(END, string)
            self.select.pack()

        scrollbar.config(command=self.select.yview)
        # display the listbox

        select = Button(self.Selection, text='Select',
                        command=self.select_choose)
        select.pack()
        # Create button that run the function select_choose()
        # (function below) when press

        self.Selection.mainloop()

        return self.select
        # return user selections so can be use by control for download

    def select_choose(self):
        '''Function for select button in Tk window Selection'''
        selection = self.select.curselection()
        self.select = [self.select.get(i) for i in selection]
        self.Selection.destroy()
        # storage all episodes that user select in listbox into a list in self
        # call select

    def error_NotFound(self):
        '''Display the error message for series that is not fount.'''
        window = Tk()
        window.withdraw()
        # To prevent Tk window show up when message box used
        messagebox.showinfo('Error', 'Title of input series is NOT IN '
                            'DATABASE or is TOO BROAD. PLEASE START the '
                            'PROGRAM AGAIN.')

    def view_download(self):
        '''This window takes the filename input and path input.'''
        self.Dwindow = Tk()
        label_1 = Label(self.Dwindow, text = 'Filename')
        label_1.grid(row = 1, column = 0)
        self.filename = Entry(self.Dwindow, width = 60)
        self.filename.grid(row = 1, column = 1)
        label_2 = Label(self.Dwindow, text = 'Path')
        label_2.grid(row = 2, column = 0)
        self.path = Entry(self.Dwindow, width = 60)
        self.path.grid(row = 2, column = 1)
        # When the user presses submit the path is generated and the get path
        # method is called
        s_button = Button(self.Dwindow, text='Submit'
                          ,command = self.get_path)
        s_button.grid(row = 3, column = 0)
        # The program stops when quit is pressed
        q_button = Button(self.Dwindow, text='Quit',
                          command = self.Dwindow.destroy)
        q_button.grid(row = 3, column = 1)
        self.Dwindow.mainloop()
        

        
    def get_path(self):
        '''This method generates the actual path needed for saving file.'''
        path = self.path.get()
        filename = self.filename.get()
        self.ac_path = os.path.join(str(path), str(filename)+'.csv')
        self.Dwindow.destroy()

    def error_view(self):
        '''This error window is generated when path is incorrect.'''
        self.Ewindow = Tk()
        label_1 = Label(self.Ewindow, text = 'The path is incorrect.'
                        ' Please Try Again')
        label_1.pack()
        # The try again button takes the user back to the fileinput window
        # through the controller
        button_t = Button(self.Ewindow, text = 'Try Again',
                          command = self.Ewindow.destroy)
        button_t.pack()
        self.Ewindow.mainloop()
        
        

if __name__ == '__main__':
    x = View()
    x.view_selection
