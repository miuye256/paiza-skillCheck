using System;

class Program
{
static void Main()
{
    string E = Console.ReadLine();
    var e = E.Split('+');
    int countA = 0;
    int countB = 0;
    int sum = 0;
    
    foreach(var C in e)
    {
        int length = C.Length;
        foreach(char c in C)
        {
            if(c == '<')
        {
            countA++;
        }
        }
        countB = length - countA;

        sum += countA * 10 + countB;
        
        countA = 0;
        countB = 0;
    }

    Console.WriteLine(sum);
}
}