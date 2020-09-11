#!/usr/bin/env python3
###############################################################################
# Created by: Domenick M. Botardo
# Program name: image_converter.py
# Description:
#   A GUI application for converting image to jpeg,
# png, bmp and also pdf format
###############################################################################
import tkinter as tk
from tkinter import filedialog as fd
from PIL import Image, UnidentifiedImageError

# Set constants
BG_COLOR = '#000000'
FG_COLOR = '#ffffff'
ERROR_COLOR = '#ff0000'
SUCCESS_COLOR = '#00d400'
BG_BUTTON = '#00d400'
FG_BUTTON = '#000000'
BG_LABEL = '#ffffff'
FG_LABEL = '#000000'
WIDTH = 480
HEIGHT = 450

class ImageFile:
    def __init__(self, filename=None):
        self.filename = filename


def browsefile(image_file, label_obj_file, label_obj_status):
    # reset labels upon clicking the button
    label_obj_file.configure(text='')
    label_obj_status.configure(text='')

    # get filename and update label
    filename = fd.askopenfilename()
    image_file.filename = filename
    label_obj_file.configure(text=filename)


def build_name(image, ext):
    uri = image.filename.split('.')[0]
    return uri + ext


def convert_image(filename, ext, label_obj):
    try:
        image = Image.open(filename)
    except UnidentifiedImageError:
        log_error('Not an image file', label_obj)
    except AttributeError:
        log_error('Please select an image file first', label_obj)
    except PermissionError:
        log_error(f'No read permission on file', label_obj)
    else:
        filename = build_name(image, ext)
        im = image.convert(mode='RGB')
        im.save(filename)
        log_success(filename, label_obj)


def log_success(filename, label_obj):
    msg = f'Success: Saved to: {filename}'
    label_status.configure(text=msg, fg=SUCCESS_COLOR)


def log_error(errormsg, label_obj):
    errormsg = f'Error: {errormsg}'
    label_obj.configure
    label_obj.configure(text=errormsg, fg=ERROR_COLOR)


def to_png(filename, label_obj):
    convert_image(filename, '.png', label_obj)


def to_jpg(filename, label_obj):
    convert_image(filename, '.jpg', label_obj)


def to_bmp(filename, label_obj):
    convert_image(filename, '.bmp', label_obj)


def to_pdf(filename, label_obj):
    convert_image(filename, '.pdf', label_obj)


# Instantite an ImageFile class
img_file = ImageFile()

root = tk.Tk()
root.minsize(width=WIDTH, height=HEIGHT)
root.resizable(width=1, height=0)
root.title('Image Converter')

canvas = tk.Canvas(root, bg=BG_COLOR)
canvas.place(relheight=1, relwidth=1)

# First frame: container for open button and label
frame1 = tk.Frame(root, bg=BG_COLOR)
frame1.place(relx=0.05, rely=0.05, relheight=0.1, relwidth=0.9)

button_open = tk.Button(frame1, text='Open File', padx=10, pady=5, font=('bold', 12),
        bg=BG_BUTTON, fg=FG_BUTTON, command=lambda: browsefile(img_file, label_file, label_status))
button_open.pack(side='left')

label_select = tk.Label(frame1, fg=BG_BUTTON, bg=BG_COLOR,
                 text='Select an image file', font=('bold', 12))
label_select.pack(side='left', padx=10)

# Second frame: container for selected file
frame2 = tk.Frame(root, bg=BG_LABEL)
frame2.place(relx=0.05, rely=0.16, relheight=0.06, relwidth=0.9)
label_file = tk.Label(frame2, fg=FG_LABEL, bg=BG_LABEL, font=('bold', 9))
label_file.place(relheight=1)

# Third frame: container for conversion buttons
frame3 = tk.Frame(root, bg=BG_COLOR)
frame3.place(relx=0.05, rely=0.26, relheight=0.6, relwidth=0.9)

button_png = tk.Button(frame3, text='Convert to PNG', fg=FG_BUTTON, bg=BG_BUTTON,
        font=('bold', 12), command=lambda: to_png(img_file.filename, label_status))
button_png.place(relx=0.25, rely=0.05, relheight=.15, relwidth=0.5)

button_jpg = tk.Button(frame3, text='Convert to JPEG', fg=FG_BUTTON, bg=BG_BUTTON,
        font=('bold', 12), command=lambda: to_jpg(img_file.filename, label_status))
button_jpg.place(relx=0.25, rely=0.30, relheight=0.15, relwidth=0.5)

button_bmp = tk.Button(frame3, text='Convert to BMP', fg=FG_BUTTON, bg=BG_BUTTON,
        font=('bold', 12), command=lambda: to_bmp(img_file.filename, label_status))
button_bmp.place(relx=0.25, rely=0.55, relheight=0.15, relwidth=0.5)

button_pdf = tk.Button(frame3, text='Convert to PDF', fg=FG_BUTTON, bg=BG_BUTTON,
        font=('bold', 12), command=lambda: to_pdf(img_file.filename, label_status))
button_pdf.place(relx=0.25, rely=0.8, relheight=0.15, relwidth=0.5)

# Fourth frame: container for status messages
frame4 = tk.Frame(root, bg=BG_COLOR)
frame4.place(relx=0.05, rely=0.9, relheight=0.06, relwidth=0.9)
label_status = tk.Label(frame4, bg=BG_COLOR, font=('bold', 9))
label_status.place(relheight=1)

root.mainloop()
