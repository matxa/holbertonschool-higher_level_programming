### AUTHOR <small>Marcelo</small>
<h1>0x12-javascript-warm_up - <small>JavaScript Tutorial</small></h1>


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
        - This can be a problem - beacuse var is not blocked scoped it can collide with later assigment or defenition of the same varibale.
        - it is easy to overight varibales accidently.
        - with var you can use a varibale before declaring it.
</pre>

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

# 🤩 const
```JavaScript
    const myVar = "I can't change";
    myVar = 10; // causes an error when trying to redifine/redeclare.
```
<pre>
    <b>const keyword</b> &#9660;
    
        - const is similar to let but the only difference is once you can't redeclare const variables.
        - const has an exception and that is its true you cant't redeclare a varible, but if const is
        a an object you can still change it property, with that in mind it's not possible to redeclare a const object.
</pre>
