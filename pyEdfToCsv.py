#!/usr/bin/python3
from edf2csv import EDF
import argparse

# Arguments and config
# #####################################################
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', type=str,
                    required=True, help='Input EDF file')
args = parser.parse_args()

edf = EDF(args.input)

signal = edf.signal()
info = edf.info()

print('Creation of .csv.')
edf.ann_to_csv()
edf.signal_to_csv()
