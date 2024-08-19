from datetime import datetime
import logging
import os

def gather_input(max_attempts=3):
    for _ in range(max_attempts):
        date = input("Enter a date (mm/dd/yyyy): ")
        logger.info(f"User input: {date}")
        try:
            parsed = datetime.strptime(date, "%m/%d/%Y")
            logger.info(f"Parsed date: {parsed}")
            return parsed
        except ValueError:
            logger.error("Error - Date Format:", exc_info=True)
            print("Invalid date format. Please try again.")

    message = "Max attempts reached. Please try again."
    logger.critical(f"{message}")
    raise ValueError(message)

def calculate_day_of_week(date):
    day_of_week = date.strftime("%A")
    logger.info(f"Type of day_of_week: {type(day_of_week)}")
    logger.info(f"Value of day_of_week: {day_of_week}")
    return day_of_week

def setup_logging():
    log_level = os.environ.get('LOG_LEVEL', 'INFO')
    logging.getLogger().setLevel(log_level)
    logger = logging.getLogger(__name__)
    file_handler = logging.FileHandler("app.log", mode="a", encoding="utf-8")
    logger.addHandler(file_handler)
    formatter = logging.Formatter(
        "{asctime} - {levelname} - {message}",
        style="{",
        datefmt="%Y-%m-%d %H:%M",
    )
    file_handler.setFormatter(formatter)
    return logger

logger = setup_logging()

if __name__ == '__main__':
    logger.info('Application started')
    
    date = gather_input()
    print(calculate_day_of_week(date))
    logger.info('Application finished')
