import os
from base64 import b64decode

def main():
    key = os.environ.get("SERVICE_ACCOUNT_KEY")
    if not key:
        print("SERVICE_ACCOUNT_KEY environment variable is not set.")
        exit(1)

    try:
        print(f"SERVICE_ACCOUNT_KEY starts with: {key[:10]}")
        decoded_key = b64decode(key).decode()
        print("Decoded key seems valid.")
    except Exception as e:
        print(f"Error decoding SERVICE_ACCOUNT_KEY: {e}")
        exit(1)

    file_path = "path.json"
    with open(file_path, "w") as json_file:
        json_file.write(decoded_key)
        print("Successfully wrote the decoded key to path.json.")
    print(os.path.abspath(file_path))  # Only this line will be used by the export command

if __name__ == "__main__":
    main()