# A WSGI application path in pattern $(MODULE_NAME):$(VARIABLE_NAME).

"""
Run server from command:
PYTHONPATH=<base_dir> gunicorn -c gunicorn.conf.py
"""
wsgi_app = "app:create_app()"

"""
Command line: --reload

Default: False

Restart workers when code changes.

This setting is intended for development. It will cause workers to be restarted 
whenever application code changes.

The reloader is incompatible with application preloading. When using a paste 
configuration be sure that the server block does not import any application 
code or the reload will not work as designed.

The default behavior is to attempt inotify with a fallback to file system 
polling. Generally, inotify should be preferred if available because it 
consumes less system resources.

Note In order to use the inotify reloader, you must have the inotify package
 installed.
"""
reload = True

"""
Command line: --reload-engine STRING

Default: 'auto'

The implementation that should be used to power reload.

Valid engines are:

'auto'
'poll'
'inotify' (requires inotify)
"""
reload_engine = 'inotify'

"""
Extends reload option to also watch and reload on additional files
(e.g., templates, configurations, specifications, etc.).
"""
# reload_extra_files = ""

"""
Command line: --spew

Default: False

Install a trace function that spews every line executed by the server.

This is the nuclear option.
"""
# spew = True

"""
Check the configuration and exit. The exit status is 0 if the configuration
is correct, and 1 if the configuration is incorrect.
"""
# check_config = False

"""
Command line: --access-logfile FILE

Default: None

The Access log file to write to.

'-' means log to stdout.
"""
accesslog = "../gunicorn_access.log"

"""
Command line: --disable-redirect-access-to-syslog

Default: False

Disable redirect access logs to syslog.
"""
disable_redirect_access_to_syslog = True

"""
Command line: --error-logfile FILE or --log-file FILE

Default: '-'

The Error log file to write to.

Using '-' for FILE makes gunicorn log to stderr.
"""
errorlog = "../gunicorn_error.log"

"""
Command line: --log-level LEVEL

Default: 'info'

The granularity of Error log outputs.

Valid level names are:

'debug'

'info'

'warning'

'error'

'critical'
"""
# loglevel = 'debug'


"""
Command line: --capture-output

Default: False

Redirect stdout/stderr to specified file in errorlog.
"""
capture_output = True

"""
Default: 'gunicorn'

Internal setting that is adjusted for each type of application.
"""
# default_proc_name = "gunicorn"

"""
Command line: --limit-request-line INT

Default: 4094
The maximum size of HTTP request line in bytes.

This parameter is used to limit the allowed size of a client’s HTTP 
request-line. Since the request-line consists of the HTTP method, URI, and 
protocol version, this directive places a restriction on the length of a 
request-URI allowed for a request on the server. A server needs this value to 
be large enough to hold any of its resource names, including any information 
that might be passed in the query part of a GET request. Value is a number 
from 0 (unlimited) to 8190.

This parameter can be used to prevent any DDOS attack.
"""
# limit_request_line = 4094

"""
Command line: --limit-request-fields INT

Default: 100

Limit the number of HTTP headers fields in a request.

This parameter is used to limit the number of headers in a request to prevent 
DDOS attack. Used with the limit_request_field_size it allows more safety. 
By default this value is 100 and can’t be larger than 32768.
"""
# limit_request_fields = 100

"""
Command line: --limit-request-field_size INT

Default: 8190

Limit the allowed size of an HTTP request header field.

Value is a positive number or 0. Setting it to 0 will allow unlimited header 
field sizes.

Warning Setting this parameter to a very high or unlimited value can open up 
for DDOS attacks.
"""
# limit_request_field_size = 8190

"""
Command line: --preload

Default: False

Load application code before the worker processes are forked.

By preloading an application you can save some RAM resources as well as speed 
up server boot times. Although, if you defer application loading to each worker
 process, you can reload your application code easily by restarting workers.
"""
preload_app = False

"""
Command line: --no-sendfile

Default: None

Disables the use of sendfile().

If not set, the value of the SENDFILE environment variable is used to enable 
or disable its usage.
"""
# sendfile = True

"""
Command line: -D or --daemon

Default: False

Daemonize the Gunicorn process.

Detaches the server from the controlling terminal and enters the background.
"""
# daemon = False

"""
Command line: -p FILE or --pid FILE

Default: None

A filename to use for the PID file.

If not set, no PID file will be written.
"""
pidfile = "gunicorn.pid"

"""
Command line: -u USER or --user USER

Default: os.geteuid()

Switch worker processes to run as this user.

A valid user id (as an integer) or the name of a user that can be retrieved 
with a call to pwd.getpwnam(value) or None to not change the worker process 
user.
"""
# user = "jobs"

"""
Command line: -g GROUP or --group GROUP

Default: os.getegid()

Switch worker process to run as this group.

A valid group id (as an integer) or the name of a user that can be retrieved 
with a call to pwd.getgrnam(value) or None to not change the worker processes
 group.
"""
# group = "jobs"

"""
Default: 
secure_scheme_headers = {
    'X-FORWARDED-PROTOCOL': 'ssl',
    'X-FORWARDED-PROTO': 'https',
    'X-FORWARDED-SSL': 'on'
}

A dictionary containing headers and values that the front-end proxy uses to 
indicate HTTPS requests. If the source IP is permitted by forwarded_allow_ips
 (below), and at least one request header matches a key-value pair listed in 
 this dictionary, then Gunicorn will set wsgi.url_scheme to https, so your 
 application can tell that the request is secure.

If the other headers listed in this dictionary are not present in the request,
 they will be ignored, but if the other headers are present and do not match 
 the provided values, then the request will fail to parse. See the note below 
 for more detailed examples of this behaviour.

The dictionary should map upper-case header names to exact string values. The 
value comparisons are case-sensitive, unlike the header names, so make sure 
they’re exactly what your front-end proxy sends when handling HTTPS requests.

It is important that your front-end proxy configuration ensures that the 
headers defined here can not be passed directly from the client.
"""
# secure_scheme_headers = ""


