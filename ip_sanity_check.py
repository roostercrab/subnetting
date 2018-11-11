#ip sanity check
def check_ip(ip):

    ip_array = [int(i) for i in ip.split('.')]
    for octet in ip_array:
        if octet > 255:
            print("Dotted decimal addresses can't be above 255 for any octet, please try again.")
            return False
        else:
            return True