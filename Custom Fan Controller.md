# Chat Conversation

Note: _This is purely the output of the chat conversation and does not contain any raw data, codebase snippets, etc. used to generate the output._

### User Input

i want to be able to control my pump fan which is acutally the water pump on an AIO.  it keeps dropping down to 2400 vs 3300 and making an anoying buzzing sound.  any fan software ive tired wont allow this level of granualar control over it to stop and start it to fix the speed and noise.  if we were to build an interface into this fan controller what libraries would we need and which language should we write the new fan fix controlller app

*Edited relevant file*

*User accepted the command `sensors && lsusb`*

*Edited relevant file*

*User accepted the command `ls -l /sys/class/hwmon/ && lsusb`*

*User accepted the command `lsusb`*

*User accepted the command `ls -l /sys/class/thermal/`*

*User accepted the command `cat /sys/class/thermal/cooling_device*/type`*

### User Input

does it matter that we are in wsl in windows 11 right now?

*Edited relevant file*

### User Input

1. DeepCool LS720 SE 360mm Liquid CPU Cooler
2. powershell

*Searched web for liquidctl support DeepCool LS720 SE*

*Edited relevant file*

*Searched web for DeepCool LS720 SE connection type USB or PWM*

*Edited relevant file*

*Edited relevant file*

### User Input

looks good proceed

*Edited relevant file*

*Edited relevant file*

*Edited relevant file*

### User Input

so how many modes does the script have are we able to show just a status output and confirm connectivity is good by outputting the fan stats / configuration

*Edited relevant file*

*Edited relevant file*

*Edited relevant file*

### User Input

ok lets run it through its modes and verify output

*Edited relevant file*

*User accepted the command `python3 pump_fix.py --sim`*

*Edited relevant file*

*Checked command status*

### User Input

continue

### User Input

ok so its running in admin here is the output.  this is still the test data though right?  not the real data?  do i need to download a dll?
PS Microsoft.PowerShell.Core\FileSystem::\\wsl.localhost\Ubuntu\home\ukmoon\Desktop\fanfix> python .\pump_fix.py
--- AIO Pump Noise Fixer ---
Warning: 'pythonnet' not installed or 'clr' import failed.
Running in SIMULATION mode automatically.
[SIM] Simulation Mode Enabled. Using Mock Hardware.
[SIM] Computer.Open()

Main Menu:
1. Show Fan/Pump Status
2. Run Fix Cycle
3. Exit

Select an option: 1

--- System Status ---

[Hardware: Gigabyte B650]
  - Control: Fan Control #1       | Value:  50.0 %
  - Sensor:  Pump Fan             | Value:  3300 RPM
  - Control: Pump Control         | Value: 100.0 %

---------------------

Main Menu:
1. Show Fan/Pump Status
2. Run Fix Cycle
3. Exit

Select an option:

### User Input

continue

*Edited relevant file*

### Planner Response

Yes, that is **Simulation Mode** (fake data). The script automatically switched to it because it couldn't find the required library.

To see **Real Data**, you need to do two things in your **Windows** PowerShell:

1.  **Install the Python library**:
    ```powershell
    pip install pythonnet
    ```
    *(If this fails, make sure you have Python installed on Windows, not just WSL)*

