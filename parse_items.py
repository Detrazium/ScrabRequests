with open('all_urls.txt', 'r', encoding='utf=8') as file:
    lines = file.readlines()
    k = 0
    for line in lines:
        k +=1
    print(k * 22.1 / 60 /60)