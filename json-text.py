# -*- coding: utf-8 -*-
import json


def main():
    json_file = "./puranas/vamana.json"
    fp = open(json_file)
    content = json.load(fp)

    fp1 = open("./puranas/vamana/vamana_full.txt", "w")
    for i in content:
        fp1.write("-----------" + i + "-----------\n")
        fp1.write('\n'.join(map(str, content[i])))
        fp1.write("\n\n\n")
    pass

if __name__ == "__main__":
    main()