from collections import Counter


def log_parser():
    log_file = open("test.log")
    d = {}
    i = 0

    for line in log_file.readlines():
        split_line = line.split(' ')  # split for blanks
        d[i] = split_line[6]  # url data in log_file's six column
        i += 1

    cnt = Counter()

    for j in d.values():
        cnt[j] += 1

    print cnt.most_common(1)

    log_file.close()

if __name__ == '__main__':
    log_parser()