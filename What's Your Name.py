def print_full_name(a, b):
    print(f"Hello {first_name} {last_name}! You just delved into python.")
    #OR
    #print("Hello {0} {1}! You just delved into python.".format(first_name,last_name))

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
