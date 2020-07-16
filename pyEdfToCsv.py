#!/usr/bin/python3
import pyedflib
import numpy as np
import argparse


def signalsToCsv(filename, labels, signals):
    ''' Export all signals to single .csv'''
    filename = filename+'.csv'
    with open(filename, 'w+') as f:
        labels_row = ','.join(labels)
        f.write(labels_row)

        # Get max samples length
        maxLength = 0
        for i in range(len(signals)):
            maxLength = max(maxLength, len(signals[i]))

        # @TODO


def signalsToCsvs(filename, labels, signals):
    ''' Export all signals to multiple .csv'''
    for i in range(len(signals)):
        filepath = filename+labels[i]+'.csv'
        with open(filepath, 'w+') as f:
            f.write('%s\n' % labels[i])
            for sample in signals[i]:
                f.write('%2.2f,\n' % sample)


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
labels = f.getSignalLabels()
print('Signal labels in file : ', labels)

signals = []
for i in np.arange(n):
    print('Reading signal %u, samples %u' % (i, f.getNSamples()[i]))
    signal = f.readSignal(i)
    signals.append(signal)

# Create .csv
print('Creation of .csv.')
signalsToCsvs(args.input, labels, signals)
