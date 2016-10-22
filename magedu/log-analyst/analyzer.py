import sys
import re
import datetime
def read_log(path):
    with open(path) as f:
        for line in f:
            yield line


def parse(path):
    o = re.compile(r'(?P<)')
    for line in read_log():
        m = o.search(line.rstrip('\n'))
        if m:
            data = m.groupdict()
            data['time'] = datetime.datetime.strptime(data['time'],'%d/%b/%Y:%H:%M:%S %z')
            yield data

def window(time):
    pass


def count(key,data):
    if key not in data.keys():
        data[key] += 1
    data[key] += 1
    return data


def analyze(path):
    ret = {}

    def init_data():
        return {
                'ip': {},
                'url': {},
                'us': {},
                'status': {},
                'throughtput': 0
                }
    for item in parse(path):
        time = item['time'].format('%Y%m')
        for key,value in data.items():
            if key != 'throughput':
                data[key] = count(item[key],value)
        data['throughtput'] += int(item['length'])
    return data


def render_line(name,data):
    pass


def render_bar(name,data):
    pass


def render_pie(name,data):
    pass


def main():
    data = analyze(sys.argv[1])
    render_line('throughput',data['throughput'])