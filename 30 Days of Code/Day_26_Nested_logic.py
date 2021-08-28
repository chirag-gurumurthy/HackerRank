# Enter your code here. Read input from STDIN. Print output to STDOUT
d_r, m_r, y_r = [int(e) for e in input().strip().split(' ')]
d_d, m_d, y_d = [int(e) for e in input().strip().split(' ')]

if y_r < y_d:
    print(0)
elif y_r == y_d:
    if m_r < m_d:
        print(0)
    elif m_r == m_d:
        if d_r <= d_d:
            print(0)
        else:
            print((d_r - d_d) * 15)
    else:
        print((m_r - m_d) * 500)
else:
    print(10000)
