# Python Template

A python template that we can use to create other Python template. It provides the pertinent setup and boilerplate code needed in a new python project.

## Setup

### Set up the Project

1. Set up tools, packages, and virtual environment 

   ```shell
   make install
   ```

1. The Makefile doesn't activate the environment, just install the it. So activate the virtualenv if you want.

   ```shell
   source .venv/bin/activate 
   ```

### Set up IDE

#### PyCharm

If you open this project in PyCharm, perform the following setup on the IDE to optimize the user experience.

1. Go to **Settings** and tweak the following
   * **Project Structure**. Mark the directories `src` and `tests` as `Sources` and `Tests` respectively. This drastically improves code completion by parsing the project code for the code completion.
   * **Python Interpreter**. Make sure we set the interpreter to the one on the project virtual environment. Remove the current interpreter if needed. Select **local interpreter... > Virtualenv > Existing**.

### Running Tests
   
1. A better way to run tests is to call pytest directly from the command line by running `python -m pytest tests`. But pytest returns `ModuleNotFoundError: No module named 'finance'` because pytest don't know where to load the module. To correct this, add the following line to `pyproject.toml`.

   ```toml
   [tool.pytest.ini_options]
   pythonpath = [
     'src'
   ]
   ```

   Now running the following command will run the tests correctly.

   ```shell
   $ make test
   $ # Alternatively, run pytest directly.
   $ python -m pytest tests
   ```
