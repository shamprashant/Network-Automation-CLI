from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException
import time
import log

def check_status():
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

		output = conn.send_command('show ip int brief', use_textfsm = True)

		l = len(output)

		log.info('Getting interfaces status')
			
		print ('\nList of interfaces which are UP \n')
		for i in range(0,l):
		    if output[i]['status'] == 'up':
		        print (output[i]['intf'] +' ' + output[i]['status'])

		print ('\nList of interfaces which are DOWN \n')
		for i in range(0,l):
		    if output[i]['status'] != 'up':
		        print (output[i]['intf'] +' ' + output[i]['status'])

	except NetMikoTimeoutException:
		log.info ('Device not reachable.')
	except AuthenticationException:
		log.info ('Authentication Failure.')
	except SSHException:
		log.info ('Make sure SSH is enabled in device.')

def change_status():

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

		output = conn.send_command('show ip int brief', use_textfsm = True)

		name = output[1]['intf']
		status = output[1]['status']
		print ('\nInterface ' + name + ' status is ' + status )

		if status == 'up':
		    log.info ('Finishing the script')
		else :
		    log.info ('making backup interface UP')

		    config_commands = [ 'int fa0/1',
		                        'no shut' ]

		    log.info('Sending below commands to the device\n')                  
		    output = conn.send_config_set(config_commands)

		    print ('\n' + output + '\n')

		    log.info ('Finished configuration')

	except NetMikoTimeoutException:
		log.info ('Device not reachable.')
	except AuthenticationException:
		log.info ('Authentication Failure.')
	except SSHException:
		log.info ('Make sure SSH is enabled in device.')