import json

productFile = open('products.txt', 'r',encoding="UTF-8")
productLines = productFile.readlines()

targetFile = open('targets.txt', 'r', encoding="UTF-8")
targetLines = targetFile.readlines()

targetValuesDict = {line.split("\t")[0] : line.rstrip().split("\t")[1] for line in targetLines}

templeteList = [ templete for templete in productLines[0].rstrip().split("|")]
productList = []
for line in productLines[1:]:
    valuesList = [value for value in line.rstrip().split("|")]
    productDict = dict(zip(templeteList[:3], valuesList[:3] ))
    productDict[templeteList[-1:][0]] = float(valuesList[-1:][0][1:].replace(',', ""))
    taxonomy = [templeteList[item][:3]+valuesList[item] for item in range(3,7)]
    productDict["taxonomy"] = taxonomy
    productDict["targetValues"] = [targetValuesDict.get(item) for item in taxonomy]
    print (productDict)
    productList.append(productDict)

file1 = open("output.json", "w")
file1.write(json.dumps(productList))
file1.close()