# task1
# import os
#
# def check_ip_addresses(ip_list, output_file):
#     with open(output_file, 'w') as file:
#         for ip in ip_list:
#             response = os.system(f"ping -c 1 {ip} > /dev/null 2>&1")
#             if response == 0:
#                 file.write(f"{ip} is reachable\n")
#             else:
#                 file.write(f"{ip} is not reachable\n")
#
# ip_list = ["192.168.1.1", "8.8.8.8"]
# check_ip_addresses(ip_list, "ping_results.txt")


# task2
# import string
#
#
# def analyze_string(s):
#     upper_count = sum(1 for c in s if c.isupper())
#     lower_count = sum(1 for c in s if c.islower())
#     digit_count = sum(1 for c in s if c.isdigit())
#     punctuation_count = sum(1 for c in s if c in string.punctuation)
#
#     print(f"Upper letters: {upper_count}")
#     print(f"Lower letters: {lower_count}")
#     print(f"Digits: {digit_count}")
#     print(f"Punctuation: {punctuation_count}")
#
#
# s = "Hello, World! 123"
# analyze_string(s)


# task3
# def common_elements(list1, list2):
#     common = set(list1) & set(list2)
#     print("Common elements:", common)
#
# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6]
# common_elements(list1, list2)


# task4
# def sort_descending(arr):
#     sorted_arr = sorted(arr, reverse=True)
#     print("Sorted in descending order:", sorted_arr)
#
# arr = [5, 2, 9, 1]
# sort_descending(arr)


# task5
# def check_uniqueness(tup):
#     is_unique = len(tup) == len(set(tup))
#     print("All elements are unique:", is_unique)
#
# tup = (1, 2, 3, 4, 4)
# check_uniqueness(tup)


# task6
# def find_files(files, substring):
#     matching_files = [file for file in files if substring in file]
#     print("Files containing substring:", matching_files)
#
# files = ["report.docx", "data.csv", "summary_report.docx"]
# find_files(files, "report")


# task7
# def common_characters(str1, str2):
#     common_chars = set(str1) & set(str2)
#     print("Common characters:", common_chars)
#
# str1 = "hello"
# str2 = "world"
# common_characters(str1, str2)


# task8
# def find_median(numbers):
#     sorted_numbers = sorted(numbers)
#     n = len(sorted_numbers)
#     mid = n // 2
#     if n % 2 == 0:
#         median = (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
#     else:
#         median = sorted_numbers[mid]
#     print("Median:", median)
#
# numbers = [1, 2, 3, 4, 5]
# find_median(numbers)


# task9
# def replace_vowels(s):
#     vowels = "aeiouAEIOU"
#     replaced = ''.join('-' if c in vowels else c for c in s)
#     print("Modified string:", replaced)
#
# s = "Hello, World!"
# replace_vowels(s)


# task10
def unique_common_elements(list1, list2):
    common = set(list1) & set(list2)
    unique_elements = list(common)
    print("Unique common elements:", unique_elements)

list1 = [1, 2, 2, 3, 4]
list2 = [3, 4, 4, 5, 6]
unique_common_elements(list1, list2)