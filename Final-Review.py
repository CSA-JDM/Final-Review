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

        self.vars["months_names"] = [
            "January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
            "November", "December"
        ]
        self.vars["dates"] = dict()
        for year in range(2000, 3001):
            self.vars["dates"][year] = dict()
            for month in range(len(self.vars["months_names"])):
                if ((month % 2 == 1 and month < 6) or (month % 2 == 0 and month > 6)) and month != 1:
                    self.vars["dates"][year][self.vars["months_names"][month]] = 31
                elif (month % 2 == 0 and month < 6) or month >= 6:
                    self.vars["dates"][year][self.vars["months_names"][month]] = 32
                else:
                    if year % 4 == 0 and (year % 100 != 0 or (year % 100 == 0 and year % 400 == 0)):
                        self.vars["dates"][year][self.vars["months_names"][month]] = 30
                    else:
                        self.vars["dates"][year][self.vars["months_names"][month]] = 29
        self.widgets["date_label"] = tk.Label(self, text="Date (d/m/y):")
        self.widgets["date_label"].place(x=0, y=0)
        self.widgets["day_spinbox"] = tk.Spinbox(
            self, values=list(range(1, list(self.vars["dates"].values())[0]["January"])), width=2
        )
        self.widgets["day_spinbox"].place(x=80, y=0)
        self.widgets["month_spinbox"] = tk.Spinbox(
            self, values=list(list(self.vars["dates"].values())[0].keys()), width=10
        )
        self.widgets["month_spinbox"].place(x=110, y=0)
        self.widgets["year_spinbox"] = tk.Spinbox(self, values=list(self.vars["dates"].keys()), width=5)
        self.widgets["year_spinbox"].place(x=190, y=0)

        self.after(1, self.widgetloop)

    def widgetloop(self):
        if len(self.widgets["day_spinbox"].cget("values").split()) + 1 != \
                self.vars["dates"][int(self.widgets["year_spinbox"].get())][self.widgets["month_spinbox"].get()]:
            self.widgets["day_spinbox"].config(
                values=list(range(
                    1, self.vars["dates"][int(self.widgets["year_spinbox"].get())][self.widgets["month_spinbox"].get()]
                ))
            )
        self.after(1, self.widgetloop)


if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()
