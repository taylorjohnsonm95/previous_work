import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--infile', help='file to read', required=True)
args = parser.parse_args()

print(args.infile)
