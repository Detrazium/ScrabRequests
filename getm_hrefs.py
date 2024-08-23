with (
    open('all_hrefs_url/all_urls.txt', 'r', encoding='utf=8') as file,
    open('all_hrefs_url/all_workers_hrefs/hrefs_one_worker_0.txt', 'w', encoding='utf=8') as file0,
    open('all_hrefs_url/all_workers_hrefs/hrefs_one_worker_1.txt', 'w', encoding='utf=8') as file1,
    open('all_hrefs_url/all_workers_hrefs/hrefs_one_worker_2.txt', 'w', encoding='utf=8') as file2,
    open('all_hrefs_url/all_workers_hrefs/hrefs_one_worker_3.txt', 'w', encoding='utf=8') as file3,
    open('all_hrefs_url/all_workers_hrefs/hrefs_one_worker_4.txt', 'w', encoding='utf=8') as file4,
    open('all_hrefs_url/all_workers_hrefs/hrefs_one_worker_5.txt', 'w', encoding='utf=8') as file5,
    open('all_hrefs_url/all_workers_hrefs/hrefs_one_worker_6.txt', 'w', encoding='utf=8') as file6,
    open('all_hrefs_url/all_workers_hrefs/hrefs_one_worker_7.txt', 'w', encoding='utf=8') as file7,
    open('all_hrefs_url/all_workers_hrefs/hrefs_one_worker_8.txt', 'w', encoding='utf=8') as file8,
    open('all_hrefs_url/all_workers_hrefs/hrefs_one_worker_9.txt', 'w', encoding='utf=8') as file9,
):
    lines = file.readlines()
    keys = [file0, file1, file2, file3, file4, file5, file6, file7, file8, file9]
    key = 0
    i = 0
    ss = 572
    for line in lines:
        s = line.replace('\n', '')
        if '/c/' not in s and '/p/agid.' in s:
            i += 1
            print(i, ' |:| ', s)
            keys[key].write(s + '\n')
            if i >= ss:
                if key < 9:
                    key += 1
                ss += 572

