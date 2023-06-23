import subprocess

def get_ram_details():
	cmd = ["free", "-h"]
	result = subprocess.run(cmd, stdout=subprocess.PIPE)
	output = result.stdout.decode('utf-8').strip().split('\n')[1].split()
	del output[0]
	total_memory, used_memory, free_memory, shared_memory, buff_cache, available_memory = output
	return {
		"Total_Memory": total_memory,
		"Used_memory": used_memory,
		"Free_Memory": free_memory,
		"Shared_Memory": shared_memory,
		"Buff_Cache": buff_cache,
		"Available_Memory": available_memory,
	}





if __name__ == '__main__':
    ram_details = get_ram_details()
    print(ram_details)