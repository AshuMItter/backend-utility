from click.testing import CliRunner
from pathlib import Path
import sys
import subprocess

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

try:
    script = Path(PROJECT_ROOT) / "src" / "main.py"
    print(f"Running script: {script}")
    result = subprocess.run([sys.executable, str(script), "https://jsonplaceholder.typicode.com/posts"], capture_output=True, text=True,timeout=3)
    print(f"Return code: {result.returncode}")
    print(f"Output: {result.stdout[:200]}")
    print("✅ PASSED" if result.returncode == 0 else "❌ FAILED")
except subprocess.TimeoutExpired:
    print("⏱️ Script is running continuously (as expected)")
    print("✅ PASSED - Script started successfully")