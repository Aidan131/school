
class LogRecord:
    args: _ArgsType
    asctime: str
    created: int
    exc_info: Optional[_SysExcInfoType]
    exc_text: Optional[str]
    filename: str
    funcName: str
    levelname: str
    levelno: int
    lineno: int
    module: str
    msecs: int
    message: str
    msg: str
    name: str
    pathname: str
    process: int
    processName: str
    relativeCreated: int
    if sys.version_info >= (3,):
        stack_info: Optional[str]
    thread: int
    threadName: str
    if sys.version_info >= (3,):
        def __init__(self, name: str, level: int, pathname: str, lineno: int,
                     msg: Any, args: _ArgsType,
                     exc_info: Optional[_SysExcInfoType],
                     func: Optional[str] = ...,
                     sinfo: Optional[str] = ...) -> None: ...
    else:
        def __init__(self,
                     name: str, level: int, pathname: str, lineno: int,
                     msg: Any, args: _ArgsType,
                     exc_info: Optional[_SysExcInfoType],
                     func: Optional[str] = ...) -> None: ...
    def getMessage(self) -> str: ...


class LoggerAdapter:
    logger: Logger
    extra: Mapping[str, Any]
    def __init__(self, logger: Logger, extra: Mapping[str, Any]) -> None: ...
    def process(self, msg: Any, kwargs: MutableMapping[str, Any]) -> Tuple[Any, MutableMapping[str, Any]]: ...
    if sys.version_info >= (3,):
        def debug(self, msg: Any, *args: Any, exc_info: _ExcInfoType = ...,
                  stack_info: bool = ..., extra: Optional[Dict[str, Any]] = ...,
                  **kwargs: Any) -> None: ...
        def info(self, msg: Any, *args: Any, exc_info: _ExcInfoType = ...,
                 stack_info: bool = ..., extra: Optional[Dict[str, Any]] = ...,
                 **kwargs: Any) -> None: ...
        def warning(self, msg: Any, *args: Any, exc_info: _ExcInfoType = ...,
                    stack_info: bool = ..., extra: Optional[Dict[str, Any]] = ...,
                    **kwargs: Any) -> None: ...
        def warn(self, msg: Any, *args: Any, exc_info: _ExcInfoType = ...,
                 stack_info: bool = ..., extra: Optional[Dict[str, Any]] = ...,
                 **kwargs: Any) -> None: ...
        def error(self, msg: Any, *args: Any, exc_info: _ExcInfoType = ...,
                  stack_info: bool = ..., extra: Optional[Dict[str, Any]] = ...,
                  **kwargs: Any) -> None: ...
        def exception(self, msg: Any, *args: Any, exc_info: _ExcInfoType = ...,
                      stack_info: bool = ..., extra: Optional[Dict[str, Any]] = ...,
                      **kwargs: Any) -> None: ...
        def critical(self, msg: Any, *args: Any, exc_info: _ExcInfoType = ...,
                     stack_info: bool = ..., extra: Optional[Dict[str, Any]] = ...,
                     **kwargs: Any) -> None: ...
        def log(self, level: int, msg: Any, *args: Any, exc_info: _ExcInfoType = ...,
                stack_info: bool = ..., extra: Optional[Dict[str, Any]] = ...,
                **kwargs: Any) -> None: ...
    else:
        def debug(self,
                  msg: Any, *args: Any, exc_info: _ExcInfoType = ...,
                  extra: Optional[Dict[str, Any]] = ..., **kwargs: Any) -> None: ...
        def info(self,
                 msg: Any, *args: Any, exc_info: _ExcInfoType = ...,
                 extra: Optional[Dict[str, Any]] = ..., **kwargs: Any) -> None: ...
        def warning(self,
                    msg: Any, *args: Any, exc_info: _ExcInfoType = ...,
                    extra: Optional[Dict[str, Any]] = ..., **kwargs: Any) -> None: ...
        def error(self,
                  msg: Any, *args: Any, exc_info: _ExcInfoType = ...,
                  extra: Optional[Dict[str, Any]] = ..., **kwargs: Any) -> None: ...
        def exception(self,
                      msg: Any, *args: Any, exc_info: _ExcInfoType = ...,
                      extra: Optional[Dict[str, Any]] = ..., **kwargs: Any) -> None: ...
        def critical(self,
                     msg: Any, *args: Any, exc_info: _ExcInfoType = ...,
                     extra: Optional[Dict[str, Any]] = ..., **kwargs: Any) -> None: ...
        def log(self,
                level: int, msg: Any, *args: Any, exc_info: _ExcInfoType = ...,
                extra: Optional[Dict[str, Any]] = ..., **kwargs: Any) -> None: ...
    def isEnabledFor(self, lvl: int) -> bool: ...
    if sys.version_info >= (3,):
        def getEffectiveLevel(self) -> int: ...
        def setLevel(self, lvl: Union[int, str]) -> None: ...
        def hasHandlers(self) -> bool: ...


if sys.version_info >= (3,):
    def getLogger(name: Optional[str] = ...) -> Logger: ...
else:
    @overload
    def getLogger() -> Logger: ...
    @overload
    def getLogger(name: Union[Text, str]) -> Logger: ...
def getLoggerClass() -> type: ...
if sys.version_info >= (3,):
    def getLogRecordFactory() -> Callable[..., LogRecord]: ...

