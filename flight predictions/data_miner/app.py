from dotenv import load_dotenv
from weather_data_miner import WeatherDataMiner

# Load environment variables from .env file
load_dotenv()

def run():
    WeatherDataMiner().run()

if __name__ == "__main__":
    run()
