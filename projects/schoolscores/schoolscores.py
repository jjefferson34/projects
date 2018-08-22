import school_scores
lists = school_scores.get_all()

#1st element in data set
#print(lists)
#print(lists[0])

#each state and year
#for i in range(len(lists)):
    #print(lists[i]["State"])
    #print(lists[i]["Year"])

#same, but for each row
#for row in lists:
    #info = row["State"]
    #print(info["Name"], row["Year"])
    #print(row["Year"])

#shorter Way
#for row in lists:
    #print(row["State"]["Name"], row["Year"])

#print # of test takers per state per year
for num in lists:
    print(num["State"]["Name"], num["Total"]["Test-takers"])
