import subprocess

for i in range(255):
    command=['ping', '-n', '1','-w','100', '192.168.1.'+str(i)]
    subprocess.call(command)

arpa = subprocess.check_output(("arp", "-a")).decode("ascii")
n_devices=[x for x in arpa.split('\n') if '192.168.1' in x]  

for device in n_devices:
	print(device, "\n")
