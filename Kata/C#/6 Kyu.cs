//Array.diff
using System.Linq;
public class Kata
{
  public static int[] ArrayDiff(int[] a, int[] b)=>a.Where(val => !b.Contains(val)).ToArray();
}


//Good vs Evil
using System;
using System.Linq;
public class Kata
{
  public static string GoodVsEvil(string g, string e)
  {
    int[] GoodWorth = {1,2,3,3,4,10}; int[] EvilWorth = {1,2,2,2,3,5,10};
    int GoodTotal=0; int EvilTotal=0;
    int[] Good = g.Split(" ").Select(int.Parse).ToArray(); int[] Evil = e.Split(" ").Select(int.Parse).ToArray();
    for(int i=0;i < Good.Length;i++)GoodTotal+= GoodWorth[i]*Good[i];
    for(int i=0;i < Evil.Length;i++)EvilTotal+= EvilWorth[i]*Evil[i];
    return "Battle Result: " + (GoodTotal<EvilTotal?"Evil eradicates all trace of Good":GoodTotal>EvilTotal?"Good triumphs over Evil":"No victor on this battle field");
  }
}
