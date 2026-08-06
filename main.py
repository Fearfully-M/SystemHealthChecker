import psutil
import time


def main(): 
    psutil.cpu_percent()
    timeOverThreshold = 0 # seconds CPU is over 90% utilization
    intervalTime = 5 # number of seconds for a measured interval of time
    thresholdPercentage = 90.0 # determined limit considered to be the threshold
    alertDurationSeconds = 10 # duration of when user should be alerted if over threshold 
    memoryThresholdPercentage = 90 # threshold limit for memory

    while True:
        time.sleep(intervalTime)
        CPU_utilization = psutil.cpu_percent() # to aborb the first placeholder value
        print(CPU_utilization)
        memory = psutil.virtual_memory()
        print(memory.percent)

        # determine if CPU utilization is over threshold 
        if CPU_utilization > thresholdPercentage:
            timeOverThreshold+=intervalTime # add interval time 
            print("Threshold Percentage:", thresholdPercentage)
            if timeOverThreshold >= alertDurationSeconds:
                print("CPU Utilization is over 90 percent.")

        # reset the time over threshold if utilization is under the threshold limit
        elif CPU_utilization <= thresholdPercentage:
            timeOverThreshold = 0

        # check if memory utilization is over the threshold
        if memory.percent > memoryThresholdPercentage:
            print("Memory utilization is over 90 percent.")



if __name__ == "__main__":
    main()