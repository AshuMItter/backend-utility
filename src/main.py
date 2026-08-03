import os
import sys
import time
from pathlib import Path
import argparse
from rich.progress import track, Progress, SpinnerColumn, TextColumn
from pathlib import Path
import uuid
import schedule
import time
import threading
import logging
from dotenv import load_dotenv
 
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

#from logs.logmanager import jsonsecurelogger
from datajson.jsonarrayclean import JSONCleaner
from httpxclient.httpxc import HTTPXClient
from automation.start import StartAutomation

job_lock = threading.Lock()  # Lock to prevent overlapping job executions

def doJob(input_url):       

    if not job_lock.acquire(blocking=False):
        print("Previous job is still running. Skipping this execution.")
        return
    try:
        print(f"Running scheduled job {str(uuid.uuid4())}...")
        primary_key = str(uuid.uuid4())
        print("Running scheduled job...")
        automate = StartAutomation(input_url,primary_key)
        automate.run()
        print("Scheduled job completed.")
        print("Next job will run in 10 seconds...")
    finally:
        job_lock.release()  # Release the lock after job completion

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
        'input_url',
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
        

    print(f"Processing {args.input_url}...")

    # for i in track(range(20), description="Processing items"):
    #     time.sleep(0.2)  # Simulate work
        
    # # Method 2: Custom progress bar
    # with Progress(
    #     SpinnerColumn(),
    #     TextColumn("[progress.description]{task.description}"),
    #     transient=True,
    # ) as progress:
    #     task = progress.add_task("[cyan]Finalizing...", total=100)
    #     for i in range(100):
    #         time.sleep(0.01)
    #         progress.update(task, advance=1)
    
    # print("Done!")  

   
   
    # print(args.input_url)
    # print(args.verbose)
    # print(args.output)
     # Adjust the message as needed


        # Here you can call your main function or any other function you want to run periodically
        
    #print(args.help)
    # tid = uuid.uuid4()
    # print(uuid.uuid4())
    # Load environment variables from .env file
    # load_dotenv()
    # argument1 = sys.argv[1] if len(sys.argv) > 1 else None
    # print(f"Argument received: {argument1}")
    # print(f"Data path from module2: {pathv}")
    schedule.clear()

    schedule.every(10).seconds.do(doJob, args.input_url)
    #schedule.every().tuesday.at("10:30").do(doJob)

    

    

if __name__ == "__main__":
    try:      

        main()
        print(logging.INFO)
        print("Starting the application...")
        while True:
            schedule.run_pending()
            time.sleep(1)  # Sleep for a short duration to avoid busy waiting
    except KeyboardInterrupt:
        print("Application interrupted by user.")
        exit_code =0
        print(f"Exiting with code {exit_code}")
    except Exception as e:
        print("Some Error Occurred in the Application")
        print({e})
        exit_code =1
        print(f"Exiting with code {exit_code}")
    finally:
        print("Application has exited.")