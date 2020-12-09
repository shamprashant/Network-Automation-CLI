from netmiko import ConnectHandler
import sys
import time
import get_config
import backup
import status

def exit():
	print('\nShutting down your python script!\nBye!')
	sys.exit(0)

if __name__ == '__main__':

	print('`'*70 + '\n')
	print('-------------------------WELCOME-----------------------------------')


	while True:
		print('\n\n\n\n')
		print('Enter 1. to see the running configuration of your device')
		print('Enter 2 to back-up your device')
		print('Enter 3 to see the interfaces status of your device')
		print('Enter 4 to change the status of an interfaces of your device')
		print('Enter 5 to Exit')

		choice = int(input('\nEnter your choice: '))

		choices = {
		1: get_config.get_running_config,
		2: backup.do_backup,
		3: status.check_status,
		4: status.change_status,
		5: exit
		}

		choices[choice]()