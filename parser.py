import datetime
import re


def read_file(file_name):

    f = open(file_name, 'r')        # Opens SNORT
    start_line = f.readlines()      # Reads in first line

    for i in start_line[0:]:        # Loops through the file but starts at line 1 to gather data

        x = re.search(r'^((?:[0-9]{2}[-\/:.]){5}[0-9]{6})(.*[{]TCP[}]\s*|.*[{]UDP[}]\s*|.*[{]ICMP[}]\s*).(.*)', i)

        # print(x.groups())
        date_time = x.group(1)
        event = x.group(2).lstrip()
        ip_info = x.group(3)

        try:
            ip_formatted = re.search(r'\s*(((?:[0-9]{1,3}[.]){1,3}[0-9]{1,3}):([0-9]{1,6}))\s*->\s*(((?:[0-9]{1,3}[.]){1,3}[0-9]{1,3}):([0-9]{1,6}))', ip_info)
            print(ip_formatted.groups())


        except AttributeError:

            try:
                icmp_formatted = re.search(r'((?:[0-9]{1, 3}[.]){1, 3}[0-9]{1, 3})\s *->\s * ((?:[0-9]{1, 3}[.]){1, 3}[0-9]{1, 3})', ip_info)
                print(icmp_formatted.groups())

            except AttributeError:
                print()

        print(date_time)
        print(event)

    f.close()


read_file('D:/Log File Samples/tg_snort_fast/alert.fast')
