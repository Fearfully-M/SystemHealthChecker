import psutil
import time


def main(): 
    psutil.cpu_percent()
    timeOverThreshold = 0 # seconds CPU is over 90% utilization
    intervalTime = 5 # number of seconds for a measured interval of time
    thresholdPercentage = 90.0 # determined limit considered to be the threshold
    alertDurationSeconds = 10 # duration of when user should be alerted if over threshold 

    while True:
        time.sleep(intervalTime)
        CPU_utilization = psutil.cpu_percent()
        print(CPU_utilization)

        if CPU_utilization > thresholdPercentage:
            timeOverThreshold+=intervalTime
            print("Threshold Percentage:", thresholdPercentage)
            # print(timeOverThreshold, "this is time overthreshold")
            if timeOverThreshold >= alertDurationSeconds:
                print("CPU Utilization is over 90 percent.")

        elif CPU_utilization <= thresholdPercentage:
            timeOverThreshold = 0



if __name__ == "__main__":
    main()