import subprocess
import ctypes
import sys
import time

service_name = "vgc"

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    print("Attempting to elevate privileges...")
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit(0)  #prevent duplicate execution
else:
    print("Running with admin privileges.")
    
    try:
        result = subprocess.run(["sc", "start", service_name], shell=True, check=True, capture_output=True, text=True)
        print(f"Service '{service_name}' started successfully.")
        print(result.stdout)
        time.sleep(3)
    except subprocess.CalledProcessError as e:
        print(f"Failed to start service '{service_name}': {e}")
        print(e.stderr)
