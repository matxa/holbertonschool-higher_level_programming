Hello World Python

## 0. Run Python file

### A Shell script that runs a Python script.

- python3 $PYFILE

  - python3 -> Is the code needed to run(exec) a python file.

    - $PYFILE -> Is a variable that holds the file name

  1. So to run this script we need to first set the `var PYFILE` equal( = ) to a file name
    `PYFILE=main.py`

  2. Now we can run the bash file 0-run (./0-run) this will run the main.py file.
    - `./0-run is` the same as -> `python3 main.py`

## 1. Run inline

### A Shell script that runs a Python script.

- *** The Python code will be saved in the environment variable `$PYCODE` ***
  `PYCODE='print("Holberton School: {}".format(88+10))'`

  - To run an in-line bash/python command you need to use the `<<<`

    1. `<<<` - stands for "Here String" -> can be considered as a stripped-down form of a here document. It consists of nothing more than COMMAND <<<$WORD, where $WORD is expanded and fed to the stdin of COMMAND.[source-link](https://linux.die.net/abs-guide/x15683.html)

    2. Running the file

      - `./1-run_inline` is the same as -> `python3 <<< PYCODE='print("Holberton School: {}".format(88+10))'`
