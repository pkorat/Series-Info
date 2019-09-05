import model
import view
import view2

class Control:
    '''This class acts as an interface between the model and the views.'''
    def __init__(self):
        self.model = model.Model()
        # call the model class in model
        self.view_1 = view.View()
        # call the View class in view

    def choose_gui(self):
        """Function to check user chosen GUI"""
        if self.view_1.view_selection():
            self.view_1 = view2.View()
        self.run()

    def run(self):
        '''A function to run the whole program'''
        try:
            # check if the user input title is in the data base
            self.model.user_search(self.view_1.menu())
        except model.NotFoundError:
            # else print out a error message for the user to input the title
            # again
            self.view_1.error_NotFound()
            return
        # expect input for download function
        # call the download function here, put the main function in model and
        # call it from here. Also put the GUI in view
        self.model.select_epi = self.view_1.scrollbar(self.model.List_of_epi)
        # We call the storage function in the model to get all info
        # about the episodes including plot
        self.model.storage()
        # After that we call the view for saving info to a file
        self.view_1.view_download()
        try:
            # We get the path for the saving info 
            path = self.view_1.ac_path
            if len(path)> 5:
                # We then try to save it
                u = self.model.save_file(path)
                while u != 1:
                    # If the path is not correct we raise the error window
                    # and we take the input again until we get the
                    # correct input
                    self.view_1.error_view()
                    self.view_1.view_download()
                    try:
                        path = self.view_1.ac_path
                        u = self.model.save_file(path)
                    except:
                        exit()
        except:
            exit()


if __name__ == '__main__':
    x = Control()
    x.choose_gui()
