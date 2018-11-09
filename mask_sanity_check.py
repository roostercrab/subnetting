#subnet mask sanity check
#mo stands for mask octet

possible_mask_values = [255, 254, 252, 248, 240, 224, 192, 128, 0]
interesting_octet_values = [254, 252, 248, 240, 224, 192, 128]

def check_mask(mask_array):
	
    mo1, mo2, mo3, mo4 = mask_array

    for octet in mask_array:
        if (octet not in possible_mask_values):
			print("Subnet masks can only have values of 255, 254, 252, 248, 240, 224, 192, 128 or 0")
			return False

        else:
			mo1 == 0 
            print("A subnet mask starting with 0 will match all addresses, please try again")
        else:
			mo1 in interesting_octet_values and (mo2 and mo3 and mo4 == 0) 
            return True
        else (mo1 == 255) and (mo2 and mo3 and mo4 == 0) 
            return True
        else (mo1 == 255) and (mo2 in interesting_octet_values and mo3 and mo4 == 0) 
            return True
        else (mo1 and mo2 == 255) and (mo3 and mo4== 0) 
            return True
        else (mo1 and mo2 == 255) and (mo3 in interesting_octet_values and mo4 == 0) 
            return True
        else (mo1 and mo2 and mo3 == 255) and (mo4== 0) 
            return True
        else (mo1 and mo2 and mo3 == 255) and (mo4 in interesting_octet_values) 
            return True
        else (mo1 and mo2 and mo3 and mo4 == 255) 
            print("This is the mask for an exact address, not a subnet")
        else:
            print("Subnet masks must have all 0s after the interesting octet")
            return False