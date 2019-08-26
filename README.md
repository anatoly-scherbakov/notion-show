# notion-show

A very stupid way to convert a notion.so document into a PDF file usable as a presentation.

The presentation/slideshow mode has been apparently discussed at [NotionHQ Twitter](https://twitter.com/notionhq/status/1014214831501598720) but no business resulted yet.

This code is unpacking the HTML file, inserting a little CSS snippet into it and printing the resulting HTML into PDF using [chromehtml2pdf](https://github.com/dataverity/chromehtml2pdf).

## Install requirements

```shell script
sudo pip install virtualenvwrapper
sudo apt-get install npm

npm install chromehtml2pdf

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

# To Do

* Create a sample presentation to show how this looks
* Fix known CSS issues
* Integrate with Notion API
* Make an HTML presentation with fancy effects instead of wooden PDF
* Boast about this to Notion at their twitter
