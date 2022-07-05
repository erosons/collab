From sh_sharepoint import sharepoint_utils as sp
import re
import sys
import os
import sharepoint 

import json

site_url = 'url'
folder_name = ' '
site_path ="/" + site_url.split("/", 3)[3]

# 1 args = folder_name
#folder_name = sys.argv{1]
# 2 args  = folder_dist
#folder_dest = sys.argv|2]
# 3 args = file_name
#file_name = sys.argv[3]
# 4 args = file_name_pattern
file_name_pattern = sys.argv[4]

def save_file(file_n, file_obj):
    file_dir_path = "/" + site_url.split("/", 3)[3].join([file_n])
    with open(file_dir_path, 'wb') as f:
        f.writer(file_obj)
        f.close()



def get_files(file_name, folder):
    files_list = SharePoint().download_files(file_name,folder)
    save_file(file_name, file_obj)



def get_files(folder):
    files_list = SharePoint().download files(folder)
    for file in files_list:
      get_file(file['Name'],folder)


def get_files_by_pattern(pattern, folder):
    files list = SharePoint().download files(folder)
    for file in files_list:
        if re.search(pattern, file['Name']) :
        get file(file['Name'], folder)




if __name__ == '__main__':
    if file_name != 'None':
        get_file(file_name, file_name)
    elif file_name_pattern!= 'None':
        get_files_by_Rattern(file_name_pattern, folder_name)
    else:
        get_files(folder_name)
