import subprocess
import json

#CPU reading might not be accurate
def get_CPU_temperature():   
    command = "sensors -j"
    output = subprocess.check_output(command, shell=True)
    temp_output = json.loads(output)
    return temp_output["coretemp-isa-0000"]["Package id 0"]["temp1_input"]



def get_CPU_usage():
    return round(
        100
        - float(
            subprocess.check_output(['top', '-n', '1'])
            .decode('utf-8')
            .split("\n")[2]
            .split()[7]
        ),
        3,
    )


print(f'CPU Usage: {get_CPU_usage()}')
print(f'CPU Temperature: {get_CPU_temperature()}')