from aiogram import Dispatcher, types
import yt_dlp
import os
import time


class FilenameCollectorPP(yt_dlp.postprocessor.common.PostProcessor):
    def __init__(self):
        super(FilenameCollectorPP, self).__init__(None)
        self.filenames = []

    def run(self, information):
        self.filenames.append(information["filepath"])
        return [], information


async def search_music(message: types.Message) -> None:
    arg = message.get_args()
    ydl_options = {'format': 'bestaudio/best',
                   'noplaylist': 'True',
                   'postprocessors': [{
                       'key': 'FFmpegExtractAudio',
                       'prefferedcodec': 'mp3',
                       'prefferedquality': '192'
                   }]
    }
    with yt_dlp.YoutubeDL(ydl_options) as ydl:
        try:
            get(arg)
        except:
            filename_collector = FilenameCollectorPP()
            ydl.add_post_processor(filename_collector)
            video = ydl.extract_info(f"ytsearch: {arg}", download=True)["entries"][0]
            await message.reply_document(open(filename_collector.filenames[0], "rb"))
            time.sleep(10)
            os.remove(filename_collector.filenames[0])
        else:
            video = ydl.extract_info(arg, download=True)
        return filename_collector.filenames[0]


def register_handlers_search_music(dp: Dispatcher):
    dp.register_message_handler(search_music, commands=['music'])
