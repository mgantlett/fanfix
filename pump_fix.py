import argparse
import sys
import os
import time

try:
    import clr
except ImportError:
    clr = None

# Configuration
DLL_NAME = "LibreHardwareMonitorLib.dll"

# Mock Classes for Simulation
class MockControl:
    def SetSoftware(self, val):
        print(f"    [SIM] Setting control to {val}%")

class MockSensor:
    def __init__(self, name, s_type, value):
        self.Name = name
        self.SensorType = s_type
        self.Value = value
        self.Control = MockControl()

class MockHardware:
    def __init__(self, name, h_type):
        self.Name = name
        self.HardwareType = h_type
        self.Sensors = []
        self.SubHardware = []
    def Update(self): pass

class MockComputer:
    def __init__(self):
        self.Hardware = []
        self.IsMotherboardEnabled = False
        self.IsCpuEnabled = False
        self.IsControllerEnabled = False
        
        # Populate with fake data
        mobo = MockHardware("Gigabyte B650", "Motherboard")
        
        # Mock Enums
        class Type:
            Control = "Control"
            Fan = "Fan"
        self.SensorType = Type()
        
        # Add sensors
        s1 = MockSensor("Fan Control #1", "Control", 50)
        s1.SensorType = self.SensorType.Control
        
        s2 = MockSensor("Pump Fan", "Fan", 3300)
        s2.SensorType = self.SensorType.Fan
        
        s3 = MockSensor("Pump Control", "Control", 100)
        s3.SensorType = self.SensorType.Control
        
        mobo.Sensors = [s1, s2, s3]
        self.Hardware.append(mobo)

    def Open(self): print("[SIM] Computer.Open()")
    def Close(self): print("[SIM] Computer.Close()")

