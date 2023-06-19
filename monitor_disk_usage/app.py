import psutil
import time

def monitor_cpu():

    cpu_percent = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_percent}%")

def monitor_memory():
    mem = psutil.virtual_memory()
    total_memory = mem.total / 1024 ** 3  # Convert bytes to GB
    available_memory = mem.available / 1024 ** 3
    used_memory = mem.used / 1024 ** 3
    memory_percent = mem.percent
    print(f"Total Memory: {total_memory:.2f}GB")
    print(f"Available Memory: {available_memory:.2f}GB")
    print(f"Used Memory: {used_memory:.2f}GB")
    print(f"Memory Usage: {memory_percent}%")

def monitor_disk():
    disk = psutil.disk_usage('/')
    total_disk = disk.total / (1024 ** 3)  # Convert bytes to GB
    used_disk = disk.used / (1024 ** 3)
    free_disk = disk.free / (1024 ** 3)
    disk_percent = disk.percent
    print(f"Total Disk Space: {total_disk:.2f}GB")
    print(f"Used Disk Space: {used_disk:.2f}GB")
    print(f"Free Disk Space: {free_disk:.2f}GB")
    print(f"Disk Usage: {disk_percent}%")

def main():
    print("Starting hardware monitoring...")
    while True:
        print("+=======================================================================================")
        monitor_cpu()  # Replace with the desired function: monitor_cpu, monitor_memory, or monitor_disk
        monitor_memory()
        monitor_disk()
        print("+=======================================================================================")
        time.sleep(10)
        print("\n")

if __name__ == '__main__':
    main()