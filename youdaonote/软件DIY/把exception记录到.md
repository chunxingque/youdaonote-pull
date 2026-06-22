  
logger.exception("Exception Logged")    
  
`logging.handlers.``RotatingFileHandler`(*'*LYYDownloaderServer.log*'*, maxBytes=102400, backupCount=5)  
什么玩意`logging.handlers.``WatchedFileHandler`  
<https://docs.python.org/3/library/logging.handlers.html#logging.handlers.WatchedFileHandler>  
`logging.handlers.``SMTPHandler`  
运行过程中出错，没有try exception 咋办
```
 logging.error(e, exc\_info=True)
```
  

```
import sys
import logging
import traceback

def log\_except\_hook(\*exc\_info):
 text = "".join(traceback.format\_exception(\*exc\_info))
 logging.error("Unhandled exception: %s", text)

sys.excepthook = log\_except\_hook
```
  
  
  
  
  
  
The logging library takes a modular approach and offers several categories of components: loggers, handlers, filters, and formatters.

* Loggers expose the interface that application code directly uses.
* Handlers send the log records (created by loggers) to the appropriate destination.
* Filters provide a finer grained facility for determining which log records to output.
* Formatters specify the layout of log records in the final output.

Log event information is passed between loggers, handlers, filters and formatters in a [`LogRecord`](https://docs.python.org/3/library/logging.html#logging.LogRecord "logging.LogRecord") instance.

  


  


### Loggers

[`Logger`](https://docs.python.org/3/library/logging.html#logging.Logger "logging.Logger") objects have a threefold job. First, they expose several methods to application code so that applications can log messages at runtime. Second, logger objects determine which log messages to act upon based upon severity (the default filtering facility) or filter objects. Third, logger objects pass along relevant log messages to all interested log handlers.

  
### Handlers

`Handler` objects are responsible for dispatching the appropriate log messages (based on the log messages’ severity) to the handler’s specified destination. [`Logger`](https://docs.python.org/3/library/logging.html#logging.Logger "logging.Logger") objects can add zero or more handler objects to themselves with an [`addHandler()`](https://docs.python.org/3/library/logging.html#logging.Logger.addHandler "logging.Logger.addHandler") method. As an example scenario, an application may want to send all log messages to a log file, all log messages of error or higher to stdout, and all messages of critical to an email address. This scenario requires three individual handlers where each handler is responsible for sending messages of a specific severity to a specific location.  
  
  
A good convention to use when naming loggers is to use a module-level logger, in each module which uses logging, named as follows:


```
logger = logging.getLogger(\_\_name\_\_)

```
This means that logger names track the package/module hierarchy, and it’s intuitively obvious where events are logged just from the logger name.

  
### Configuring Logging

Programmers can configure logging in three ways:

1. Creating loggers, handlers, and formatters explicitly using Python code that calls the configuration methods listed above.
2. Creating a logging config file and reading it using the [`fileConfig()`](https://docs.python.org/3/library/logging.config.html#logging.config.fileConfig "logging.config.fileConfig") function.
3. Creating a dictionary of configuration information and passing it to the [`dictConfig()`](https://docs.python.org/3/library/logging.config.html#logging.config.dictConfig "logging.config.dictConfig") function.
In Python 3.2, a new means of configuring logging has been introduced, using dictionaries to hold configuration information. This provides a superset of the functionality of the config-file-based approach outlined above, and is the recommended configuration method for new applications and deployments.  
  
  
  
  
  
  
  
  
  
  
  
  
