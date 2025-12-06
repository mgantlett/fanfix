import sys
import os
import clr

DLL_NAME = "LibreHardwareMonitorLib.dll"
dll_path = os.path.abspath(DLL_NAME)
print(f"Loading DLL from: {dll_path}")

if not os.path.exists(dll_path):
    print("DLL not found!")
    sys.exit(1)

try:
    clr.AddReference(dll_path)
    print("DLL loaded successfully!")
    from LibreHardwareMonitor.Hardware import Computer
    print("Computer class imported successfully!")
except Exception as e:
    print(f"Error loading DLL: {e}")
    import traceback
    traceback.print_exc()
