#!/usr/bin/env python3
"""Working with imports and copying files"""

# import additional code to complete our task
import shutil
import os

def main():
    # moving into the working directory
    os.chdir("/home/student/mycode/")

    # copying a single file within the directory
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

    # copying an entire directory tree within that directory
    os.system("rm -rf /home/student/mycode/5g_research_backup/")
    shutil.copytree("5g_research/","5g_research_backup/")

if __name__ == "__main__":
    main()