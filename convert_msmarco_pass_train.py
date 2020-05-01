import argparse
from Processors.msmarco_passages import convert_train_dataset


def main():
    
    parser = argparse.ArgumentParser()

    ## Required parameters
    parser.add_argument("--output_folder", default=None, type=str, required=True)
    parser.add_argument("--triples_train_path", default=None, type=str, required=True,
                            help="query pos_passage neg_passage")
    parser.add_argument("--set_name", default='train', type=str, required=False,
                            help="set name.")
    args = parser.parse_args()

    
    convert_train_dataset(args.triples_train_path, args.output_folder, args.set_name) 

if __name__ == "__main__":
    main()