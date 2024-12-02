import os
from dotenv import load_dotenv

def load_env():
  BASE_DIR = os.path.dirname(os.path.abspath(__file__))
  load_dotenv(os.path.join(BASE_DIR, ".env"))