#!/usr/bin/python3
import pyedflib
import numpy as np
import argparse

# Arguments and config
# #####################################################
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', type=str,
                    required=True, help='Input EDF file')
args = parser.parse_args()


# Open EDF file
f = pyedflib.EdfReader(args.input)
print('Opened', args.input)
n = f.signals_in_file
print('%u signals in file.' % (n))
signal_labels = f.getSignalLabels()
print('Signal labels in file : ', signal_labels)

signals = []
for i in np.arange(n):
    print('Reading signal %u, samples %u' % (i, f.getNSamples()[i]))
    signal = f.readSignal(i)
    signals.append(signal)

# Create .csv
print('Creation of .csv.')
print(sigbufs)
