# Customer Support Bot

![Telegram Bot](https://img.shields.io/badge/Telegram-Bot-blue.svg)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![MongoDB](https://img.shields.io/badge/MongoDB-Database-brightgreen.svg)

## Overview

The **Customer Support Bot** is an intelligent Telegram bot designed to automate customer support. It can handle requests in real-time, provide information, and interact with users through a friendly interface. This bot leverages the power of Python, the `python-telegram-bot` library, and MongoDB to create a seamless customer service experience.

## Features

- **User Registration**: Automatically registers new users and stores their information.
- **Command Handling**: Supports commands like `/start`, `/help`, `/info`, and `/menu`.
- **Interactive Menu**: Provides an easy-to-use menu for navigating the bot's features.
- **Logging**: Logs all user interactions for easy monitoring and debugging.
- **Scalable**: Built with scalability in mind, ready to handle numerous customer requests simultaneously.

## Technologies Used

- **Programming Language**: Python
- **Libraries**: `python-telegram-bot`, `pymongo`
- **Database**: MongoDB
- **Tools**: Visual Studio Code

## Installation

Follow these steps to set up the bot on your local machine:

1. **Clone the repository**:
    ```sh
    git clone https://github.com/levklon/customer_support_bot.git
    ```

2. **Navigate to the project directory**:
    ```sh
    cd customer_support_bot
    ```

3. **Create a virtual environment**:
    ```sh
    python -m venv venv
    ```

4. **Activate the virtual environment**:
    - On Windows:
      ```sh
      .\venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```sh
      source venv/bin/activate
      ```

5. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

6. **Set up environment variables**:
    Create a `.env` file in the root directory of the project and add the following lines:
    ```
    TELEGRAM_TOKEN=your_telegram_token
    MONGODB_URI=your_mongodb_uri
    ```
    
## Usage

   To start the bot, run the following command:
   ```sh
   python -m bot.main
   ```

## Future Enhancements

- Multi-language Support: Add support for multiple languages to cater to a global audience.
- Advanced Analytics: Integrate with analytical tools to provide insights into customer interactions.
- AI Integration: Use AI to provide more intelligent and personalized customer support.

## License

This project is licensed under the MIT License. See the [LICENSE] file for details.




