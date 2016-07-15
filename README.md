# Form Hero

Create forms easily and integrate with a variety of services

## Install

> Note: the following code snippets are here for illustration. If you use them, please make sure you understand what you are doing exactly. Read the source code for each command to gain understanding of what is happening.

Run `./.danger`. Follow any instructions until success. If you run into errors, let us know.

This will create all required containers and set up git hooks to allow you to commit your code only if it complies to all rules mentioned in the gitbook.

## Development

All commands should be ran from within a container with the exception of `.serve`; you can access the einvormentby using the `./.shell` helper script.

Then you will need to load basic data:

```
./manage.py importtestdata
```

### Useful commands inside the container

- `./.test <path.to.optional.Class.or_test_method`: Run the test suite
- `./.run_flake8`: Check code conforms to python style-guide
