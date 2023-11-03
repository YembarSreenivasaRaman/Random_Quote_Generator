import tkinter as tk
import requests
from threading import Thread

api = "http://api.quotable.io/random"

quotes = []
quote_number = 0

# BOX
window = tk.Tk()
window.geometry("900x260")
window.title("Quote Generator")
window.grid_columnconfigure(0, weight=1)
window.resizable(False, False)
window.config(bg="white")


# PRE LOADING QUOTES
def preload_quote():
    global quotes

    print("***Loading more Quotes***")
    for x in range(10):
        random_quote = requests.get(api).json()
        content = random_quote["content"]
        author = random_quote["author"]
        quote = content + "  " + "By" + "  " + author
        print(quote)

        quotes.append(quote)
    print("***Finished Loading more quotes!***")


preload_quote()


# MAIN FUNTION
def get_random_quote():
    global quote_label
    global quotes
    global quote_number

    quote_label.configure(text=quotes[quote_number])
    quote_number = quote_number + 1
    print(quote_number)

    if quotes[quote_number] == quotes[-3]:
        thread = Thread(target=preload_quote)
        thread.start()


# UI
quote_label = tk.Label(window, text="click on the button to generate a random number!",
                       height=6,
                       pady=10,
                       wraplength=700,
                       font=("Helvetica", 14))
quote_label.grid(row=0, column=0, stick="WE", padx=20, pady=10)

# BUTTON
button = tk.Button(text='Generate', command=get_random_quote, bg='black', fg='blue',
                   activebackground='white', font=("Helvetica", 14))
button.grid(row=1, column=0, stick="WE", padx=10, pady=20)
button.grid_size()

# INFINITE LOOP
if __name__ == "__main__":
    window.mainloop()
