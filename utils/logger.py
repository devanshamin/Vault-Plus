import logging
from pathlib import Path

from rich.logging import RichHandler

path = Path("logs")
if not path.exists():
    path.mkdir()

logger = logging.getLogger(__name__)
 
file_handler = logging.FileHandler(Path(path, "debug.log"))

logger.setLevel(logging.DEBUG)
file_handler.setLevel(logging.DEBUG)

fmt_file = '%(levelname)s %(asctime)s [%(filename)s:%(funcName)s:%(lineno)d] %(message)s'
file_formatter = logging.Formatter(fmt_file)
file_handler.setFormatter(file_formatter)

logger.addHandler(file_handler)