import sys
import os

print("------ Subs fixer for MediaServer! ------")
print("\n")

if (len(sys.argv) < 3):
    print("Please run this script with the following args:")
    print("1 - Substring to find (i.e. _eng.ass)")
    print("2 - Substring to replace (i.e. .eng.ass)")
    print("3 - Folder path")
    print("Example: python3 fix_subs_names.py \"_eng.ass\" \".eng.ass\" PATH ")
    exit()

old_string = sys.argv[1]
new_string = sys.argv[2]
path = sys.argv[3]

print(f"old_string: {old_string} | new_string: {new_string} | path: {path}")

for count, file in enumerate(sorted(os.listdir(path))):
    src =f"{path}/{file}"
    dst=f"{path}/{file.replace(old_string, new_string)}"
    os.rename(src, dst)

print("Renamed!")