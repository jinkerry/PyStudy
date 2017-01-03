__author__ = 'jinfeng'


def camel(str):
    print str
    processed_list = []
    bottom_index = 0
    for a_char in str:
        if len(processed_list) < 2:
            processed_list.append(a_char)
        else:
            if a_char != processed_list[bottom_index]:
                processed_list.append(a_char)
                bottom_index += 1

    for ch in processed_list:
        print ch,


if __name__ == "__main__":
    camel('abaabcbcdcddd')