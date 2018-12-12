# Jacob Meadows
# Computer Programming, 6th Period
# 12 December 2018
"""
Final-Review.py

Employees,
I need a quick program to help me with keeping track of worker's time. I need it to have a last name/last name entry,
a spinny box thing that has the date (month, day, year), and something that says what time it is. The user then needs
to have a 'Clock in' button, and a 'Clock out' button. Clock in should be the only clickable one to start with, and
then once they click that the 'Clock out' button should only be available. Of course I would like this data written to
a file so I can see who is clocking in/out and when.

Copyright (C) 2018 Jacob Meadows

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
import tkinter as tk


class App(tk.Frame):
    def __init__(self, master):
        self.master = master
        self.master.title("Final Review")
        super().__init__(self.master)
        self.place(x=0, y=0, relwidth=1, relheight=1)

        self.widgets = dict()
        self.vars = dict()

        self.vars["first_name_variable"] = tk.StringVar()
        self.widgets["first_name_label"] = tk.Label(self, text="First Name:")
        self.widgets["first_name_entry"] = tk.Entry(self, textvariable=self.vars["first_name_variable"])

        self.vars["last_name_variable"] = tk.StringVar()
        self.widgets["last_name_label"] = tk.Label(self, text="Last Name:")
        self.widgets["last_name_entry"] = tk.Entry(self, textvariable=self.vars["last_name_variable"])

        self.vars["months"] = {"January", "February", "March", "April", "May", "June", "July", "August", "September",
                               "October", "November", "December"}
        self.widgets["date_spinbox"] = tk.Spinbox(self)


if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()
