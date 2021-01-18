results1 = {
    "sec1":{
       "line1":{
          "notes":"",
          "value":""
       },
       "line2":{
          "value":""
       }
    },
    "sec2":{
       "line1":{
          "notes":""
       }
    }
 }



results2 = {
    "sec1":{
       "line1":{
          "notes":"Some Notes",
          "value":"AA"
       },
       "line2":{
          "value":"BB"
       }
    },
    "sec2":{
       "line1":{
          "notes":"sdfs"
       }
    }
 }

# print(len(results1))
# print(sum([len(results1[k]) for k in results1]))

# print(sum([len(results1[k]) for k in results1 if len(results1[k]) > 0]))

lineCount = 0
for section in results2:
    for line in results2[section].values():
        for item in line.values():
            if len(item) > 0:
                lineCount +=1



print(lineCount)



