# Public domain

import urllib2
import re

STATS_URL = 'http://marconi.kmnr.org:7000/status2.xsl'
LISTENERS_REGEX = re.compile('"CurrentListeners":(\d+),')

def getListeners():
  webstream_stats_file = urllib2.urlopen(STATS_URL)
  webstream_stats_raw = webstream_stats_file.read()
  listeners = LISTENERS_REGEX.findall(webstream_stats_raw)
  
  totalListeners = 0
  for stream in listeners:
    totalListeners += int(stream)
  
  return totalListeners

if __name__ == "__main__":
  print str(getListeners())
