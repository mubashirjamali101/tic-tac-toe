import time
import sys
for i in range(100):
    sys.stdout.write("Downloading ... %s%%\r" % (i))
    sys.stdout.flush()
    time.sleep(1)
