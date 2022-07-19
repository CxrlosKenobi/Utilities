import time

def spigot(measure, i):
    try:
        x = []
        q, r, t, k, n, l = 1, 0, 1, 1, 3, 3
        start = time.time()

        if measure == False:
            while True:
                if 4*q + r-t < n * t:
                    x.append(n)
                    q, r, t, k, n, l = (
                        10*q, 10*(r - n*t), t, k,
                        (10 * (3*q + r)) // t- 10*n, l)
                else:
                    q, r, t, k, n, l = (
                        q * k, (2*q + r) * l, t * l, k + 1,
                        (q * (7*k +2)+ r*l) // (t * l), l + 2)
                print(f'[{len(x)}]')
        elif measure == True:
            while len(x) < i:
                if 4*q + r - t < n*t:
                    x.append(n)
                    q, r, t, k, n, l = (
                        10 * q, 10 * (r-n * t), t, k,
                        (10 * (3*q + r)) // t - 10*n, l)
                else:
                    q, r, t, k, n, l = (
                        q * k, (2*q + r) * l, t * l, k + 1,
                        (q * (7*k + 2)+ r*l) // (t * l), l + 2)
                print(f'[{len(x)}]')
            end = time.time()
            print('\n\nElapsed Time: ' + f'{round(end-start, 4)}s')
            print(f'{len(x)} digits!')
            if input('Wanna take a look? (yes/no): ') == 'yes':
                print(x)
            else:
                exit()
        else:
            print('Usage error.') 
            exit()   
    except KeyboardInterrupt:
        end = time.time()
        # print(x)
        print('\n\nElapsed Time: ' + f'{round(end-start, 4)}s')
        print(f'{len(x)} digits!')
        if input('Wanna take a look? (yes/no): ') == 'yes':
            print(x)
        else:
            exit()

ans = input('Measure mode? (yes/no): ')
if ans == 'yes':
    ans = True
    limit = int(input('Limit? (integer): '))
    spigot(measure=ans, i=limit)
elif ans == 'no':
    ans = False
    spigot(measure=ans, i=0)
else:
    print('Usage error.')
    exit()
