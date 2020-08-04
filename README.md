![License](https://img.shields.io/github/license/folkien/pyEdfToCsv)
![Size](https://img.shields.io/github/repo-size/folkien/pyEdfToCsv)
![pythonversion](https://img.shields.io/badge/python-3.6-blue)

# pyEdfToCsv
EDF to CSV converter. Makes many .csv for each signal inside EDF.

```bash
usage: pyEdfToCsv.py [-h] -i INPUT [-s SEPARATOR] [-d] [-t]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input EDF file
  -s SEPARATOR, --separator SEPARATOR
                        Data CSV separator
  -d, --decimalpoint
  -t, --timeAbsolute    Default behaviour is relative time printing (First
                        sample is 0s). Absolute time prints time according to
                        record start time.
```

Example usage

`./pyEdfToCsv.py -i example/11-56-29.EDF -t`

