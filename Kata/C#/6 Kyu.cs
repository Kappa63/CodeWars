//Array.diff
using System.Linq;
public class Kata
{
  public static int[] ArrayDiff(int[] a, int[] b)=>a.Where(val => !b.Contains(val)).ToArray();
}
