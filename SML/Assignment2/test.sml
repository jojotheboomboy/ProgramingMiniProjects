fun closer (infile, outfile) = 
    (
    TextIO.closeIn(infile);
    TextIO.closeOut(outfile);
    ()
    );

fun check(x::xs) = if Int.fromString(str(x)) = NONE then true else check(xs)
    |check([]) = false;

fun parser(NONE, infile, outfile) = closer(infile, outfile)
    |parser (SOME value, infile, outfile) = 
    if check(explode(value)) = true 
        then (print("hit");TextIO.output(outfile, value); parser(TextIO.inputLine(infile), infile, outfile))
    else parser(TextIO.inputLine(infile), infile, outfile)

fun strip (readFile, writeFile) = 
    let
        val infile = TextIO.openIn(readFile)
        val outfile = TextIO.openOut(writeFile)
    in 
        parser(TextIO.inputLine(infile), infile, outfile)
    end;

(* CALLING STATEMENT for strip function *)
strip("input.txt","output.txt");