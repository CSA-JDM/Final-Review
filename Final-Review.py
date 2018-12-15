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
import time


class App(tk.Frame):
    def __init__(self, master):
        self.master = master
        self.master.config(width=250, height=150)
        self.master.title("Final Review")
        super().__init__(self.master, width=250, height=150)
        self.place(x=0, y=0, relwidth=1, relheight=1)

        self.widgets = dict()
        self.vars = dict()

        self.vars["first_name_variable"] = tk.StringVar()
        self.widgets["first_name_label"] = tk.Label(self, text="First Name:")
        self.widgets["first_name_label"].place(x=0, y=0)
        self.widgets["first_name_entry"] = tk.Entry(self, textvariable=self.vars["first_name_variable"], width=25)
        self.widgets["first_name_entry"].place(x=80, y=0)

        self.vars["last_name_variable"] = tk.StringVar()
        self.widgets["last_name_label"] = tk.Label(self, text="Last Name:")
        self.widgets["last_name_label"].place(x=0, y=30)
        self.widgets["last_name_entry"] = tk.Entry(self, textvariable=self.vars["last_name_variable"], width=25)
        self.widgets["last_name_entry"].place(x=80, y=30)

        self.vars["dates"] = dict()
        for year in range(2000, 3001):
            if year % 4 == 0 and (year % 100 != 0 or (year % 100 == 0 and year % 400 == 0)):
                self.vars["dates"][year] = {
                    'January': 32, 'February': 30, 'March': 32, 'April': 31, 'May': 32, 'June': 31, 'July': 32,
                    'August': 32, 'September': 31, 'October': 32, 'November': 31, 'December': 32
                }
            else:
                self.vars["dates"][year] = {
                    'January': 32, 'February': 29, 'March': 32, 'April': 31, 'May': 32, 'June': 31, 'July': 32,
                    'August': 32, 'September': 31, 'October': 32, 'November': 31, 'December': 32
                }
        self.widgets["date_label"] = tk.Label(self, text="Date (d/m/y):")
        self.widgets["date_label"].place(x=0, y=60)
        self.widgets["month_spinbox"] = tk.Spinbox(
            self, values=list(list(self.vars["dates"].values())[0].keys()), width=10
        )
        self.widgets["month_spinbox"].place(x=80, y=60)
        self.widgets["day_spinbox"] = tk.Spinbox(
            self, values=list(range(1, list(self.vars["dates"].values())[0]["January"])), width=2
        )
        self.widgets["day_spinbox"].place(x=160, y=60)
        self.widgets["year_spinbox"] = tk.Spinbox(self, values=list(self.vars["dates"].keys()), width=5)
        self.widgets["year_spinbox"].place(x=190, y=60)

        self.widgets["time_message"] = tk.Message(self, text=time.asctime(), justify="center")
        self.widgets["time_message"].place(x=0, y=90)

        self.widgets["clock_in_button"] = tk.Button(self, text="Clock in", command=self.clock_in_and_out_command,
                                                    state="disabled")
        self.widgets["clock_in_button"].place(x=90, y=90)

        self.widgets["clock_out_button"] = tk.Button(self, text="Clock out", command=self.clock_in_and_out_command,
                                                     state="disabled")
        self.widgets["clock_out_button"].place(x=160, y=90)

        self.after(1, self.widgetloop)

    def clock_in_and_out_command(self):
        try:
            final_review_file_txt = open("final_review_file.txt", "r")
            final_review_file = final_review_file_txt.read()
            final_review_file_txt.close()
        except FileNotFoundError:
            open("final_review_file.txt", "w").close()
            final_review_file = ""
        final_review_file_txt = open("final_review_file.txt", "w")
        if self.widgets["clock_out_button"].cget("state") == "disabled":
            self.widgets["clock_out_button"].config(state="normal")
            final_review_file_txt.write(final_review_file +
                                        "First Name: " + self.widgets["first_name_entry"].get().strip() +
                                        " Last Name: " + self.widgets["last_name_entry"].get().strip() +
                                        " Clocked in at: " + self.widgets["time_message"].cget("text") + "\n")
        elif self.widgets["clock_out_button"].cget("state") == "normal":
            self.widgets["clock_out_button"].config(state="disabled")
            final_review_file_txt.write(final_review_file +
                                        "First Name: " + self.widgets["first_name_entry"].get().strip() +
                                        " Last Name: " + self.widgets["last_name_entry"].get().strip() +
                                        " Clocked out at: " + self.widgets["time_message"].cget("text") + "\n")
        final_review_file_txt.close()

    def widgetloop(self):
        if len(self.widgets["day_spinbox"].cget("values").split()) + 1 != \
                self.vars["dates"][int(self.widgets["year_spinbox"].get())][self.widgets["month_spinbox"].get()]:
            text = self.widgets["day_spinbox"].get()
            self.widgets["day_spinbox"].config(
                values=list(range(
                    1, self.vars["dates"][int(self.widgets["year_spinbox"].get())][self.widgets["month_spinbox"].get()]
                ))
            )
            self.widgets["day_spinbox"].delete(0, tk.END)
            while text not in self.widgets["day_spinbox"].cget("values"):
                text = str(int(text) - 1)
            self.widgets["day_spinbox"].insert(0, text)
        if self.widgets["time_message"].cget("text") != time.asctime():
            self.widgets["time_message"].config(text=time.asctime())
        if self.widgets["clock_out_button"].cget("state") == "disabled" and \
            self.widgets["first_name_entry"].get().strip() != "" and \
                self.widgets["last_name_entry"].get().strip() != "":
            self.widgets["clock_in_button"].config(state="normal")
        else:
            self.widgets["clock_in_button"].config(state="disabled")
        self.after(1, self.widgetloop)


if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()
