list_member = []


class Member():
    def __init__(self):
        for i in range(5):
            list_member.append([f'username{i}', f'12345678_{i}', 13 + i * 3])


def five_member():
    Member()
    #


if __name__ == '__main__':
    five_member()
    print(list_member)
