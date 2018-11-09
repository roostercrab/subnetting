#Returns whether the octet is sane True=correct ip format; False=incorrect ip format
#ip sanity check
def check_ip(ip_array):
	
	for octet in ip_array:
		if (octet > 255):
			print("Dotted decimal addresses can't be above 255 for any octet, please try again.")
			return False
		else:
			return True