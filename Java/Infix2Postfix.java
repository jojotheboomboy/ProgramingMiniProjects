////////////////////////////////////////////////////
/ Josiah Norman
/ 11/13/2021
////////////////////////////////////////////////////

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;

public class Infix2Postfix
{
    public static void main(String[] args)
    {
        List<String> equations = new List<String>();

        readFile(equations);

        equations.First();
        List<Queue<Character>> postF = new List<Queue<Character>>();


        for(int row = 0; row < equations.GetSize(); row++)
        {
            Queue<Character> temp = in2Post(str2Queue(equations.GetValue()));
            postF.InsertAfter(temp);
            postF.Last();
            equations.Next();
        }

        List<Double> evals = new List<Double>();

        postF.First();
        for(int row = 0; row < postF.GetSize(); row++)
        {
            Double temp = Calculate(postF.GetValue());
            evals.InsertAfter(temp);
            evals.Last();
            postF.Next();
        }


        // Print Everything
        equations.First();
        postF.First();
        evals.First();
        for(int i = 0; i < equations.GetSize(); i++)
        {
            System.out.println(equations.GetValue());
            equations.Next();
            System.out.println(q2Str(postF.GetValue()));
            postF.Next();
            System.out.println(evals.GetValue());
            evals.Next();
            System.out.println();
        }
    }

    public static double Calculate(Queue<Character> q)
    {
        boolean DEBUG = false;

        Queue<Character> postQ = new Queue<>(q);

        if(DEBUG) {System.out.println(postQ);}

        Stack<Double> last = new Stack<Double>();
        while (!postQ.IsEmpty())
        {
            char token = postQ.Dequeue();
            if (isOperand(token))
            {
                double temp = (double) (token - '0');
                if(DEBUG){System.out.println(token + " -> " + temp);}
                last.Push(temp);
            }
            else {
                double j = (Double) last.Pop();
                double k = (Double) last.Pop();
                last.Push(eval(j,k,token));
            }
        }
        return last.Pop();
    }

    public static double eval(double j, double k, char token)
    {
        if(token == '+')
        {
            return k+j;
        }
        else if(token == '-')
        {
            return k-j;
        }
        else if(token == '*')
        {
            return k*j;
        }
        else if(token == '/')
        {
            return k/j;
        }
        else
        {
            return Math.pow(k,j);
        }
    }

    public static Queue<Character> str2Queue(String str)
    {
        Queue<Character> newQueue = new Queue<Character>();
        for(int i = 0; i < str.length(); i++)
        {
            newQueue.Enqueue(str.charAt(i));
        }
        return newQueue;
    }

    public static String q2Str(Queue<Character> q)
    {
        Queue<Character> copy = new Queue<Character>(q);
        String str = "";
        while (!copy.IsEmpty())
        {
            str += copy.Dequeue();
        }
        return str;
    }


    public static boolean isOperand(char c)
    {
//        char[] operators = {'+','-','*','/','^'};
        char[] operators = {'1','2','3','4','5','6','7','8','9','0'};
        for(char item : operators)
        {
            if(c == item)
                return true;
        }
        return false;
    }

    public static Queue<Character> in2Post(Queue<Character> infix)
    {
        boolean DEBUG = false;

        Queue<Character> infixQ = new Queue<Character>(infix);
        Queue<Character> postfixQ = new Queue<Character>();
        Stack<Character> operS = new Stack<Character>();
        while (!infixQ.IsEmpty())
        {
            if(DEBUG){System.out.println("Start");}
            char token = infixQ.Dequeue();
            if(DEBUG){System.out.println(token);}
            if(isOperand(token))
            {
                if(DEBUG){System.out.println("token is operand");}
                postfixQ.Enqueue(token);
            }
            else if(token==')')
            {
                char op = operS.Pop();
                while (op != '(')
                {
                    postfixQ.Enqueue(op);
                    op = operS.Pop();
                }
            }
            else if(operS.Size() < 1)
            {
                operS.Push(token);
            }
            else
            {

                char op = operS.Peek();

                if(DEBUG) { System.out.println(String.format("%s >= %s == %s", stack_priority(op), infix_priority(token), stack_priority(op) >= infix_priority(token))); }
                try {
                    while (stack_priority(op) >= infix_priority(token)) {
                        op = operS.Pop();
                        postfixQ.Enqueue(op);
                        op = operS.Peek();
                    }
                } catch (Exception e) {
                    //Ye
                }
                operS.Push(token);
            }
        }
        while (!operS.IsEmpty())
        {
            char op = operS.Pop();
            postfixQ.Enqueue(op);
        }
        return postfixQ;
    }


    public static int stack_priority(char op)
    {
        final HashMap<Character, Integer> postRank = new HashMap<Character, Integer>();
        postRank.put('^',2); postRank.put('*',2); postRank.put('/',2);
        postRank.put('+',1); postRank.put('-',1);
        int postRankNum = 0;
        if(postRank.get(op) != null)
            postRankNum = postRank.get(op);
        return postRankNum;
    }

    public static int infix_priority(char token)
    {
        final HashMap<Character, Integer> inRank = new HashMap<Character, Integer>();
        inRank.put('(',4); inRank.put('^',3); inRank.put('*',2);
        inRank.put('/',2); inRank.put('+',1); inRank.put('-',1);
        int inRankNum = 0;
        if(inRank.get(token) != null)
            inRankNum = inRank.get(token);
        return inRankNum;
    }


    /*
     * Adds every line from the input file to the given list
     */
    public static void readFile(List<String> l)
    {
        String str = "";
        try
        {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            String line;
            l.First();
            while ((line = br.readLine()) != null)
            {
                l.InsertAfter(line);
                l.Next();
            }
            br.close();
        } catch (Exception e) {
            //TODO: handle exception
        }
    }

}

