import os
import tkinter as tk
from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter.filedialog import askopenfilename
from tkinter.ttk import *
from tkinter import font, filedialog
from PIL import Image, ImageDraw, ImageFont, ImageTk

# Get path of current directory
basedir = os.path.dirname(__file__)


def file_open():
    global file_path
    file_path = askopenfilename(title="Select An Image", filetypes=[('Images', '*.jpg *.jpeg *.png *.webp *.gif')])
    if file_path:
        display_image(file_path)


def display_image(file_path):
    global image, img_width, img_height, current_height, current_width, width_label, height_label, current_logo_height, \
        current_logo_width, current_height_logo, current_width_logo, width_label_logo, height_label_logo, height_size_logo
    image = Image.open(file_path)
    image.thumbnail((900, 900))
    photo = ImageTk.PhotoImage(image)
    image_label.config(image=photo)
    image_label.photo = photo
    img_height = image.height
    img_width = image.width
    if display_image:
        # set the text scale according to image size
        height_position.config(to=img_height - 30, variable=current_height)
        width_position.config(to=img_width - 100, variable=current_width)
        height_position.set(img_height / 2)
        width_position.set(img_width / 2)
        # set the logo scale according to image size
        height_position_logo.config(to=img_height - 30, variable=current_height_logo)
        width_position_logo.config(to=img_width - 100, variable=current_width_logo)
        height_position_logo.set(img_height / 2)
        width_position_logo.set(img_width / 2)


def water_text():
    global pic
    pic = image.convert("RGBA")
    opacity_tuple = ((round(current_opacity.get() * 2.55)),)
    rgba_text_color = text_color + opacity_tuple
    drawing = ImageDraw.Draw(pic)
    font = ImageFont.truetype(font_var.get(), current_font_size.get())
    watermark_text = watermark_input.get()
    position = (current_width.get(), current_height.get())
    drawing.text(xy=position, text=watermark_text, font=font, fill=rgba_text_color)
    pic.save('watermark_image.png')
    watermark_pic = Image.open('watermark_image.png')
    photo = ImageTk.PhotoImage(watermark_pic)
    image_label.config(image=photo)
    image_label.photo = photo


def water_logo():
    global back
    back = Image.open(file_path)
    back.thumbnail((900, 900))
    watermark = Image.open(file_path_logo)
    size = (current_logo_height.get(), current_logo_width.get())
    watermark.thumbnail(size)
    copied_image = watermark.copy()
    back.paste(copied_image, (current_width_logo.get(), current_height_logo.get()))
    photo = ImageTk.PhotoImage(back)
    image_label.config(image=photo)
    image_label.photo = photo


def rgb_to_hex(rgb):
    return "#%02x%02x%02x" % rgb


def get_text_color():
    colors = askcolor(title="Watermark Color Chooser")
    global text_color
    text_color = colors[0]  # colors[0] is RGB value
    color_selection.configure(bg=colors[1])


def width_slider_moved(event):
    width_label.configure(text=f"Width: \n{current_width.get() - 1 / 2 * img_width}")


def height_slider_moved(event):
    height_label.configure(text=f"Height: \n {-1 * (current_height.get() - 1 / 2 * img_height)}")


def width_slider_moved_logo(event):
    width_label_logo.configure(text=f"Width:\n {current_width_logo.get() - 1 / 2 * img_width}")


def height_slider_moved_logo(event):
    height_label_logo.configure(text=f"Height:\n {-1 * (current_height_logo.get() - 1 / 2 * img_height)}")


def logo_to_watermark():
    global file_path_logo
    file_path_logo = askopenfilename(title="Select An Image", filetypes=[('Images', '*.jpg *.jpeg *.png *.webp *.gif')])


def save():
    path_save = filedialog.asksaveasfilename(defaultextension=".png")
    image.save(path_save)
    try:
        back.save(path_save)
    except NameError:
        pic.save(path_save)
    else:
        pass


# -----------------------------GUI---------------------------------------------------------
# GUI using Tkinter
window = tk.Tk()
window.title("Image Watermark")
window.config(pady=20, padx=20)

# Image display
blank_img = PhotoImage(file="img_1.png")
image_label = tk.Label(window)
image_label.config(image=blank_img, width=900, height=900)
image_label.pack(side="left", padx=10, pady=20)

# edit_frame
edit_frame = Frame(window, height=600)
edit_frame.pack(padx=10, pady=10)

# -----------------------------EDIT TEXT DISPLAY----------------------------------------------
# upload
upload_button = Button(edit_frame, text="Upload Image", command=file_open, style="Color.TButton", width=15)
upload_button.grid(column=1, row=0, columnspan=1, pady=(0,50))
# save
save_btn = Button(edit_frame, text="Save", command=save, style="Color.TButton", width=15)
save_btn.grid(column=2, row=0, columnspan=1, pady=(0,50))

# Watermark text
watermark_label = Label(edit_frame, text="Text to Watermark: ")
watermark_label.grid(column=0, row=2)
watermark_input = tk.Entry(edit_frame, width=19)
watermark_input.insert(0,"Type Your Text")
watermark_input.grid(column=1, row=2, pady=20)

