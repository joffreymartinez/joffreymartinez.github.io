#-------------------------------------------------------------------------------
# Name:        Prototype Survey 1
# Purpose:      Collection of data re Silk Road historic sites
#
# Author:      cmhmorden
#
# Created:     10/01/2020
# Copyright:   (c) cmhmorden 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# This prototype is to explore using a web interface to collect user data to be
# added to the Silk Road database for inclusion in the SR database.
# To match a basic web layout concept by Joffrey Martinez.
# Acknowledgement of some of the basic code template based on the materials from
# "Python GUI Development with Tkinter" course by Barron Stone offered on
# LinkedIn Learning.

# import Tkinter and modules to help build code. ttk is the Themed Tkinter module
# that helps will appearance across platforms, and messagebox will allow for
# creation of popup messages, such as when data successfully submitted.

from Tkinter import *
from Tkinter import ttk
from Tkinter import messagebox

# creating DataCollect class, so that code can be run as standalone or as
# triggered event through other programs.

class DataCollect:

    def __init__(self, master):

        # formating window to have meaningful label and nice colours
        master.title('Silk Road Historic Feature Data Collection')
        master.configure(background = '#00000')

        # add in some window-universal styling
        self.style = ttk.Style()
        self.style.configure('TFrame', background = '#7387ed')
        self.style.configure('TButton', background = '#7387ed')
        self.style.configure('TLabelFrame', background = '#7387ed', font=('Arial', 12))
        self.style.configure('TLabel', background = '#7387ed', font = ('Arial', 11))
        self.style.configure('Header.TLabel', font = ('Arial', 18, 'bold'))

        # creating header frame and using pack geometry master to place at
        # top of window. This frame thanks user for contributing data.
        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()

        ttk.Label(self.frame_header, text = "Thank you for sharing information about the Silk Road!",
         font = ('Arial', 14), background = '#7387ed').pack(pady=5)

        # creating a second frame in window - this time using the LabelFrame
        # constructor, so that the Location data being collected is made
        # distinct from other data types to avoid confusion about state (i.e.,
        # want location and not current status). Using pack geometry manager to
        # add frame under header.

        self.frame_loc = ttk.Labelframe(master, text="Location of Historic Feature")
        self.frame_loc.pack()

        # creating labels for each of the location inputs
        ttk.Label(self.frame_loc, text = "City:").grid(row = 0, column = 0, pady = 3, sticky = 'sw')
        ttk.Label(self.frame_loc, text = "State:").grid(row = 2, column = 0, pady = 3, sticky = 'sw')
        ttk.Label(self.frame_loc, text = "Country:").grid(row = 4, column = 0, pady = 3, sticky = 'sw')


        # creating Entry widgets for user input of location info
        self.entry_city = ttk.Entry(self.frame_loc, width = 50, font = ('Arial', 11))
        self.entry_state = ttk.Entry(self.frame_loc, width = 50, font = ('Arial', 11))
        self.entry_country = ttk.Entry(self.frame_loc, width = 50, font =('Arial', 11))

        # using grid geometry manager on entry widgets
        self.entry_city.grid(row = 1, column = 0)
        self.entry_state.grid(row = 3, column = 0)
        self.entry_country.grid(row = 5, column = 0)

        # creating another LabelFrame for Feature Detail section. Using pack
        # geometry mananger to add it under the Location frame.
        self.frame_details = ttk.Labelframe(master, text = "Feature Details")
        self.frame_details.pack()

        # creating Label widgets for each input
        ttk.Label(self.frame_details, text = "Name of Feature:").grid(row=0, column = 0, pady = 3, sticky = 'sw')
        ttk.Label(self.frame_details, text = "Type of Feature:").grid(row=2, column=0, pady = 3, sticky = 'sw')

        # creating widgets for feature details; name will be an Entry widget and
        # type will be a text widget to allow multi-line entry
        self.entry_name = ttk.Entry(self.frame_details, width = 60, font = ('Arial', 11))
        self.text_type = Text(self.frame_details, width = 60, height = 10, font = ('Arial', 11))

        # using grid geometry manager on feature detail widgets
        self.entry_name.grid(row = 1, column = 0)
        self.text_type.grid(row = 3, column = 0)


        # create buttons for Submit and Clear options. Submit sends data and
        # then the data is cleared from the fields ready for next entry. Clear
        # deletes all information from all fields.

        ttk.Button(self.frame_details, text = "Submit", command = self.submit).grid(row = 4, column = 0, pady=5)
        ttk.Button(self.frame_details, text = "Clear", command = self.clear).grid(row = 4, column = 1, pady=5)

    # create command events for Submit button. For now, Submit just prints the
    # data to the Python consule and then clears the fields ready for next entry.
    # In future, Submit will organize and save data into the Silk Road database.
    def submit(self):
        print('City: {}'.format(self.entry_city.get()))
        print('State: {}'.format(self.entry_state.get()))
        print('Country: {}'.format(self.entry_country.get()))
        print('Name: {}'.format(self.entry_name.get()))
        print('Type: {}'.format(self.text_type.get(1.0, 'end')))
        self.clear()
        messagebox.showinfo(title = "Silk Road Historic Feature Survey", message = "Data successfully submitted - thank you!")

    # create command events for Clear button - this option clears all data in all
    # fields
    def clear(self):
        self.entry_city.delete(0,'end')
        self.entry_state.delete(0,'end')
        self.entry_country.delete(0,'end')
        self.entry_name.delete(0,'end')
        self.text_type.delete(1.0,'end')



def main():
    root = Tk()
    datacollect = DataCollect(root)
    root.mainloop()

if __name__ == '__main__':
    main()
