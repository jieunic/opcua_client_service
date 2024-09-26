import math
import time

def count_kw(voltage, current, cosphi, rt):
    power = (voltage * current * cosphi * rt) / 1000
    return power

# def start_cn(val):
#     if isinstance(val, list):
#         if val[0] == 0 and val[1] == 0 and val[2] == 0 and val[3] == 0 and val[4] == 0 and val[5] == 0:
#             time.sleep(2)
#             count = 0
#             while True:
#                 count += 1
#                 time.sleep(1)
#                 if val[0] > 0 or val[1] > 0 or val[2] > 0 or val[3] > 0 or val[4] > 0 or val[5] > 0:
#                     print(count)
#                     break
#                 elif KeyboardInterrupt:
#                     print(count)
#                     break

def start_cn(val):
    if isinstance(val, list):
        if val[0] == 0 and val[1] == 0 and val[2] == 0 and val[3] == 0 and val[4] == 0 and val[5] == 0:
            time.sleep(2)
            count = 0
            try:
                while True:
                    try:
                        print(val)
                    except KeyboardInterrupt:
                        break
                    # count += 1
                    # time.sleep(1)
                    # print(f"Checking at count {count}, val: {val}")
                    # if val[0] > 0 or val[1] > 0 or val[2] > 0 or val[3] > 0 or val[4] > 0 or val[5] > 0:
                    #     print(count)
                    #     break
            # except val[0] > 0 or val[1] > 0 or val[2] > 0 or val[3] > 0 or val[4] > 0 or val[5] > 0:
            #     print(count)
            except KeyboardInterrupt:
                print("Process interrupted by user.")



def count_kwh(actual_waiting, tt, power, time):
    unit = 3600 / tt
    total_waiting = actual_waiting * unit
    energy = (power * total_waiting) / 3600
    return energy