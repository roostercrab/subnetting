from ip_sanity_check import check_ip
from mask_sanity_check import check_mask

ip_sanity = False

while ip_sanity == False:

    ip = input("What is the IP address? ")
    ip_array = [int(i) for i in ip.split('.')]

mask_sanity = False

while mask_sanity == False:

    subnet_mask = input("What is the subnet mask? ")
    mask_array = [int(i) for i in subnet_mask.split('.')]

    check_mask(mask_array)
    
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
