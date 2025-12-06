import os
import sys
import clr

DLL_NAME = "LibreHardwareMonitorLib.dll"

if not os.path.exists(DLL_NAME):
    print(f"Error: {DLL_NAME} not found.")
    sys.exit(1)

try:
    clr.AddReference(os.path.abspath(DLL_NAME))
    from LibreHardwareMonitor.Hardware import Computer
except Exception as e:
    print(f"Error loading DLL: {e}")
    sys.exit(1)

def dump_sensors(hardware, indent=""):
    hardware.Update()
    print(f"{indent}- [Hardware] {hardware.Name} (Type: {hardware.HardwareType})")
    
    for sensor in hardware.Sensors:
        print(f"{indent}  - [Sensor] {sensor.Name} | Type: {sensor.SensorType} | Value: {sensor.Value}")

    for sub in hardware.SubHardware:
        dump_sensors(sub, indent + "  ")

def main():
    print("--- Hardware Monitor Diagnostic Dump ---")
    computer = Computer()
    computer.IsMotherboardEnabled = True
    computer.IsCpuEnabled = True
    computer.IsControllerEnabled = True
    computer.IsGpuEnabled = True
    computer.IsStorageEnabled = True
    computer.IsMemoryEnabled = True
    
    try:
        computer.Open()
        if not computer.Hardware:
            print("No hardware detected!")
        
        for hardware in computer.Hardware:
            dump_sensors(hardware)
            
    except Exception as e:
        print(f"Error opening computer: {e}")
    finally:
        computer.Close()
        print("\nDone.")

if __name__ == "__main__":
    main()
