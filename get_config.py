from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException
import time
import log

def get_running_config():
	try:

		IP = input('\n\nEnter your device ip: ')

		device1 = {
			'device_type': 'cisco_ios',
			'ip': IP,
			'username': 'prashant',
			'password': 'cisco'
		}

		conn = ConnectHandler(**device1)

		print('\n')
		log.info('Connected with ' + IP + '\n\n')
		log.info('Script has taken control of the device\n')
		
		time.sleep(2)

		conn.send_command('term length 0')
		output = conn.send_command('show run')
		log.info('Script is sending show run command to the device\n\n')

		log.info('Getting your device configurations.....\n\n\n')

		print(output + '\n')

	except NetMikoTimeoutException:
		log.info ('Device not reachable.')
	except AuthenticationException:
		log.info ('Authentication Failure.')
	except SSHException:
		log.info ('Make sure SSH is enabled in device.')