if sys.version_info >= (3,):
    def debug(msg: Any, *args: Any, exc_info: _ExcInfoType = ...,
              stack_info: bool = ..., extra: Optional[Dict[str, Any]] = ...,
              **kwargs: Any) -> None: ...
    def info(msg: Any, *args: Any, exc_info: _ExcInfoType = ...,
             stack_info: bool = ..., extra: Optional[Dict[str, Any]] = ...,
             **kwargs: Any) -> None: ...
    def warning(msg: Any, *args: Any, exc_info: _ExcInfoType = ...,
                stack_info: bool = ..., extra: Optional[Dict[str, Any]] = ...,
                **kwargs: Any) -> None: ...
    def warn(msg: Any, *args: Any, exc_info: _ExcInfoType = ...,
             stack_info: bool = ..., extra: Optional[Dict[str, Any]] = ...,
             **kwargs: Any) -> None: ...
    def error(msg: Any, *args: Any, exc_info: _ExcInfoType = ...,
              stack_info: bool = ..., extra: Optional[Dict[str, Any]] = ...,
              **kwargs: Any) -> None: ...
    def critical(msg: Any, *args: Any, exc_info: _ExcInfoType = ...,
                 stack_info: bool = ..., extra: Optional[Dict[str, Any]] = ...,
                 **kwargs: Any) -> None: ...
    def exception(msg: Any, *args: Any, exc_info: _ExcInfoType = ...,
                  stack_info: bool = ..., extra: Optional[Dict[str, Any]] = ...,
                  **kwargs: Any) -> None: ...
    def log(level: int, msg: Any, *args: Any, exc_info: _ExcInfoType = ...,
            stack_info: bool = ..., extra: Optional[Dict[str, Any]] = ...,
            **kwargs: Any) -> None: ...
else:
    def debug(msg: Any, *args: Any, exc_info: _ExcInfoType = ...,
              extra: Optional[Dict[str, Any]] = ..., **kwargs: Any) -> None: ...
    def info(msg: Any, *args: Any, exc_info: _ExcInfoType = ...,
             extra: Optional[Dict[str, Any]] = ..., **kwargs: Any) -> None: ...
    def warning(msg: Any, *args: Any, exc_info: _ExcInfoType = ...,
                extra: Optional[Dict[str, Any]] = ..., **kwargs: Any) -> None: ...
    warn = warning
    def error(msg: Any, *args: Any, exc_info: _ExcInfoType = ...,
              extra: Optional[Dict[str, Any]] = ..., **kwargs: Any) -> None: ...
    def critical(msg: Any, *args: Any, exc_info: _ExcInfoType = ...,
                 extra: Optional[Dict[str, Any]] = ..., **kwargs: Any) -> None: ...
    def exception(msg: Any, *args: Any, exc_info: _ExcInfoType = ...,
                  extra: Optional[Dict[str, Any]] = ..., **kwargs: Any) -> None: ...
    def log(level: int, msg: Any, *args: Any, exc_info: _ExcInfoType = ...,
            extra: Optional[Dict[str, Any]] = ..., **kwargs: Any) -> None: ...
fatal = critical

def disable(lvl: int) -> None: ...
def addLevelName(lvl: int, levelName: str) -> None: ...
def getLevelName(lvl: Union[int, str]) -> Any: ...

def makeLogRecord(attrdict: Mapping[str, Any]) -> LogRecord: ...

if sys.version_info >= (3,):
    def basicConfig(*, filename: Optional[_Path] = ..., filemode: str = ...,
                    format: str = ..., datefmt: Optional[str] = ..., style: str = ...,
                    level: Optional[_Level] = ..., stream: Optional[IO[str]] = ...,
                    handlers: Optional[Iterable[Handler]] = ...) -> None: ...
else:
    @overload
    def basicConfig() -> None: ...
    @overload
    def basicConfig(*, filename: Optional[str] = ..., filemode: str = ...,
                    format: str = ..., datefmt: Optional[str] = ...,
                    level: Optional[_Level] = ..., stream: IO[str] = ...) -> None: ...
def shutdown() -> None: ...

def setLoggerClass(klass: type) -> None: ...

def captureWarnings(capture: bool) -> None: ...

if sys.version_info >= (3,):
    def setLogRecordFactory(factory: Callable[..., LogRecord]) -> None: ...


if sys.version_info >= (3,):
    lastResort: Optional[StreamHandler]


class StreamHandler(Handler):
    stream: IO[str]  # undocumented
    if sys.version_info >= (3, 2):
        terminator: str
    def __init__(self, stream: Optional[IO[str]] = ...) -> None: ...
    if sys.version_info >= (3, 7):
        def setStream(self, stream: IO[str]) -> Optional[IO[str]]: ...


class FileHandler(StreamHandler):
    baseFilename: str  # undocumented
    mode: str  # undocumented
    encoding: Optional[str]  # undocumented
    delay: bool  # undocumented
    def __init__(self, filename: _Path, mode: str = ...,
                 encoding: Optional[str] = ..., delay: bool = ...) -> None: ...


class NullHandler(Handler): ...


class PlaceHolder:
    def __init__(self, alogger: Logger) -> None: ...
    def append(self, alogger: Logger) -> None: ...


# Below aren't in module docs but still visible

class RootLogger(Logger): ...

root: RootLogger


if sys.version_info >= (3,):
    class PercentStyle(object):
        default_format: str
        asctime_format: str
        asctime_search: str
        _fmt: str

        def __init__(self, fmt: str) -> None: ...
        def usesTime(self) -> bool: ...
        def format(self, record: Any) -> str: ...

    class StrFormatStyle(PercentStyle):
        ...

    class StringTemplateStyle(PercentStyle):
        _tpl: Template

    _STYLES: Dict[str, Tuple[PercentStyle, str]]


BASIC_FORMAT: str
