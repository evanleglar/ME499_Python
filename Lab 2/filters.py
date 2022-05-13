#!/usr/bin/env python3

import sensor as sen


def mean_filter(data, n=3):

    m_avg = []

    if (n % 2) == 0:
        raise ValueError
    else:
        for i in range(len(data)):
            avg = sum(data[i:i+n])/n
            m_avg.append(avg)
        return m_avg


if __name__ == '__main__':
    # data = sen.generate_sensor_data(200)
    data = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]
    mov_avg = mean_filter(data, 5)
    print(mov_avg)

    with open('me499_lab2_4_1.csv', 'w') as f_1:
        for i in range(len(data)):
            f_1.write(str(data[i])+'\n')

    with open('me499_lab2_4_2.csv', 'w') as f_ma:

        for i in range(len(mov_avg)):
            f_ma.write(str(mov_avg[i])+'\n')
