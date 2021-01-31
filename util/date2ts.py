import sys
from datetime import datetime
import dateparser

dt = dateparser.parse(sys.argv[1])
print(dt.timestamp())
