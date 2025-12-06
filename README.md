# FanFix - AIO Pump Noise Fixer

This tool is designed to fix a buzzing noise from AIO pump fans (specifically on MSI motherboards, but may work for others) by cycling the pump speed. It also provides a dashboard to view fan speeds, pump status, and system temperatures.

## Features

- **Pump Noise Fix**: Cycles the selected fan/pump control from 0% to 100% to clear air bubbles or reset the pump mechanism, which often resolves buzzing noises.
- **System Monitor**: Displays real-time status of:
    - Fan Controls (%)
    - Fan Speeds (RPM)
    - System Temperatures (°C) (CPU, VRM, System, etc.)
- **Conflict Management**: Detects and offers to kill MSI Center processes that might conflict with fan control.

## Requirements

- Windows OS
- Python 3.x
- [LibreHardwareMonitorLib.dll](https://github.com/LibreHardwareMonitor/LibreHardwareMonitor/releases) (Included in this repo or download separately)
- **Administrator Privileges**: required to access hardware sensors and controls.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/mgantlett/fanfix.git
   cd fanfix
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   *(Note: primarily requires `pythonnet`)*

## Usage

**IMPORTANT: You must run this script as Administrator.**

1. Open a terminal (PowerShell or Command Prompt) as Administrator.
2. Run the script:
   ```bash
   python pump_fix.py
   ```

### Menu Options
1. **Show Fan/Pump Status**: Lists all detected fans, controls, and temperature sensors.
2. **Run Fix Cycle**: Prompts you to select a specific control (e.g., Pump Fan) and runs the stop/start cycle.
3. **Check/Kill MSI Center**: Checks for interfering MSI software and allows you to terminate it.

## Troubleshooting

- **DLL Not Found**: Ensure `LibreHardwareMonitorLib.dll` is in the same directory as the script.
- **Access Denied**: Make sure you are running the terminal as Administrator.
- **Simulation Mode**: If the DLL cannot be loaded, the script will default to a simulation mode with mock data.

## Liability

Use this tool at your own risk. Controlling hardware fans manually involves risks. Ensure you do not leave critical cooling components (like CPU fans) off for extended periods.
