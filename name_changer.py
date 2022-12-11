import sys
import os

print("------ Name changer for MediaServer! ------")
print("\n")

if (len(sys.argv) < 5):
    print("Please run this script with the following args:")
    print("1 - The name of the show")
    print("2 - Season number")
    print("3 - First episode index value, use 1 if unknown")
    print("4 - The path of the season folder")
    print("Example: python3 name_changer.py \"Naruto Shippuden\" 2 53")
    exit()

name = sys.argv[1]
season_number = sys.argv[2]
first_index = sys.argv[3]
path = sys.argv[4]

# print(f"name: {name} | season_number: {season_number} | first_index: {first_index} | path: {path}")

for count, file in enumerate(sorted(os.listdir(path))):
    # print (f"count: {count} | file: {file}")
    filename, file_extension = os.path.splitext(f"{path}/{file}")
    episode_number = count + int(first_index)
    dst = f"{path}/{name} - S{'0' if int(season_number) <= 9 else ''}{season_number}E{'0' if episode_number <= 9 else ''}{episode_number}{file_extension}"
    src =f"{path}/{file}"
    os.rename(src, dst)

print("Renamed!")