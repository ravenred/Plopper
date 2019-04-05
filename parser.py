import datetime


def read_file(file_name):

    f = open(file_name, 'r')        # Opens SNORT
    start_line = f.readlines()      # Reads in first line

    for i in start_line[0:]:        # Loops through the file but starts at line 1 to gather data

        print(i)
        # i.split(" ")

        # All the fields from the http.log are mapped to a variable in this tuple
        timestamp, sig_generator, sig_id, sig_rev, msg, proto, src, srcport, dst, dstport, snort_id, \
        classification, priority = \
            tuple(map(str, i.split(" ")))       # SNORT logs are spaced using tabs to separate each field

    f.close()


read_file('D:/Log File Samples/tg_snort_fast/alert.fast')
