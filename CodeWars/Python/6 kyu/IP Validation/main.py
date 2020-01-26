def is_valid_IP(s):
    return len(s.split('.')) == 4 and all([int(x) in range(0, 255) if x.isdigit() and x[0] != '0' else False for x in s.split('.')])