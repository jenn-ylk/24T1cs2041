import sys, re, subprocess
from collections import Counter
import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    # check command line for whether the output should be sorted by frequency
    sort_by_freq = False
    if "-f" in sys.argv:
        sort_by_freq = True
        sys.argv.remove("-f")

    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <url> -f[opt]") # e.g. https://www.unsw.edu.au
        exit()

    # find all tags (contained in "<>")
    contents = requests.get(sys.argv[1]).text

    # capture tags using the parsed contents
    tags = BeautifulSoup(contents, "html.parser").find_all()
    tag_frequency = Counter([tag.name.lower() for tag in tags])

    if sort_by_freq:
        for tag in sorted(tag_frequency, key=lambda k: tag_frequency[k]):
            print(tag + "\t" + str(tag_frequency[tag]))
    else:
        for tag in sorted(tag_frequency):
            print(tag + "\t" + str(tag_frequency[tag]))



# if __name__ == "__main__":
#     if len(sys.argv) < 2:
#         print(f"Usage: {sys.argv[0]} <url>") # e.g. https://www.unsw.edu.au
#         exit()

#     # find all tags (contained in "<>")
#     contents = subprocess.run(["wget", "-O-", "-q", sys.argv[1]], capture_output=True, text=True).stdout
#     # print(contents)
#     # capture any <thing>s (this would need to be refined to exclude comments)
#     tags = [tag[0].lower() for tag in re.findall(r"<([a-zA-Z]+)( [^>]*)?>", contents)]
#     # print(Counter(tags))
#     tag_frequency = Counter(tags)

#     for tag in sorted(tag_frequency):
#         print(tag, tag_frequency[tag])