import xml.etree.ElementTree as et
import datetime

f = open("sample-1-working.xml", "rt")
tree = et.parse("sample-1-working.xml")
root = tree.getroot()
# root = et.fromstring(f.read())

secs = {}
xrefs = {}
title = "179_nac_"
for number in root.iter("number"):
    sec_id = number.get("id")
    text = number.text
    secs.update({sec_id: text})

for xref in root.iter("xref"):
    xref_cite = xref.get("cite").replace("#", "")
    xref_text = xref.text
    xrefs.update({xref_cite: xref_text})


# List of secs keys
sec_keys = list(secs.keys())

# List of secs values
sec_values = list(secs.values())

# List of xrefs keys
xref_keys = list(xrefs.keys())

# List of xrefs values
xref_values = list(xrefs.values())

i = 0

while i < len(xref_keys):
    if xref_keys[i] in sec_keys:
        sec_match_index = sec_keys.index(xref_keys[i])

        if xref_values[i] in sec_values[sec_match_index]:
            xref_values[i] = sec_values[sec_match_index]
            xref_keys[i] = "#" + sec_keys[sec_match_index]
            # print(xref_keys[i], xref_values[i])
            # print("secs and xrefs are the same")
        else:
            # Update the xref_key
            xref_keys[i] = "#" + title + sec_values[sec_match_index]
            # Update the xref_value
            xref_values[i] = sec_values[sec_match_index]
            # Update the original sec_key
            sec_keys[sec_match_index] = xref_keys[i].replace("#", "")

            print(datetime.datetime.now(), "New xref_key: ", xref_keys[i])
            print(datetime.datetime.now(), "New xref_value: ", xref_values[i])
            print(datetime.datetime.now(), "New og key: ", sec_keys[sec_match_index])

    i += 1

i = 0

for number in root.iter("number"):
    number.text = sec_values[i]
    number.set("id", sec_keys[i])
    i += 1

i = 0

for xref in root.iter("xref"):
    xref.text = xref_values[i]
    xref.set("cite", xref_keys[i])
    i += 1

tree.write("output-sample-3.xml")
