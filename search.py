from googlesearch import search

query = "sched/ file changed site:lkml.org"

for link in search(query, tbs='cdr%3A1%2Ccd_min%3A1%2F1%2F2019%2Ccd_max%3A3%2F27%2F2020'):
    print(link)
