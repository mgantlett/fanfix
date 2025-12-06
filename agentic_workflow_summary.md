# Agentic Workflow Case Study: Fixing AIO Pump Noise

This project demonstrates how an Agentic LLM acts not just as a code generator, but as a **reasoning engine (CPU)** that navigates complex environments, debugs runtime failures, and adapts to system constraints.

## The Mission
**Goal**: Fix a noisy AIO pump (DeepCool LS720 SE) that kept dropping RPM, causing a buzzing sound.
**Constraint**: Manufacturer software (MSI Center) failed to lock the speed.
**Solution**: Build a custom Python tool to hijack the motherboard's fan controller.

## The Workflow (LLM as CPU)

### 1. Context Awareness & Platform Adaptation
*   **Initial State**: User was in WSL (Linux subsystem).
*   **Agent Action**: Recognized that hardware access requires direct Windows drivers.
*   **Adaptation**: Directed the user to migrate the workspace to the Windows Desktop to bypass network drive security restrictions on loading .NET DLLs.

### 2. Dependency Hell & Dynamic Problem Solving
*   **Issue**: The app crashed immediately.
*   **Agent Action**:
    1.  Switched to "Simulation Mode" to verify logic (it worked).
    2.  Wrote a minimal `test_dll.py` to isolate the failure.
    3.  Identified a missing dependency (`HidSharp.dll`) that wasn't in the initial download.
    4.  **Execution**: Found the correct release URL, downloaded it, extracted the specific missing file, and unblocked it.

### 3. Debugging "Invisible" Hardware
*   **Issue**: The app ran but reported "No sensors found."
*   **Agent Action**:
    1.  Hypothesized that sensors might be named differently or hidden.
    2.  **Tool Creation**: Wrote a custom diagnostic tool (`diagnose_sensors.py`) to dump the entire raw hardware tree.
    3.  **Discovery**: Found the sensors were nested deep under a "SuperIO" chip, not at the top level.
    4.  **Refactor**: Rewrote the main application to use **recursive search**, instantly making the sensors visible.

### 4. Overcoming Security & Antivirus Blocks
*   **Issue**: Windows Defender blocked the driver (`LibreHardwareMonitorLib.sys`) as a "Vulnerable Driver."
*   **Agent Action**: Explained the technical nuance (legitimate tools use low-level drivers that *can* be exploited) and guided the user to whitelist the specific file, distinguishing a false positive from a real threat.

### 5. The "Boss Fight": Software Conflict
*   **Issue**: The script sent the "100% Speed" command, but the pump ignored it.
*   **Reasoning**: The agent deduced that the manufacturer software (MSI Center) was likely fighting back, overwriting the command milliseconds later.
*   **Agent Action**:
    1.  Confirmed the theory by scanning running processes.
    2.  **Feature Implementation**: Added a "Kill Switch" to terminate MSI Center.
    3.  **Tactical Upgrade**: Implemented a "Force Mode" that spams the command repeatedly for 2 seconds to override any lingering background services.

## Conclusion
The LLM didn't just "write a script." It:
*   **Diagnosed** system-level permissions.
*   **Debugged** missing binary dependencies.
*   **Reverse-engineered** the hardware tree structure.
*   **Navigated** antivirus security policies.
*   **Architected** a solution to defeat conflicting software.

This is **Agentic AI**: Moving beyond text generation to **stateful, goal-oriented problem solving**.
