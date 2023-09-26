parties = {
    "Person_A": {
        "apple": 5,
        "orange": 2
    },
    "Person_B": {
        "cherry": 3,
        "orange": 1
    },
    "Person_C": {
        "grape": 10,
        "mango": 6
    }
}
count = {}

for v in parties.values():
    for i,k in v.items():
        if count.get(i) is None:
        # if not count.get(i):
            count[i] = k
        else:
            count[i] += k

print('Total')
for i,v in count.items():
    print(f'  {i}: {v}')
