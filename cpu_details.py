import subprocess

#CPU reading might not be accurate
def get_CPU_temperature():   
    temp_output = subprocess.check_output(['sensors']).decode('utf-8')
    return temp_output.strip().split('\n')[2].split()[1]



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