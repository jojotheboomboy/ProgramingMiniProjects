(* 
NAME: Josiah Norman
DATE: 12/15/22
COURSE: CSC 330-002
QUARTER: Winter
ASSIGNMENT: #1
*)

(* 1 *)
fun replace ([],target,replacement) = []
    | replace(x::xs, target, replacement) = if target = x 
    then replace(replacement::xs,target,replacement)
    else x::replace(xs,target,replacement);

(* 2 *)
fun stringfun (x:string) = fn (y:string) => y^x;

(* 3 *)
fun avg(list) = 
    let 
        val s = real(length(list))
        fun helper([]) = 0.0
            | helper(x::xs) = x + helper(xs)
    in 
        helper(list)/s
    end;
