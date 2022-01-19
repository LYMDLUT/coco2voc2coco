from os.path import isdir, abspath, getsize, join
from os import listdir, system
import os
filenames = []


def append_filename(path):
    contents = listdir(path)
    for content in contents:
        content = join(path, content)
        if isdir(content):
            append_filename(content)
        else:
            filenames.append(content)
    return filenames


def main():
    path = "./"
    append_filename(path)
    #print(filenames)
    for filename in filenames:
        if getsize(filename) == 0:
            os.remove(filename)
            #system('del %s' % abspath(filename))
            print("[-] Deleting %s ...\n" % filename)


if __name__ == '__main__':
    main()