using System;
using System.Collections.Generic;

namespace Brackeys09
{
    class Program
    {
        static void Main(string[] args)
        {
            CreateGrid();  
            Console.ReadKey();
        }
        public static void CreateGrid()
        {
            int width, height;
            width = 20;
            height = 20;

            int[,] grid = new int[width,height];
            grid[2, 3] = 7;

            for ( int x =0; x < width; x++)
            {
                for (int y = 0; y < height; y++)
                {
                    grid [x,y] = x + y;
                    Console.Write(grid[x,y] + " ");
                }
                Console.WriteLine();
            }
            Console.ReadLine();
        }
    }
}
