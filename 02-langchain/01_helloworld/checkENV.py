import os
from dotenv import load_dotenv

load_dotenv()

print(f'model: {os.getenv("MODEL")}')
print(f'model provider: {os.getenv("MODELPROVIDER")}')
print(f'API Key: {os.getenv("APIKEY")}')
print(f'Base URL: {os.getenv("BASEURL")}')