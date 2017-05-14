import sys
import traceback


def main():
    if sys.version_info < (3, 6, 0):
        print("Python 3.6.0 required to run pybot")
        sys.exit(4)

    import _main
    _main.main()


if __name__ == "__main__":
    try:
        main()
    except (ImportError, ModuleNotFoundError) as e:
        name = e.name
        path = f' located at {e.path}' if e.path else ''
        print(f"No module named {name}{path}. Please try 'pip install -r ./requirements.py'")
    except Exception as e:
        print(f'Internal error occurred: {e}. Please contact  ja222ja@gmail.com  with  pybot.error  file (paths to files will be compromised).')
        with open('pybot.error', 'a') as file:
            file.write('**********************************************************************************************\n')
            file.write(traceback.format_exc())
            file.write('**********************************************************************************************\n')
