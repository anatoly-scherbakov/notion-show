import logging
import zipfile
from glob import glob
from typing import Optional

from fire import Fire

logger = logging.getLogger(__name__)


def process(archive_path: str = None, output_path: Optional[str] = None):
    archive_path = glob(archive_path)[0]

    logger.info('Source file: %s found.', archive_path)

    archive = zipfile.ZipFile(archive_path)
    for filename in archive.namelist():
        content = archive.read(filename)

        print(content)


def main():
    return Fire({
        'process': process
    })


if __name__ == '__main__':
    main()
