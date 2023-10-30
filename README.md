# FSEconomy Python Bindings

This package provides Python bindings for various [FSEconomy](https://www.fseconomy.net) APIs.

[![Documentation Status](https://readthedocs.org/projects/fseconomy-python/badge/?version=latest)](https://fseconomy-python.readthedocs.io/en/latest/?badge=latest)

**Important Links**

* Documentation: https://fseconomy-python.readthedocs.io/
* GitHub: https://github.com/fseconomy/fseconomy-python
* Bug Tracker: https://github.com/fseconomy/fseconomy-python/issues

## Usage

### Initialization

In order to use any of FSEconomy's APIs, you will need to initialize 
the corresponding API keys:

```python
import fseconomy

fseconomy.set_access_key('0123456789ABCDEF')
fseconomy.set_service_key('0123456789ABCDEF')
fseconomy.set_user_key('0123456789ABCDEF')
```

Please refer to the corresponding section of the
[FSEconomy Operations Guide](https://sites.google.com/site/fseoperationsguide/data-feeds)
for an explanation of the different keys and their purpose.

### FSEconomy Data Feeds

### FSEconomy REST API

### FSEconomy Auth API
