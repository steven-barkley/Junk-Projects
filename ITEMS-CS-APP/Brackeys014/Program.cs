using System;

namespace Brackeys014
{
    class Program
    {
        //Interfaces
        interface IItem
        {
            string name { get; set; }
            int goldValue { get; set; }

            //Methods
            void Equip();
            void Sell();
        }

        class Sword : IItem
        {
            public string name { get; set; }
            public int goldValue { get; set; }

            public void Equip()
            {
                Console.WriteLine("The sword {0} has been equipped.",name);
            }
            public void Sell()
            {
                Console.WriteLine("The sword {0} has been sold for {1} gold.", name, goldValue);
            }

            public Sword (string _name)
            {
                name = _name;
                goldValue = 100;
            }
        }
            //A structure of methods and properties that need to be in a class

        public static void Main(string[] args)
        {
            Sword jagged
            Console.ReadLine();
        }
    }
}
