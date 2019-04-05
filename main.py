import sys
import parser


def main():
    # print command line arguments

    for arg in sys.argv[1:]:
        print("Reading Log file")
        print(arg)
        parser.read_file(arg)


if __name__ == "__main__":
    main()
