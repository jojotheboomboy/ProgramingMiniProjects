(*
NAMES: JAY REICH, JOSIAH NORMAN
DATE: 1/27/23
COURSE/SECTION: CSC-330-002
QUARTER: WINTER
PROJECT: 1
 *)

(* WORK DIVISION *)
(* JOSIAH, checkChar, checker, comments, portions of parse function *)
(* JAY, checkerHelper, strGrabber, portions of parse function *)
(* JASON, token datatype *)

(* DataType definition for Token *)
datatype token = ID of string | EQ | PL | MI | TI | DI;

(*  checkChar returns false if the character recieved as input is outside the bounds of
upper case or lower case letters. Returns true if the character is within those bounds *)
fun checkChar (x) = if (ord(x)<65 orelse ord(x)>90) andalso (ord(x)<97 orelse ord(x)>122) 
  then false
  else true;

(* Iterates character by character over the given char list, if the charlist contains a character 
that is not in the set of allowed chars (+, -, *, /, =, \n, or the space character) if a uppercase or lowercase
letter is the head of the list then send to checkChar to verify if it is a valid character, if it fails print 
"Complilation Error", if it does pass the test then simply recursivly call the function with the tail as the argument. *)
fun checkerHelper [] = true
   |checkerHelper(#"+"::xs) = checkerHelper(xs)
   |checkerHelper(#"-"::xs) = checkerHelper(xs)
   |checkerHelper(#"*"::xs) = checkerHelper(xs)
   |checkerHelper(#"/"::xs) = checkerHelper(xs)
   |checkerHelper(#"="::xs) = checkerHelper(xs)
   |checkerHelper(#" "::xs) = checkerHelper(xs)
   |checkerHelper(#"\n"::xs) = checkerHelper(xs)
   |checkerHelper(x::xs) = if checkChar(x) 
      then checkerHelper(xs)
      else (print("Compilation error\n");false);

(* Checks a list of strings and feeds the exploded strings, which are now char lists, 
into the checkerHelper function, if checkerHelper return false then this functions also returns false *)
fun checker ([]) = true
  |checker (x::xs) = if checkerHelper(explode(x)) then checker(xs) else false;

(* Recursive function that checks for specfic patterns and builds the token list for output *)
fun strGrabber ([],"") = []
   |strGrabber ([],s) = [ID s]
   |strGrabber ((#"+"::xs),"") = PL :: strGrabber(xs,"")
   |strGrabber ((#"-"::xs),"") = MI :: strGrabber(xs,"")
   |strGrabber ((#"*"::xs),"") = TI :: strGrabber(xs,"")
   |strGrabber ((#"/"::xs),"") = DI :: strGrabber(xs,"")
   |strGrabber ((#"="::xs),"") = EQ :: strGrabber(xs,"") 
   |strGrabber ((#" "::xs),"") = strGrabber(xs,"")
   |strGrabber ((#"\n"::xs),"") = strGrabber(xs,"") (**)
   |strGrabber ((#"+"::xs),s) = [ID s, PL] @ strGrabber(xs,"")
   |strGrabber ((#"-"::xs),s) = [ID s, MI] @ strGrabber(xs,"")
   |strGrabber ((#"*"::xs),s) = [ID s, TI] @ strGrabber(xs,"")
   |strGrabber ((#"/"::xs),s) = [ID s, DI] @ strGrabber(xs,"")
   |strGrabber ((#"="::xs),s) = [ID s, EQ] @ strGrabber(xs,"")
   |strGrabber ((#" "::xs),s) = ID s :: strGrabber(xs,"")
   |strGrabber ((#"\n"::xs),s) = ID s :: strGrabber(xs,"")
   |strGrabber ((x::xs),s) = strGrabber(xs,s^str(x))

(* PARSE
TextList is a list for each line in read file
Getlist is used to seperate each line in the given file to build textList
Checked calls checker and stores the boolean value given.
*)

(* Parser Helper
Recursive pattern matching function that given checked is true calls string grabber to build token list 
if checked is false then returns empty list.
parsed is the variable that stores the token list.
*)
fun parse (input) = 
let
  val infile = TextIO.openIn(input)

  fun getList (NONE) = []
     |getList (SOME x) = (x)::getList(TextIO.inputLine(infile))
  val textList = getList(TextIO.inputLine(infile))

  val checked = checker(textList)

  fun parseHelper ([]) = []
     |parseHelper (x::xs) = if (checked)
     then (strGrabber(explode(x),"")@parseHelper(xs))
     else []
  val parsed = parseHelper(textList)
in
  (TextIO.closeIn(infile);parsed)
end;

(* parse("input.txt"); *)