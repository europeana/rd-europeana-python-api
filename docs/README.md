# Read the docs

Coming ...

# Build the docs

1. Install pyeuropeana according to the [installation guidelines](../README.md#installation)
2. Install sphinx with  `pip install -U sphinx` the the Read the Docs theme with `pip install sphinx_rtd_theme`
3. Run `make html` from this directory
4. Open `build/html/index.html` with your browser or start a web server with `python -m http.server 8000` and access it at `http://localhost:8000/build/html/`
5. Reinstall the library and compile documentation when you make changes to the pyeuropeana package with `cd ../ && pip install . && cd docs && make html`
