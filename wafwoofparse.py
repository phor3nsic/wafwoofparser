import json
import argparse
import sys

def get_hosts_no_safe(data):
	for x in data:
		if x["firewall"] == "None" or x["firewall"] == "Generic":
			print(x["url"])

def get_hosts_safe(data):
	for x in data:
		if x["firewall"] != "None":
			print(x["url"])

def main():
	parser = argparse.ArgumentParser(add_help=True)
	parser.add_argument("-f","--file", help="Outpuf wafwoof json", type=argparse.FileType('r'), default=sys.stdin)
	parser.add_argument("-ns","--nosafe", help="Extract hosts without WAF or Generic WAF", action="store_true")
	parser.add_argument("-s","--safe", help="Extract hosts with WAF", action="store_true")
	args = parser.parse_args()

	data = json.load(args.file)
	
	if args.nosafe:
		get_hosts_no_safe(data)

	if args.safe:
		get_hosts_safe(data)

if __name__ == '__main__':
	main()