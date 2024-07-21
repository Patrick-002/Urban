def data_structure(*args):
    structure = args

    def helper(structure, current_sum=0):
        for i in structure:
            if isinstance(i, int):
                current_sum += i
            elif isinstance(i, str):
                current_sum += len(i)
            elif isinstance(i, dict):
                list_from_dict = []
                for key, value in i.items():
                    list_from_dict.append(key)
                    list_from_dict.append(value)
                current_sum = helper(list_from_dict, current_sum)
            else:
                current_sum = helper(i, current_sum)
        return current_sum
    return helper(structure)


print(data_structure([
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]))
