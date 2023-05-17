import logging
import os
from dotenv import load_dotenv

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(),
        # logging.FileHandler("momo-ai.log")
    ]
)

def load_env():
    env = os.getenv("ENV", "dev")

    if env == "dev":
        load_dotenv("config/.env.dev")
    elif env == "prod":
        load_dotenv("config/.env.prod")
    else:
        raise Exception(f"Unknown environment {env}")