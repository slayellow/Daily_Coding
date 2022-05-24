from collections import UserList


class GoodList(UserList):
    def __getitem__(self, index):
        value = super().__getitem__(index)
        if index % 2 == 0:
            prefix = "짝수"
        else:
            prefix = "홀수"
        return f"[{prefix}] {value}"

class BadList(list):
    def __getitem__(self, index):
        value = super().__getitem__(index)
        if index % 2 == 0:
            prefix = "짝수"
        else:
            prefix = "홀수"
        return f"[{prefix}] {value}"


def wrong_user_display(user_metadata: dict = {"name": "John", "age": 30}):
    name = user_metadata.pop("name")
    age = user_metadata.pop("age")
    return f"{name} ({age})"


# b1 = BadList((0, 1, 2, 3, 4, 5))
b1 = GoodList((0, 1, 2, 3, 4, 5))
print(b1[0])
print(b1[1])

print("".join(b1))
# print(wrong_user_display())
# print(wrong_user_display({"name": "Jane", "age": 25}))
# print(wrong_user_display())
