using System;

namespace Brackeys1
{
    class Program
    {
        static void Main(string[] args)
        {
            Random numberGenerator = new Random();

            int num01 = numberGenerator.Next(1, 11);
            int num02 = numberGenerator.Next(1, 11);

            Console.WriteLine("What is " + num01 + " times " + num02 + "?");

            int answer = Convert.ToInt32(Console.ReadLine());

            if (answer == num01 * num02)
            {
                Console.WriteLine("Well done! Your answer is correct.");
            }
            else
            {
                Console.WriteLine("Are you even trying?");
            }
            Console.ReadKey();
        }
    }
}
