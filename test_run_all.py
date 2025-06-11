import sys
import pytest


def run_tests():
    print("Test execution started\n")
    test_results = pytest.main(["tests"])

    if test_results != 0:
        print("There is at least 1 test failure, the information run will not be started!")
        sys.exit(1)


def run_information():
    print("Tests passed! Running player information\n")
    from information import information
    information.run_information_for_players()


def main():
    run_tests()
    run_information()

if __name__ == "__main__":
    main()