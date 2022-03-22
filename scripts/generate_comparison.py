import multiprocessing
import os
from pprint import pformat

from jinja2 import Template
from lib.transformcompare import TransformCompare

FILES_PATH = '../examples/input/'


def render_results():
    # Load files
    examples_json_files = [FILES_PATH + f for f in os.listdir(FILES_PATH) if f.endswith('.json')]

    # Perform comparison with input and transformed (expected)
    tc = TransformCompare()
    comparisons = dict()
    for f in sorted(examples_json_files):
        comparisons |= {f: tc.compare_transform(f, f.replace('input/', 'expected/'))}

    # Results summary stats
    total_files = len(comparisons)
    flagged = tc.count_flagged(comparisons)
    no_issues = total_files - flagged

    # Use Jinja2 template to render results into README file for the examples folder
    results_template = open('./templates/comparison_results.jinja2').read()
    t = Template(results_template)
    t.globals['format_key'] = format_key
    t.globals['pformat'] = pformat
    t.globals['basename'] = os.path.basename
    results_rendered = t.render(comparisons=comparisons,
                                total_files=total_files,
                                no_issues=no_issues,
                                flagged=flagged)

    # Write out README for the examples folder
    readme = open('../examples/README.md', 'w')
    readme.write(results_rendered)


def format_key(key):
    if len(key) <= 1:
        return key[0] + ":"

    formatted_key = key[0]
    for k in range(1, len(key)):
        formatted_key += " --> " + key[k]
    return formatted_key + ":"


# NOTE: If the packages aren't tar-ed and are available on disk at ~/.fhir for example, this runs in a few seconds.
# The packages are included in the repo so there is minimal config needed to run it out of the box
def main():
    render_results()


if __name__ == "__main__":
    main()
