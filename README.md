# System Health Monitor

A Python system health monitor that tracks CPU, memory, and disk utilization, logs readings to a timestamped file, and flags threshold-crossing alerts in real time.

## Overview

**System Health Monitor** is a Python-based system monitoring utility built with `psutil`. It periodically checks the system's CPU, memory, and root disk utilization and records the results to a timestamped log file.

The monitor runs continuously at **5-second intervals** and uses configurable utilization thresholds to identify potential resource issues.

CPU utilization receives additional handling to reduce false positives caused by normal, short-lived CPU spikes. A CPU alert is only generated when utilization remains above 90% for at least **10 consecutive seconds**. Memory and disk utilization generate an alert whenever a reading exceeds 90%.

The project also demonstrates graceful program termination and basic file-system error handling.

## Features

* **CPU Monitoring**

  * Tracks CPU utilization as a percentage.
  * Triggers an alert when CPU utilization remains above 90% for 10 seconds or longer.
  * Uses a persistence threshold to reduce false positives from short CPU spikes.

* **Memory Monitoring**

  * Tracks system memory utilization as a percentage.
  * Generates an alert when utilization exceeds 90%.

* **Disk Monitoring**

  * Tracks root disk (`/`) utilization as a percentage.
  * Generates an alert when utilization exceeds 90%.

* **Timestamped Logging**

  * Records system health readings every 5 seconds.
  * Creates a uniquely timestamped log file when the program starts.
  * Records the date and time associated with each reading.

* **Graceful Shutdown**

  * Uses `KeyboardInterrupt` handling to allow the monitor to be stopped cleanly with `Ctrl+C`.
  * Avoids displaying an unnecessary traceback when the program is intentionally terminated.

* **File Error Handling**

  * Handles `OSError` exceptions when the log file cannot be written.
  * Allows the monitoring process to continue running if writing to the log file fails.

## How It Works

The monitoring loop follows a simple process:

1. Wait for the configured 5-second monitoring interval.
2. Collect CPU utilization using `psutil`.
3. Collect memory utilization using `psutil`.
4. Collect root disk utilization using `psutil`.
5. Compare each measurement against its threshold.
6. Track how long CPU utilization remains above its threshold.
7. Determine whether the current reading should be marked as an alert.
8. Write the reading and timestamp to the system log.
9. Repeat until the program is manually stopped.

### Alert Logic

| Resource | Threshold | Alert Condition                          |
| -------- | --------: | ---------------------------------------- |
| CPU      |     > 90% | Remains above threshold for ≥ 10 seconds |
| Memory   |     > 90% | Alert generated when detected            |
| Disk     |     > 90% | Alert generated when detected            |

CPU is handled differently because CPU utilization can naturally spike for short periods when applications are launched or other intensive operations occur. Requiring the CPU to remain above the threshold for 10 seconds helps prevent these temporary spikes from generating unnecessary alerts.

## Tech Stack

* **Python 3.13.5**
* **[psutil](https://github.com/giampaolo/psutil)** — system and process monitoring
* **`time`** — monitoring interval and timing logic
* **`datetime`** — timestamp generation
* **File I/O** — persistent system health logging

## Project Structure

```text
SystemHealthChecker/
├── main.py
├── requirements.txt
└── README.md
```

## Getting Started

### Prerequisites

Make sure Python 3.13.5 or a compatible Python 3 version is installed.

Verify your Python installation:

```bash
python3 --version
```

### Installation

Clone the repository:

```bash
git clone https://github.com/Fearfully-M/SystemHealthChecker.git
```

Navigate into the project directory:

```bash
cd SystemHealthChecker
```

Install the required dependency:

```bash
pip3 install -r requirements.txt
```

## Usage

Start the system monitor with:

```bash
python3 main.py
```

The program will begin collecting system utilization data every 5 seconds.

A log file is automatically created when the monitor starts. The filename includes the date and time the monitoring session began:

```text
System_Log_Initiated 2026-08-12_01-00-00
```

Example log output:

```text
CPU: 24.5%, Memory: 67.2%, Disk: 81.4% 2026-08-12_01-00-05
CPU: 31.8%, Memory: 67.5%, Disk: 81.4% 2026-08-12_01-00-10
ALERT: CPU: 94.2%, Memory: 68.1%, Disk: 81.4% 2026-08-12_01-00-20
```

To stop the monitor, press:

```text
Ctrl+C
```

The program will exit gracefully and display:

```text
Exited System Monitoring
```

## Error Handling

The monitor includes basic error handling for two expected situations.

## Hybrid Logging 

Hybrid-logging: instead of simply writing to a txt file the resources that pass the predetermined threshold, the monitor writes every resource to the file on every interval with timestamps. This is important so a user can diagnose potential issues before they arise that might not surpass the predetermined threshold (high CPU usage on a normally low CPU usage application). These values are also important for statistical analysis to get trends on how the machine performs over long durations of time

### Keyboard Interrupt


Because the monitoring process runs continuously, `KeyboardInterrupt` is handled so the user can terminate the program without receiving a Python traceback.

### File System Errors

Log writing is wrapped in an `OSError` handler. If the program cannot write to the log file—for example, because of a permissions issue or insufficient storage—the error is handled without terminating the monitoring loop.

The program reports:

```text
Unable to write to file.
```

while continuing to monitor system resources.

## Future Enhancements

The current implementation intentionally keeps the project lightweight. Possible future improvements include:

### CSV Logging

Replace or supplement the current text-based logging system with CSV output.

This would make the collected data easier to analyze programmatically and could provide a foundation for generating statistics and visualizations.

### Web-Based Monitoring Dashboard

A future version could use **Flask** to expose system health data through a simple web application.

The monitoring data could be displayed through an HTML dashboard, allowing users to visually track:

* CPU utilization
* Memory utilization
* Disk utilization
* Alert events
* Historical resource usage

This would turn the current command-line monitoring tool into a small web-based monitoring application.

### Additional Monitoring Capabilities

The project could also be expanded to monitor additional system resources, such as:

* Network utilization
* Individual processes
* CPU temperature where supported
* Disk I/O
* Network connections

## Project Goals

This project was built as a practical exercise in Python system monitoring and resource management.

The primary goals were to practice:

* Working with third-party Python libraries
* Reading system-level metrics
* Implementing threshold-based logic
* Managing time-based conditions
* Writing persistent log data
* Handling runtime exceptions
* Designing a continuously running process
* Gracefully terminating a long-running program

## License MIT


Built as a portfolio project to demonstrate practical use of the pscutil Python Library and system resources and monitoring checking
