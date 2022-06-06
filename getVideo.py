from pytube import YouTube

def getVideo(linkYoutube = ''):
    if linkYoutube == '':
        return -1, 'Нет ссылки'

    try:
        yt_obj = YouTube(linkYoutube)

        filters = yt_obj.streams.filter(
            progressive=True,
            file_extension='mp4'
        )
        #download the highest quality video
        filters.get_highest_resolution().download()
        return 1, ''
    except Exception as e:
        return -1, e
