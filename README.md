# python-project
import urllib.request #downloading a file over the internet
import re #regular expressions
from pathlib import Path
import operator

log_url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
local_log_file = Path("logfile.txt")

# Retrieve File (below). I have already downloaded it add a conditional to che$
# urllib.request.urlretrieve(log_url, 'logfile.txt')
if local_log_file.is_file():
    #file exists
    print("Log file exists!\n")
else: #file does not exist
    print("Downloading log file now!\n")
    urllib.request.urlretrieve(log_url, 'logfile.txt')
    
fh = open(local_log_file)
# Loop through the file
count = 0
for line in fh:
  count += 1
  #print(line)
print(count)
fh.close()

