import os
import sys
from server.instance import server

# Need to import all resources
# so that they register with the server 
from resources.badge import BadgeList, Badge

if __name__ == '__main__':
    server.run()