# Get fonts list from Tkinter
list_fonts = list(font.families())

# Watermark text font
font_var = StringVar()
drop_menu = OptionMenu(edit_frame, font_var, list_fonts[0], *list_fonts)
drop_menu.config(width=15)
drop_menu.grid(column=1, row=4, pady=5)

# Watermark Font Size
current_font_size = IntVar(value=30)
font_size = Spinbox(edit_frame, from_=8, to=250, wrap=True, textvariable=current_font_size, )
font_size.config(width=10)
font_size.grid(column=2, row=4, pady=5)

# Watermark Color
text_color = (0, 0, 0)
color_selection = Canvas(edit_frame,
                         bg=rgb_to_hex(text_color),
                         width=185,
                         height=20)
color_selection.grid(column=1, row=6, pady=10)
color_button = Button(edit_frame,
                      text="Select Color",
                      command=get_text_color,
                      style="Color.TButton",
                      width=9)
color_button.grid(column=2, row=6, columnspan=1)

# Watermark Opacity
current_opacity = IntVar(value=100)
opacity_label = Label(edit_frame, text="Opacity", width=12, anchor="w")
opacity_label.grid(column=1, row=7)
opacity_spinbox = Spinbox(edit_frame,
                          from_=0,
                          to=100,
                          textvariable=current_opacity,
                          wrap=False,
                          width=7
                          )
opacity_spinbox.grid(column=2, row=7, pady=10)

img_height = 0
img_width = 0

# Watermark Text Height position
height_label = Label(edit_frame, text="Height: ", width=12, anchor="w")
height_label.grid(column=1, row=8, sticky='w')
current_height = IntVar(value=int(img_height / 2))
height_position = Scale(edit_frame,
                        from_=0,
                        to=img_height - 30,
                        variable=current_height,
                        orient=VERTICAL,
                        command=height_slider_moved)
height_position.grid(column=1, row=8)

# Watermark Text Width position
width_label = Label(edit_frame, text="Width: ", width=5, anchor="w")
width_label.grid(column=1, row=8, sticky='e', padx=20)
current_width = IntVar(value=int(img_width / 2))
width_position = Scale(edit_frame,
                       from_=0,
                       to=img_width - 100,
                       variable=current_width,
                       orient=HORIZONTAL,
                       command=width_slider_moved)
width_position.grid(column=2, row=8, pady=10)

# Apply text watermark
apply_button = Button(edit_frame, text="Apply Text", command=water_text, width=30)
apply_button.grid(column=1, row=9, columnspan=2, pady=(20,100))

# -----------------------------------EDIT LOGO DISPLAY-----------------------------------------------------

# Logo to watermark
watermark_label = Label(edit_frame, text="Logo to Watermark: ")
watermark_label.grid(column=0, row=10)

# Import logo
import_logo_button = Button(edit_frame, text="Import Logo", command=logo_to_watermark, width=30)
import_logo_button.grid(column=1, row=10, columnspan=2, pady=10)

# Watermark Logo Height position
height_label_logo = Label(edit_frame, text="Height: ", width=12, anchor="w")
height_label_logo.grid(column=1, row=11, sticky='w')
current_height_logo = IntVar(value=int(img_height / 2))
height_position_logo = Scale(edit_frame,
                             from_=0,
                             to=img_height - 30,
                             variable=current_height_logo,
                             orient=VERTICAL,
                             command=height_slider_moved_logo)
height_position_logo.grid(column=1, row=11)

# Watermark Logo Width position
width_label_logo = Label(edit_frame, text="Width: ", width=5, anchor="w")
width_label_logo.grid(column=1, row=11, sticky='e', padx=20)
current_width_logo = IntVar(value=int(img_width / 2))
width_position_logo = Scale(edit_frame,
                            from_=0,
                            to=img_width - 100,
                            variable=current_width_logo,
                            orient=HORIZONTAL,
                            command=width_slider_moved_logo)
width_position_logo.grid(column=2, row=11)

# Logo Height Size
current_logo_height = IntVar(value=120)
logo_height_label = Label(edit_frame, text="height: ", width=5, anchor="w")
logo_height_label.grid(column=1, row=12, sticky='w', pady=10)
height_size_logo = Spinbox(edit_frame,
                           from_=8,
                           to=250,
                           wrap=True,
                           textvariable=current_logo_height)
height_size_logo.config(width=10)
height_size_logo.grid(column=1, row=12, sticky='e', pady=20)

# Logo Width Size
current_logo_width = IntVar(value=120)
logo_width_label = Label(edit_frame, text="width: ", width=5, anchor="w")
logo_width_label.grid(column=1, row=13, sticky='w')
width_size_logo = Spinbox(edit_frame,
                          from_=8,
                          to=250,
                          wrap=True,
                          textvariable=current_logo_width)
width_size_logo.config(width=10)
width_size_logo.grid(column=1, row=13, sticky='e')

# Apply logo watermark
logo_button = Button(edit_frame, text="Apply Logo", command=water_logo, width=30)
logo_button.grid(column=1, row=14, columnspan=2, pady=30)

window.mainloop()
