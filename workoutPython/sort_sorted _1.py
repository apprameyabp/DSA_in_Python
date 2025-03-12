#  Problem:
# You are given a list of tuples, where each tuple contains a name and a score.

# 👉 Task: Use a lambda function to sort the list based on the following rules:

# Sort by score in descending order.
# If scores are equal, sort by name in alphabetical order.


batting_avgs = [('Virat',56.78),('Rohith',50.45),('Gill',51.37),('Iyer',48.95),('Rahul',50.45)]
highest_avg_order = sorted(batting_avgs,key = lambda x : (-x[1], x[0]))
print(highest_avg_order)
