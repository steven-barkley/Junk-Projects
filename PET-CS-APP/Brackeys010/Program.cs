using System;

namespace Brackeys010
{
    class Animal
    {
        //Properties

        public int Count = 0;
       
        public string name;
        public int age;
        public float happiness;

        //CLASS CONSTRUCTORS

        public Animal()
        {
            name = "Spotty";
            age = 6;
            happiness = 0.4f;

            Count++;
        }

        public Animal(string _name, int _age, float _happiness)
        {
            name = _name;
            age = _age;
            happiness = _happiness;
            Count++;
        }

        public void Print()
        {
            Console.WriteLine("Name: {0}",name);
            Console.WriteLine("Age: {0}",age);
            Console.WriteLine("Happiness: {0}",happiness);
            Console.ReadLine();
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            //Using Classes

            Animal bear = new Animal();
            bear.Print();

            Animal tiger = new Animal("Lyzer", 12, .07f);

            Console.WriteLine();
            Console.WriteLine( "Number of Animals is {0}", (bear.Count+tiger.Count));

            Console.ReadLine();
        }
    }
}
