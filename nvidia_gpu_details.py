import subprocess

def get_gpu_details():
    """
    Run the nvidia-smi command and return GPU details as a dictionary
    """
    result = subprocess.check_output(["nvidia-smi", "--query-gpu=name,driver_version,memory.total,memory.used,memory.free,temperature.gpu", "--format=csv,noheader"])
    output = result.decode('utf-8').strip()
    gpu_details = {}
    gpu = output.split(', ')
    name, driver_version, memory_total, memory_used, memory_free, temperature = gpu
    gpu_details = {
        "GPU_name": name,
        "memory_total": memory_total,
        "driver_version": driver_version,
        "memory_used": memory_used,
        "memory_free": memory_free,
        "temperature": temperature
    }
    return gpu_details

if __name__ == '__main__':
    gpu_details = get_gpu_details()
    print(gpu_details)