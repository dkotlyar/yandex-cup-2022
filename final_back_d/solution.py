with open('input.txt', 'r') as f:
    input_txt = f.readlines()
    d, s = map(int, input_txt[0].split())
    services = input_txt[1:s + 1]
    services = [
        dict(
            n=serv[0],
            rt=serv[1],
            ds=set(serv[3:]),
        )
        for serv in map(lambda s: list(map(int, s.split())), services)
    ]

    c = int(input_txt[s + 1])
    commits = input_txt[s + 2: s + 2 + c]
    commits = [
        dict(
            ts=commit[0],
            dc=set(commit[2:]),
        )
        for commit in map(lambda c: list(map(int, c.split())), commits)
    ]

    q = int(input_txt[s + c + 2])
    requests = input_txt[s + c + 3:]
    requests = map(lambda s: list(map(int, s.split())), requests)

services_commits = [
    [-1] * len(commits)
    for _ in services
]

services_times = [0] * len(services)
service_last_commit = [-1] * len(services)
services_queue = [serv['n'] for serv in services]


def intersects(set1, set2):
    return any(s in set2 for s in set1)

def t(i):
    services_queue[i] -= 1
    return services_queue[i] == 0

def a(i):
    start_release = max(services_times[i], ts)
    # print(services_times[i], ts)
    release_time = start_release + services[i]['rt']
    services_times[i] = release_time
    commits_to_release = [
        j
        for j, comm in enumerate(commits)
        if comm['ts'] <= start_release and services_commits[i][j] == -1
    ]
    for _j in commits_to_release:
        services_commits[i][_j] = release_time
    service_last_commit[i] = commits_to_release[-1]
    services_queue[i] = services[i]['n']

for j, commit in enumerate(commits):
    ts, dc = commit['ts'], commit['dc']
    _servs = [
        i
        for i, serv in enumerate(services)
        if service_last_commit[i] < j and intersects(dc, serv['ds']) and t(i)
    ]
    [a(i) for i in _servs]
    # for i in _servs:


# print(services_commits)

for c, s in requests:
    print(services_commits[s - 1][c - 1])
