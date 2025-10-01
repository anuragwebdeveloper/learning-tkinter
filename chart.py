import tkinter as tk

window = tk.Tk()
window.geometry("1280x720")
window.title("Nested Frames Example")

top_frame = tk.Frame(window, bg="lightblue", height=100)
top_frame.pack(fill="x")

label1 = tk.Label(top_frame, text="I am in the TOP frame", bg="blue", fg="white")
label1.pack(pady=10)

window.mainloop()
