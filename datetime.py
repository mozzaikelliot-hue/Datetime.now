from datetime import datetime
import time
while True:
	print("\r", datetime.now().
	strftime("%H:%M:%S"), end="")
	time.sleep(1)