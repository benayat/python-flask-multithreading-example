# python-flask-multithreading-example
<h1>python-flask-multithreading-example</h1>
a simplle python-flask-rq-supervisor boilerplate for multithreading and schedulling tasks. 
requirements: 
- redis.
- python3
- flask
- rq
- supervisord

<h2>to run:</h2>
1. run redis-server
2. run python app.py
3. run supervisord
4. go to the endpoint "/task?n=100"
results:
- the supervisor process id is in supervisord.pid
- the processes info from the OS is in supervisord.log
- the program info about the running tasks and processes is in super_logs.conf