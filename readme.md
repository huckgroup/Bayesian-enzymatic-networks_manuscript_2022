# A Bayesian approach to extracting kinetic information from artificial enzymatic networks

This repository contains all data, notebooks, software requirements, and supporting information for the publication 'A Bayesian approach to extracting kinetic information from artificial enzymatic networks'.

After installing the required python packages from the `environment.yaml` file (either directly or via Conda), the notebooks used for data analysis and creation of the various figures found in the final manuscript can be run locally.

## Compiling the manuscript

The manuscript is compiled from a text-based markdown file into a docx file. 
This requires a pandoc installation (provided in the conda-environment) and manual installation of the pandoc-crossref package and lua-filters.

### pandoc-crossref

Pandoc-crossref can be installed by downloading the suitable binary from Github and installing it in the local path.
```bash
wget https://github.com/lierdakil/pandoc-crossref/releases/download/v0.3.12.0d/pandoc-crossref-Linux.tar.xz
tar -xf pandoc-crossref-Linux.tar.xz 
sudo mv pandoc-crossref /usr/local/bin/
sudo chmod a+x /usr/local/bin/pandoc-crossref
sudo mkdir -p /usr/local/man/man1
sudo mv pandoc-crossref.1  /usr/local/man/man1
```
### pandoc lua-filters

The Lua-filters can be downloaded from Github, and take as installation parameter the absolute path to the pandoc data directory
```bash
pandoc -v
```

```bash
export PANDOC_DIR={path to pandoc user data directory}
```

```bash
RELEASE_URL=https://github.com/pandoc/lua-filters/releases/latest
curl -LSs $RELEASE_URL/download/lua-filters.tar.gz |     tar --strip-components=1 --one-top-level=$PANDOC_DIR -zvxf -
```

### Creating the SI pdf

The final Supporting Information document can be created by simply running the available `makefile` command:
```bash
make si
```
The document will then appear in the `out` folder.