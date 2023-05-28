from tkinter import *
from PIL import Image, ImageTk

root = Tk()


def add_photo():
    frame = Frame(root, width=600, height=400)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)
    # Create an object of the PIL ImageTk
    image1 = Image.open("cat.jpg")
    photo = ImageTk.PhotoImage(image1)
    # Create a Label widget to display the image
    label = Label(root, image=photo)
    label.image = photo
    label.pack()


def main():
    root.geometry("800x800")
    msg = Label(root, text="What's my favorite video", font=("Arial", 16, "bold"))
    msg.place(x=320, y=20)
    button = Button(root, text="Click to find out!", command=add_photo)
    button.place(x=320, y=80)
    root.mainloop()


if __name__ == '__main__':
    main()
