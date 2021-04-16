logs = ["1 2 50", "1 7 70", "1 3 20", "2 2 17"]
threshold = 2

def processLogs(logs, threshold):
    log_hash = {}

    # populate log_hash
    for log in logs:
        cur_string = log.split(" ")
        if cur_string[0] == cur_string[1]:
            try:
                log_hash[cur_string[0]] += 1
            except KeyError:
                log_hash[cur_string[0]] = 1
        else:
            try:
                log_hash[cur_string[0]] += 1
            except KeyError:
                log_hash[cur_string[0]] = 1

            try:
                log_hash[cur_string[1]] += 1
            except KeyError:
                log_hash[cur_string[1]] = 1

    # filter log_hash with values greater than threshold, return as array
    filtered_log_hash_array = [int(k) for (k,v) in log_hash.items() if v >= threshold]

    # ensure result is sorted
    sorted_result = sorted(filtered_log_hash_array)

    # cast elements back to strings, and return

    return [str(user_id) for user_id in sorted_result]
        


print(processLogs(logs, threshold))