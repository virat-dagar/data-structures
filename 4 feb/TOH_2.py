def t_o_h(n, source ='a', help = 'b', destination = 'c'):
    if n==0:
        return
    t_o_h(n-1, source, destination, help)
    print(f'move disk from {source} -> {destination}')
    t_o_h(n-1, help, source, destination)

n = int(input('enter number of disks'))
t_o_h(n,'a')