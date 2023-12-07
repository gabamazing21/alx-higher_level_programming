#!/usr/bin/python3
"""
Inherenting from list
in here

"""


class MyList(list):
    """
    Mylist inherent from list
    and represnt list object

    """
    def print_sorted(self):
        """
        function sort list
        and print sorted list

        """
        for i in self:
            if type(i) is not int:
                raise ValueError("Value shold be int")
        sorted_list = sorted(self)
        print(sorted(sorted_list))
