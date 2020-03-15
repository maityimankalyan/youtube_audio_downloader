# youtube_audio_downloader
download only audio from a youtube video

Command to use:

  python youtube_audio.py  >>  it takes the URL from clipboard (you have to copy the URL then run the cmd) default bitrate is 64, formate is mp3 and save location is current directory

  -l or --link <URL>  >>  user specified youtube URL to download the audio.

  -b or --bitrate <64/128/192>  >> user specified bit rate.

  -f or --formate <mp3/wav/aac/wma>  >>  User specified saving formate.

  -o or --outdir <path>  >>  user specified saving directory.
  
In GUI: (see screenshot for ref.)
 
  Video URL: takes the Youtube URL from the user. If nothing is given then it takes from the clipboard.

  Bit Rate: Dropdown takes the user specified bitrate.

  Format: Dropdown takes the user specified saving format.

  Output Dir: Taked the output directory path.

  Browse: Button opens the explorer to select the path to save the file.

  Download: Button starts the download process. Once Download is done you can see a text saying 'Audio Download Completed!' in green. For failure you can see 'Audio Download Failed!' in red.
