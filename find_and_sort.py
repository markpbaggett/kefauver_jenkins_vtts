import os
import shutil


class PathFinder:
    def __init__(self, tree):
        self.tree = tree
        self.paths = self.__find_paths()

    def __find_paths(self):
        paths = []
        with open(self.tree, 'r') as tree_text:
            for line in tree_text:
                if 'Web Copy' in line:
                    paths.append({line.split('/')[2]: line.strip().replace('./', '')})
        return paths

    def __create_directories(self, path):
        directories = path.split('/')
        if not os.path.exists(f"KefauverJenkins/{directories[0]}"):
            os.makedirs(f"KefauverJenkins/{directories[0]}")
        if not os.path.exists(f"KefauverJenkins/{directories[0]}/{directories[1]}"):
            os.makedirs(f"KefauverJenkins/{directories[0]}/{directories[1]}")
        if not os.path.exists(f"KefauverJenkins/{directories[0]}/{directories[1]}/{directories[2]}"):
            os.makedirs(f"KefauverJenkins/{directories[0]}/{directories[1]}/{directories[2]}")
        return

    def reorganize(self, directory):
        for path, directories, files in os.walk(directory):
            for file in files:
                if 'EKAV' in file:
                    new_directory = file.split('_')[0]
                    for path in self.paths:
                        if new_directory in path:
                            self.__create_directories(path[new_directory])
                            shutil.copy2(os.path.join(directory, file), f"KefauverJenkins/{path[new_directory]}")
        return


if __name__ == "__main__":
    x = PathFinder("directories.txt").reorganize('/Users/markbaggett/Downloads/transcripts/output/')
