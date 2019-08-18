import logging
import os
import subprocess
import tempfile
import zipfile
from glob import glob
from typing import Optional

from bs4 import BeautifulSoup
from fire import Fire

logger = logging.getLogger(__name__)


def to_pdf(input_filename: str, output_filename: str):
    input_filename = 'file://' + os.path.join(
        os.path.dirname(__file__),
        input_filename
    )

    subprocess.run([
        'chromehtml2pdf',
        '--landscape', '1',
        # '--format A4',
        f'--out={output_filename}',
        input_filename,
    ])


def convert(content: str):
    """Perform actual code conversion to add presentation capabilities."""
    soup = BeautifulSoup(content)

    tag = soup.new_tag('style')
    with open('presentation.css', 'r') as f:
        tag.string = f.read()

    soup.style.insert_before(tag)

    return str(soup)


def process(archive_path: str = None, output_path: Optional[str] = None):
    archive_path = glob(archive_path)[0]

    logger.info('Source file: %s found.', archive_path)

    with tempfile.TemporaryDirectory() as temporary_directory:
        with zipfile.ZipFile(archive_path) as archive:
            archive.extractall(temporary_directory)

        filename = [
            filename
            for filename in os.listdir(temporary_directory)
            if filename.endswith('.html')
        ][0]

        with open(os.path.join(
            temporary_directory,
            filename
        ), 'r') as source_html_file:
            content = source_html_file.read()

        content = convert(content)

        output_path = os.path.join(
            temporary_directory,
            f'output.{filename}'
        )

        with open(output_path, 'w+') as output_html_file:
            output_html_file.write(content)

        to_pdf(output_path, 'show.pdf')


def main():
    return Fire({
        'process': process
    })


if __name__ == '__main__':
    main()
