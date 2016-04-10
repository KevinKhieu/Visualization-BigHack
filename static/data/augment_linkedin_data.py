import csv
import json
linkedin_field = "If yes to either of the above, paste your LinkedIn below (or we can ask you for it later)"

with open("volunteer-signups.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    headers = reader.fieldnames
    augmented_header = headers.copy()
    augmented_header.append("Skills")
    augmented_header.append("Industry")

    enclosed_headers = []
    for header in augmented_header:
        enclosed_headers.append('"' + header + '"')

    print(",".join(enclosed_headers))

    results = []
    for row in reader:
        results.append(row)
        to_print = []
        for field in headers:
            to_print.append('"' + row[field] + '"')

        if "/in/" in row[linkedin_field]:
            filename = row[linkedin_field].split("/in/")[-1]
            with open("volunteers/" + filename) as profile:
                things = profile.readlines()
                things = "".join(things)
                person = json.loads(things)
                if person["skills"]:
                    skills = ", ".join(filter(lambda x:x != "See less" and "See " not in x, person["skills"]))
                    to_print.append('"' + skills + '"')
                else:
                    to_print.append("")

                if person["industry"]:
                    to_print.append('"' + person["industry"] + '"')
                else:
                    to_print.append("")
        else:
            to_print.append("")
        print(",".join(to_print))