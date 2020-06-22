import os

a = []
summary = '# 目录\n'
for i in os.listdir("src"):
    folder = os.path.join('src', i)
    if os.path.isdir(folder):
        summary += f"* [{i}](./SUMMARY.md)\n"
        for j in os.listdir(folder):
            summary += f"  * [{j}](./{i}/{j})\n"
open('src/SUMMARY.md', 'w').write(summary)
