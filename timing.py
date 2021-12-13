import timeit, os

files = [file for file in os.listdir('.') if file.startswith('aoc2021-')]
times = {}

start = timeit.default_timer()

for i,f in enumerate(files):
    date = str(i + 1)
    if len(date) < 2: date = '0' + date
    start1 = timeit.default_timer()
    exec(open('aoc2021-' + date + '.py').read())
    stop1 = timeit.default_timer()
    times[date] = stop1-start1

stop = timeit.default_timer()

print('======= Results =======')
for date in times:
    print(date + ':', times[date])
print('Total time: ', stop - start)
