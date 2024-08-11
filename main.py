

from parser import parser
import argparse

args = argparse.ArgumentParser(description='OKX news parser and loader')
args.add_argument('--folder', type=str, default='data',
                    help='name folder where to store data, it will appera in temporary file')
args.add_argument('--start_date', type=str, default='2024-7-24',
                    help='we load news, this is date where to start, follow defaut example structure YEAR-MONTH-DAY')
args.add_argument('--end_date', type=str, default='2024-7-27',
                    help='this is date where to finish')

args = args.parse_args()


if __name__ == '__main__':

    try:
        parser(args.folder, args.start_date, args.end_date)
        
    except Exception as e:
        print(e)
