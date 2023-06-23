import subprocess
import json

#CPU reading might not be accurate
def get_CPU_temperature():   
    command = "sensors -j"
    output = subprocess.check_output(command, shell=True)
    temp_output = json.loads(output)
    return temp_output["coretemp-isa-0000"]["Package id 0"]["temp1_input"]



def get_CPU_usage():  # sourcery skip: avoid-builtin-shadow
    def get_CPU_usage():
        cpu_stats = subprocess.check_output(["top","-b", "-n", "1"]).decode('utf-8').split("\n")[2]
        stats_list = cpu_stats.replace("%Cpu(s):", "").split(",")

        total_cpu_time = 0

        for stat in stats_list:
            key, value = stat.strip().split(" ", 1)
            key = key.strip()
            if value =="id":
                id = float(key)
                continue
            total_cpu_time +=float(key)
            
        cpu_utilization = round((total_cpu_time / (total_cpu_time + id)) * 100, 2)

        return cpu_utilization


print(f'CPU Usage: {get_CPU_usage()}')
print(f'CPU Temperature: {get_CPU_temperature()}')