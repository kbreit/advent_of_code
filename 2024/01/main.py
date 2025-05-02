#!/usr/bin/env python3


def open_file(filename):
    with open(filename, "r") as file:
        content = file.read()
    return content


def main():
    data = open_file("data.txt")
    distance = 0
    first_list = []
    second_list = []
    for line in data.splitlines():
        split_line = line.split()
        first_list.append(split_line[0])
        second_list.append(split_line[1])
    first_list.sort()
    second_list.sort()
    for i, value in enumerate(first_list):
        distance = distance + abs(int(first_list[i]) - int(second_list[i]))
    print(distance)


if __name__ == "__main__":
    main()
