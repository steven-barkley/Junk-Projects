using System;

namespace Brackeys08
{
    class Program
    {
        public static void Main(string[] args)
        {
            int result = Add(4, 9);

            Console.WriteLine(result);

            if (result >= 10)
            {
                Console.WriteLine("Result is larger than 10");
            }
            else
            {
                Console.WriteLine("Result is less than 10");
            }

            Console.ReadLine();
        }
        //Methods are also known as Functions in C#

       public static int Add(int i, int j)
        {
            return i + j;
        }
        
    }
}
