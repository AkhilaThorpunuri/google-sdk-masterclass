import sys
from importlib.metadata import version

from google import genai


def main():
    print("Python version:")
    print(sys.version)

    print("\nGoogle Gen AI SDK installation:")
    print(f"Google Gen AI SDK version: {version('google-genai')}")

    print("\nImport verification:")
    print("Google Gen AI SDK imported successfully.")

    print("\nInstallation verified.")


if __name__ == "__main__":
    main()
