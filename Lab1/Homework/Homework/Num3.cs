using System;

namespace Homework
{
    class Num3
    {
        //для невпорядкованого масиву
        int CountUnorderedArray<T>(T[] arr)
        {
            List<T> uniqueElements = new List<T>();
            foreach (var element in arr)
            {
                if (!uniqueElements.Contains(element))
                {
                    uniqueElements.Add(element);
                }
            }
            return uniqueElements.Count;
        }

        //для впорядкованого масиву
        int CountOrderedArray<T>(T[] arr)
        {
            int uniqueCount = 1; // Початково в масиві точно є один унікальний елемент
            for (int i = 1; i < arr.Length; i++)
            {
                if (arr[i] != arr[i - 1])
                {
                    uniqueCount++;
                }
            }
            return uniqueCount;
        }

        static void Main(string[] args)
        {
            
        }
    }
}