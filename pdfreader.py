import pdftotext
import sys

file = sys.argv[1]
if file == "":
    print("Usage: pdfreader.py {FILE}")
    exit(1)

# Load your PDF
with open(file, "rb") as f:
    pdf = pdftotext.PDF(f)

# If you need to debug:
#
# # Save all text to a txt file.
# with open('output.txt', 'w') as f:
#     f.write("\n\n".join(pdf))


page = pdf[0]
applicableDateStartIndex = page.index("Valable pour le") + len("Valable pour le") + 2 # (new lines)
applicableDateEndIndex = applicableDateStartIndex + 10 # (date format: DD/MM/YYYY)

applicableDate = ""
for i in range(applicableDateStartIndex, applicableDateEndIndex):
    applicableDate += page[i]

publicationDateIndex = page.index("Publicatie datum")

# Format is:
# 01 - 02
#
# 83,62
#...
pricingTableStartIndex = page.index("eSpot Eur/MWh (1)") + len("eSpot Eur/MWh (1)") + 2 # (new lines)
pricingTableEndIndex = page.index("Publicatie datum")

print("date,startHour,endHour,price")

lineDefault = applicableDate + ","
line = lineDefault
charPos = 0
for i in range(pricingTableStartIndex, pricingTableEndIndex):
    char = page[i]
    charPos += 1

    if char == "-":
        continue
    if charPos == 5:
        # Skip the additional space
        continue

    if charPos == 8:
        line += ',"'
    # Skipping new lines
    if charPos == 8 or charPos == 9:
        continue

    if char == " ":
        line += ","
        continue

    if char == "\n":
        if charPos == 1:
            charPos = 0
            continue

        line += '"'
        print(line)
        charPos = 0
        line = lineDefault
        continue

    line += char