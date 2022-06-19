using System;

namespace Brackeys012
{
    class Program
    {   
        enum Breed { Bulldog, Boxer, Chihuahua, Briard};

        //BASE CLASS
        class Animal
        {
            public string name;
            public int age;
            public float happiness;
        }
        //DERIVED CLASS
        class Dog : Animal
        {
            public Breed breed;
            //CONSTRUCTOR
            public Dog (string _name, int _age, float _happiness, Breed _breed)
            {
                name = _name;
                age = _age;
                happiness = _happiness;

                breed = _breed;
            }
            public void Print() // Prints info about our dog to the console
            {
                Console.WriteLine("Name: " + name);
                Console.WriteLine("Age:" + age);
                Console.WriteLine("Happiness:" + happiness);

                Console.WriteLine("Breed: " + breed);
            }
        }
        public static void Main (string[] args)
        {
            Dog hulk = new Dog("Hulk", 6, 0.7f, Breed.Briard);
            hulk.Print();

            Console.ReadKey();
        }
    }
}
