import subprocess

#CPU reading might not be accurate
def get_CPU_temprature():   
    temp_output = subprocess.check_output(['sensors']).decode('utf-8')
    cpu_temp = temp_output.strip().split('\n')[2].split()[1]
    return cpu_temp



def get_CPU_usage():
    GPU_usage = round(100 - float(subprocess.check_output(['top', '-n', '1']).decode('utf-8').split("\n")[2].split()[7]), 3)
    return GPU_usage


print('CPU Usage: {}'.format(get_CPU_usage()))
print('CPU Temperature: {}°C'.format(get_CPU_temprature()))