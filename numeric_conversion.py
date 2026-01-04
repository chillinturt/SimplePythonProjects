remover = ""

#Decodes hexadecimal digit  and returns its value
def hex_char_decode(digit):
    if '0' <= digit <= '9':
        return ord(digit) - ord('0')
    elif 'a' <= digit <= 'f':
        return ord(digit) - ord('a') + 10
    elif 'A' <= digit <= 'F':
        return ord(digit) - ord('A') + 10
    else:
        raise ValueError(f"Invalid hexadecimal digit: {digit}")

#Decodes hexadecimal string and returns its value
def hex_string_decode(hex_str):
    if hex_str[:2] == '0x':
        hex_str = hex_str[2:]  # Remove '0x' prefix
    decimal_value = 0
    for digit in hex_str:
        decimal_value = decimal_value * 16 + hex_char_decode(digit)
    return decimal_value

#Decodes a binary string and returns its value
def binary_string_decode(binary_str):
    global remover
    if binary_str[1] == "b":
                remover = remove(binary_str, 1)
                remover = remove(remover, 0)
    
    decimal_value = 0
    for digit in remover:
        decimal_value = decimal_value * 2 + int(digit)
    return decimal_value

#Converts binary to string, encodes it as hex, then returns the hex string
def binary_to_hex(binary_str):
    decimal_value = binary_string_decode(binary_str)
    return hex(decimal_value)[2:].upper()
    
#removes the n-th values of a string
def remove(string, n):  
      first = string[:n]   
      last = string[n+1:]  
      return first + last

def main():
    while True:
        print("Decoding Menu")
        print("-------------")
        print("1. Decode hexadecimal")
        print("2. Decode binary")
        print("3. Convert binary to hexadecimal")
        print("4. Quit")
        
        choice = input("Please enter an option: ")
        
        if choice == '1':
            hex_str = input("Please enter the numeric string to convert: ")
            decimal_value = hex_string_decode(hex_str)
            print(f"Result: {decimal_value}")
        elif choice == '2':
            binary_str = input("Please enter the numeric string to convert: ")
            decimal_value = binary_string_decode(binary_str)
            print(f"Result: {decimal_value}")
        elif choice == '3':
            binary_str = input("Please enter the binary string to convert: ")
            hex_value = binary_to_hex(binary_str)
            print(f"Result: 0x{hex_value}")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()