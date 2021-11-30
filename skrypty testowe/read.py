import glob

file_path = '/Users/Alex/Desktop/BSI2/PY/TEXTVIRUS310/test/read.txt'

for file in glob.glob(file_path):
    # open text file in read mode
    text_file = open(file, 'r+')
    data = text_file.read()
    print(data)
    # read whole file to a string
    text_file.truncate(0)
    #data = text_file.read()
    # close file
    text_file.close()
    text_file = open(file, 'r+')
    text_file.write("usuniete")
    text_file.close()
    text_file = open(file, 'r+')
    data = text_file.read()
    print(data)
    text_file.close()

