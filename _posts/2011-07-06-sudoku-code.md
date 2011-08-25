---
layout: post
title: "Sudoku code: another encryption scheme"
categories:
- algorithms
- useless
code: true
published: true
---

Another useless encryption scheme devised by yours truly. While my last one ([pi code](/posts/pi-code/)) was primarily a substitution cipher, this one most significantly involves a transposition cipher, with a simple substitution cipher used as an additional layer. The main idea here is the use of certain numbers in a particular sudoku grid, resulting in a grid cipher. The strength (if any) in this method lies in its unexpected nature; it certainly takes quite a leap of the imagination to correctly deduce the method from the ciphertext. Of course, once the method has been discovered, deciphering merely involves solving a sudoku grid and then figuring out the substitution cipher used, meaning that the key is easy to determine and so this method kind of just looks at Kerckhoffs's Principle and then keeps walking. But that's okay, that's why this is filed under **useless**.

### The setup ###

Find a sudoku puzzle. I happened to have a sudoku game installed, so I just ran that and started a random puzzle, which looked like this:

<table class="sudoku">
	<tr>
		<td>5</td>
		<td></td>
		<td></td>
		<td>1</td>
		<td>7</td>
		<td></td>
		<td></td>
		<td>8</td>
		<td></td>
	</tr>
	<tr>
		<td>3</td>
		<td>1</td>
		<td>9</td>
		<td></td>
		<td>5</td>
		<td></td>
		<td>4</td>
		<td></td>
		<td></td>
	</tr>
	<tr>
		<td></td>
		<td></td>
		<td></td>
		<td>3</td>
		<td></td>
		<td></td>
		<td></td>
		<td>1</td>
		<td>5</td>
	</tr>
	<tr>
		<td>2</td>
		<td></td>
		<td></td>
		<td></td>
		<td>8</td>
		<td></td>
		<td></td>
		<td></td>
		<td></td>
	</tr>
	<tr>
		<td>4</td>
		<td></td>
		<td></td>
		<td>7</td>
		<td></td>
		<td>5</td>
		<td></td>
		<td></td>
		<td>9</td>
	</tr>
	<tr>
		<td></td>
		<td></td>
		<td></td>
		<td></td>
		<td>9</td>
		<td></td>
		<td></td>
		<td></td>
		<td>4</td>
	</tr>
	<tr>
		<td>6</td>
		<td>5</td>
		<td></td>
		<td></td>
		<td></td>
		<td>2</td>
		<td></td>
		<td></td>
		<td></td>
	</tr>
	<tr>
		<td></td>
		<td></td>
		<td>2</td>
		<td></td>
		<td>6</td>
		<td></td>
		<td>5</td>
		<td>4</td>
		<td>8</td>
	</tr>
	<tr>
		<td></td>
		<td>4</td>
		<td></td>
		<td></td>
		<td>3</td>
		<td>7</td>
		<td></td>
		<td></td>
		<td>2</td>
	</tr>
</table>

(Putting in the borders between the 9 squares is too much work, CSS-wise.)

Once solved, it looked like this (as sudoku puzzles always have a unique solution):

<table class="sudoku">
	<tr>
		<td>5</td>
		<td>2</td>
		<td>4</td>
		<td>1</td>
		<td>7</td>
		<td>9</td>
		<td>3</td>
		<td>8</td>
		<td>6</td>
	</tr>
	<tr>
		<td>3</td>
		<td>1</td>
		<td>9</td>
		<td>6</td>
		<td>5</td>
		<td>8</td>
		<td>4</td>
		<td>2</td>
		<td>7</td>
	</tr>
	<tr>
		<td>8</td>
		<td>6</td>
		<td>7</td>
		<td>3</td>
		<td>2</td>
		<td>4</td>
		<td>9</td>
		<td>1</td>
		<td>5</td>
	</tr>
	<tr>
		<td>2</td>
		<td>9</td>
		<td>5</td>
		<td>4</td>
		<td>8</td>
		<td>3</td>
		<td>6</td>
		<td>7</td>
		<td>1</td>
	</tr>
	<tr>
		<td>4</td>
		<td>8</td>
		<td>6</td>
		<td>7</td>
		<td>1</td>
		<td>5</td>
		<td>2</td>
		<td>3</td>
		<td>9</td>
	</tr>
	<tr>
		<td>1</td>
		<td>7</td>
		<td>3</td>
		<td>2</td>
		<td>9</td>
		<td>6</td>
		<td>8</td>
		<td>5</td>
		<td>4</td>
	</tr>
	<tr>
		<td>6</td>
		<td>5</td>
		<td>1</td>
		<td>8</td>
		<td>4</td>
		<td>2</td>
		<td>7</td>
		<td>9</td>
		<td>3</td>
	</tr>
	<tr>
		<td>7</td>
		<td>3</td>
		<td>2</td>
		<td>9</td>
		<td>6</td>
		<td>1</td>
		<td>5</td>
		<td>4</td>
		<td>8</td>
	</tr>
	<tr>
		<td>9</td>
		<td>4</td>
		<td>8</td>
		<td>5</td>
		<td>3</td>
		<td>7</td>
		<td>1</td>
		<td>6</td>
		<td>2</td>
	</tr>
