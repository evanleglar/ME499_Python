#!/usr/bin/env python3


import sensor as sen
import amp_filter as amp

X = sen.generate_sensor_data(200)
Y = amp.apply_amp_filter(X)

with open('me499_lab2_3_1.csv', 'w') as f_1:
    for i in X:
        f_1.write(str(i)+'\n')
    f_1.close()


with open('me499_lab2_3_2.csv', 'w') as f_2:
    for j in Y:
        f_2.write(str(j)+'\n')
    f_2.close()


if __name__ == '__main__':
    for k in Y:
        if k > 0.95:
            raise ValueError

    print('complete')
