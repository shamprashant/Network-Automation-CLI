import datetime

def info(message):
	current_time = datetime.datetime.now()

	current_time = current_time.strftime('%d:%m:%Y %H:%M:%S')

	print(current_time + "    " + message)
