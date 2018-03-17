Developers
----------

To install a development environment:

    pip install pipenv
    pipenv install --dev
    
To build the doc (docs/build/html/index.html)

    python setup.py doc
    
## Tests

To run individual tests or modules, use

```
pytest -s test_fixerio.py::TestBook_access_book::test_commodity_quantity

pytest -s test_fixerio.py::test_if_alive
```
