def extsort(files, ext):
    indices = {k: i for i, k in enumerate(ext)}
    new=sorted(files, key=lambda s: indices[s.rsplit('.', 1)[1]])
    return new


def main():
    files = ["file1.pdf","file2.jpg","file3.xl","file4.jpeg","file1.csv"]
    ext = ["xl","csv","jpg","pdf","jpeg"]
    print(extsort(files, ext))

if __name__ == '__main__':    # main function
    main()