"""
Default: '127.0.0.1,::1'

Front-end’s IPs from which allowed to handle set secure headers. 
(comma separated).

Set to * to disable checking of front-end IPs. This is useful for setups 
where you don’t know in advance the IP address of front-end, but instead have 
ensured via other means that only your authorized front-ends can access 
Gunicorn.

By default, the value of the FORWARDED_ALLOW_IPS environment variable. If
 it is not defined, the default is "127.0.0.1,::1".
"""
# forwarded_allow_ips = ""

"""
Command line: -b ADDRESS or --bind ADDRESS

Default: ['127.0.0.1:8000']

The socket to bind.

A string of the form: HOST, HOST:PORT, unix:PATH, fd://FD. An IP is a valid HOST.

Changed in version 20.0: Support for fd://FD got added.

Multiple addresses can be bound. ex.:

$ gunicorn -b 127.0.0.1:8000 -b [::1]:8000 test:app
will bind the test:app application on localhost both on ipv6 and ipv4 interfaces.

If the PORT environment variable is defined, the default is ['0.0.0.0:$PORT']. 
If it is not defined, the default is ['127.0.0.1:8000'].
"""
bind = "0.0.0.0:8000"

"""
Command line: --backlog INT

Default: 2048

The maximum number of pending connections.

This refers to the number of clients that can be waiting to be served.
 Exceeding this number results in the client getting an error when attempting
  to connect. It should only affect servers under significant load.

Must be a positive integer. Generally set in the 64-2048 range.
"""
# backlog = 2048

"""
Command line: -w INT or --workers INT

Default: 1

The number of worker processes for handling requests.

A positive integer generally in the 2-4 x $(NUM_CORES) range. You’ll want to 
vary this a bit to find the best for your particular application’s work load.

By default, the value of the WEB_CONCURRENCY environment variable, which is 
set by some Platform-as-a-Service providers such as Heroku. If it is not 
defined, the default is 1.
"""
workers = 4

"""
Command line: -k STRING or --worker-class STRING

Default: 'sync'

The type of workers to use.

The default class (sync) should handle most “normal” types of workloads. 
You’ll want to read Design for information on when you might want to choose
 one of the other worker classes. Required libraries may be installed using 
 setuptools’ extras_require feature.

A string referring to one of the following bundled classes:

sync

eventlet - Requires eventlet >= 0.24.1 (or install it via pip install 
gunicorn[eventlet])

gevent - Requires gevent >= 1.4 (or install it via pip install 
gunicorn[gevent])

tornado - Requires tornado >= 0.2 (or install it via pip install 
gunicorn[tornado])

gthread - Python 2 requires the futures package to be installed 
(or install it via pip install gunicorn[gthread])

Optionally, you can provide your own worker by giving Gunicorn a Python path to
 a subclass of gunicorn.workers.base.Worker. This alternative syntax will load
  the gevent class: gunicorn.workers.ggevent.GeventWorker.
"""
# worker_class = "sync"

"""
Command line: --threads INT

Default: 1

The number of worker threads for handling requests.

Run each worker with the specified number of threads.

A positive integer generally in the 2-4 x $(NUM_CORES) range. You’ll want to
 vary this a bit to find the best for your particular application’s work load.

If it is not defined, the default is 1.

This setting only affects the Gthread worker type.

Note If you try to use the sync worker type and set the threads setting to 
more than 1, the gthread worker type will be used instead.
"""
# threads = 1

"""
Command line: --worker-connections INT

Default: 1000

The maximum number of simultaneous clients.

This setting only affects the gthread, eventlet and gevent worker types.
"""
# worker_connections = 512

"""
Command line: --max-requests INT

Default: 0

The maximum number of requests a worker will process before restarting.

Any value greater than zero will limit the number of requests a worker will
 process before automatically restarting. This is a simple method to help 
 limit the damage of memory leaks.

If this is set to zero (the default) then the automatic worker restarts are
 disabled.
"""
# max_requests = 1024

"""
Command line: --max-requests-jitter INT

Default: 0

The maximum jitter to add to the max_requests setting.

The jitter causes the restart per worker to be randomized by randint(0, 
max_requests_jitter). This is intended to stagger worker restarts to avoid 
all workers restarting at the same time.
"""
# max_requests_jitter = 512

"""
Command line: -t INT or --timeout INT

Default: 30

Workers silent for more than this many seconds are killed and restarted.

Value is a positive number or 0. Setting it to 0 has the effect of infinite 
timeouts by disabling timeouts for all workers entirely.

Generally, the default of thirty seconds should suffice. Only set this 
noticeably higher if you’re sure of the repercussions for sync workers. 
For the non sync workers it just means that the worker process is still 
communicating and is not tied to the length of time required to handle a
 single request.
"""
# timeout = 30

"""
Command line: --graceful-timeout INT

Default: 30

Timeout for graceful workers restart.

After receiving a restart signal, workers have this much time to finish serving
 requests. Workers still alive after the timeout (starting from the receipt of 
 the restart signal) are force killed.
"""
# graceful_timeout = 30

"""
Command line: --keep-alive INT

Default: 2

The number of seconds to wait for requests on a Keep-Alive connection.

Generally set in the 1-5 seconds range for servers with direct connection to
 the client (e.g. when you don’t have separate load balancer). When Gunicorn 
 is deployed behind a load balancer, it often makes sense to set this to a 
 higher value.

Note sync worker does not support persistent connections and will ignore this 
option.
"""
# keepalive = 2