def load_libre_hardware_monitor(sim_mode=False):
    """Loads the LibreHardwareMonitorLib.dll assembly or returns Mock."""
    if sim_mode:
        print("[SIM] Simulation Mode Enabled. Using Mock Hardware.")
        return MockComputer

    if not os.path.exists(DLL_NAME):
        print(f"Error: {DLL_NAME} not found.")
        print("Please download it from GitHub releases.")
        sys.exit(1)

    try:
        clr.AddReference(os.path.abspath(DLL_NAME))
        from LibreHardwareMonitor.Hardware import Computer
        return Computer
    except Exception as e:
        print(f"Error loading DLL: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

def get_all_sensors(hardware):
    """Recursively get all sensors from hardware and its sub-hardware."""
    sensors = []
    hardware.Update()
    sensors.extend(hardware.Sensors)
    for sub in hardware.SubHardware:
        sensors.extend(get_all_sensors(sub))
    return sensors

def list_sensors(computer):
    """Lists all fan sensors and controls."""
    print("\n--- System Status ---")
    found_any = False
    
    for hardware in computer.Hardware:
        print(f"\n[Hardware: {hardware.Name}]")
        
        all_sensors = get_all_sensors(hardware)
        
        for sensor in all_sensors:
            s_type = str(sensor.SensorType)
            if "Control" in s_type:
                print(f"  - Control: {sensor.Name:<20} | Value: {sensor.Value:>5.1f} %")
                found_any = True
            elif "Fan" in s_type:
                print(f"  - Sensor:  {sensor.Name:<20} | Value: {sensor.Value:>5.0f} RPM")
                found_any = True
    
    if not found_any:
        print("No fan sensors or controls found.")
    print("\n---------------------")

def select_control_and_fix(computer):
    """Scans for controls, asks user to select one, and runs the fix."""
    controls = []
    print("\nSelect a Control to Fix:")
    
    idx_counter = 1
    for hardware in computer.Hardware:
        all_sensors = get_all_sensors(hardware)
        for sensor in all_sensors:
            if "Control" in str(sensor.SensorType):
                controls.append(sensor)
                # Try to find parent hardware name if possible, or just use hardware.Name
                # Since we flattened it, we might lose the immediate parent name, 
                # but we can just show the sensor name which is usually unique enough.
                print(f"  {idx_counter}. {sensor.Name} (from {hardware.Name}) - Current: {sensor.Value}%")
                idx_counter += 1

    if not controls:
        print("No controllable fans found.")
        return

    while True:
        choice = input("\nEnter number (or 'b' to back): ")
        if choice.lower() == 'b':
            return
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(controls):
                fix_pump_noise(controls[idx])
                return
            print("Invalid number.")
        except ValueError:
            print("Please enter a number.")

def kill_msi_processes():
    """Detects and kills MSI Center processes."""
    import subprocess
    print("\nChecking for MSI Center processes...")
    try:
        # Get list of MSI processes
        cmd = "Get-Process | Where-Object { $_.Name -like '*MSI*' } | Select-Object -ExpandProperty Name"
        result = subprocess.run(["powershell", "-Command", cmd], capture_output=True, text=True)
        processes = [p.strip() for p in result.stdout.splitlines() if p.strip()]
        
        if not processes:
            print("No MSI Center processes found.")
            return

        print(f"Found conflicting processes: {', '.join(processes)}")
        choice = input("Do you want to terminate them to prevent interference? (y/n): ")
        if choice.lower() == 'y':
            for proc in processes:
                print(f"Terminating {proc}...")
                subprocess.run(["powershell", "-Command", f"Stop-Process -Name '{proc}' -Force"], capture_output=True)
            print("MSI Center processes terminated.")
        else:
            print("Skipping termination. Note: Fan control may be overwritten by MSI Center.")
            
    except Exception as e:
        print(f"Error checking processes: {e}")

def force_set_speed(control, value, duration=2):
    """Sets the speed repeatedly for a duration to fight other software."""
    end_time = time.time() + duration
    count = 0
    while time.time() < end_time:
        control.Control.SetSoftware(value)
        count += 1
        time.sleep(0.1)
    return count

def fix_pump_noise(control):
    """Performs the stop/start cycle to fix pump noise."""
    print(f"\nSelected Control: {control.Name}")
    print("Starting Fix Cycle...")
    
    # Step 1: Stop the pump
    print("Stopping pump (0%)...")
    # Force it for 3 seconds to ensure it stays off
    c = force_set_speed(control, 0, duration=3)
    print(f"  (Sent 0% command {c} times)")
    
    # Step 2: Full speed
    print("Restarting pump (100%)...")
    # Force it for 2 seconds
    c = force_set_speed(control, 100, duration=2)
    print(f"  (Sent 100% command {c} times)")
    
    print("Fix Cycle Complete. Pump set to 100%.")
    input("Press Enter to return to menu...")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--sim", action="store_true", help="Run in simulation mode")
    args = parser.parse_args()

    print("--- AIO Pump Noise Fixer ---")
    
    if not args.sim and clr is None:
        print("Warning: 'pythonnet' not installed or 'clr' import failed.")
        print("Running in SIMULATION mode automatically.")
        args.sim = True

    # Check for conflicts at startup
    if not args.sim:
        kill_msi_processes()

    Computer = load_libre_hardware_monitor(args.sim)
    computer = Computer()
    computer.IsMotherboardEnabled = True
    computer.IsCpuEnabled = True
    computer.IsControllerEnabled = True
    computer.Open()

    try:
        while True:
            print("\nMain Menu:")
            print("1. Show Fan/Pump Status")
            print("2. Run Fix Cycle (0% -> 100%)")
            print("3. Check/Kill MSI Center")
            print("4. Exit")
            
            choice = input("\nSelect an option: ")
            
            if choice == '1':
                list_sensors(computer)
            elif choice == '2':
                select_control_and_fix(computer)
            elif choice == '3':
                kill_msi_processes()
            elif choice == '4':
                break
            else:
                print("Invalid option.")
    finally:
        computer.Close()
        print("Hardware connection closed.")

if __name__ == "__main__":
    main()
