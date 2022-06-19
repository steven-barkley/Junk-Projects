using System;
using System.Collections.Generic;
using System.Text;

namespace Brackeys05
{
    class Class1
    {
        public static void Main(string[] args)
        {
            Start:
            Random numGen = new Random();

            int numberofattempts;
            numberofattempts = 0;

            int attempt = 0;

            while (attempt !=6)
            {
                attempt = numGen.Next (1, 7);
                Console.WriteLine("Tom rolled:" + attempt + ".");
                numberofattempts++;
            }
            Console.WriteLine("It took Tom {}\\ attempts to roll a six",numberofattempts);

            Console.ReadLine();
            goto Start;
        }
        
    }
}
