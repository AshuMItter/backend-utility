import os
from dotenv import load_dotenv

import sys


def main():
    # Load environment variables from .env file
    # load_dotenv()
    argument1 = sys.argv[1] if len(sys.argv) > 1 else None
    print(f"Argument received: {argument1}")
    
    

if __name__ == "__main__":
    print("Starting the application...") 
    main()   