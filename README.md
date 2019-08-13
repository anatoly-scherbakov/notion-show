# notion-show

A very stupid way to convert a notion.so document into a PDF file usable as a presentation.

## Install requirements

```shell script
sudo pip install virtualenvwrapper

npm install -g chromehtml2pdf

mkvirtualenv -p `which python3.7` notion-show
pip install -r requirements.txt
```

## Export the document

* Open the document you're interested in at [notion.so](https://notion.so);
* Use top-right menu to click Export option;
* Export as HTML;
* Download the resulting ZIP file.

## Perform the conversion

```shell script
python notion_show.py Export_123.zip my-show.pdf
```

# References

* [chromehtml2pdf](https://github.com/dataverity/chromehtml2pdf)
