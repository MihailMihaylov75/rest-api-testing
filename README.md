# Introduction

Git hook scripts are useful for identifying simple issues before submission to code review

**Note:** this is an example repository containing the following pre-commit hooks:
* pylint (configured)
* unit tests (just one used for example)
* check-yaml
* end-of-file-fixer
* trailing-whitespace
* black
* flake8 (not configured)

The hooks are executed on the delta between the repository and master.

# Installation

```bash
pip install pre-commit
```


# Quick start

### Add a pre-commit configuration


* create a file named .pre-commit-config.yaml
* you can generate a very basic configuration using: ```pre-commit sample-config ```


### Install the git hook scripts
* run ```pre-commit install``` to set up the git hook scripts
* now ```pre-commit``` will run automatically on git ```commit```!

## Run against all the files

*
    it's usually a good idea to run the hooks against all the files when adding new hooks (usually pre-commit will only run on the changed files during git hooks)

```bash
pre-commit run --all-files
```

To run individual hooks use:
```bash
pre-commit run <hook_id>
```

## References

[pre-commit](https://pre-commit.com/)
