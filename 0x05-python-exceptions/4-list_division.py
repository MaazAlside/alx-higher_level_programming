#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    divided_list = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        finally:
            divided_list.append(result)
    return divided_list
