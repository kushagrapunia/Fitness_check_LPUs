import subprocess as sp
import json
import codecs
import re


#CPU reading might not be accurate
def get_cpu_temprature():   
    temp_output = sp.check_output(['sensors']).decode('utf-8')
    cpu_temp = temp_output.strip().split('\n')[2].split()[1]
    return cpu_temp


def get_cpu_usage():
    cpu_usage = round(100 - float(sp.check_output(['top', '-n', '1']).decode('utf-8').split("\n")[2].split()[7]), 3)
    return cpu_usage

#considering_only_NVIDIA_GPUs
def get_gpu_details():
    result = sp.check_output(["nvidia-smi", 
                                "--query-gpu=name,driver_version,memory.total,memory.used,memory.free,temperature.gpu", 
                                "--format=csv,noheader"])
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

def get_ram_details():
    cmd = ["free", "-h"]
    result = sp.check_output(["free", "-h"])
    output = result.decode('utf-8').strip().split('\n')[1].split()
    del output[0]
    ram_details = {}
    total_memory, used_memory, free_memory, shared_memory, buff_cache, available_memory = output
    ram_details = {
                    "Total_Memory": total_memory,
                    "Used_memory": used_memory,
                    "Free_Memory": free_memory,
                    "Shared_Memory": shared_memory,
                    "Buff_Cache": buff_cache,
                    "Available_Memory": available_memory
                    }
    return ram_details

def get_ping_details(to_ping_ip, no_of_pings, time_limit):
    pinging = sp.run(f"ping -c {no_of_pings} -w {time_limit} " + to_ping_ip, stdout=sp.PIPE, shell=True)
    ping_stats = pinging.stdout.decode().split("\n")[-4:-1]
    ping_ip, packets_transmited, packets_recieved, packet_loss_percent, total_ping_time, round_trip_time_average = ping_stats[0].split()[1], ping_stats[1].split()[0], ping_stats[1].split()[3], ping_stats[1].split()[5], ping_stats[1].split()[-1], ping_stats[2].split()[3].split("/")[1]
    ping_details = {
                    "ping_ip": ping_ip, 
                    "packets_transmited": packets_transmited, 
                    "packets_recieved": packets_recieved, 
                    "packet_loss_percent": packet_loss_percent, 
                    "total_ping_time": total_ping_time, 
                    "round_trip_time_average": round_trip_time_average
                    }
    return ping_details


class Fitness_Check():

    def __init__(self):
        self.gpu_stats = get_gpu_details()
        self.cpu_usage = get_cpu_usage()
        self.ram_stats = get_ram_details()

    def ping_cameras(json_data):
        IPv4_regex = r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"
        camera_list_ip = []
        camera_list = json_data["camera_list"]
        for individual_camera in camera_list:
            camera_list_ip.append(re.findall(IPv4_regex, individual_camera["IP"])[0])
        
        camera_ping_details = {}
        for x in camera_list_ip:
            camera_ping_details.append(get_ping_details(x,10,10))

        return camera_ping_details

        
    


if __name__=="__main__":
    # dummy_json = "dummy_json.json"
    # json_data = json.load(open(dummy_json, mode="r", encoding="utf-8"))
    # fitness_check = Fitness_Check()
    # cameras_ping_details = fitness_check.ping_cameras(json_data)
    print(f"CPU temperature: {get_cpu_temprature()}\nCPU usage: {get_cpu_usage()}\n RAM stats: {get_ram_details()}\n, GPU stats: {get_gpu_details()}")
