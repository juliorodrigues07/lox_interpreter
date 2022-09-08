from runner import run
import sys


def open_file(file_name):
    print(True)


def run_prompt():

    while True:

        print('>>> ', end='')
        line = input()
        run(line)

        if not line:
            break


def main():

    if len(sys.argv) > 2:
        print('Error!')
    elif len(sys.argv) == 2:
        open_file(sys.argv[1])
    else:
        run_prompt()


if __name__ == '__main__':
    main()