</table>

Obviously, each solved grid can be represented by a sequence of 81 numbers. Furthermore, due to the uniqueness of the solution, the initial grid and the solved grid are equivalent in the sense that from the initial grid one can determine the solved grid. So we represent the initial grid as follows (with 0s standing for spaces):

`500170080319050400000300015200080000400705009000090004650002000002060548040037002`

This results in the following solution grid:

`524179386319658427867324915295483671486715239173296854651842793732961548948537162`

Now, depending on the length of the plaintext, we can choose somewhere between one and five numbers to use as the "holes" in the grid. For example, if we had a plaintext of 45 characters or less, we could choose the numbers 1, 2, 5, 6 and 9. Removing those numbers from the grid would leave us with this:

<table class="sudoku">
	<tr>
		<td> </td>
		<td> </td>
		<td>4</td>
		<td> </td>
		<td>7</td>
		<td> </td>
		<td>3</td>
		<td>8</td>
	</tr>
	<tr> 
		<td>3</td>
		<td> </td>
		<td> </td>
		<td> </td>
		<td> </td>
		<td>8</td>
		<td>4</td>
		<td> </td>
		<td>7</td>
	</tr>
	<tr>
		<td>8</td>
		<td> </td>
		<td>7</td>
		<td>3</td>
		<td> </td>
		<td>4</td>
		<td> </td>
		<td> </td>
		<td> </td>
	</tr>
	<tr> 
		<td> </td>
		<td> </td>
		<td> </td>
		<td>4</td>
		<td>8</td>
		<td>3</td>
		<td> </td>
		<td>7</td>
		<td>1</td>
	</tr>
	<tr>
		<td>4</td>
		<td>8</td>
		<td> </td>
		<td>7</td>
		<td> </td>
		<td> </td>
		<td> </td>
		<td>3</td>
		<td> </td>
	</tr>
	<tr>
		<td> </td>
		<td>7</td>
		<td>3</td>
		<td> </td>
		<td> </td>
		<td> </td>
		<td>8</td>
		<td> </td>
		<td>4</td>
	</tr>
	<tr>
		<td> </td>
		<td> </td>
		<td> </td>
		<td>8</td>
		<td>4</td>
		<td> </td>
		<td>7</td>
		<td> </td>
		<td>3</td>
	</tr>
	<tr>
		<td>7</td>
		<td>3</td>
		<td> </td>
		<td> </td>
		<td>6</td>
		<td> </td>
		<td> </td>
		<td>4</td>
		<td>8</td>
	</tr>
	<tr>
		<td> </td>
		<td>4</td>
		<td>8</td>
		<td> </td>
		<td>3</td>
		<td>7</td>
		<td> </td>
		<td> </td>
		<td> </td>
	</tr>
</table>

which of course has an entirely different arrangement of empty spaces than the initial grid, and which can represented by this:

`50017008031905040000030001520008000040070500900009000465000200000206054804003700212569`

or, if the numbers that remain as opposed to the numbers that are taken away are used, with the result scrambled and with extra zeros added in, for confusion:

`5001700803190504000003000152000800004007050090000900046500020000020605480400370027003804`

