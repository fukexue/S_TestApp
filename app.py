from cytomine import Cytomine
from cytomine import CytomineJob
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Parse Cytomine job parameters.")

    parser.add_argument("--cytomine_host", type=str, required=True, help="Cytomine host URL.")
    parser.add_argument("--cytomine_public_key", type=str, required=True, help="Cytomine public API key.")
    parser.add_argument("--cytomine_private_key", type=str, required=True, help="Cytomine private API key.")
    parser.add_argument("--cytomine_id_project", type=int, required=True, help="Cytomine project ID.")
    parser.add_argument("--cytomine_id_software", type=int, required=True, help="Cytomine software ID.")
    parser.add_argument("--alpha", type=float, required=False, default=0.5, help="Alpha value for the task.")

    args = parser.parse_args()

    return args

def main(argv):
    with Cytomine.connect(args.cytomine_host, args.cytomine_public_key, args.cytomine_private_key) as c:
        # Implements your software here.

        # Will print the parameters with their values
        print("end")

if __name__ == "__main__":
    args = parse_arguments()
    main(args)
