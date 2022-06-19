using System;

namespace Brackeys5
{
    class Program
    {
        public static void Main(string[] args)
        {Start:
            Random numberGenerator = new Random();

            int num01 = numberGenerator.Next(1,11);
            int num02 = numberGenerator.Next(1,11);

            Console.WriteLine("What is {0} times {1} equal to?",num01,num02);

            int answer = Convert.ToInt32(Console.ReadLine());

            if (answer == num01 * num02)
            {
                Console.WriteLine("Correct!");
            }
            else
            {
                Console.WriteLine("Are you even trying??");
            }
            Console.ReadLine();
            goto Start;
        }
    }
}
