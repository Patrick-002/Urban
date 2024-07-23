def data_structure(*structure, current_sum=0):
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
                current_sum = data_structure(*list_from_dict, current_sum)
            else:
                current_sum = data_structure(*i, current_sum)
        return current_sum

print(data_structure([
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]))
