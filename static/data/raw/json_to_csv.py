import json

files = [
	"adrianna.json",
	"alberto.json",
	"alexanderyku.json",
	"alinaahmad.json",
	"amy.json",
	"arjunkunna.json",
	"asjchen.json",
	"augustinechemparathy.json",
	"austin.json",
	"bentyeh.json",
	"charles.json",
	"daniel.json",
	"david.json",
	"davidtleee.json",
	"dingv.json",
	"fanny.json",
	"grace.json",
	"hormazd.json",
	"jimmy.json",
	"jori.json",
	"kevin.json",
	"kevinkhieu.json",
	"ksnazir.json",
	"linmarisa.json",
	"mayaganesan.json",
	"mzhang8.json",
	"robert.json",
	"ronaldtep.json",
	"sample.json",
	"tgsido.json",
	"victorniu.json",
	"xnancy.json",
	"yannagong.json",
	"yincynthia.json",
	"yitzdeng.json",
]

fields = [
	"name",
	"location",
	"country",
	"industry",
	"title",
	"skills"	
]

print(",".join(fields))

for filename in files:
	with open(filename, 'r') as f:
		things = f.readlines()
		if len(things) == 1:
			person = json.loads(things[0])
			to_print = ""
			for field in fields:
				to_print += '"' + str(person[field]) + '"'
				if field != fields[-1]:
					to_print += ","
			print(to_print)
			