//Difference of Volumes of Cuboids
using System;
public class Kata
{
  public static int FindDifference(int[] a, int[] b) => return Math.Abs((a[0]*a[1]*a[2])-(b[0]*b[1]*b[2]));
}


//Get the mean of an array
using System.Linq;
using System.Collections.Generic;
using System;
public class Kata
{
  public static int GetAverage(int[] marks) => return marks.Sum()/marks.Count();
}


//Do I get a bonus?
public static class Kata
{
    public static string bonus_time(int salary, bool bonus) => return "$"+(bonus? (salary*10) : salary).ToString();
}


//Counting sheep...
using System;
using System.Linq;
public static class Kata
{
  public static int CountSheeps(bool[] sheeps) => return sheeps.Count(x => x == true);
}


//Miles per gallon to kilometers per liter
using System;
public static class Kata
{
  public static double Converter(int mpg)=> Math.Round(mpg*0.354006, 2);
}


//Cat years, Dog years
public class Dinglemouse 
{
  public static int[] humanYearsCatYearsDogYears(int hy) 
  {
    int cy, dy;
    cy = dy = hy>=2? 24:15;
    if(hy-2>0){cy+= 4*(hy-2); dy+= 5*(hy-2);}  
    return new int[]{hy,cy,dy};
  }
}


//FIXME: Replace all dots
using System.Text.RegularExpressions;
public class Kata
{
  public static string ReplaceDots(string str) => return Regex.Replace(str, "[.]","-");
}


//Remove exclamation marks
public class Kata
{
  public static string RemoveExclamationMarks(string s) => s.Replace("!", "");
}


//Reversed sequence 
using System.Linq;
public static class Kata
{
  public static int[] ReverseSeq(int n) => Enumerable.Range(1,n).Reverse().ToArray();
}


//Drink about
public class Kata
{
  public static string PeopleWithAgeDrink(int old){
    return old<14?"drink toddy":old<18?"drink coke":old<21?"drink beer":"drink whisky";
  }
}


//Swap Values
public class Swapper
{
    public object[] Arguments { get; private set; }
    
    public Swapper(object[] args) => Arguments = args;
    
    public void SwapValues()
    {
        object temp = Arguments[0];
        Arguments[0] = Arguments[1];
        Arguments[1] = temp;
    }
}
