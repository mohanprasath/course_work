#!/usr/bin/env python3

def file_extensions(filename):
    file_names = []
    with open(filename, 'r') as infile:
        for line in infile:
            file_names.append(line)
    result_dict = {} # contains file names with extensions
    result_list = [] # contains file names that has not extensions
    for file_name in file_names:
        file_name = file_name.rstrip("\n")
        split_result = file_name.split(".")
        if len(split_result) == 1:
            result_list.append(file_name)
        else:
            if split_result[-1] in result_dict.keys():
                existing = result_dict[split_result[-1]]
                existing.append(file_name)
                result_dict[split_result[-1]] = existing
            else:
                existing = []
                existing.append(file_name)
                result_dict[split_result[-1]] = existing
    return (result_list, result_dict)

def main():
    result_lst, result_dict = file_extensions("filenames.txt")
    print(str(len(result_lst)) + " files with no extension")
    for key, value in result_dict.items():
        print(key + " " + str(len(value)))

if __name__ == "__main__":
    main()
