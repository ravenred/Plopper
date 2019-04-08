import re

# timestamp,sig_generator,sig_id,sig_rev,msg,proto,src,srcport,dst,dstport,id,classification,priority


def read_file(file_name):

    f = open(file_name, 'r')        # Opens SNORT
    start_line = f.readlines()      # Reads in first line

    for i in start_line[0:]:        # Loops through the file but starts at line 1 to gather data

        print("************ALERT START************")

        x = re.search(r'^((?:[0-9]{2}[-\/:.]){5}[0-9]{6})(.*[{]TCP[}]\s*|.*[{]UDP[}]\s*|.*[{]ICMP[}]\s*).(.*)', i)

        # print(x.groups())
        date_time = x.group(1)
        event = x.group(2).lstrip()
        ip_info = x.group(3)

        print(date_time)
        print(event)

        if "{ICMP}" in event:

            icmp_formatted = re.search(r'((?:[0-9]{1,3}[.]){1,3}[0-9]{1,3})\s*->\s*((?:[0-9]{1,3}[.]){1,3}[0-9]{1,3})', ip_info)
            # print(icmp_formatted.groups())

            icmp_src_ip = icmp_formatted.group(1)
            icmp_dest_ip = icmp_formatted.group(2)
            print(icmp_src_ip)
            print(icmp_dest_ip)

        elif "{TCP}" or "{UDP}" in event:

            ip_formatted = re.search(r'\s*(((?:[0-9]{1,3}[.]){1,3}[0-9]{1,3}):([0-9]{1,6}))\s*->\s*(((?:[0-9]{1,3}[.]){1,3}[0-9]{1,3}):([0-9]{1,6}))',ip_info)
            # print(ip_formatted.groups())
            src_ip = ip_formatted.group(2)
            src_port = ip_formatted.group(3)
            dest_ip = ip_formatted.group(5)
            dest_port = ip_formatted.group(6)

            print(src_ip)
            print(src_port)
            print(dest_ip)
            print(dest_port)

        print("************ALERT END************")

    f.close()


read_file('D:/Log File Samples/tg_snort_fast/alert.fast')
