Hello World Python

# Things to keep in mind while reading this README.md

- #!/usr/bin/python3 -> This sh-bang allows me to run my python file as follows ./file.py
after giving the user/file executable permission using the command `chmod u+x file.py`

- There are multiple ways to print in python as you can see in task #0, #1

- to escape a character use `\` follow by the character.. `print("\"Hey\"")`

- Python print's function adds a new line by itself, to stop it from doing so just use (`end=''`).. `print("Hello, World", end='')`


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

- ***The Python code will be saved in the environment variable `$PYCODE`***

`PYCODE='print("Holberton School: {}".format(88+10))'`

  - To run an in-line bash/python command you need to use the `<<<`

    1. `<<<` - stands for "Here String" -> can be considered as a stripped-down form of a here document. It consists of nothing more than COMMAND <<<$WORD, where $WORD is expanded and fed to the stdin of COMMAND.[source-link](https://linux.die.net/abs-guide/x15683.html)

    2. Running the file

      - `./1-run_inline` is the same as -> `python3 <<< PYCODE='print("Holberton School: {}".format(88+10))'`

## 2. Hello, print

### Printing in Python (    print()   ) - Write a Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.

1. Here we have to read the task carefully. It's asking to print exactly what it shows, include the double quote in the beginning ("Programming... ). There are different was to do achieve this end result.

  - The 2 most common ways are:

  1. using double quotes inside of single quotes. `print('"Programming... ')`
  2. using the escape character. `print("\"Programming... ")`

## 3. Print integer , 4. Print float, 5. Print string, 6. Play with strings

### Print using format [Helpful-link](https://pyformat.info/)

## 7. Copy - Cut - Paste, 8. Create a new sentence

### String slicing

```
a[start:stop]  # items start through stop-1
a[start:]      # items start through the rest of the array
a[:stop]       # items from the beginning through stop-1
a[:]           # a copy of the whole array

There is also the step value, which can be used with any of the above:

a[start:stop:step]
```
## 9. Easter Egg

### [Helpful link](https://www.python.org/dev/peps/pep-0020/)

## 10. Linked list cycle

## 11. Hello, write

### Writing to stderr in python3

- Step by Step

1- import the module `sys`
2- to use it just call the module `sys`
3- next state where/what you want to write to my case is `stderr`
4- then use the write func to write the text... `write(text)`

```
sys.stderr.write(text)
```
[Helpful-link](https://docs.python.org/3/library/sys.html)
