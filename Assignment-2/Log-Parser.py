def parse_log(file_name):
    counts = {"INFO": 0, "ERROR": 0, "DEBUG": 0}
    try:
        with open(file_name) as f:
            for line in f:
                for level in counts:
                    if level in line:
                        counts[level] += 1
    except FileNotFoundError:
        print("Log file not found")
    return counts

result = parse_log("application.log")
print(result)
