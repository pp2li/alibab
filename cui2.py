import sys

f = open('czy_input.txt', 'r')
# q = int(f.readline().strip())
q = int(sys.stdin.readline().strip())
def step1(s, idx):
    t1, t2 = int(s[idx]), int(s[idx+1])
    if t1 == 0 or t2 ==9:
        return False
    else:
        t1 = t1 -1
        t2 = t2+1
    if idx == 0:
        return [str(t1)] + [str(t2)] + s[idx+1:]
    else:
        return s[0:idx] + [str(t1)] + [str(t2)] + s[idx+1:]

def step2(s, idx):
    t1, t2 = int(s[idx]), int(s[idx+1])
    if t1 == 9 or t2 ==0:
        return False
    else:
        t1 = t1 +1
        t2 = t2-1
    if idx == 0:
        return [str(t1)] + [str(t2)] + s[idx+1:]
    else:
        return s[0:idx] + [str(t1)] + [str(t2)] + s[idx+1:]


for _ in range(q):
    # s = list(f.readline().strip())
    s = list(sys.stdin.readline().strip())
    l = len(s)
    queue = [s]
    has_see_set = set([''.join(s)])
    # idx = 0
    # jdx = 0
    while queue:
        s = queue.pop(0)
        for idx in range(l -1):
            new_s = step1(s, idx)
            if new_s and ''.join(new_s) not in has_see_set:
                has_see_set.add(''.join(new_s))
                queue.append(new_s)

        for idx in range(l -1):
            new_s = step2(s, idx)
            if new_s and ''.join(new_s) not in has_see_set:
                has_see_set.add(''.join(new_s))
                queue.append(new_s)

        # queue.pop(0)

    print len(has_see_set) % 1000000007




f.close()