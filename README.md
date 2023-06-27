# GitHub Repository README

This repository contains the following files:

- `main.py`: Python script for running the internet speed complaint bot.
- `complaint_bot.py`: Python module containing the `InternetSpeedTwitterBot` class used by `main.py` script.

## Prerequisites

Before running the `main.py` script, ensure that you have the following dependencies installed:

- Selenium: `pip install selenium`

Additionally, you will need to download the ChromeDriver executable appropriate for your system and set the `CHROME_DRIVER_PATH` variable in the `main.py` script to the path of the ChromeDriver executable.

## Usage

To use the internet speed complaint bot, follow these steps:

1. Set the promised download and upload speeds in the `PROMISED_DOWN` and `PROMISED_UP` variables in the `main.py` script.
2. Set the `TWITTER_EMAIL` and `TWITTER_PASSWORD` environment variables with your Twitter account credentials.
3. Run the `main.py` script.

The script will launch a Chrome browser window and perform the following actions:

1. Open the Speedtest website and measure the internet speed.
2. Log in to your Twitter account.
3. Compose a tweet mentioning your internet service provider and complaining about the actual internet speed.

Please note that the script may take some time to complete the speed test, so be patient.

## Disclaimer

This script is provided as-is without any warranty. Use it at your own risk.

## Contributions

Contributions to improve the functionality or fix issues with the script are welcome. Feel free to submit a pull request or open an issue on the GitHub repository.
