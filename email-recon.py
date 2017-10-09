#!/usr/bin/python
#
# Author(s): Matias Menares (Gh0st)
# Email Recon

from core.searcher import Searcher
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-m", help="Email")
params = parser.parse_args()

def main(params):
	if params.m:
		search.searcher()
	else:
		print("Type -h for help.")

if __name__ == '__main__':
	search = Searcher(params.m)

try:
    main(params)
except (KeyboardInterrupt, EOFError):
    log.info('Exiting.')