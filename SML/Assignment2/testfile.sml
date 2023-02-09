fun closer (infile, outfile) = 
    (
    TextIO.closeIn(infile);
    TextIO.closeOut(outfile);
    ()
    );

(* [#"3",#"5",#"A",#"3"]
fun parser2 (x::xs, infile, outfile) =
    if Int.fromString(str(x)) = NONE then 

fun parser (NONE, infile, outfile) = closer(infile, outfile)
    |parser (SOME value, infile, outfile) = parser2(explode(value), infile, outfile);
*)
(*)
fun succeed(infile, outfile, value) = 
    (
        TextIO.output(outfile, value);
        parser(TextIO.inputLine(infile), infile, outfile)
    );

fun failed(infile, outfile, value) = 
    parser(TextIO.inputLine(infile), infile, outfile)
fun isEmpty(xs,infile, outfile, value) = if xs = [#" "] then print("empty") else print("not empty"); *)
fun check(x::xs) = if (print("hit "); print(str(x)); print(" no\n"); Int.fromString(str(x))) = NONE then true else check(xs)
    |check([]) = false
and 
    parser(NONE, infile, outfile) = closer(infile, outfile)
    |parser (SOME value, infile, outfile) = 
    if check(explode(value)) = false 
        then (TextIO.output(outfile, value); parser(TextIO.inputLine(infile), infile, outfile))
    else parser(TextIO.inputLine(infile), infile, outfile);
(*and 
    check([]) = (print("hit"); true)
    |check(x::xs) = if Int.fromString(str(x)) = NONE then (print(implode(xs)); false) else (print(implode(xs)); check(xs));
(*)
    check(x::xs, infile, outfile, value) = 
    if Int.fromString(str(x)) = NONE 
        then parser(TextIO.inputLine(infile), infile, outfile)
    else check(xs, infile, outfile, value)
    |check([], infile, outfile, value) = 
    (
        TextIO.output(outfile, value);
        parser(TextIO.inputLine(infile), infile, outfile)
    );
    (*)*)
    charEval(x::xs, infile, outfile, value) = 
    if Int.fromString(str(x)) = NONE 
        then parser(TextIO.inputLine(infile), infile, outfile) 
    else (print(implode(xs)); charEval(xs, infile, outfile, value))
    |charEval(,infile, outfile, value) = 
        (
        print("hit");
        TextIO.output(outfile, value);
        parser(TextIO.inputLine(infile), infile, outfile)
        );
    (*
    characterEvaluation(x::xs, infile, outfile, value) = 
    if Int.fromString(str(x)) = NONE 
        then parser(TextIO.inputLine(infile), infile, outfile)
    else characterEvaluation(xs, infile, outfile, value)
    |characterEvaluation([], infile, outfile, value) = 
        (
            print(value);
            TextIO.output(outfile, value);
            parser(TextIO.inputLine(infile), infile, outfile)
        );
    *)*)*)

fun strip (readFile, writeFile) = 
    let
        val infile = TextIO.openIn(readFile)
        val outfile = TextIO.openOut(writeFile)
    in 
        parser(TextIO.inputLine(infile), infile, outfile)
    end;

strip("input.txt","output.txt");