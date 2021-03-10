# Documentation:
# https://docs.opencv.org/master/d6/d00/tutorial_py_root.html
# http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter

# Install OpenCV in order for the imports to work properly,
# open the terminal on your machine and run the command:
# Mac / Linux users: pip3 install opencv-python
# Windows users: pip install opencv-python
# or hover over the red underlined import and select "install opencv"

# Import Modules:

import cv2
import numpy as np
import tkinter as tk

time = 3000 # should be 3000

# Create object
splash_root = tk.Tk()

# Removes Toolbar from Splash Screen
splash_root.overrideredirect(1)
splash_root.overrideredirect(0)

# Removes Option to Close out of Loading Screen
splash_root.overrideredirect(True)

# Adjust size & Centers Splash Screen
splash_root_width = 640
splash_root_height = 400

sw = splash_root.winfo_screenwidth()
sh = splash_root.winfo_screenheight()

x = (sw/2)-(splash_root_width/2)
y = (sh/2)-(splash_root_height/2)

splash_root.geometry(f'{splash_root_width}x{splash_root_height}+{int(x)}+{int(y)}')
splash_root.resizable(False, False)

# Splash screen canvas & image
splash_screen_canvas = tk.Canvas(splash_root, highlightthickness=0, width = splash_root_width, height = splash_root_height)
splash_screen_img = tk.PhotoImage(file = "assets/splash_screen.png")
splash_screen_canvas.create_image(0,0, anchor = 'nw', image = splash_screen_img)
splash_screen_canvas.pack()

# main window function
def main():
    # destory splash window
    splash_root.destroy()

    # Execute tkinter
    root = tk.Tk()

    # Adjust size
    root_width = root.winfo_screenwidth()
    root_height = root.winfo_screenheight()

    root.geometry("%dx%d" % (root_width, root_height))
    root.resizable(True, True)

    # Properties
    root.title("Oracle of Delphi")

    # Main Canvas
    main_frame = tk.Frame(root, bg="grey", highlightthickness=1, highlightbackground="blue", width=root_width, height=root_height)

    main_frame.pack(expand = True, fill = 'both')

    # Test Button (Thanks John :D! )
    button = tk.Button(main_frame, background='#DEEBF7', activebackground='#DEEBF7', text="Button", width=9,border=0, font=("Helvetica 13 italic"))
    button.pack() # pack literally packs the object somewhere in the box, top, left, right etc
    button.place(relx=0.5, rely=0.5, anchor='center') # place lets you give absolute coordinates


# Set Interval
splash_root.after(time, main)

# Execute tkinter
tk.mainloop()

#Created Button Above Background Image
#entry = tk.Button(root, text="Begin")
#entry.pack()


############################################################################################################


# Loads Image (stored in the "img" variable)
#img = cv2.imread('assets/alphabet.png', -1)
#face_img = cv2.imread('assets/face.png', -1)

# Resize Image (To 25% of its original size)
#img = cv2.resize(img, (0,0), fx=0.25, fy=0.25)

# Write an image (filename, source)
# cv2.imwrite("new_img", img)

# Displays Image
#cv2.imshow(windowName,img)

# Waits an infinite amount of time for a key press
# Once the user presses any key on the keyboard
# all the displayed images will be destroyed / closed
#cv2.waitKey(0)
#cv2.destroyAllWindows()