#!/usr/bin/python3
import pyedflib
import numpy as np
import argparse
import datetime

# defaults
separator = ';'


def signalsToCsv(filename, labels, signals):
    ''' Export all signals to single .csv'''
    filename = filename+'.csv'
    with open(filename, 'w+') as f:
        labels_row = separator.join(labels)
        f.write(labels_row)

        # Get max samples length
        maxLength = 0
        for i in range(len(signals)):
            maxLength = max(maxLength, len(signals[i]))

        # @TODO


def signalsToCsvs(filename, labels, signals, sampleRates):
    ''' Export all signals to multiple .csv'''
    for i in range(len(signals)):
        filepath = filename+labels[i]+'.csv'
        with open(filepath, 'w+') as f:
            # Labels
            f.write('Time[s]%c%s\n' % (separator, labels[i]))

            # Prepare time values
            if (args.timeAbsolute):
                time = startTime
                delta = datetime.timedelta(seconds=1.0/sampleRates[i])
            else:
                time = 0
                delta = 1.0/sampleRates[i]

            # Samples saving
            for sample in signals[i]:
                if (args.timeAbsolute):
                    # Absolute time used
                    text = '%s%c%2.2f\n' % (time.strftime(
                        '%H:%M:%S.%f'), separator, sample)
                else:
                    # Relative time used
                    text = '%2.4f%c%2.2f\n' % (time, separator, sample)
                time += delta
                # Decimal mark conversion
                if (args.decimalpoint):
                    text = text.replace('.', ',')
                # Save
                f.write(text)


# Arguments and config
# #####################################################
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', type=str,
                    required=True, help='Input EDF file')
parser.add_argument('-s', '--separator', type=str,
                    required=False, help='Data CSV separator')
parser.add_argument('-d', '--decimalpoint', action='store_true',
                    required=False, help='')
parser.add_argument('-t', '--timeAbsolute', action='store_true',
                    required=False, help='Default behaviour is relative time printing (First sample is 0s). Absolute time prints time according to record start time.')
args = parser.parse_args()

if (args.separator is not None):
    separator = args.separator


# Open EDF file
f = pyedflib.EdfReader(args.input)
print('(File) Opened', args.input)
n = f.signals_in_file
print('(File) %u signals in file.' % (n))
labels = f.getSignalLabels()
print('(File) Signal labels in file : ', labels)
startTime = f.getStartdatetime()
print('(File) Start of recording', startTime)

sampleRates = f.getSampleFrequencies()
signals = []
for i in np.arange(n):
    print('(Signal) Reading signal %u `%s`, sampling freqeuncy %u, samples %u' % (
        i, labels[i], f.getSampleFrequency(i), f.getNSamples()[i]))
    print('(Signal) Signal header : ', f.getSignalHeader(i))
    print('')
    signal = f.readSignal(i)
    signals.append(signal)

# Create .csv
print('Creation of .csv.')
signalsToCsvs(args.input, labels, signals, sampleRates)
