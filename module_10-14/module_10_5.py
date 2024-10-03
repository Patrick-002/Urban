from multiprocessing import Pool
from datetime import datetime

filenames = [f'./file {number}.txt' for number in range(1, 5)]

def read_info(name):
    all_data = []
    with open(name) as f:
        while f.readline():
            all_data.append(f.readline())

# start_time = datetime.now()
#
# for file in filenames: # 0:00:04.728956
#     read_info(file)
#
# end_time = datetime.now()
# print(end_time - start_time)

if __name__ == '__main__': # 0:00:01.922600
    start_time = datetime.now()

    with Pool(processes=6) as pool:
        pool.map(read_info, filenames)

    end_time = datetime.now()
    print(end_time - start_time)