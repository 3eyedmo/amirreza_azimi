

def write_lines(string_list, filename):
    f = open(filename, 'a', encoding='utf-8')
    print("*" * 50)
    print(string_list)
    for item in string_list:
        print(item, end="  ")
        f.write(item)
        f.write('\n')
    print()
    f.close()
