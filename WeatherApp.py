import tkinter as tk
import requests

# GUI
root = tk.Tk()
root.title("Weather App By Neksha/Soleous")
root.geometry("400x400")

# Labels
city_label = tk.Label(root, text="City: ")
city_label.pack()

temperature_label = tk.Label(root, text="Temperature: ")
temperature_label.pack()

description_label = tk.Label(root, text="Description: ")
description_label.pack()

# Entry
city_entry = tk.Entry(root)
city_entry.pack()

# Button
def get_weather():
    city = city_entry.get()
    url = f"https://wttr.in/{city}?format=%C\n%t\n%T"
    response = requests.get(url).text.strip().split('\n')

    description, temperature, feels_like = response

    temperature_label.config(text=f"Temperature: {temperature}")
    description_label.config(text=f"Description: {description}")

button = tk.Button(root, text="Get Weather", command=get_weather)
button.pack()

root.mainloop()
