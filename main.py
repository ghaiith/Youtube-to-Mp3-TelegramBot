import os
import telebot
from yt_dlp import YoutubeDL
from moviepy.editor import *

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with the API token you obtained from BotFather
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

# Initialize the bot
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_instructions(message):
    instructions = (
        "Send me a YouTube link and I will convert it to MP3 for you!\n\n"
        "Just send me the link, and I'll handle the rest."
    )
    bot.reply_to(message, instructions)

@bot.message_handler(content_types=['text'])
def handle_youtube_link(message):
    try:
        youtube_link = message.text.strip()

        # Download the YouTube video
        with YoutubeDL() as ydl:
            info_dict = ydl.extract_info(youtube_link, download=True)
            video_title = info_dict.get('title', 'video')

        # Find the downloaded file with the highest resolution (in MP4 format)
        mp4_files = [f for f in os.listdir('.') if f.endswith('.mp4')]
        if not mp4_files:
            bot.reply_to(message, "Failed to download the video.")
            return

        mp4_files.sort(key=lambda f: os.path.getsize(f), reverse=True)
        downloaded_mp4 = mp4_files[0]

        # Convert the MP4 to MP3 using moviepy
        mp3_file = f'{video_title}.mp3'
        video_clip = VideoFileClip(downloaded_mp4)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(mp3_file)

        # Send the MP3 file to the user
        with open(mp3_file, 'rb') as f:
            bot.send_audio(message.chat.id, f)

        # Clean up downloaded files
        os.remove(downloaded_mp4)
        os.remove(mp3_file)

    except Exception as e:
        bot.reply_to(message, "An error occurred. Please try again later.")

if __name__ == '__main__':
    bot.polling()
