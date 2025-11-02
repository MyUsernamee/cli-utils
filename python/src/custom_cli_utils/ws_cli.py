from argparse import ArgumentParser
import os
import re
import step

def get_configs():
    '''Returns a tuple with the first being the tex template, the second being the match regex'''
    template = open(os.path.join(os.environ['HOME'], ".config", "ws-cli", "template.tex"), "r").read()
    regex = open(os.path.join(os.environ['HOME'], ".config", "ws-cli", "problem.regex"), "r").read()
    return (template, regex)

def main():
    parser = ArgumentParser()

    _ = parser.add_argument("filename")

    args = parser.parse_args()

    try:
        template, regex = get_configs()
        regex = re.compile(regex)
        template = step.Template(template)
    except Exception as e:
        raise Exception("Failed to load template or regex: ", e)

    if not os.path.exists(args.filename) or not os.path.isfile(args.filename):
        raise Exception("File dones't exist or isn't a file")

    with open(args.filename, "r") as f:
        file_lines = f.readlines()
        file_content = "".join(file_lines[1:])
        title = file_lines[0].strip()
        problems = re.findall(regex, file_content)

        print(problems)
        print(title)
        with open(os.path.join( os.path.dirname(args.filename),os.path.basename(args.filename).split(".")[0] + ".tex" ), "w") as f:
            f.write(template.expand({"title": title, "problems": problems}))

    print("Done!")

