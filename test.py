import subprocess
import sys


def test(equation):
    expression, answer = equation.split('=')
    p = subprocess.Popen(['python3', 'calc.py', expression],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    result, _ = p.communicate()

    if answer.strip() == '?':
        return p.returncode != 0

    return result.strip() and abs(float(result) - float(answer)) < 0.001 and \
            p.returncode == 0


for case in open('testcase.txt'):
    if not test(case):
        print('Incorrect: {}'.format(case))
        sys.exit(1)
