import subprocess
script_fn = 'C:/Program Files (x86)/WinSCP/prova1ot4.txt'
script_fn2 = 'C:/Program Files (x86)/WinSCP/stockcdc.txt'
test_fn = 'test.txt'
log_fn = 'log.txt'
# parameters to pass to the script (uploading the test file and the script)
parameters = [test_fn, script_fn]
# the adjusted command, passing '/parameter' and then just the parameters
subprocess.run([
    'C:/Program Files (x86)/WinSCP/WinSCP.com',
    '/script=' + script_fn,
    '/log=' + log_fn,
    '/ini=nul'
] , shell=True)

subprocess.run([
    'C:/Program Files (x86)/WinSCP/WinSCP.com',
    '/script=' + script_fn2,
    '/log=' + log_fn,
    '/ini=nul'
] , shell=True)
