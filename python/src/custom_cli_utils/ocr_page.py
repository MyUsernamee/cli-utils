from argparse import ArgumentParser
import os

def main():
    
    parser = ArgumentParser('ocr_page')

    _ = parser.add_argument("filename")
    _ = parser.add_argument('page')

    args = parser.parse_args()
    
    filename = args.filename
    base_file_name = os.path.basename(filename).split(".")[:-2]
    page_index = int(args.page)

    start = page_index - 1
    end = page_index

    os.system(f'mineru -b vlm-transformers -p {filename} -s {start} -e {end} -o /tmp/ && cat /tmp/{base_file_name}/vlm/{base_file_name}.md')


