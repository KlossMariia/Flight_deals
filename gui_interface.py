from tkinter import *
from flight_data import FlightData
from flight_search import FlightSearch
from datetime import datetime

# creating programs interface


class GuiInterface:
    def __init__(self):
        self.city_from = ""
        self.city_to = ""
        self.date = ""
        self.stops_number = 0

        self.window = Tk()
        self.window.geometry("400x430")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg="#FFFFFF",
            height=600,
            width=400,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)
        self.canvas.create_text(
            46.0,
            238.0,
            anchor="nw",
            text="Date of the flight:",
            fill="#000000",
            font=("HappyMonkey Regular", 20 * -1)
        )

        self.canvas.create_text(
            270.0,
            105.0,
            anchor="nw",
            text="To",
            fill="#000000",
            font=("HappyMonkey Regular", 20 * -1)
        )

        self.canvas.create_text(
            69.0,
            106.0,
            anchor="nw",
            text="From",
            fill="#000000",
            font=("HappyMonkey Regular", 20 * -1)
        )

        self.canvas.create_text(
            46.0,
            305.0,
            anchor="nw",
            text="Max stops number:",
            fill="#000000",
            font=("HappyMonkey Regular", 20 * -1)
        )

        self.canvas.create_rectangle(
            192.0,
            90.78218078613281,
            194.0,
            189.089111328125,
            fill="#000000",
            outline="")

        self.canvas.create_rectangle(
            0.0,
            200.0,
            400.0,
            217.0,
            fill="#779CE4",
            outline="")

        self.heading_image = PhotoImage(
            file="imgs/image_1.png")
        self.image_1 = self.canvas.create_image(
            200.0,
            42.0,
            image=self.heading_image
        )

        self.entry_image = PhotoImage(
            file="imgs/entry.png")
        self._city_to_entry_bg = self.canvas.create_image(
            288.0,
            159.0,
            image=self.entry_image
        )
        self.city_to_entry = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
        )

        self.city_to_entry.place(
            x=234.0,
            y=145.0,
            width=108.0,
            height=30.0
        )

        city_from_entry_bg = self.canvas.create_image(
            288.0,
            250.5,
            image=self.entry_image
        )
        self.date_entry = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.date_entry.place(
            x=234.0,
            y=235.0,
            width=108.0,
            height=30.0
        )

        # getting today's date for writing one to data entry
        today = datetime.now()
        today_formatted = today.strftime("%d/%m/%Y")

        self.date_entry.insert(0, today_formatted)

        self.city_from_entry_bg = self.canvas.create_image(
            100.0,
            159.0,
            image=self.entry_image
        )
        self.city_from_entry = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )

        self.city_from_entry.place(
            x=46.0,
            y=143.0,
            width=108.0,
            height=30.0
        )

        stops_entry_bg = self.canvas.create_image(
            288.0,
            315.5,
            image=self.entry_image
        )
        self.stops_entry = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.stops_entry.place(
            x=234.0,
            y=300.0,
            width=108.0,
            height=30.0
        )

        self.stops_entry.insert(0, "0")

        self.button_image_1 = PhotoImage(
            file="imgs/button_1.png")
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command= self.get_values,
            relief="flat"
        )
        self.button_1.place(
            x=138.0,
            y=365.0,
            width=124.0,
            height=37.0
        )

        self.window.mainloop()

    # This function gets iata codes and sends them for flights data searching
    def run_the_code(self):
        iata_codes = FlightData(self.city_from, self.city_to).iata_codes
        FlightSearch(iata_codes, self.date, self.stops_number)

    # this function gets all needed values
    def get_values(self):
        global city_from, city_to, date
        self.city_from = self.city_from_entry.get()
        self.city_to = self.city_to_entry.get()
        self.date = self.date_entry.get()
        self.stops_number = int(self.stops_entry.get())
        self.run_the_code()
