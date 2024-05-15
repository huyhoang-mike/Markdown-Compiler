# MARIMO NOTEBOOK - ADVANTAGES
Marimo is an open-source reactive notebook for Python that’s reproducible, git-friendly (stored as Python files), executable as a script, and deployable as an app.

## Reproducible Experiments
Run a cell and marimo reacts by automatically running the cells that reference its variables, eliminating the error-prone task of manually re-running cells. 
Delete a cell and marimo scrubs its variables from program memory, eliminating hidden state.

![marimo](https://github.com/huyhoang-mike/Markdown-Compiler/assets/109945762/af307e4b-31a8-4867-95d1-30b400defc1a)

Hidden state — where a variable no longer exists in your code, but still exists in program memory. You’ve almost certainly received a notebook from a colleague that 
utterly failed to reproduce — when you ran it, you saw outputs different from the ones serialized in the notebook (or maybe it didn’t run at all!). 

![jupyter](https://github.com/huyhoang-mike/Markdown-Compiler/assets/109945762/c1e7743c-2566-487b-9f2e-6bf3c5db2d5f)

## Execute as a Script or an App
You can run marimo notebooks as scripts at the command line, just like any other Python script. For example,
```
python my_marimo_notebook.py
```
The marimo CLI lets you run any notebook as an app: marimo run lays out the notebook as an app and starts a web server that hosts the resulting app.

By default, apps are laid out as a concetentation of their outputs, with code hidden. You can customize the layout using marimo’s built-in drag-and-drop 
grid editor; you can also choose to include code in the app view.
```
Usage: marimo run [OPTIONS] NAME

  Run a notebook as an app in read-only mode.

  If NAME is a url, the notebook will be downloaded to a temporary file.

  Example:

      * marimo run notebook.py

Options:
  -p, --port INTEGER  Port to attach to.
  --host TEXT         Host to attach to.
  --headless          Don't launch a browser.
  --include-code      Include notebook code in the app.
  --base-url TEXT     Base URL for the server. Should start with a /.
  --help              Show this message and exit.
```
![vi](https://github.com/huyhoang-mike/Markdown-Compiler/assets/109945762/3cc70f94-a657-4ef3-9633-3ed05f4703ce)


## Version Control with Git
You may have tried, and failed, to version your notebooks with git — you changed just one line of code, but the git diff showed an enormous change in 
the notebook’s JSON representation. You likely have directories cluttered with dozens of UntitledXX.ipynb files — some of which 
are mostly copies of other notebooks, since it wasn’t really possible to reuse your notebook code as you would regular Python.

Marimo save notebooks in .py format so that you can use Git easily. 

## Built-in VS Code Extension
Use side by side in VS Code or open in seperate browser like Jupyter.
![image](https://github.com/huyhoang-mike/Markdown-Compiler/assets/109945762/ad4ff4da-d9bf-4bc4-b1d8-cc640c552699)

## Jupyter notebook conversion
Automatically translate Jupyter notebooks to marimo notebooks with `marimo convert`:
```
marimo convert your_notebook.ipynb > your_notebook.py
```
