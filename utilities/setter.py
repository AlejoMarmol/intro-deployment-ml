import os
from base64 import b64decode, binascii

def main():
    # Check if the environment variable is set
    key = os.environ.get('SERVICE_ACCOUNT_KEY')
    if not key:
        raise EnvironmentError("SERVICE_ACCOUNT_KEY environment variable is not set.")
    
    # Debug: Print the first few characters of the key (safe to debug)
    print("SERVICE_ACCOUNT_KEY starts with:", key[:10])
    
    try:
        # Decode the key
        decoded_key = b64decode(key).decode()
        print("Decoded key seems valid.")
    except binascii.Error as e:
        # Catch base64 decoding errors and print a clear message
        print("Error decoding SERVICE_ACCOUNT_KEY:", e)
        raise ValueError("SERVICE_ACCOUNT_KEY is not a valid base64-encoded string.")

    # Save the decoded key to a file
    try:
        with open('path.json', 'w') as json_file:
            json_file.write(decoded_key)
        print("Successfully wrote the decoded key to path.json.")
    except Exception as e:
        # Catch any file writing errors
        print("Error writing to path.json:", e)
        raise

    # Debug: Print the absolute path of the written file
    print("Credential file created at:", os.path.realpath('path.json'))

if __name__ == '__main__':
    main()