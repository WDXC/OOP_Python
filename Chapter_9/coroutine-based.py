import re
def match_regex(filename, regex):
    with open(filename) as file:
        lines = file.readlines()
    for line in reversed(lines):
        match = re.match(regex, line)
        if match:
            regex = yield  match.groups()[0]

def get_serials(filename):
    ERROR_RE = 'XFS ERROR (\[sd[a-z]\])'
    matcher = match_regex(filename, ERROR_RE)
    device = next(matcher)
    while True:
        bus = matcher.send(
            '(sd \S+) {}.*'.format(re.escape(device))
        )
        servial = matcher.send('{} \ (SERIAL=([^)]*)\)'.format(bus))
        yield servial
        device = matcher.send(ERROR_RE)
for serial_number in get_serials('EXAMPLE_LOG.log'):
    print(serial_number)