(*
JOSIAH NORMAN
1/11/2023
CSC-330-002
WINTER QUARTER
Assignment #2
*)

(* CLOSER FUNCTION of the type    TextIO.instream * TextIO.outstream -> unit *)

(* closes the respective reading file and writing file and returns unit *)
fun closer (infile, outfile) = 
    (
    TextIO.closeIn(infile);
    TextIO.closeOut(outfile);
    ()
    );

(*  PARSER FUNCTION of type    string option * TextIO.instream * TextIO.outstream -> unit *)

(* returns a call to the closer function if the TextIO.inputLine(infile) is yields NONE.
 NOTE: the only time in which this will occur is if the readfile is empty *)

(* if the TextIO.inputLine(infile) is yields SOME value, then the we will attempt to convert
the value to an integer and store this value under the variable cached *)

(* if cached cannot be converted to an integer then the variable cached will be set to NONE. 
In this case a recursive call will be returned where the infile, outfile remain and the next 
line are given as arguments. *)

(* in the case where cached can be converted to an integer, value will be written into the 
specified file for writing and the same recursive call from the previous example will be returned *)
fun parser (NONE, infile, outfile) = closer(infile, outfile)
    |parser (SOME value, infile, outfile) =   
    let  
        val cached = Int.fromString(value)
    in 
        if cached = NONE 
        then parser(TextIO.inputLine(infile), infile, outfile)
        else 
            (
                TextIO.output(outfile, value);
                parser(TextIO.inputLine(infile), infile, outfile)
            )
    end;

(*  STRIP FUNCTION of type    string * string -> unit *)

(* infile references the opened file for reading 
outfile references the opened file for writing *)

(*  calls parser with the ladder variables as 
arguments as well as the first line of the infile *)
fun strip (readFile, writeFile) = 
    let
        val infile = TextIO.openIn(readFile)
        val outfile = TextIO.openOut(writeFile)
    in 
        parser(TextIO.inputLine(infile), infile, outfile)
    end;

(* CALLING STATEMENT for strip function 
strip("input.txt","output.txt"); *)