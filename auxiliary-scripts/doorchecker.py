#!/usr/bin/python

import sys, getopt, urllib


def main(argv):
    
    try:
        opts, args = getopt.getopt(argv,"hk:",["help","key="])
    except getopt.GetoptError:
        print 'doorchecker.py -k <key>'
        sys.exit(2)

    params = ''
    for opt, arg in opts:
        if opt in ('-k', '--key'):
            params = urllib.urlencode({'doorkey':arg,'extra':arg})
            # print params
            print urllib.urlopen("http://127.0.0.1:8000/doorlogin/", params).read() 
        # elif opt in ('-h', '--help'):
        #     print 'doorchecker.py -k <key>'


if __name__ == "__main__":
   main(sys.argv[1:])