

#Returns whether the octet is sane True=sane; False=either insane, or crazy
def check255(octet):
	if (octet > 255):
		print("Dotted decimal addresses can't be above 255 for any octet, please try again.")
		return False
	else:
		return True


#ip sanity check
ip_sanity = False

while ip_sanity == False:

    ip = input("What is the IP address? ")
    ip_array = [int(i) for i in ip.split('.')]
    first_octet, second_octet, third_octet, fourth_octet = ip_array

    ip_sanity = (check255(first_octet) and check255(second_octet) and check255(third_octet) and check255(fourth_octet))


#subnet mask sanity check

def check_mask(octet):
	if (octet not in [255, 254, 252, 248, 240, 224, 192, 128, 0]):
		print("Subnet masks can only have a value of 255, 254, 252, 248, 240, 224, 192, 128 or 0")
		return False
	else:
		return True


mask_sanity = False

while mask_sanity == False:

    subnet_mask = input("What is the subnet mask? ")
    mask_array = [int(i) for i in subnet_mask.split('.')]
    first_mask_octet, second_mask_octet, third_mask_octet, fourth_mask_octet = mask_array

    mask_sanity = (check_mask(first_mask_octet) and check_mask(second_mask_octet) and check_mask(third_mask_octet) and check_mask(fourth_mask_octet))

    if first_mask_octet != 255 and (second_mask_octet or third_mask_octet or fourth_mask_octet != 0):
        print("Subnet masks must have all 0s after the interesting octet")
        mask_sanity = False

    elif second_mask_octet != 255 and (third_mask_octet or fourth_mask_octet != 0):
        print("Subnet masks must have all 0s after the interesting octet")
        mask_sanity = False

    elif third_mask_octet != 255 and fourth_mask_octet != 0:
        print("Subnet masks must have all 0s after the interesting octet")
        mask_sanity = False

    else:
        mask_sanity = True
        break


print('\nThe IP address ' + ip + ' is written this way in dotted decimal binary:')

ip.split('.')
print(ip)

print('.'.join([bin(int(x)+256)[3:] for x in ip.split('.')]))

print('\nIf we take out all of the dots (because they are just used for humans) this is the IP address in binary :')
print(''.join([bin(int(x)+256)[3:] for x in ip.split('.')]))

print('\nThis is the subnet mask ' + subnet_mask + ' written in binary: ')
print(''.join([bin(int(x)+256)[3:] for x in subnet_mask.split('.')]))

print("\nIf we compare the IP address to the subnet mask, we can see how the subnet mask is measuring the IP address")

print(''.join([bin(int(x)+256)[3:] for x in ip.split('.')]))
print(''.join([bin(int(x)+256)[3:] for x in subnet_mask.split('.')]))

#we can color code this somehow....
# print("12" + "\033[1;32;47mBright Green  Is this a different color?\n")
