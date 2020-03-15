from tkinter import filedialog
from tkinter import *
import yotube_audio
from PIL import Image, ImageTk


screen = Tk()
screen.geometry("800x400")
screen.title("YouTube Audio Downloader")
heading = Label(
    text = "Download Only Audio from YouTube",
    bg = "red",
    fg = "white",
    width = "800",
    height = "1")
heading.pack()


class Example(Frame):
    """used in flexiable background image setting"""
    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)

        self.image = Image.open("bg.png")
        self.img_copy= self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

    def _resize_image(self,event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image =  self.background_image)


# bgimg = Example(screen)
# bgimg.pack(fill=BOTH, expand=YES)


def callYouTubeAudio():
    video_URL, out_DIR, bit_rate, curr_format = '', '', '', ''

    try:
        video_URL = videoURL.get()
        out_DIR = outDIR.get()
        bit_rate = bitRate.get()
        curr_format = currFormat.get()
    except Exception as e:
        print(e)

    print('video_URL: {} \nout_DIR: {} \nbit_rate: {} \ncurr_format: {}'.format(
        video_URL, out_DIR, bit_rate, curr_format))
    # CurrTxt = Label(text="Downloading...", fg='blue')
    # CurrTxt.place(x=550, y=200)

    if yotube_audio.downloadAudio(bit_rate, curr_format, video_URL, out_DIR):  # (bitrate=64, formate='mp3', weblink='', outdir='')
        StatusTxt = Label(text="Audio Download Completed!", fg='green')
        StatusTxt.place(x=550, y=200)
    else:
        StatusTxt = Label(text="Audio Download Failed!", fg='red')
        StatusTxt.place(x=550, y=200)


def browse_button():
    global outDIR
    filename = filedialog.askdirectory()
    outDIR.set(filename)
    print(filename)

VideoURLtxt = Label(text="Video URL (def Clipboard): ")
VideoURLtxt.place(x=20, y=60)

outDIRtxt = Label(text="   Output Dir (def Current): ")
outDIRtxt.place(x=20, y=100)

videoURL = StringVar()
videoURLentry = Entry(textvariable=videoURL, width=60)
videoURLentry.place(x=175, y=60)

outDIR = StringVar()  # IntVar()
outDIRentry = Entry(textvariable=outDIR, width=60)
outDIRentry.place(x=175, y=100)

BrowsButton = Button(text="Browse", command=browse_button)
BrowsButton.place(x=550, y=97)

VideoURLtxt = Label(text="Bit Rate: ")
VideoURLtxt.place(x=550, y=60)

bitRates = [64, 120, 192]
bitRate = IntVar()
bitRate.set(bitRates[0])
bitRateDrop = OptionMenu(screen, bitRate, *bitRates)
bitRateDrop.place(x=600, y=53)

formatTxt = Label(text="Format: ")
formatTxt.place(x=670, y=60)

formats = ['mp3', 'wav', 'aac', 'wma']
currFormat = StringVar()
currFormat.set(formats[0])
currFormatDrop = OptionMenu(screen, currFormat, *formats)
currFormatDrop.place(x=720, y=53)


download = Button(
    screen,
    text="Download",
    width="10", height="1",
    command=callYouTubeAudio)
download.place(x=175, y=200)



screen.mainloop()