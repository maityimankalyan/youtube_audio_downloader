"""
	download ffmpeg from https://ffmpeg.zeranoe.com/builds/
	make environment variable ...\\ffmpeg-4.1-win64-static\bin
	install youtube_dl: pip install youtube_dl
	install clipboard: pip install clipboard
	TODO: search for better alternetives
"""

from __future__ import unicode_literals
from argparse import ArgumentParser
import os
import youtube_dl
import clipboard

video_title = ''
ydl_opt = {}
clip_link = clipboard.paste()

parser = ArgumentParser()
parser.add_argument("-l", "--link", dest="weblink",
                    help="YouTube.com website link", type=str, default=clip_link)
parser.add_argument("-b", "--bitrate", dest="bitrate",
                    help="higher bitrate for better quality: 64/128/192", type=int, default=64)
parser.add_argument("-f", "--formate", dest="formate",
                    help="chose audio formate: mp3/wav/aac/wma", type=str, default='mp3')
parser.add_argument("-o", "--outdir", dest="outdir",
                    help='example: -o <destination path>. default is current directory', type=str, default=os.getcwd())
args = parser.parse_args()

with youtube_dl.YoutubeDL(ydl_opt) as ydl:
	meta_data = ydl.extract_info(str(args.weblink), download=False)
	video_title = meta_data['title']
	print('[user] Video name: {}'.format(video_title))

outtmpl = video_title + '.%(ext)s'

ydl_opts = {
			'format'			: 'bestaudio/best',
			'outtmpl'			: outtmpl,
			'postprocessors'	: [{
									'key'				: 'FFmpegExtractAudio',
									'preferredcodec'	: args.formate,
									'preferredquality'	: str(args.bitrate), # ?need to be string
									}],
		}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	ydl.download([args.weblink])
