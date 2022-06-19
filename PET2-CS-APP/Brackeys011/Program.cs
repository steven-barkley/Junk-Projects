using System;

namespace Brackeys011
{
    //BASE CLASS
    class Animal
    {
        public string name;
        public int age;
        public float happiness;

        public void PrintBase()
        {
            Console.WriteLine("Name: {0}", name);
            Console.WriteLine("Age: {0}", age);
            Console.WriteLine("Happiness: {0}", happiness);
        }
    }

    //DERIVED CLASS
    class Dog : Animal
    {
        public int spotCount;



        public void Bark ()
        {
            Console.WriteLine("WooF!");
            base.happiness += 0.1f;
        }
    }

    class Cat : Animal
    {
        public float cuteness;

        public void Meow()
        {
            Console.WriteLine("Mew!");
            cuteness++;
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            //Instance base and derived classes in Main method!

            Dog spotty = new Dog();
            spotty.name = "Spotty";
            spotty.age = 5;
            spotty.happiness = 0.8f;
            spotty.spotCount = 12;
            spotty.PrintBase();
            spotty.Bark();
            Console.WriteLine("New happiness = {0}", spotty.happiness);

            Console.ReadLine();

            Cat heisenberg = new Cat();
            heisenberg.name = "Heisenberg";
            heisenberg.happiness = 04f;
            heisenberg.age = 10;
            heisenberg.cuteness = .69f;
            Console.WriteLine("Cuteness is {0}",heisenberg.cuteness);
            heisenberg.PrintBase();
            heisenberg.Meow();
            Console.WriteLine("After meow cuteness is {0}", heisenberg.cuteness);
            heisenberg.PrintBase();

            //Console.WriteLine("New cuteness = {0}",heisenberg.cuteness);
            Console.ReadLine();
        }
    }
}
