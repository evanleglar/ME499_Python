#!/usr/bin/env python3
import csv
from math import log, sqrt, pi


def load_data_from_file(txt_file):
    with open(txt_file, 'r') as f:
        txt_file = csv.reader(f, delimiter=',')

        data_times = []
        data_values = []

        next(txt_file)

        for line in txt_file:
            data_times.append(float(line[0]))
            data_values.append(float(line[1]))
    return data_times, data_values


def greater_than_index(data_values, n):
    greater_val = next(x for x, val in enumerate(data_values) if val >= n)
    return greater_val


def system_c_values(data_values):
    c_initial = data_values[0]
    c_max = max(data_values)
    c_final = data_values[-1]
    return c_initial, c_max, c_final


def system_characteristics(txt_file):
    time, c_value = load_data_from_file(txt_file)
    c_initial, c_max, c_final = system_c_values(c_value)

    ten_percent_c_value = greater_than_index(c_value, (0.1 * (c_max - c_initial) + c_initial))
    ten_percent_time = time[ten_percent_c_value]

    ninety_percent_c_value = greater_than_index(c_value, (0.9 * (c_max - c_initial) + c_initial))
    ninety_percent_time = time[ninety_percent_c_value]

    t_r = ninety_percent_time - ten_percent_time

    t_p = time[greater_than_index(c_value, c_max)]

    percent_overshoot = round(abs((c_max - c_final) / (c_final - c_initial)) * 100, 1)

    """steps backwards through the list, using next function and indexing in the negative i direction, to find last time
        any c_values fall outside 2% range"""

    settling_time_2 = time[next(
        len(c_value) - i for i in range(2, len(c_value) - 1) if abs(c_value[-i] / c_value[-1]) > 1.02)] - time[0]

    return t_r, t_p, percent_overshoot, settling_time_2


def get_system_params(percent_overshoot, settling_time_2):
    zeta = -log(percent_overshoot / 100) / (sqrt(pi ** 2 + log(percent_overshoot / 100) ** 2))
    omega_n = 4 / (zeta * settling_time_2)
    system_spring = omega_n ** 2
    system_damping = 2 * zeta * omega_n
    return zeta, omega_n, system_spring, system_damping


def analyze_data(txt_file):
    time, c_value = load_data_from_file(txt_file)
    c_initial, c_max, c_final = system_c_values(c_value)
    t_r, t_p, percent_overshoot, settling_time_2 = system_characteristics(txt_file)
    zeta, omega_n, system_spring, system_damping = get_system_params(percent_overshoot, settling_time_2)

    system_summary = {'c_initial': c_initial, 'c_max': c_max, 'c_final': c_final, 'rise_time': t_r, 'peak_time': t_p,
                      'perc_overshoot': percent_overshoot, 'settling_time': settling_time_2, 'system_mass': 1,
                      'system_spring': system_spring, 'system_damping': system_damping}

    return system_summary


if __name__ == '__main__':
    txt_file = 'data1.csv'
    sys_summary = analyze_data(txt_file)
    print('\n', f'Final System Parameters for {txt_file}:', '\n')
    for key in sorted(sys_summary.keys()):
        print(str(key), ': ', sys_summary[key])
