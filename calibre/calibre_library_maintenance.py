import os
import glob
from os import listdir
from os.path import isfile, join

import os
import shutil
# from pyspark.sql import SparkSession

# spark = SparkSession.builder.master("local[*]").appName("Calibre").getOrCreate().sparkContext

# path = "D:/_books/_calibre_library/"
path = "F:/Books/_all_books/"
# dest_path = "F:/_calibre_just_books/"
dest_path = "F:/Books/_all_book_files_only/"

count = 0
extensions = []
os.chdir(path)

from os import walk

file_types = ['azw', 'azw3', 'chm', 'djv', 'djvu', 'docx', 'epub',
              'lit', 'mbp', 'mobi', 
              'pdf', 'prc', 'ps', 'rar', 'txt', 'zip']

# to_spark = []
for r, d, f in os.walk(path):
    print("Total no. of Files count is ", len(f))
    for file in f:
        file_extension = file.split(".")[-1]
        if file_extension in file_types:
            temp_file_path_and_name = os.path.join(r, file).replace("\\","/")
            temp_dest_path_and_name = dest_path + file
            # to_spark.append([temp_file_path_and_name, temp_dest_path_and_name])
            try:
                shutil.copy2(temp_file_path_and_name, temp_dest_path_and_name)
                print(file)
            except:
                continue

'''
def spark_func_file_moving(entry):
    for entry in e:
        if isinstance(entry, list):
            try:
                shutil.move(entry[0], entry[1])
                return True
            except:
                return False

result = spark.parallelize(to_spark, 100).map(shutil).collect()
print(sum(result))
'''