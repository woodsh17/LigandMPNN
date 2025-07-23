from LigandMPNN.__main__ import main
from LigandMPNN.cli import get_argparser

if __name__ == "__main__":
    parser = get_argparser(include_main_args=True)
    args = parser.parse_args()
    main(args)
