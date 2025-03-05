# Purpose
Implement the interpreted language found at the following tutorial:
1. https://accu.org/journals/overload/26/145/balaam_2510/
2. https://accu.org/journals/overload/26/146/balaam_2532/
3. https://accu.org/journals/overload/26/147/balaam_2565/

Class/function names may be changed 
Code was modified to reflect the next philosophy: the input code is correct, no errors, can be expected, all string literals are closed
 all function calls are followed by closed paranthesis, braces are closed, etc. 
From "asgn": ('nr', 10.0)
From comp: ('nr', ('nr', 101.0, 'nr', 10.0)) 
<!--
This part of the output is wrong, it should become another value
But, no the two numbers aren't added to make '111', the two tuples get concatenated
It's likely that there is an implementation mistake somewhere

-->
From "asgn": ('nr', ('nr', 101.0, 'nr', 10.0))
From "asgn": ('sr', 'This is the value:')
Does this execute?
This is the printer: ('id', 'print') [('sr', 'This is the value:'), ('nr', ('nr', 101.0, 'nr', 10.0))]
No, I am the printer: None
From "asgn": ('nr', 10.0)
From comp: ('nr', 111.0)
From "asgn": ('nr', 111.0)
From "asgn": ('sr', 'This is the value:')
Does this execute?
This is the printer: ('id', 'print') [('sr', 'This is the value:'), ('nr', 111.0)]
No, I am the printer: None
