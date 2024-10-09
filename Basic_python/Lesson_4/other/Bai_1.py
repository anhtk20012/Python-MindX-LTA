# import pickle
# from pathlib import Path
# label_path = Path(__file__).parent / 'func_label.pkl'
# label_path_all = Path(__file__).parent / 'func_label_all.pkl'
# save_file = Path(__file__).parent / 'check.txt'
# save_file_all = Path(__file__).parent / 'check_all.txt'
# with open(label_path, 'rb') as f_label:
#     label_dict = pickle.load(f_label)

# with open(label_path_all, 'rb') as f_label:
#     label_dict_all = pickle.load(f_label)
    
# # count = 0
# # with open (save_file, 'w') as file:   
# #     for name in label_dict_all:
# #         if label_dict[name] != label_dict_all[name]:
# #             count += 1
# #             file.write(name + '\n')
# print(label_dict['1_php_c1224573c773b6845e83505f717fbf820fc18415'])
# print(label_dict_all['1_php_c1224573c773b6845e83505f717fbf820fc18415'])
# # print(count)
        
import difflib
import pandas as pd

from pathlib import Path
pd_filter_1 = Path(__file__).parent / 'MSR_data_filtered_1.csv'
pd_filter_1 = pd.read_csv(pd_filter_1)
# pd_filter = Path(__file__).parent / 'MSR_data_filtered.csv'
# pd_filter = pd.read_csv(pd_filter)
# filter_csv = pd_filter.loc[pd_filter['Unnamed: 0'] == 177740]
# filter_csv.to_csv(pd_filter_1)

for index, row in pd_filter_1.iterrows():
    func_before = row['func_before']
    func_after = row["func_after"]
    with open (Path(__file__).parent / 'before.c', 'w') as file:
        file.write(func_before)
    with open (Path(__file__).parent / 'after.c', 'w') as file:
        file.write(func_after)
    if pd.isnull(row['lines_before']):
            continue
    else:
        label_dict = []
        diff = list(difflib.unified_diff(func_after.splitlines(), func_before.splitlines()))
        print(diff)
        split_list = [i for i,line in enumerate(diff) if line.startswith("@@")]
        split_list.append(len(diff))
        print(split_list)
        i = 0
        for i in range(len(split_list) - 1):
            start = split_list[i]
            del_linenum = diff[start].split("@@ -")[-1].split(",")[0].split('+')[-1].strip()
            end = split_list[i + 1]
            
            line_num = int(del_linenum)
            line_de = 0
            for line in diff[start+1 : end]:
                if line.startswith("-"):
                    label_dict.append(line_num)
                elif line.startswith("+"):
                    line_num -= 1
                line_num += 1
            i += 1
        print(label_dict)

    break

