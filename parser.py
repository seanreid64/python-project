# python-project
#1fetch File
#2save to disk
#3loop through File
#3.1 count lines
#3.2 parse elements of log line out of each line
#3.3 store data by date
#3.4 count requests based on redirect 3xx & 4xx
#3.5 store data by filename
#4.0 save lines in new files by month
import os.path
import urllib.request
log_url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
local_file = "logfile.txt"


urllib.request.urlretrieve (log_url, local_file) #downloading a file over the internet
import re #regular expressions
from pathlib import Path
import operator


if not os.path.isfile(local_file):
    # Retrieve File (below).
    local_path, headers = urlretrieve(log_url, local_file)

#initialize the count vars
count = 0
# a list to store errors from the parsing process
ERRORS = []

# Prepare the regex (this is independent from using the pattern, so it can happen outside a loop, e.g.)
regex = re.compile(".*\[([^:]*):(.*) \-[0-9]{4}\] \"([A-Z]+) (.+?)( HTTP.*\"|\") ([2-5]0[0-9]) .*")

# Loop through the file
file2=open('testfile.txt','w')
for line in open(local_file):
  count += 1
  print(line)

  # Call the split() method to get all the capture groups put in a list
  parts = regex.split(line)
  # Let's see what the regex grabbed...
  print(parts)
  print(parts[1])
  file2.write(parts[1])
  file2.write('\n')  
  if count > 100:
      break
  #print dates

print(count)
# Sanity check the line -- there should be 7 elements in the list (remember that index 0 has the whole string)
# if not parts or len(parts) < 7:
#   print "Error parsing line! Log entry added to ERRORS[] list..."
#   errors.append(log_line)

import re

# Initialize a dictionary to track the items
#   The keys will be a unique string that represents the item,
#   and the values will be a single int that tracks how many of the thing exists
things = {}
# Let's say we're counting the number of times that a particular filename appears in a log file
for line in open('logfile.txt'):

  # Use the Regex module to split out the filename from the line
    pieces = re.split("(0[1-9]|[12][0-9]|3[01])[/](0[1-9]|1[012])[/]\d{4}", line)

  # Let's further say that we can get the filename part at the 4th list element
    filename = pieces[0]
  # Now we need to use a little logic: if this is the first time we've seen this filename,
  #   then we need to add it to the 'things' dict. If we've already seen this filename
  #   before, then we need to increment the counter (the int in the value) for that filename.
  #
  # Check and see if a key that matches 'filename' exists using the 'in' operator
    if filename in things: #('logfile.txt')
        things[filename] += 1
    # So we've already added this file -- let's increment the counter
    else:
        # This is a new filename -- let's add it to the dictionary
        things[filename] = 1
    #for item in filename:
        #print(item[1])
        #file2.write(item)    
file2.close()