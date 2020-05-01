import argparse
from Processors.mb import convert_train_dataset, convert_eval_dataset


def main():
    
    parser = argparse.ArgumentParser()

    ## Required parameters
    parser.add_argument("--output_folder", default=None, type=str, required=True)
    parser.add_argument("--data_path", default=None, type=str, required=True,
                            help="folder containing a.toks, b.toks, sim.txt")
    parser.add_argument("--set_name", default='train', type=str, required=False,
                            help="set name.")
    parser.add_argument("--mode", default='test', type=str, required=False,
                            help="mode: train / test")
    args = parser.parse_args()

    if args.mode.lower() == 'test':
        convert_eval_dataset(args.data_path, args.output_folder, args.set_name)
    elif args.mode.lower() == 'train':
        convert_train_dataset(args.data_path, args.output_folder, args.set_name)
    else : 
        raise ValueError('mode must be in: train, test ')
     

if __name__ == "__main__":
    main()