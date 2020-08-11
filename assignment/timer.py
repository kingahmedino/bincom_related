import time

seconds = 30
for x in range(10):
	for i in range(seconds):
		print(str(seconds - i))
		time.sleep(1)
	time.sleep(7)	