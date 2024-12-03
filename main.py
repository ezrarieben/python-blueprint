import os
import logging
import yaml  # PyYAML
from dotenv import load_dotenv  # .env file support using python-dotenv

load_dotenv(override=True)  # Loads environment variables without cache

# Load config.yaml
with open("config.yaml") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

# Configure logger
logfilePath = os.path.join(config["log"]["path"], config["log"]["file"])
logLevel = str(config["log"]["level"]).upper()
logLevels = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
}
logging.basicConfig(
    filename=logfilePath,
    level=logLevels.get(logLevel, logging.INFO),
    format="%(asctime)s - %(levelname)s - %(message)s",  # Define the log message format
)


##########################################################################################
# Script start
##########################################################################################


def main():
    logging.info("Starting script...")
    hello()


def hello():
    print("Hello, World!")


if __name__ == "__main__":
    main()