2.  **Download the DLL**:
    *   Download the zip from [LibreHardwareMonitor Releases](https://github.com/LibreHardwareMonitor/LibreHardwareMonitor/releases).
    *   Extract **`LibreHardwareMonitorLib.dll`** and put it in the **same folder** as [pump_fix.py](cci:7://file:///home/ukmoon/Desktop/fanfix/pump_fix.py:0:0-0:0) (which seems to be `\\wsl.localhost\Ubuntu\home\ukmoon\Desktop\fanfix`).

Once you do those two things, run `python pump_fix.py` again, and it should show real hardware!

*User accepted the command `pip install pythonnet`*

### User Input

this means we should use a venv? pip install pythonnet
error: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try apt install
    python3-xyz, where xyz is the package you are trying to
    install.
    
    If you wish to install a non-Debian-packaged Python package,
    create a virtual environment using python3 -m venv path/to/venv.
    Then use path/to/venv/bin/python and path/to/venv/bin/pip. Make
    sure you have python3-full installed.
    
    If you wish to install a non-Debian packaged Python application,
    it may be easiest to use pipx install xyz, which will manage a
    virtual environment for you. Make sure you have pipx installed.
    
    See /usr/share/doc/python3.12/README.venv for more information.

note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification.
╭─ ~/Desktop/fanfix ·········································································································· 23:22:41 ─╮
╰─❯                

*Edited relevant file*

### Planner Response

You are seeing that error because you ran the command in **Linux (WSL)** (the terminal with the `❯` prompt).

You need to install `pythonnet` on **Windows** so that the Windows Python can use it.

**Please switch back to your PowerShell window** (the one that said `PS Microsoft.PowerShell...`) and run the command there:

```powershell
pip install pythonnet
```

If that works, then run the script again:
```powershell
python pump_fix.py
```

### User Input

[notice] To update, run: C:\Users\mgant\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\python.exe -m pip install --upgrade pip
PS Microsoft.PowerShell.Core\FileSystem::\\wsl.localhost\Ubuntu\home\ukmoon\Desktop\fanfix> python .\pump_fix.py
--- AIO Pump Noise Fixer ---
Traceback (most recent call last):
  File "\\wsl.localhost\Ubuntu\home\ukmoon\Desktop\fanfix\pump_fix.py", line 202, in <module>
    main()
    ~~~~^^
  File "\\wsl.localhost\Ubuntu\home\ukmoon\Desktop\fanfix\pump_fix.py", line 173, in main
    Computer = load_libre_hardware_monitor(args.sim)
  File "\\wsl.localhost\Ubuntu\home\ukmoon\Desktop\fanfix\pump_fix.py", line 64, in load_libre_hardware_monitor
    if not os.path.exists(DLL_NAME):
           ^^
NameError: name 'os' is not defined. Did you forget to import 'os'?
PS Microsoft.PowerShell.Core\FileSystem::\\wsl.localhost\Ubuntu\home\ukmoon\Desktop\fanfix>

*Edited relevant file*

### Planner Response

Ah, my apologies! I accidentally removed the imports when I added the simulation mode. I've just fixed it.

Please run the script again in PowerShell:

```powershell
python pump_fix.py
```

It should work now!

### User Input

PS Microsoft.PowerShell.Core\FileSystem::\\wsl.localhost\Ubuntu\home\ukmoon\Desktop\fanfix> python .\pump_fix.py
--- AIO Pump Noise Fixer ---
Error: LibreHardwareMonitorLib.dll not found.
Please download it from GitHub releases.
PS Microsoft.PowerShell.Core\FileSystem::\\wsl.localhost\Ubuntu\home\ukmoon\Desktop\fanfix> ls

    Directory: \\wsl.localhost\Ubuntu\home\ukmoon\Desktop\fanfix

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-----          2025-12-04 11:25 PM           6355 pump_fix.py
-----          2025-12-04 10:59 PM             10 requirements.txt

PS Microsoft.PowerShell.Core\FileSystem::\\wsl.localhost\Ubuntu\home\ukmoon\Desktop\fanfix>

*Edited relevant file*

### Planner Response

Great, `pythonnet` is working now! The error confirms the script is running but can't find the **DLL file**.

You need to download **`LibreHardwareMonitorLib.dll`** and put it in that same folder (`fanfix`).

1.  **Download this zip file**: [LibreHardwareMonitor-v0.9.3.zip](https://github.com/LibreHardwareMonitor/LibreHardwareMonitor/releases/download/v0.9.3/LibreHardwareMonitor-v0.9.3.zip) (or the latest from [Releases](https://github.com/LibreHardwareMonitor/LibreHardwareMonitor/releases)).
2.  **Open the zip**.
3.  **Copy** the file named `LibreHardwareMonitorLib.dll`.
4.  **Paste** it into your `fanfix` folder (where [pump_fix.py](cci:7://file:///home/ukmoon/Desktop/fanfix/pump_fix.py:0:0-0:0) is).

Then run `python pump_fix.py` one more time!

### User Input

so what do we run or copy from :
C:\Users\mgant\Downloads\LibreHardwareMonitor-net472

*Edited relevant file*

### Planner Response

You need to copy just **one file** from that folder:

**File to copy:** `LibreHardwareMonitorLib.dll`

**Where to put it:** Paste it into your `fanfix` folder (the same place where [pump_fix.py](cci:7://file:///home/ukmoon/Desktop/fanfix/pump_fix.py:0:0-0:0) is).

You don't need to run anything from that downloaded folder. Just copy that DLL, then go back to PowerShell and run:

```powershell
python pump_fix.py
```

### User Input

PS Microsoft.PowerShell.Core\FileSystem::\\wsl.localhost\Ubuntu\home\ukmoon\Desktop\fanfix> python .\pump_fix.py
--- AIO Pump Noise Fixer ---
Error loading DLL: name 'clr' is not defined
PS Microsoft.PowerShell.Core\FileSystem::\\wsl.localhost\Ubuntu\home\ukmoon\Desktop\fanfix> ls -l
Get-ChildItem: Missing an argument for parameter 'LiteralPath'. Specify a parameter of type 'System.String[]' and try again.
PS Microsoft.PowerShell.Core\FileSystem::\\wsl.localhost\Ubuntu\home\ukmoon\Desktop\fanfix> ls

    Directory: \\wsl.localhost\Ubuntu\home\ukmoon\Desktop\fanfix

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-----          2025-12-04 11:27 PM         712192 LibreHardwareMonitorLib.dll
-----          2025-12-04 11:28 PM             25
-----          2025-12-04 11:25 PM           6355 pump_fix.py
-----          2025-12-04 10:59 PM             10 requirements.txt

PS Microsoft.PowerShell.Core\FileSystem::\\wsl.localhost\Ubuntu\home\ukmoon\Desktop\fanfix>

*Edited relevant file*

*Edited relevant file*

### Planner Response

I've fixed the `NameError`! It was a scoping issue with the `clr` import.

Please try running it again in PowerShell:

```powershell
python pump_fix.py
```

(Make sure you've copied the `LibreHardwareMonitorLib.dll` file to the folder first!)

### User Input

before we go any futher what is the 25 line item with no filename? PS Microsoft.PowerShell.Core\FileSystem::\\wsl.localhost\Ubuntu\home\ukmoon\Desktop\fanfix> ls

    Directory: \\wsl.localhost\Ubuntu\home\ukmoon\Desktop\fanfix

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-----          2025-12-04 11:27 PM         712192 LibreHardwareMonitorLib.dll
-----          2025-12-04 11:28 PM             25
-----          2025-12-04 11:29 PM           6351 pump_fix.py
-----          2025-12-04 10:59 PM             10 requirements.txt

PS Microsoft.PowerShell.Core\FileSystem::\\wsl.localhost\Ubuntu\home\ukmoon\Desktop\fanfix> 

*User accepted the command `ls -la /home/ukmoon/Desktop/fanfix`*

*Edited relevant file*

### Planner Response

That file is **`LibreHardwareMonitorLib.dll:Zone.Identifier`**.

It's a hidden Windows file that marks the DLL as "downloaded from the internet" (a security feature). It's completely harmless and you can ignore it.

**You are ready to go!**
Run the script now:
```powershell
python pump_fix.py
```

### User Input

PS Microsoft.PowerShell.Core\FileSystem::\\wsl.localhost\Ubuntu\home\ukmoon\Desktop\fanfix> python .\pump_fix.py
--- AIO Pump Noise Fixer ---
Error loading DLL: Could not load file or assembly 'file://\\wsl.localhost\Ubuntu\home\ukmoon\Desktop\fanfix\LibreHardwareMonitorLib.dll' or one of its dependencies. Operation is not supported. (Exception from HRESULT: 0x80131515)
File name: 'file://\\wsl.localhost\Ubuntu\home\ukmoon\Desktop\fanfix\LibreHardwareMonitorLib.dll' ---> System.NotSupportedException: An attempt was made to load an assembly from a network location which would have caused the assembly to be sandboxed in previous versions of the .NET Framework. This release of the .NET Framework does not enable CAS policy by default, so this load may be dangerous. If this load is not intended to sandbox the assembly, please enable the loadFromRemoteSources switch. See http://go.microsoft.com/fwlink/?LinkId=155569 for more information.
   at System.Reflection.RuntimeAssembly._nLoad(AssemblyName fileName, String codeBase, Evidence assemblySecurity, RuntimeAssembly locationHint, StackCrawlMark& stackMark, IntPtr pPrivHostBinder, Boolean throwOnFileNotFound, Boolean forIntrospection, Boolean suppressSecurityChecks)
   at System.Reflection.RuntimeAssembly.InternalLoadAssemblyName(AssemblyName assemblyRef, Evidence assemblySecurity, RuntimeAssembly reqAssembly, StackCrawlMark& stackMark, IntPtr pPrivHostBinder, Boolean throwOnFileNotFound, Boolean forIntrospection, Boolean suppressSecurityChecks)
   at System.Reflection.RuntimeAssembly.InternalLoadFrom(String assemblyFile, Evidence securityEvidence, Byte[] hashValue, AssemblyHashAlgorithm hashAlgorithm, Boolean forIntrospection, Boolean suppressSecurityChecks, StackCrawlMark& stackMark)
   at System.Reflection.Assembly.LoadFrom(String assemblyFile)
   at Python.Runtime.AssemblyManager.LoadAssemblyFullPath(String name)
   at Python.Runtime.CLRModule.AddReference(String name)


PS Microsoft.PowerShell.Core\FileSystem::\\wsl.localhost\Ubuntu\home\ukmoon\Desktop\fanfix>

*Edited relevant file*

### Planner Response

This is a classic Windows security error. Because the DLL was downloaded from the internet (and you are running it from a "network" path `\\wsl.localhost`), Windows is blocking it.

**The Fix:**
Run this command in your PowerShell window to "Unblock" the file:

```powershell
Unblock-File -Path .\LibreHardwareMonitorLib.dll
```

After you run that, try running the script again:
```powershell
python pump_fix.py
```

### User Input

PS Microsoft.PowerShell.Core\FileSystem::\\wsl.localhost\Ubuntu\home\ukmoon\Desktop\fanfix> Unblock-File -Path .\LibreHardwareMonitorLib.dll
PS Microsoft.PowerShell.Core\FileSystem::\\wsl.localhost\Ubuntu\home\ukmoon\Desktop\fanfix> python .\pump_fix.py
--- AIO Pump Noise Fixer ---
Error loading DLL: Could not load file or assembly 'file://\\wsl.localhost\Ubuntu\home\ukmoon\Desktop\fanfix\LibreHardwareMonitorLib.dll' or one of its dependencies. Operation is not supported. (Exception from HRESULT: 0x80131515)
File name: 'file://\\wsl.localhost\Ubuntu\home\ukmoon\Desktop\fanfix\LibreHardwareMonitorLib.dll' ---> System.NotSupportedException: An attempt was made to load an assembly from a network location which would have caused the assembly to be sandboxed in previous versions of the .NET Framework. This release of the .NET Framework does not enable CAS policy by default, so this load may be dangerous. If this load is not intended to sandbox the assembly, please enable the loadFromRemoteSources switch. See http://go.microsoft.com/fwlink/?LinkId=155569 for more information.
   at System.Reflection.RuntimeAssembly._nLoad(AssemblyName fileName, String codeBase, Evidence assemblySecurity, RuntimeAssembly locationHint, StackCrawlMark& stackMark, IntPtr pPrivHostBinder, Boolean throwOnFileNotFound, Boolean forIntrospection, Boolean suppressSecurityChecks)
   at System.Reflection.RuntimeAssembly.InternalLoadAssemblyName(AssemblyName assemblyRef, Evidence assemblySecurity, RuntimeAssembly reqAssembly, StackCrawlMark& stackMark, IntPtr pPrivHostBinder, Boolean throwOnFileNotFound, Boolean forIntrospection, Boolean suppressSecurityChecks)
   at System.Reflection.RuntimeAssembly.InternalLoadFrom(String assemblyFile, Evidence securityEvidence, Byte[] hashValue, AssemblyHashAlgorithm hashAlgorithm, Boolean forIntrospection, Boolean suppressSecurityChecks, StackCrawlMark& stackMark)
   at System.Reflection.Assembly.LoadFrom(String assemblyFile)
   at Python.Runtime.AssemblyManager.LoadAssemblyFullPath(String name)
   at Python.Runtime.CLRModule.AddReference(String name)


PS Microsoft.PowerShell.Core\FileSystem::\\wsl.localhost\Ubuntu\home\ukmoon\Desktop\fanfix>

*Edited relevant file*

### Planner Response

Ah, the error persists because you are running it from `\\wsl.localhost\...`, which Windows treats as a **Network Drive**. .NET blocks loading DLLs from network drives by default for security.

**The Solution:**
You need to move the `fanfix` folder to your **local Windows C: drive** (e.g., your Desktop).

1.  **Copy** the entire `fanfix` folder from your WSL location.
2.  **Paste** it onto your Windows Desktop.
3.  Open a **new PowerShell** window.
4.  `cd` to the new folder on your Desktop (e.g., `cd C:\Users\mgant\Desktop\fanfix`).
5.  Run `python pump_fix.py` from there.

This will bypass the network security restriction!

### User Input

i want us to pause on this task and im going to reopen you from windows powershell direct so it will be much easier to work on this.  i need you to output our current task state in a way i can reload you up over there

*Viewed [task.md](file:///home/ukmoon/.gemini/antigravity/brain/c0097c09-55c1-42bc-b8c6-02ec080da157/task.md) *

*Viewed [pump_fix.py](file:///home/ukmoon/Desktop/fanfix/pump_fix.py) *

*Viewed [requirements.txt](file:///home/ukmoon/Desktop/fanfix/requirements.txt) *

### Planner Response

Here is the current state of your project so you can pick it up easily in Windows PowerShell.

### **Current Status**
*   **Goal**: Control DeepCool LS720 SE pump speed to fix buzzing.
*   **Method**: Python script using `LibreHardwareMonitorLib.dll` to control motherboard headers.
*   **Blocker**: Running from WSL caused network security errors with the DLL. Moving to a local Windows folder will fix this.

### **Next Steps (Run these in your new PowerShell window)**

1.  **Create a folder** on your Desktop (e.g., `fanfix`).
2.  **Create the files** ([pump_fix.py](cci:7://file:///home/ukmoon/Desktop/fanfix/pump_fix.py:0:0-0:0) and [requirements.txt](cci:7://file:///home/ukmoon/Desktop/fanfix/requirements.txt:0:0-0:0)) with the content below.
3.  **Download the DLL**:
    *   Download [LibreHardwareMonitor-v0.9.3.zip](https://github.com/LibreHardwareMonitor/LibreHardwareMonitor/releases/download/v0.9.3/LibreHardwareMonitor-v0.9.3.zip).
    *   Extract `LibreHardwareMonitorLib.dll` into your `fanfix` folder.
4.  **Unblock the DLL** (Important!):
    ```powershell
    Unblock-File -Path .\LibreHardwareMonitorLib.dll
    ```
5.  **Install Dependencies**:
    ```powershell
    pip install -r requirements.txt
    ```
6.  **Run the Script**:
    ```powershell
    python pump_fix.py
    ```

---

### **File 1: [requirements.txt](cci:7://file:///home/ukmoon/Desktop/fanfix/requirements.txt:0:0-0:0)**
```text
pythonnet
```

### **File 2: [pump_fix.py](cci:7://file:///home/ukmoon/Desktop/fanfix/pump_fix.py:0:0-0:0)**
```python
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
        sys.exit(1)

def list_sensors(computer):
    """Lists all fan sensors and controls without asking for selection."""
    print("\n--- System Status ---")
    found_any = False
    for hardware in computer.Hardware:
        hardware.Update()
        
        # Handle Mock vs Real Enum types slightly differently if needed, 
        # but if we structure Mock correctly it should be transparent.
        # For simplicity in this hybrid script, we'll do a quick check or duck typing.
        
        # Helper to get type string
        def get_type(s):
            return str(s.SensorType)

        print(f"\n[Hardware: {hardware.Name}]")
        for sub_hardware in hardware.SubHardware:
            sub_hardware.Update()
            
        for sensor in hardware.Sensors:
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
        hardware.Update()
        for sensor in hardware.Sensors:
            if "Control" in str(sensor.SensorType):
                controls.append(sensor)
                print(f"  {idx_counter}. {sensor.Name} ({hardware.Name}) - Current: {sensor.Value}%")
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

def fix_pump_noise(control):
    """Performs the stop/start cycle to fix pump noise."""
    print(f"\nSelected Control: {control.Name}")
    print("Starting Fix Cycle...")
    
    # Step 1: Stop the pump
    print("Stopping pump (0%)...")
    control.Control.SetSoftware(0) 
    time.sleep(3) # Wait for it to spin down
    
    # Step 2: Full speed
    print("Restarting pump (100%)...")
    control.Control.SetSoftware(100)
    time.sleep(2)
    
    print("Fix Cycle Complete. Check if the noise is gone.")
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
            print("2. Run Fix Cycle")
            print("3. Exit")
            
            choice = input("\nSelect an option: ")
            
            if choice == '1':
                list_sensors(computer)
            elif choice == '2':
                select_control_and_fix(computer)
            elif choice == '3':
                break
            else:
                print("Invalid option.")
    finally:
        computer.Close()
        print("Hardware connection closed.")

if __name__ == "__main__":
    main()
```