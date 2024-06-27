# https://leetcode.com/problems/insert-delete-getrandom-o1/?envType=study-plan-v2&envId=top-interview-150
# In order to make every ops to O(1), we use 1 dict and 1 list to store the elements and the indices
# For the insert operator, we simply use the dict to check the existence of the val, and then insert new value
# to the dict and the list, so the TC is O(1)
# For the getRan, we use simply generate a random index and return the element at that index, so the TC is also O(1)
# And for the remove op, after checking the existence, we swap the val with the last el in the list, delete it
# from the list and the dict and update the index in the dict, so the TC is also O(1) since delete last el of a list
# is O(1) complexity

import random


class RandomizedSet:
    def __init__(self):
        self.num_list = []
        self.num_dict = dict()

    def insert(self, val: int) -> bool:
        if val in self.num_dict:
            return False

        self.num_list.append(val)
        self.num_dict[val] = len(self.num_list) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.num_dict:
            return False

        val_idx = self.num_dict[val]
        # move val to the end
        last_el = self.num_list[-1]
        self.num_list[-1] = val
        self.num_list[val_idx] = last_el
        # change the index of the last el
        self.num_dict[last_el] = val_idx
        # drop val
        self.num_list.pop()
        self.num_dict.pop(val)
        return True

    def getRandom(self) -> int:
        return random.choice(self.num_list)


# obj = RandomizedSet()
# obj.insert(1)
# obj.insert(2)
# obj.remove(1)
