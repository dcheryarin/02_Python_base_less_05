import json

total_pribyl = 0
all_comp = 0
with open('exercise7.json', 'w', encoding='utf-8') as f_json:
    with open('exercise7.txt', encoding='utf-8') as f_txt:
        companies = {}
        middle_prib = []
        line = f_txt.read().split("\n")
        for words in line:
            word = words.split()
            #            print(word)
            pribyl = int(word[2]) - int(word[3])
            if pribyl > 0:
                total_pribyl += pribyl
                all_comp += 1
                middle_prib = total_pribyl / all_comp
            #            print(middle_prib)
            companies[word[0]] = pribyl
        #            print(companies)
        all_list = [companies, middle_prib]
        print(all_list)
    json.dump(all_list, f_json, ensure_ascii=False, indent=4)
