#!/usr/bin/env python
import subprocess
import datetime


def commit(timestamp):
    env = f"GIT_AUTHOR_DATE='{timestamp}' GIT_COMMITTER_DATE='{timestamp}'"
    cmd = f" git commit --allow-empty -m '{timestamp}'"
    subprocess.run(env + cmd, shell=True)


if __name__ == "__main__":
    blocks = ["░", "▒", "▓", "█"]

    banner=[]
    with open("banner.txt") as f:
        for line in f:
            banner.append(line)

    for week in range(2, 52): # exclude week 1 and week 52
        for day in range(1, 8):
            c = banner[day-1][week-2]
            if c in blocks:
                d = datetime.datetime.fromisocalendar(1985, week, day)
                for _ in range(blocks.index(c)+1):
                    commit(f"{d}")
