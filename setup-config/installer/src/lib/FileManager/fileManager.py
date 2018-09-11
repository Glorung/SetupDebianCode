#!/usr/bin/python3

from os import listDir
from os.path import isFile, join

class           fileManager:

    # Return all elems in the given path
    def getAll(self, path):
        elems = listDir(path)
        return elems

    # Return a list of files for the given path
    def getFiles(self, path):
        elems = self.getAll(path)
        while (elems):
            File = isFile(elems.first())
            if (File):
                elems_files += elems.first()
            elems.pop()
        return elems_files

    # Return a list of directories for the given path
    def getDirs(self, path):
        elems = self.getAll(path)
        while (elems):
            File = isFile(elems.first())
            if (not File):
                elems_dirs += elems.first()
            elems.pop()
        return elems_dirs
