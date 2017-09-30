import os
if __name__ == '__main__':
    pathDir = r'\\192.168.30.89\share\第29次南极考察原始数据（不包括田启国提交的天文数据）'
    # (dir_path,subpaths,files) = os.walk(pathDir)
    for dir_path, subpaths, files in os.walk(pathDir, False):
        print (dir_path,subpaths,files)