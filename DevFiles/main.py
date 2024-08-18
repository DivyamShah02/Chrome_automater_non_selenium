import os
import sys
from library.Config import Config
from library.GetLogger import GetLogger
from library.ChromeHandler import ChromeHandler

def main():
    try:
        cwd_path = os.getcwd()
        config_path = cwd_path.replace('DevFiles', 'BotConfig\\config.ini')
        config = Config(filename=config_path)

        logs_dir: str = config.paths.logs_path
        logger = GetLogger(log_file_dir=logs_dir, log_file_name="chrome_automater.log", file_handler=True).logger

        chrome_handler = ChromeHandler(logger=logger, config=config)

        if not chrome_handler.start_chrome():
            logger.error("Failed to start Chrome.")
            sys.exit(1)

        if not chrome_handler.select_profile(profile_index=int(config.chrome_config.profile_index)):
            logger.error("Failed to select profile.")
            chrome_handler.kill_all_chrome()
            sys.exit(1)

        if not chrome_handler.maximise_chrome():
            logger.error("Failed to maximize Chrome.")
            chrome_handler.kill_all_chrome()
            sys.exit(1)

        if not chrome_handler.load_url(url=config.chrome_config.url):
            logger.error("Failed to load URL.")
            chrome_handler.kill_all_chrome()
            sys.exit(1)

        ################
        ## YOUR LOGIC ##
        ################

        import pdb; pdb.set_trace()

        chrome_handler.kill_all_chrome()
        logger.info("Chrome automation completed successfully.")

    except Exception as e:
        logger.error("An unexpected error occurred.", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()
