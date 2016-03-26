# Alfred 2 TeXdoc workflow

This repository contains a Workflow for [Alfred 2][alfred2] that allows you to easily open the documentation of your [TeX distribution][mactex].

It makes use of your local LaTeX installation, so searching the documentation is really fast and does not depends on websites such as [texdoc.net](texdocnet).

## Installation

Installation is pretty easy:

 1. Download [TeXdoc.alfredworkflow](TeXdoc.alfredworkflow) from this repository.
 2. Open the workflow and install it in Alfred.

## Usage

To use the workflow, type `td` in your Alfred, followed by the name of the documentation you want to consult.

![Example `td texdoc`](img/example.png)

Internally, the [texdoc][texdoc] command is used to query the documentation present on your local computer.
Hence, the query in the figure above will open the documentation of [texdoc][texdoc] in your default viewer.

## Links

 - [Alfred forum topic](http://www.alfredforum.com/topic/8705-texdoc-workflow/)
 - [Packal page](http://www.packal.org/workflow/texdoc)

[alfred2]: https://www.alfredapp.com
[mactex]: https://tug.org/mactex/
[texdoc]: https://www.tug.org/texdoc/
[texdocnet]: http://texdoc.net
