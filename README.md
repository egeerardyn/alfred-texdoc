# TeXdoc workflow for Alfred

![TeXdoc](./img/texdoc-logo.png)

This repository contains a Workflow for [Alfred 5](https://www.alfredapp.com/) that allows you to easily open the documentation of your [TeX distribution][mactex].

It makes use of your local LaTeX installation, so searching the documentation is really fast and does not depends on websites such as [texdoc.net][texdocnet].

## Installation

Installation is pretty easy:

 1. Download `TeXdoc.alfredworkflow` from the [latest release](https://github.com/egeerardyn/alfred-texdoc/releases/latest).
 2. Open the workflow and install it in Alfred.

Alternatively, if you want to build from the repository, run the following instructions in your working directory

```bash
make alfredworkflow # build the workflow
make install  # install into Alfred
```
## Usage

### Keyword `td`

To use the workflow, type `td` in your Alfred, followed by the name of the documentation you want to consult.

![Example `td texdoc`](img/example-td.png)

Internally, the [texdoc][texdoc] command is used to query the documentation present on your local computer.
Hence, the query in the figure above will open the documentation of [texdoc][texdoc] in your default viewer.

### Keyword `tdn`

![Example `tdn texdoc`](img/example-tdn.png)

If you type `tdn` followed by a package name into Alfred, you will download the corresponding documentation from [texdoc.net][texdocnet].

### Keyword `ctan`

![Example `td texdoc`](img/example-ctan.png)

This keyword opens the [CTAN][CTAN] page for the package you specify, i.e. `https://www.ctan.org/pkg/<name>`.

## Links

 - [Alfred forum topic](http://www.alfredforum.com/topic/8705-texdoc-workflow/)
 - [Packal page](http://www.packal.org/workflow/texdoc)

[alfred2]: https://www.alfredapp.com
[CTAN]: https://www.ctan.org
[mactex]: https://tug.org/mactex/
[texdoc]: https://www.tug.org/texdoc/
[texdocnet]: http://texdoc.net