We can then use the empty spaces for the grid cipher, and add characters in the rest of the spaces to try and flatten frequencies. A simple substitution cipher should be used as well to prevent the ciphertext from looking too much like a transposition cipher. The alphabetic characters can then be interspersed with the numerals above, with the resulting string separated into chunks of 32 characters (with extra alphabetic characters appended as necessary, since only 81 are needed) so as to superficially resemble MD5 (because that's just fun).

Optimally, the solutions to the possible sudoku grids being used should be stored in a dictionary somewhere, so that each grid only has to be solved once. The point of this encryption scheme is to be diabolically tricky but solvable, although perhaps only if you figure out the sudoku aspect and know a crib or two.

### Encoding and decoding a sequence ###

Let's say you want to encode:

`admiral yamamoto to visit solomon islands eight am`

First, remove spaces:

`admiralyamamototovisitsolomonislandseightam`
	
This is 43 characters, so let's aim for one grid with 5 numbers. This means there will be 2 extra invalid characters and 36 nonsense characters. Since some spaces will be fairly large, it's a good idea to use a simple substitution cipher as well (or even a less simple one like Vigenère for additional fiendishness). In this case, we'll use the reverse alphabet cipher:

`abcdefghijklm`  
`zyxwvutsrqpon`

So the encrypted plaintext becomes

`admiralyamamototovisitsolomonislandseightam`  
`zwnrizobznznlglglerhrghlolnlmrhozmwhvrtsgzn`

Now put it in the grid:

<table class="sudoku">
	<tr>
		<td>z</td>
		<td>w</td>
		<td>4</td>
		<td>n</td>
		<td>7</td>
		<td>r</td>
		<td>3</td>
		<td>8</td>
		<td>i</td>
	</tr>
	<tr>
		<td>3</td>
		<td>z</td>
		<td>o</td>
		<td>b</td>
		<td>z</td>
		<td>8</td>
		<td>4</td>
		<td>n</td>
		<td>7</td>
	</tr>
	<tr>
		<td>8</td>
		<td>z</td>
		<td>7</td>
		<td>3</td>
		<td>n</td>
		<td>4</td>
		<td>l</td>
		<td>g</td>
		<td>l</td>
	</tr>
	<tr>
		<td>g</td>
		<td>l</td>
		<td>e</td>
		<td>4</td>
		<td>8</td>
		<td>3</td>
		<td>r</td>
		<td>7</td>
		<td>h</td>
	</tr>
	<tr>
		<td>4</td>
		<td>8</td>
		<td>r</td>
		<td>7</td>
		<td>g</td>
		<td>h</td>
		<td>l</td>
		<td>3</td>
		<td>o</td>
	</tr>
	<tr>
		<td>l</td>
		<td>7</td>
		<td>3</td>
		<td>n</td>
		<td>l</td>
		<td>m</td>
		<td>8</td>
		<td>r</td>
		<td>4</td>
	</tr>
	<tr>
		<td>h</td>
		<td>o</td>
		<td>z</td>
		<td>8</td>
		<td>4</td>
		<td>m</td>
		<td>7</td>
		<td>w</td>
		<td>3</td>
	</tr>
	<tr>
		<td>7</td>
		<td>3</td>
		<td>h</td>
		<td>v</td>
		<td>r</td>
		<td>t</td>
		<td>s</td>
		<td>4</td>
		<td>8</td>
	</tr>
	<tr>
		<td>g</td>
		<td>4</td>
		<td>8</td>
		<td>z</td>
		<td>3</td>
		<td>7</td>
		<td>n</td>
		<td>c</td>
		<td>a</td>
	</tr>
</table>

(The last two characters are the extra invalid characters used to fill up the empty spaces.)

Now replace the remaining numbers with letters:

<table class="sudoku">
	<tr>
		<td>z</td>
		<td>w</td>
		<td>e</td>
		<td>n</td>
		<td>a</td>
		<td>r</td>
		<td>o</td>
		<td>t</td>
		<td>i</td>
	</tr>
	<tr>
		<td>q</td>
		<td>z</td>
		<td>o</td>
		<td>b</td>
		<td>z</td>
		<td>a</td>
		<td>e</td>
		<td>n</td>
		<td>s</td>
	</tr>
	<tr>
		<td>f</td>
		<td>z</td>
		<td>t</td>
		<td>r</td>
		<td>n</td>
		<td>m</td>
		<td>l</td>
		<td>g</td>
		<td>l</td>
	</tr>
	<tr>
		<td>g</td>
		<td>l</td>
		<td>e</td>
		<td>e</td>
		<td>a</td>
		<td>s</td>
		<td>r</td>
		<td>h</td>
		<td>h</td>
	</tr>
	<tr>
		<td>t</td>
		<td>r</td>
		<td>r</td>
		<td>a</td>
		<td>g</td>
		<td>h</td>
		<td>l</td>
		<td>m</td>
		<td>o</td>
	</tr>
	<tr>
		<td>l</td>
		<td>c</td>
		<td>c</td>
		<td>n</td>
		<td>l</td>
		<td>m</td>
		<td>z</td>
		<td>r</td>
		<td>v</td>
	</tr>
	<tr>
		<td>h</td>
		<td>o</td>
		<td>z</td>
		<td>l</td>
		<td>p</td>
		<td>m</td>
		<td>p</td>
		<td>w</td>
		<td>p</td>
	</tr>
	<tr>
		<td>a</td>
		<td>e</td>
		<td>h</td>
		<td>v</td>
		<td>r</td>
		<td>t</td>
		<td>s</td>
		<td>b</td>
		<td>d</td>
	</tr>
	<tr>
		<td>g</td>
		<td>g</td>
		<td>f</td>
		<td>z</td>
		<td>e</td>
		<td>q</td>
		<td>n</td>
		<td>c</td>
		<td>a</td>
	</tr>
</table>

Written as one line, the grid would look like

`zwenarotiqzobzaensfztrnmlglgleeasrhhtrraghlmolccnlmzrvhozlpmpwpaehvrtsbdggfzeqnca`

Recall that the original grid looks as follows:

`500170080319050400000300015200080000400705009000090004650002000002060548040037002`

With the numbers used added to the end of the grid, it might look like this:

`50017008031905040000030001520008000040070500900009000465000200000206054804003700215926`
	
Now, we randomly combine the two: (split across two lines here due to design considerations)

`z50w0ena1r7o008tiq0zo3bz1ae9nsf0z5t0r4n0mlgl0g0le0e0as3rhh00tr0rag1h5lm2ol00ccn0l8mz`  
`r0v0ho0z0400lp7mpwp0a500eh9v0r0t0sbd090gg0046f500ze02000q0020n6054c80400a3700215926`
	
We could even put in extra characters at the end, since only the first 81 characters will be used:

`z50w0ena1r7o008tiq0zo3bz1ae9nsf0z5t0r4n0mlgl0g0le0e0as3rhh00tr0rag1h5lm2ol00ccn0l8mzr0v`  
`0ho0z0400lp7mpwp0a500eh9v0r0t0sbd090gg0046f500ze02000q0020n6054c80400a3f70gg02a1e59f26x`
	
Now we split it up into chunks of 32 digits each:
	
`z50w0ena1r7o008tiq0zo3bz1ae9nsf0`  
`z5t0r4n0mlgl0g0le0e0as3rhh00tr0r`  
`ag1h5lm2ol00ccn0l8mzr0v0ho0z0400`  
`lp7mpwp0a500eh9v0r0t0sbd090gg004`  
`6f500ze02000q0020n6054c80400a3f7`  
`0gsssg02ea1e5dllg9famezelr2ezz6x`
	
(This one was badly spaced, because I didn't plan it out well ... the characters should be more or less evenly spaced.)

And there you go. not indecipherable but certainly very misleading. To decipher, first separate the numerals from the alphabetic characters, then write out the first 81 characters within a 9x9 grid. Then fill another 9x9 grid with the first 81 numerals (one digit per box), omitting the zeros, and solve the resulting sudoku puzzle. Take the remaining (non-zero) digits and highlight the positions in the grid corresponding to those digits. The characters corresponding to the non-highlighted positions can be discarded. Now it only remains to reverse the substitution cipher and insert spaces where necessary.

Challenge:

### Implementation in various programming languages ###