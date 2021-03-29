


queries = open("midterm_query_counts.txt", "r").read()
queries = queries.split("\n")

check_cheating = []


for query in queries:
    query = query.split(", ")
    student = query[0]
    try:
        count = query[1].split(" ")
        count = count[1].replace("}]", "")
    except: 
        count = 0
    try:
        count = int(count)
        print(count)
    except:
        count = 0
    if count == 0:
        pass
    elif 100 < count < 120:
        check_cheating.append(student)
    else: 
        pass

print(check_cheating)

#
# count < 100 = ['lijinhu (49 queries)', 'tkarki (89 queries)', 'zhuoqunw (97 queries)'] Taya Vilify
#did nopt finish the exam. Jinhu got a 65. Lea Wei got a 75.

# count 100 < count <120 = ['czj (106 queries, score: 100/100)', 'acaranna (116 queries, score: 75/87)', 
# 'rmconnot (109 queries, score: 90/87)', 'ekaser (113 queries, score: 90/91)', 
# 'imulhern (101 queries, score: 90/95)', 'ipanema (118 queries, score: 90/92)', 'zhangjw (108 queries, score: 90/100)']