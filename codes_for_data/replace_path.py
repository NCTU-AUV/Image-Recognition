
def replace(filename):
	rep = []
	with open(filename, 'r') as file:
		for row in file:
			#n_path = row.replace("/mnt/e", "E:")
			n_path = row.replace("/mnt/e/darknet/test/data/t3/img/", "")
			
			rep.append(n_path)
	
	#with open("rep_train"+"."+filename.split(".")[1], 'w') as output:
	with open("img_name.list", 'w') as output:
		for row in rep:
			output.write(row)

def Exec(files):
	for f in files:
		replace(f)

Exec(["name.list"])