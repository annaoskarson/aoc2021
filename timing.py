import timeit, os

files = sorted([file for file in os.listdir('.') if file.startswith('aoc2021-')])
times = {}

start = timeit.default_timer()
print(type(start))
#print(files)

for f in files:
    #date = str(i + 1)
    #if len(date) < 2: date = '0' + date
    start1 = timeit.default_timer()
    exec(open(f).read())
    stop1 = timeit.default_timer()
    times[f] = stop1-start1

stop = timeit.default_timer()
#print(times)
print(type(start), type(stop))
print('======= Results =======')
for f, t in times.items():
    print(f, ':', t)
print('Total time: ', stop - start)
