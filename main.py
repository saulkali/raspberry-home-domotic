from app import run
from helper import get_file
import configparser

config = configparser.ConfigParser()
config.read(get_file("config.ini"))

def main():
    run.run_app()

if __name__ == '__main__':
    main()