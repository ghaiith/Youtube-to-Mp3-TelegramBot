# YouTube to MP3 Telegram Bot

This is a simple Telegram bot that allows you to send a YouTube link, and the bot will convert the video to MP3 and send it back to you.

<img src="https://github.com/ghaiith/Youtube-to-Mp3-TelegramBot/blob/main/Example.PNG " width="200">

## Getting Started

### Prerequisites

To run this bot, you need to have the following installed:

- Python 3.6 or higher
- `telebot` library
- `yt_dlp` library
- `moviepy` library

You can install the required libraries using the following command:

```bash
pip install telebot yt-dlp moviepy
```
or
```bash
pip install -r requirements.txt
```

### Creating a Telegram Bot and Obtaining the API Token

To use this bot, you need to create a Telegram bot and obtain the API token. Follow these steps to create a new bot and get the token:

1. Open Telegram and search for the "BotFather" bot.

2. Start a chat with the BotFather by clicking on the "Start" button or by sending a message with the `/start` command.

3. Use the `/newbot` command to create a new bot. The BotFather will guide you through the process of creating the bot. You will need to perform the following steps:

   a. Choose a name for your bot. This name will be displayed in Telegram chats and will be used to mention your bot when users interact with it.

   b. Choose a username for your bot. The username must end with "bot" (e.g., `mytelegrambot`). It will be used as the bot's unique identifier and will be used to create the bot's link (e.g., `t.me/mytelegrambot`).

4. Once the bot is created, the BotFather will provide you with the API token. This token is essential for the bot to communicate with Telegram's API. It should look something like this:

   ```
   1234567890:ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnop
   ```

5. Copy the API token and paste it into the `TOKEN` variable in the code of your bot (`bot.py`). Replace `'YOUR_TELEGRAM_BOT_TOKEN'` with the token you obtained.

6. Now, your bot is ready to use! Start the bot by running the Python script (`bot.py`) as mentioned in the "Running the Bot" section.

Remember to keep your API token private and do not share it with anyone you don't trust. If you accidentally leak the token or suspect that it has been compromised, you can regenerate a new token by talking to the BotFather and using the `/token` command for your bot.

### Running the Bot

1. Clone this repository to your local machine.

2. Replace `'YOUR_TELEGRAM_BOT_TOKEN'` in the code with the token obtained from the BotFather.

3. Open a terminal or command prompt and navigate to the cloned repository directory.

4. Run the bot using the following command:

```bash
python main.py
```

The bot will now be running and ready to receive YouTube links.

## How the Bot Works

1. When you start or send a message with the `/start` or `/help` command, the bot will send you instructions on how to use it.

2. To convert a YouTube video to MP3, simply send the bot a YouTube link as a text message.

3. The bot will download the video using `yt_dlp`, extract the title of the video, and save it as an MP4 file.

4. Next, the bot will convert the downloaded MP4 file to an MP3 file using `moviepy`.

5. Finally, the bot will send the converted MP3 audio file back to you.

Please note that the bot will delete the downloaded MP4 and MP3 files after processing to save storage space.


## Contributing

Contributions to this project are welcome! If you encounter any bugs, have suggestions for improvements, or would like to add new features, feel free to contribute. Here's how you can get started:

1. **Fork the Repository**: Click the "Fork" button at the top right corner of this repository to create your copy.

2. **Clone the Repository**: Clone the forked repository to your local machine using the following command (replace `[YOUR_USERNAME]` with your GitHub username):

   ```
   git clone https://github.com/[YOUR_USERNAME]/youtube-to-mp3-bot.git
   ```

3. **Create a New Branch**: Move into the repository's directory and create a new branch for your changes:

   ```
   cd youtube-to-mp3-bot
   git checkout -b my-feature
   ```

4. **Make Changes**: Make your desired changes to the codebase.

5. **Commit Your Changes**: After making changes, commit them with a descriptive commit message:

   ```
   git add .
   git commit -m "Add new feature" (replace with your message)
   ```

6. **Push Changes**: Push your changes to your forked repository:

   ```
   git push origin my-feature (replace with your branch name)
   ```

7. **Create a Pull Request**: Go to the original repository (https://github.com/OpenAI/Youtube-to-mp3-bot) and click on the "Pull Request" button. Fill in the details of your pull request and submit it for review.

8. **Discuss and Review**: Once you've created a pull request, the maintainers of the repository will review your changes. Be prepared to address any feedback or comments.

9. **Merge**: If everything looks good and your changes are approved, they will be merged into the main repository.

Please ensure that your contributions adhere to the project's coding guidelines and are respectful to all members of the community.

Thank you for contributing to this project! Your efforts help make it better for everyone. If you have any questions or need help with the contribution process, feel free to open an issue or reach out to the maintainers.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This bot is provided as-is and without any warranty. Use it at your own risk. The developers are not responsible for any misuse or legal issues that may arise from using this bot to convert copyrighted content without permission.

