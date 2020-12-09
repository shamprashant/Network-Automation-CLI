from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException
import time
import log

#expect language
#TCL language


def do_backup():
	
	try:

		IP = input('\n\nEnter your device ip: ')

		device1 = {
			'device_type': 'cisco_ios',
			'ip': IP,
			'username': 'prashant',
			'password': 'cisco'
		}

		conn = ConnectHandler(**device1)

		print('\n\n')
		log.info('Connected with ' + IP)
		log.info('Script has taken control of the device\n')

		time.sleep(2)

		conn.send_command('term length 0')
		output = conn.send_command('show run')

		with open(IP + ' backp.txt','w') as file:
			file.write(output)

		log.info('Your device backup has been done \n')
		log.info('backup file name: ' + IP + ' backup.txt')

	except NetMikoTimeoutException:
		log.info ('Device not reachable.')
	except AuthenticationException:
		log.info ('Authentication Failure.')
	except SSHException:
		log.info ('Make sure SSH is enabled in device.')