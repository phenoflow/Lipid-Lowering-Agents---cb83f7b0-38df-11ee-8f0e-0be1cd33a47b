# Alison K Wright, Evangelos Kontopantelis, Richard Emsley, Iain Buchan, Naveed Sattar, Martin K Rutter, Darren M. Ashcroft, 2023.

import sys, csv, re

codes = [{"code":"17614","system":"gprdproduct"},{"code":"23153","system":"gprdproduct"},{"code":"29213","system":"gprdproduct"},{"code":"32921","system":"gprdproduct"},{"code":"34181","system":"gprdproduct"},{"code":"40729","system":"gprdproduct"},{"code":"40885","system":"gprdproduct"},{"code":"42801","system":"gprdproduct"},{"code":"49609","system":"gprdproduct"},{"code":"52814","system":"gprdproduct"},{"code":"58635","system":"gprdproduct"},{"code":"59002","system":"gprdproduct"},{"code":"602","system":"gprdproduct"},{"code":"60385","system":"gprdproduct"},{"code":"64503","system":"gprdproduct"},{"code":"66425","system":"gprdproduct"},{"code":"66564","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('lipid-lowering-agents-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["lipid-lowering-agents-modifiedrelease---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["lipid-lowering-agents-modifiedrelease---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["lipid-lowering-agents-modifiedrelease---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
