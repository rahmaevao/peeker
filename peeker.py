import subprocess
import sys

file_name = sys.argv[-1]
 
code = subprocess.call(["streamlit", "run", "src/main.py", "--", file_name])