fun closer (infile, outfile) = 
    (
    TextIO.closeIn(infile);
    TextIO.closeOut(outfile);
    ()
    );

fun writer(value, outfile) = TextIO.output(outfile, value);

fun check(x::xs) = if Int.fromString(str(x)) = NONE then false else check(xs)
    |check([]) = true;

fun parser(NONE, infile, outfile) = closer(infile, outfile)
    |parser(SOME value, infile, outfile) = 
    let 
        val list = explode(value)
    in 
        if check(list) = true 
        then (writer(value, outfile); parser(TextIO.inputLine(infile), infile, outfile)) 
        else parser(TextIO.inputLine(infile), infile, outfile)
    end;

fun strip (readFile, writeFile) = 
    let
        val infile = TextIO.openIn(readFile)
        val outfile = TextIO.openOut(writeFile)
    in 
        parser(TextIO.inputLine(infile), infile, outfile)
    end;

(* CALLING STATEMENT for strip function *)
strip("input.txt","output.txt");