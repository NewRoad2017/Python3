import csv
import sys
class CSVset:
    # __fileDirpath = ""
    # csvFilepath = ""
    # csvFile = None
    def __setCSV(self):
        try:
            self.csvFile = open(self.filePath, 'w', newline="")
            self.csvWriter = csv.writer(self.csvFile,dialect=("excel"))
            self.csvWriter.writerow(dataTable)
        except Exception as e:
            print (str(e))
            sys.exit()

    def __init__(self, dataPath, dataTable):
        self.filePath = dataPath
        self.__setCSV(dataTable)