import os
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-u", "--uuid", dest="uuid")

args = parser.parse_args()

path = os.path.join("uploads", args.uuid)

# Modify code beloe to do whatever processing you need
import time
time.sleep(2)
with open(os.path.join(path, "test.txt"), "w") as file:
    file.write(f'hello world! {args.uuid}')
