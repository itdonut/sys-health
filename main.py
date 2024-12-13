import sys
import os
import platform
import psutil
import GPUtil

def main() -> None:
    # Get OS name and version
    os_name = os.name  # This returns 'nt' for Windows
    system_name = platform.system()  # This returns the OS name, e.g., 'Windows'
    version = platform.version()  # This returns the OS version, e.g., '10.0.19041'

    # Get detailed information
    release = platform.release()  # This returns the release, e.g., '10'
    detailed_version = platform.platform()  # This returns a detailed version string

    print(f"OS Name: {system_name}")
    print(f"OS Version: {version}")
    print(f"OS Release: {release}")
    print(f"Detailed Version: {detailed_version}")

    # Get basic CPU info
    cpu_info = platform.processor()

    print(f"Processor: {cpu_info}")

    # Get CPU details
    cpu_count = psutil.cpu_count(logical=True)  # Logical cores
    physical_cores = psutil.cpu_count(logical=False)  # Physical cores
    cpu_freq = psutil.cpu_freq()  # CPU frequency

    print(f"Physical Cores: {physical_cores}")
    print(f"Logical Cores: {cpu_count}")
    print(f"Max Frequency: {cpu_freq.max:.2f} MHz")
    print(f"Current Frequency: {cpu_freq.current:.2f} MHz")

    # Get RAM details
    virtual_memory = psutil.virtual_memory()

    total_ram = virtual_memory.total  # Total physical memory
    available_ram = virtual_memory.available  # Available memory
    used_ram = virtual_memory.used  # Used memory
    ram_percentage = virtual_memory.percent  # RAM usage percentage

    print(f"Total RAM: {total_ram / (1024 ** 3):.2f} GB")
    print(f"Available RAM: {available_ram / (1024 ** 3):.2f} GB")
    print(f"Used RAM: {used_ram / (1024 ** 3):.2f} GB")
    print(f"RAM Usage: {ram_percentage}%")

    # Get ROM details
    # Initialize totals
    total_rom = 0
    used_rom = 0
    free_rom = 0

    # Get storage details for each partition
    partitions = psutil.disk_partitions()

    for partition in partitions:
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
            total_rom += partition_usage.total
            used_rom += partition_usage.used
            free_rom += partition_usage.free

            print(f"Drive: {partition.device}")
            print(f"  Total Size: {partition_usage.total / (1024 ** 3):.2f} GB")
            print(f"  Used: {partition_usage.used / (1024 ** 3):.2f} GB")
            print(f"  Free: {partition_usage.free / (1024 ** 3):.2f} GB")
            print(f"  Usage: {partition_usage.percent}%\n")
        except PermissionError:
            print(f"Drive: {partition.device} - Permission Denied\n")

    # Display total storage info
    print("---- Total Storage Across All Drives ----")
    print(f"Total Storage: {total_rom / (1024 ** 3):.2f} GB")
    print(f"Used Storage: {used_rom / (1024 ** 3):.2f} GB")
    print(f"Free Storage: {free_rom / (1024 ** 3):.2f} GB")

    # Get all available GPUs
    gpus = GPUtil.getGPUs()

    for gpu in gpus:
        print(f"GPU ID: {gpu.id}")
        print(f"Name: {gpu.name}")
        print(f"Load: {gpu.load * 100:.2f}%")
        print(f"Free Memory: {gpu.memoryFree:.2f} MB")
        print(f"Used Memory: {gpu.memoryUsed:.2f} MB")
        print(f"Total Memory: {gpu.memoryTotal:.2f} MB")
        print(f"Temperature: {gpu.temperature:.2f} °C")
        print(f"UUID: {gpu.uuid}")
        print("-" * 30)


if __name__ == '__main__':
    main()