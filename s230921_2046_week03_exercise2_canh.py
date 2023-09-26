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
tong = {}
for i, j in parties.items():
	for k,l in j.items():
		if k in tong:
			tong[k]+=l
		else:
			tong[k]=l
	print(tong)
