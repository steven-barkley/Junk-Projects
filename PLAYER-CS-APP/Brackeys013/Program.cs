using System;

namespace Brackeys013
{
    class Program
    {
        class Player
        {
            int _health = 100;

            public int health
            {
                get
                {
                    return _health;
                }
                set
                {
                    if (value <= 0)
                    {
                        _health = 0;
                    }
                    else if (value >=100)
                    {
                        _health = 100;
                    }
                    else
                    {
                        _health = value;
                    }
                    
                }
            }

            public void Damage (int _dmg)
                {
                _health -= _dmg;
                }

        }
        public static void Main(string[] args)
        {
            Player tom = new Player();

            Console.WriteLine(tom.health);
            tom.Damage(50);

            tom.health = 20;

            Console.WriteLine(tom.health);
            
            Console.ReadKey();
        }
    }
}
