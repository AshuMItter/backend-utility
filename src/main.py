import os
import sys
from pathlib import Path

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from module2 import pathv


def main():
    # Load environment variables from .env file
    # load_dotenv()
    argument1 = sys.argv[1] if len(sys.argv) > 1 else None
    print(f"Argument received: {argument1}")
    print(f"Data path from module2: {pathv}")


if __name__ == "__main__":
    print("Starting the application...")
    main()