from tkinter import *
import urllib.request
from PIL import Image,ImageDraw,ImageFont


def image():
    needed_image = image_entry.get()
    urllib.request.urlretrieve(
        needed_image,
        "image")

    img = Image.open("image")
    img_width, img_height = img.size
    draw = ImageDraw.Draw(img)
    font_size = int(img_width/10)
    font = ImageFont.truetype("arial.ttf",font_size)
    text = watermark_entry.get().title()
    draw.text((10, 20), text, font=font)



    img.show()





#---------------------------------------------------------------------------#

window = Tk()
window.title("Watermark App")
window.config(padx=50, pady=50, background="skyblue")

#---------------------------------------------------------------------------#

#Labels
image_label = Label(text="Please give your image address: ", bg= "skyblue")
image_label.grid(row=1, column=0)
watermark_label = Label(text= "Watermark to add:", bg="skyblue")
watermark_label.grid(row=2, column=0)
#---------------------------------------------------------------------------#
#Entry
image_entry = Entry(width=35)
image_entry.grid(row=1, column=1, columnspan=2)
image_entry.focus()
watermark_entry = Entry(width=35)
watermark_entry.grid(row=2,column=1)

#---------------------------------------------------------------------------#

#Button

submit_button = Button(text="Submit", command= image, bg="skyblue")
submit_button.grid(row=4, column=1)















window.mainloop()

