import multiprocessing
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name, 'r') as f:
        for line in f:
            f.readline()
            all_data.append(line)


filenames = [f'./file {number}.txt' for number in range(1, 5)]
#print(filenames)

# time_start = datetime.now()
# for i in filenames:
#     read_info(i)
# time_end = datetime.now()
# time_res = time_end - time_start
# print(time_res)


if __name__ == '__main__':
    time_start_2 = datetime.now()
    with  multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    time_end_2 = datetime.now()
    time_res_2 = time_end_2 - time_start_2
    print(time_res_2)

