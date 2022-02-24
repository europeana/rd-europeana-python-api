# Build the docs

1. Install pyeuropeana according to the [installation guidelines](../README.md#installation)
2. Install sphinx with  `pip install -U sphinx`, `pip install sphinx-gallery`, `pip install nbsphinx`. If you are using conda you might need to use `conda install sphinx` 
3. Run `make html` from this directory
4. Open `build/html/index.html` with your browser or start a web server with `python -m http.server 8000` and access it at `http://localhost:8000/build/html/`
5. If you make changes to `pyeuropeana` you can re-compile the documentation with `cd ../ && pip install . && cd docs && make html`
