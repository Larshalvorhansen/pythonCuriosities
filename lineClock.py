import tkinter as tk
import math

def update_clock():
    # Get the time from sliders
    hours = hour_slider.get()
    minutes = minute_slider.get()
    #seconds = second_slider.get()

    # Calculate the angles for clock hands
    hour_angle = 360 * (hours % 12) / 12 + 360 * (minutes / 60) / 12
    minute_angle = 360 * minutes / 60
    #second_angle = 360 * seconds / 60

    # Clear the canvas
    canvas.delete("all")

    # Draw clock face
    canvas.create_oval(199, 199, 201, 201)
    canvas.create_text(200, 30, text=f"{hours:02d}:{minutes:02d}", font=("Helvetica", 12))

    # Draw clock hands
    draw_hand(hour_angle, 60, "blue")
    draw_hand(minute_angle, 90, "green")
    #draw_hand(second_angle, 90, "red")

    # Calculate the endpoint coordinates of the hour and minute hands
    hour_x = 200 + 60 * math.sin(math.radians(hour_angle))
    hour_y = 200 - 60 * math.cos(math.radians(hour_angle))
    minute_x = 200 + 90 * math.sin(math.radians(minute_angle))
    minute_y = 200 - 90 * math.cos(math.radians(minute_angle))

    # Draw the hour hand
    #canvas.create_line(200, 200, hour_x, hour_y, fill="blue", width=3)

    # Draw the minute hand
    #canvas.create_line(200, 200, minute_x, minute_y, fill="green", width=3)

    # Draw a line between the hour and minute hands
    canvas.create_line(hour_x, hour_y, minute_x, minute_y, fill="white", width=2)

    # Update every 1000 ms (1 second)
    root.after(1000, update_clock)

def draw_hand(angle, length, color):
    x = 200 + length * math.sin(math.radians(angle))
    y = 200 - length * math.cos(math.radians(angle))
    #canvas.create_line(200, 200, x, y, fill=color, width=3)

root = tk.Tk()
root.title("Lineclock by Lars Halvor")

hour_slider = tk.Scale(root, from_=0, to=24, label="Hours")
hour_slider.pack()
minute_slider = tk.Scale(root, from_=0, to=59, label="Minutes")
minute_slider.pack()
# second_slider = tk.Scale(root, from_=0, to=59, label="Seconds")
# second_slider.pack()

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

update_clock()

root.mainloop()

