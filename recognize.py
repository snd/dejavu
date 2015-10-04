import sys

import warnings
warnings.filterwarnings("ignore")

import argparse
import timeit

from dejavu import Dejavu
from dejavu.timer import Timer
from dejavu.recognize import FileRecognizer

parser = argparse.ArgumentParser()
parser.add_argument("file", help="the file to recognize")
parser.add_argument(
        "-s",
        "--secs",
        help="how many seconds to fingerprint for recognition",
        type=int)

args = parser.parse_args()

# load config from a JSON file (or anything outputting a python dictionary)
config = {
    "database": {
        "host": "127.0.0.1",
        "user": "root",
        "passwd": "", 
        "db": "dejavu"
    }
}

if args.secs:
    config["fingerprint_limit"] = args.secs

if __name__ == '__main__':

        # create a Dejavu instance
        djv = Dejavu(config)

        # Recognize audio from a file
        print("start recognizing")
        with Timer("djv.recognize") as t:
            song = djv.recognize(FileRecognizer, args.file)
        print("From file we recognized: %s\n" % song)
