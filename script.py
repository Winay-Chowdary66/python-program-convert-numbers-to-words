single_digits = ["zero", "one", "two", "three",
 					"four", "five", "six", "seven",
 					"eight", "nine"]

two_digits = ["ten", "eleven", "twelve",
 				"thirteen", "fourteen", "fifteen",
 				"sixteen", "seventeen", "eighteen",
 				"nineteen"]
 		
tens_multiple = ["", "", "twenty", "thirty", "forty",
 					"fifty", "sixty", "seventy", "eighty",
 					"ninety"]

tens_power = ["hundred", "thousand"]


def tens_print(tens):
    result_str = " "
    if tens != 0:
        if tens == 1:
            result_str += two_digits[ones]
        else:
            
            result_str += tens_multiple[tens] + " "
    if ones > 0:
        print_ones = single_digits[ones]
    else:
        print_ones = " "
    result_str += print_ones
    result_str = result_str.strip()
    return result_str
n = 199300

ones = n%10
tens = (n//10) % 10
hundreds = (n // 100) % 10
thousands = n // 1000
#print(ones, tens, hundreds, thousands)
if len(str(n)) == 1:
    print(single_digits[ones])
elif len(str(n)) == 2:
    print(tens_print(tens))
elif len(str(n)) == 3:
    print(single_digits[hundreds], tens_power[0], tens_print(tens))
elif len(str(n)) == 4:
    result_str_thousands = ""
    result_str_thousands += single_digits[thousands]+ " " + tens_power[1]
    if hundreds != 0:
        hundreds_print = " " + single_digits[hundreds] + " " + tens_power[0]
        result_str_thousands += hundreds_print
    else:
        result_str_thousands += ""
    
    result_str_thousands += " " + tens_print(tens)
    
    print(result_str_thousands)
    
else:
    print("Sorry this version won't support {} digits, You get it in next update.. :-)".format(len(str(n))))
