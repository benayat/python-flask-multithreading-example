# python-flask-multithreading-example
<h1>python-flask-multithreading-example</h1>
a simplle python-flask-rq-supervisor boilerplate for multithreading and schedulling tasks. 

requirements:
<ul> 
<li>redis.</li>
<li>python3</li>
<li>flask</li>
<li>rq</li>
<li>supervisord</li>
</ul>
<h2>to run:</h2>
<ol>
<li>run redis-server</li>
<li>run python app.py</li>
<li>run supervisord</li>
</li>go to the endpoint "/task?n=100"</li>
</ol>
results:
<ul>
<li>the supervisor process id is in supervisord.pid</li>
<li>the processes info from the OS is in supervisord.log</li>
<li>the program info about the running tasks and processes is in super_logs.conf</li>
</ol>