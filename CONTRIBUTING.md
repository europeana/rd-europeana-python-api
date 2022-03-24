# Contributing to PyEuropeana

**Hello there!** We created this document as a way to communicate with potential contributors (that's you) and to establish a common ground over which we can keep on growing and solidifying the PyEuropeana project. If you made up your mind about being a contributor, **that's great!** Reading through this document can help you immensely and cut back on the time you need to contribute to PyEuropeana. If you are not sure about being a contributor yet or if you are just taking a look, then this document can still provide you some insights about how we go about developing PyEuropeana. 

## Table of contents

- [**Different ways of contributing**](#different-ways-of-contributing)
- [**Communicating with the maintainers**](#communicating-with-the-maintainers)
  - [**Who are the maintainers?**](#who-are-the-maintainers)
  - [**How do I initiate communication?**](#how-do-i-initiate-communication)
  - [**Writing a meaningful issue**](#writing-a-meaningful-issue)
- [**Understanding our Git workflow**](#understanding-our-git-workflow)
  - [**Possible branches**](#possible-branches)
  - [**Branching rules**](#branching-rules)
  - [**General tips and guidelines**](#general-tips-and-guidelines)
  - [**Git commands cheatsheet**](#git-commands-cheatsheet)
- [**Setting up and using your development environment**](#setting-up-and-using-your-development-environment)
  - [**Prerequisites**](#prerequisites)
  - [**Download all the files related to the project**](#download-all-the-files-related-to-the-project)
  - [**Create a Python virtual environment & install PyEuropeana and its dependencies**](#create-a-python-virtual-environment--install-pyeuropeana-and-its-dependencies)
  - [**Configure local development tools**](#configure-local-development-tools)

## Different ways of contributing

So, what do we mean by contributing? One thing that probably comes to your mind is **writing Python code and adding it to the PyEuropeana codebase.** This code can be:

- the code necessary for a new feature
- code for the refactoring of the existing codebase
- a bugfix

However, **writing code is not the only way through which you can contribute to PyEuropeana.** For us, contribution also includes:

- Offering feedback on the project
- Submitting bug reports
- Submitting feature requests and enhancement proposals
- Improving API documentation
- Improving high-level documentation files (like this file and README.md)
- Adding tutorials and use cases
- Increasing test coverage

**All of these items are as valuable to us as dealing directly with the codebase by means of writing Python code** Do not hesitate to communicate with the maintainers if you have a question, an idea, or a proposal.

## Communicating with the maintainers

### Who are the maintainers?

The PyEuropeana project is developed and maintained by a core group of developers from Europeana. **This group of people are called *the maintainers.***

### How do I initiate communication?

If you have any idea about potential contributions or a request, it is a good idea to first get into contact with them or at least to look at the current issues that are being discussed. You can do that through [the **issues tab** found in the project's GitHub repository](https://github.com/europeana/rd-europeana-python-api/issues). You can use the issues tab not only to request or propose enhancements, but also to:

- Give feedback
- Ask questions
- Create a discussion topic
- Point at bugs

If you want to initiate discussion regarding any of these, click on the **new issue** button and start writing! 

### Writing a meaningful issue

With this said, here's a list of tips and best practices that can help you in getting your request, idea or message across.

1. Choose a meaningful title. The title of your issue should be brief yet informative about its scope. Refrain from composing titles like *x doesn't work* or *please help me!*. Instead, briefly mention what the issue is about.
2. Use prefixes in the title. You've seen above that we were able to roughly classify different reasons for communication. It is a good idea to prefix your title by using the following prefixes:
   1. *feedback:*...
   2. *question:*...
   3. *discussion:*...
   4. *bug:*...
   5. *enhancement:*...
3. Add more context to prefixes by using labels. GitHub allows us to tag issues with labels while you are working on composing them. We've prepared a list of eight labels that can further add context to your issue. You can access these labels in GitHub while you are preparing or editing an issue. These labels are:
   1. *feedback*
   2. *question*
   3. *discussion*
   4. *potential-bug*
   5. *confirmed-bug*
   6. *general-enhancement*
   7. *feature-enhancement*
   8. *documentation-enhancement*
4. If you are reporting a potential bug, provide context and code. Stating the exact conditions under which you encountered a problem will help you get to a solution faster. By stating the exact conditions, we mean:
   1. Briefly explaining what the bug you encountered is. Is it an error? Is it a mismatch of expectations?
   2. Listing the details of the computational environment you encountered the bug in. What version of the package? Which Python version? Which operating system?
   3. A minimally reproducible code snippet that can be used to replicate the error. Try to tidy up your code beforehand so that we can understand it better. Abstract away usecase-specific details and include only what is necessary.
5. If you are proposing or requesting an enhancement of any kind, try to explain the reasoning behind your request or proposal. Why was this enhancement needed? What problems does it solve?

## Development workflow

## Understanding our Git workflow

PyEuropeana uses the Git version control system to allow version controlling and facilitate distributed development. Our repository host of choice is GitHub and the following guidelines include some GitHub-specific sections. We try to stick to a pre-determined workflow to standardize how we use Git. The workflow that we use is a derivation of the workflow as explained [here](https://gist.github.com/digitaljhelms/4287848). Below you can find an overview of the current workflow.

### Possible branches

There are two evergreen branches that are present at any given time during project development:

1. The **stable** branch: This branch is the branch that contains the code deployed to production.
2. The **master** branch: This is the branch that most of the development efforts start with and end in.

Besides these evergreen branches, three types of temporary branches can exist:

1. The **feature-** branches: These branches are used to develop new features and implement minor/major overhauls.
2. The **bug-** branches: These branches are used to fix non-critical bugs that are discovered in the codebase.
3. The **hotfix-** branches: These branches are used to fix critical bugs that are discovered in the codebase. The main difference in between these branches and the **bug-** branches are urgency and branching rules (see below).

### Branching rules

The branches above not only differ in semantics but also in **how they are interacted with, where they stem from and where they terminate in.** The branching rules that govern how to interact with these branch types are as follows:

- **origin/stable** is the production branch. Temporary branches do not stem from or merge to **origin/stable** with the exception of **hotfix-** branches.
- **origin/master** is the development branch. It is in principle a branch of the **origin/stable** branch. **feature-** branches and **bug-** branches stem from and merge to this branch.
- Once **origin/master** reaches a certain level of maturity and robustness after bugfixes and feature development, it is merged into **origin/stable**. This merge also constitutes a minor/major version increment.
- **feature-** branches stem from and merge to **origin/master**.
- **bug-** branches stem from and merge to **origin/master**.
- **hotfix-** branches stem from and merge to **origin/stable**.
- Once a **-hotfix-** branch is merged to master, master is retroactively updated from **origin/stable** and all of the merge conflicts are resolves in favor of the **origin/stable** branch.
- It is up to the branch contributor to periodically check for and fetch changes from **origin/master** in order to keep the current branch updated.

### General tips and guidelines

There are a few more things to keep in mind while working with our Git workflow besides the interactions patterns outlined above.

- Collaborators from outside Europeana do not have branch manipulation rights in the GitHub repo. As an external contributor, you need to make a fork of the project using the GitHub interface before making any branches.
- Use the prefixes outlined above when naming your branches along with short but informative names. *fix-bug* is not a good branch name, but *bug-duplicate-search-results* is. You can alternatively use issue numbers, issue names or even ticket numbers after the prefixes.
- Always make your branch remotely available. This allows you to reference your branch on GitHub and for other people to see the current development efforts. When other people can see the current progress on a branch and contribute to it, collaboration and troubleshooting becomes easier.

### Git commands cheatsheet

Below is a very brief list of Git commands that can be used to achieve the workflow described above. For a more in-depth reference and learning tutorial, you can check [**the Git documentation**](https://git-scm.com/doc) or the official [**ProGit**](https://git-scm.com/book/en/v2) book.

- `git clone https://github.com/europeana/rd-europeana-python-api.git`: Create a local clone of the PyEuropeana repository or your personal fork of it.
- `git checkout -b [BRANCH-NAME] [TARGET-BRANCH]`: Create a branch based on [TARGET-BRANCH] and immediately switch to it. When our Git workflow is considered only the following options are possible:
  - `git checkout -b [FEATURE-[BRANCH-NAME]] master`
  - `git checkout -b [BUG-[BRANCH-NAME]] master`
  - `git checkout -b [HOTFIX-[BRANCH-NAME]] stable`
- `git push origin [BRANCH-NAME]`: Push commited changes to origin. If used right after `git checkout`, this command makes [BRANCH-NAME] remotely available.
- `git fetch --prune origin`: Fetch changes from the origin branch (most likely master). `--prune` option also updates the list of remote branches that is maintained locally. Used in conjunction with the command below.
- `git merge origin [BRANCH-NAME]`: Merge the recently fetched changes. Used in conjunction with the command above.
- `git branch -a`: To see all local and remote branches.


## Setting up and using your development environment

In order to make code contributions to PyEuropeana, you need to set up a **development environment.**: a Python environment in which all the tools that you need to write, test and debug the Python code related to PyEuropeana can be found. This can be achieved by following these steps:

1. Downloading all the files related to the project
2. Creating a Python virtual environment
3. Installing PyEuropeana and its dependencies
4. Configuring local development tools

### Prerequisites

There are three prerequisites that you need to have on installed on your machine before setting up a development environment. Please check the links to learn how to install these three prerequisites if you do not already have them.

- A working [Python (v3.7+)](https://www.python.org/downloads/) installation
- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [Poetry](https://python-poetry.org/docs/)

### Download all the files related to the project

You can download the source code of the project by:

1. Using the Git CLI
2. Using the GitHub Desktop Client
3. Downloading the repo as a .zip file through our GitHub repository

**Since we use Git and GitHub to enable distributed development the options one and two are the preffered options.** A detailed description of how to use Git is beyond the scope of this document. Instead you can refer to [this article](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository) for a specific guide on how to `git clone` a Git repository.

### Create a Python virtual environment & Install PyEuropeana and its dependencies

After obtaining a local copy of the PyEuropeana project, **you need to create a Python virtual environment so that the project and its dependencies have an isolated environment to live without conflicts.** Poetry automatically creates a new virtual environment for local installs, so this requires no extra step and can be achieved by installing the project locally.

To install the project locally:

1. Open any terminal that you can access Poetry from.
2. Navigate to the folder that contains the PyEuropeana files
3. Call `poetry shell` to spawn a Poetry shell and create a new virtual environment
4. Call `poetry install` to install PyEuropeana along with its dependencies

By default Poetry will install **both the dependencies that are needed to run the wrapper and the dependencies that are needed to develop it (dev dependencies).**

The Poetry shell that spawns after calling `poetry shell` also allows you to run any .py scripts or tests that are associated with the PyEuropeana project. For example, you can call `poetry run pytest` in the root of the project to run the tests. Alternatively, you can call `poetry run python [PATH_TO_PYTHON_SCRIPT]` to execute any individual .py file using the virtual environment we've created.

### Configure local development tools

If you peek into the `pyproject.toml` file you might notice that we are listing several Python packages as development dependencies. We use Python packages such as **flake8**, **black** and **pre-commit** to speed up our development workflow while making improvements in code quality. flake8 is a linter that checks for code styleguide compliance, black is a formatter that formats your code according to a predefined guideline and pre-commit is a tool that allows you to run these two automatically each time you make a commit.

**It is highly suggested that you as a contributor use these tools while developing locally.** We automatically check for code styleguide compliance in our CI/CD pipeline. Therefore, using these tools while developing will help you contribute to the PyEuropeana project in a better way.

Configuration files that customize our local development tools are already present in the repo you've downloaded. The only thing you need to do in order to configure your local development tools is to do the following:

- If you haven't already: open any terminal you can run Poetry from, navigate to the root of the PyEuropeana project, run `poetry shell`
- Run `poetry run pre-commit install`

## Style guide

WIP

## Building the PyEuropeana API docs, reference docs and tutorials

WIP

## Writing tests

WIP

## Extra: Releasing a version

WIP

## Extra: our CI/CD pipeline

WIP

