
def replace(filename):
	rep = []
	with open(filename, 'r') as file:
		for row in file:
			rep.append(row.replace("/mnt/e", "E:"))
	
	with open("rep_"+filename, 'w') as output:
		for row in rep:
			output.write(row)

def Exec(files):
	for f in files:
		replace(f)

Exec(["test.list", "train.list"])