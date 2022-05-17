from matplolib import pyplot as pt
over = [1,2,3,4,5,6,7,8,9,10]
runs = [8,2,5,9,0,1,3,4,6,2]
wickets = [0,1,0,1,1,1,0,0,2]

pt.scatter(over,runs)
pt.scatter(over,wickets)

pt.xlabel("Overs")
pt.ylabel("Runs")
pt.title("Match Score")