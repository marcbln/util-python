# 12/2017 copied from push v3

import json
import os

#
#
# def file_put_contents( path, content):
#     f = open(path, 'w')
#     f.write( str(content))
#     f.close()
#
# def get_files_full_path( path, allowedMimeTypes):
#     allFiles = reduce( lambda files1, files2: files1+files2, map( lambda (path_, dirs_, files_): map( lambda f: os.path.join( path_, f), files_), os.walk(path, followlinks=True)), [])
#     # filter by mimeType
#     allFilesFiltered = [p for p in allFiles if mimetypes.guess_type(p)[0] in allowedMimeTypes ]
#
#     return allFilesFiltered
#
#
# def get_files_relative_path( path, allowedMimeTypes):
#     path = os.path.realpath( path) # remove trailing '/'
#     start_at = len(path) + 1
#     # remove path prefix
#     filesWithFullPath = get_files_full_path( path, allowedMimeTypes)
#     files = map( lambda p: p[start_at:], filesWithFullPath)
#     # print "\n".join(files)
#
#     return files
#
#
# def mkdir_p(path):
#     try:
#         os.makedirs(path)
#     except OSError as exc: # Python >2.5
#         if exc.errno == errno.EEXIST and os.path.isdir(path):
#             pass
#         else: raise
#
#
# def mkdir_if_not_exists(directory):
#     if not os.path.exists(directory):
#         mkdir_p(directory)
#
#
#
# def parse_list(path, castTo=None):
#     f = open( path)
#     lst = []
#     for line in f:
#         line = line.strip()
#         if not line or line[0] == '#':
#             continue
#         if castTo == None:
#             lst.append(line)
#         else:
#             lst.append( castTo(line) )
#     f.close()
#     return lst
#
# def relative_to_absolute_path( rootPath, path):
#     if not os.path.isabs( path):
#         path = os.path.join( rootPath, path)
#     path = os.path.realpath( path)
#     return path
#
# def save_json(obj, path):
#     with open(path, 'w') as outfile:
#         json.dump(obj, outfile, indent=4)
#
#
# def get_sub_directories(path):
#     return [os.path.join(path,o) for o in os.listdir(path) if os.path.isdir(os.path.join(path,o))]
#
from glob import glob


class UtilFile:

    # 12/2017
    @staticmethod
    def fileGetContents(path):
        f = open(path)
        ret = f.read()
        f.close()
        return ret

    # 01/2018
    @staticmethod
    def filePutContents(filename, content):
        f = open(filename, 'w')
        f.write(content)
        f.close()

    # 12/2017
    @staticmethod
    def loadJson(path):
        strJson = UtilFile.fileGetContents(path)
        return json.loads(strJson)

    # 12/2017
    @staticmethod
    def loadJsonWithFallback(path, default={}):
        if not os.path.isfile(path):
            return default
        strJson = UtilFile.fileGetContents(path)
        return json.loads(strJson)

    # 01/2019 from photoBot
    @classmethod
    def appendToFilename(cls, path, suffix):
        name, ext = os.path.splitext(path)
        return "{name}{suffix}{ext}".format(name=name, suffix=suffix, ext=ext)

    # 03/2019 PhotoBot
    # returns list of filenames only .. without directory .. eg ['a.json', 'b.json']
    @classmethod
    def getFilenamesInDirectory(cls, pathDirectory, pattern="*"):
        return [os.path.basename(x) for x in glob(os.path.join(pathDirectory, pattern))]
