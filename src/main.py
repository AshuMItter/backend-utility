import os
import sys
import time
from pathlib import Path
import argparse
from rich.progress import track, Progress, SpinnerColumn, TextColumn
from pathlib import Path
import uuid

from dotenv import load_dotenv
 
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


def main():
    parser = argparse.ArgumentParser(
        description="My app from processing data",
        epilog='''Examples:
  python main.py data.csv                    # Positional only
  python main.py data.csv --output out.csv  # Positional + Option
  python main.py data.csv --verbose         # Positional + Flag'''
    )

    # Positional Argument 
    parser.add_argument(
        'input_file',
        help='input file to process (required)'
    )
    # Option Argument
    parser.add_argument(
        '--output',
        '-o',
         help='Output file path'
    )
    # FLAG (Optional, with -- but no value)
    parser.add_argument(
        '--verbose',
        '-v',
        action='store_true',
        help='Enable verbose output'

    )
    args = parser.parse_args()
        

    print(f"Processing {args.input_file}...")

    for i in track(range(20), description="Processing items"):
        time.sleep(0.2)  # Simulate work
        
    # Method 2: Custom progress bar
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        task = progress.add_task("[cyan]Finalizing...", total=100)
        for i in range(100):
            time.sleep(0.01)
            progress.update(task, advance=1)
    
    print("Done!")  

   
   
    print(args.input_file)
    print(args.verbose)
    print(args.output)
    #print(args.help)
    tid = uuid.uuid4()
    print(uuid.uuid4())
    # Load environment variables from .env file
    # load_dotenv()
    # argument1 = sys.argv[1] if len(sys.argv) > 1 else None
    # print(f"Argument received: {argument1}")
    # print(f"Data path from module2: {pathv}")


if __name__ == "__main__":
    print("Starting the application...")
    main()