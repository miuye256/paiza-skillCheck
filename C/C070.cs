using System;

class Program
{
    public static int minus(int number)
    {
        int goalnum = number / 10;
        goalnum *= 10;
        int count = 0;

        while(number != goalnum)
        {
            number -= 1;
            count++;
        }
        return count;
    }

    static void Main()
    {
        int num = Console.ReadLine().Trim();
        int[] numbers;

        for(int i = 0; i < num; i++)
        {
            numbers[i] = Console.ReadLine().Trim();
        }

        for (var i = 0; i < num; i++)
        {

        }
    }
}