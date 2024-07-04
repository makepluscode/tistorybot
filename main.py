from logger import setup_logger
from login import TistoryLogin

def main():
    logger = setup_logger()
    tistory = TistoryLogin(logger)
    tistory.login()

if __name__ == "__main__":
    main()