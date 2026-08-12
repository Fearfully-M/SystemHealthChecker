import psutil
import time
from datetime import datetime as dt

def main(): 
    psutil.cpu_percent()
    timeOverThreshold = 0 # seconds CPU is over 90% utilization
    intervalTime = 5 # number of seconds for a measured interval of time
    thresholdPercentage = 90.0 # determined limit considered to be the threshold
    alertDurationSeconds = 10 # duration of when user should be alerted if over threshold 
    memoryThresholdPercentage = 90 # threshold limit for memory
    diskThresholdPercentage = 90 # threshold limit for disk usage
    filename = "System_Log_Initiated "+ dt.now().strftime("%Y-%m-%d_%H-%M-%S") 

    # try allows for a clean KeyboardInterrupt escape
    try:
        while True:
            alert = False # default alert to false assume no issues initially
            time.sleep(intervalTime)
            CPU_utilization = psutil.cpu_percent() # to aborb the first placeholder value
            print(CPU_utilization)
            memory = psutil.virtual_memory()
            disk_usage = psutil.disk_usage("/") # disk usage
            print(memory.percent)

            # determine if CPU utilization is over threshold 
            if CPU_utilization > thresholdPercentage:
                timeOverThreshold+=intervalTime # add interval time 
                print("Threshold Percentage:", thresholdPercentage)
                if timeOverThreshold >= alertDurationSeconds:
                    print("CPU Utilization is over 90 percent.")
                    alert = True

            # reset the time over threshold if utilization is under the threshold limit
            elif CPU_utilization <= thresholdPercentage:
                timeOverThreshold = 0

            # check if memory utilization is over the threshold
            if memory.percent > memoryThresholdPercentage:
                print("Memory utilization is over 90 percent.")
                alert = True

            # check if disk usage utilization is over the threshold
            if disk_usage.percent > diskThresholdPercentage: 
                print("Disk utilization is over 90 percent.")
                alert = True

            # print to the log file the results of this loop cycle
            log_reading(CPU_utilization,memory,disk_usage,alert,filename)

    # exit the program cleanly
    except KeyboardInterrupt:
        print("\nExited System Monitoring")


# reads the system and processes and saves the results in a csv file
def log_reading(cpu, memory, disk, alert, filename):
    alertTag = ""

    # attempt to write system processes to the output file
    try: 
        with open(filename, "a") as f:
            if alert is True:
                alertTag = "ALERT: "
            results = f.write(f"{alertTag}CPU: {cpu}%, Memory: {memory.percent}%, Disk: {disk.percent}% " + dt.now().strftime("%Y-%m-%d_%H-%M-%S")+ "\n")

    # if the file is unable to be written to (i.e. permission, no storage) print back to the screen
    except OSError:
        print("\n Unable to write to file.")


if __name__ == "__main__":
    main()