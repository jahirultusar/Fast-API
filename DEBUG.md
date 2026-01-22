# to find a process ID or PID in linux for example the process running on port 8000
 => sudo lsof -i :8000

 ^ that will come back with something like this:

COMMAND    PID USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
hp-printe 1672 root    4u  IPv4  19162      0t0  TCP *:8000 (LISTEN)
hp-printe 1672 root    5u  IPv6  19163      0t0  TCP *:8000 (LISTEN)


# to kill that specific process to free up port 8000
=> sudo kill 1672