import subprocess

saitama_ip = "192.168.29.55"

no_of_pings = "5"
time_limit = "5"
pinging = subprocess.run(f"ping -c {no_of_pings} -w {time_limit} " + saitama_ip, stdout=subprocess.PIPE, shell=True)
ping_stats = pinging.stdout.decode().split("\n")[-4:-1]
ping_ip, packets_transmited, packets_recieved, packet_loss_percent, total_ping_time, round_trip_time_average = ping_stats[0].split()[1], ping_stats[1].split()[0], ping_stats[1].split()[3], ping_stats[1].split()[5], ping_stats[1].split()[-1], ping_stats[2].split()[3].split("/")[1]
ping_details = {"ping_ip": ping_ip, "packets_transmited": packets_transmited, "packets_recieved": packets_recieved, "packet_loss_percent": packet_loss_percent, "total_ping_time": total_ping_time, "round_trip_time_average": round_trip_time_average}
print(round_trip_time_average)