### AUTHOR <small>Marcelo</small>
<h1>0x12-javascript-warm_up - <small>JavaScript Tutorial</small></h1>
<br>

# 🤨 var
```Javascript
    function varExample() {
        for (var n = 1; n < 3; n++) {
            console.log(n);
        }
        console.log(n);
        // even though var n was declared in a the block for loop it can still be accessible outside of the for loop block.
    }
```

<pre>
    <b>var keyword</b> &#9660;
    
        - is function scoped, meaning it can be accessed from anywhere in the function.
        - This can be a problem - beacuse var is not block scoped it can collide with later assigment or defenition of the same varibale.
        - it is easy to overwrite varibales accidently.
        - with var you can use a varibale before declaring it.
</pre>

<br>

# 🤓 let
```Javascript
    function letExample() {
        for (let n = 1; n < 3; n++) {
            console.log(n);
        }
        console.log(n);
        // becuase we are using let the variable n only exist inside the for loop.
        // running console.log(n) outside the for loop will cause an error of varible is not defined.
    }
```
<pre>
    <b>let keyword</b> &#9660;

        - is block scoped, meaning it can only be accessed in the block it was declared.
        - with let you can not use a varibale before declaring it.
</pre>

<br>

# 🤩 const
```JavaScript
    const myVar = "I can't change";
    myVar = 10; // causes an error when trying to redifine/redeclare.
```
<pre>
    <b>const keyword</b> &#9660;
    
        - const is similar to let but the only difference is once declared it you can't redeclare const variables.
        - const has an exception and that is its true you cant't redeclare a varible, but if const is
        a an object you can still change it property, with that in mind it's not possible to redeclare a const object but its properties.
</pre>

<br>

# Methods/Functions Used &#9660;
<pre>
    <h4>Standard LIB &#9660;</h4>
    <b>console.log()</b>  - print to console, if using node then prints to standard output.
    <b>process.argv</b>   - for getting arguments.
    <b>parseInt()</b>     - converts to interger.
    <b>repeat()</b>       - duplicates or repeat string X number of times.
    <b>sort()</b>         - array method to sort.
    <b>push()</b>         - array method to add to end of array.
    <b>module.export</b> - export module to can importable, from any file.

    <h4>Created by Author &#9660;</h4>
    <b>factorial()</b>   - finds the factorial of a number.
    <b>SecondLargest()</b> - finds the second largerst number in a given array.
</pre>

<br>

## Requirements
<a href="https://nodejs.org/en/">Install NodeJs</a>
```bash
curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt-get install -y nodejs
```
<a href="https://www.npmjs.com/package/semistandard">Install semistandard</a>
```bash
sudo npm install semistandard --global
```

## Helpful Links
<a href="https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics">JavaScript Basics</a>

<a href="https://www.youtube.com/watch?v=sjyJBL5fkp8&ab_channel=FunFunFunction">Watch - var, let and const</a>

<a href="https://github.com/mbeaudru/modern-js-cheatsheet">Modern JS</a>
