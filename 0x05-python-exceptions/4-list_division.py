#!usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):

    new_list = []
    try:
        for i in range(list_length):
            try:
                new_list.append(float(my_list_1[i] / my_list_2[i]))
            except ZeroDivisionError:
                new_list.append(0)
                print("division by 0")
            except TypeError:
                new_list.append(0)
                print("wrong type")
            except IndexError:
                print("out of range")
            finally:
                continue
    finally:
        return (new_list)
