import dis
import marshal

def main():
    with open('hidden_4.pyc', 'rb') as pyc_file:
        code_object = marshal.load(pyc_file)

    names = [name for name in code_object.co_names if not name.startswith('__')]
    names.sort()

    for name in names:
        print(name)

if __name__ == '__main__':
    main()
