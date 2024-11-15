import os
import json
from base64 import b64decode

def main():
    # Get the encoded service account key
    key = os.getenv("SERVICE_ACCOUNT_KEY")
    if not key:
        raise ValueError("SERVICE_ACCOUNT_KEY environment variable is not set")

    # Decode and write to a file
    decoded_key = b64decode(key).decode()
    with open("service-account.json", "w") as json_file:
        json_file.write(decoded_key)
    
    # Print the absolute path of the credentials file
    print(os.path.abspath("service-account.json"))

if __name__ == "__main__":
    main()
