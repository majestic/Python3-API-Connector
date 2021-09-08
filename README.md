Python3-API-Connector (for Python 3.7.4)
====================

Majestic® surveys and maps the Internet and has created the largest commercial Link Intelligence database in the world. The Majestic® search engine is mainly used to instantly provide Flow Metric® scores which evaluate the quality of any page on the Internet on a scale from 0 to 100. The connector libraries are supplied to assist in using the Majestic® API and are available in a number of programming languages.

This is the Python 3 connector.  For Python 2, go [here](https://github.com/majestic/Python-API-Connector).
 
Setup
---------------
Clone this repository in a directory.

You can import the connector from a subdirectory of your project or set it as an environment variable, making it available to all projects.

To import it without setting the environment variable, place the API connector within the project (such as in `C:\project\lib\Python3-API-Connector`) and import it using a relative path (such as `from lib.majesticseo_external_rpc.APIService import APIService`)

Setting the environment variable allows Python to find the library and import it into any project. To set the `PYTHONPATH` environment variable:

On Windows you can use the `setx` command:
```
setx PYTHONPATH C:\path\to\Python3
```
On linux use the `export` command instead: 
```
export PYTHONPATH=/usr/path/to/Python3-API-Connector
```
You can then import the connector using:
```
from majesticseo_external_rpc.APIService import APIService
```


Examples
-------------
There are a few examples of using the API-Connector in the following scripts:

* GetIndexItemInfo.py 
	* The GetIndexItemInfo command provides data on the number of backlinks to any web page or site, linking domains and the main topics for that page or website
* GetBackLinkData.py 
	* GetBacklinkData will return rows of data with information about all the pages linking to a given URL or domain
* OpenAppGetIndexItemInfo.py
	* This example shows how to use the API connector for a Majestic OpenApp

The following code is from GetIndexItemInfo.py and shows how the API-Connector can be used:

```
api_service = APIService(app_api_key, endpoint)
response = api_service.execute_command('GetIndexItemInfo', parameters)
```

Further notes
------------------
The Python Connector has been developed using Python 3.7.4.
To run the examples
* Have python 3+ installed
* Run the script in terminal using one of the following commands (this will depend on your particular Python installation):
	* `python somefile.py`
	* `python3 somefile.py`
	* `py somefile.py`

For further information see the API documentation @ https://developer-support.majestic.com/


