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


//Chess Fun #1: Chess Board Cell Color
using System;
using System.Text;
namespace myjinxin
{   
  public class Kata
  {
    public bool ChessBoardCellColor(string cell1, string cell2){
      int H1 = Encoding.ASCII.GetBytes(cell1.Substring(0, 1))[0]; int W1 = Convert.ToInt32(cell1.Substring(1));
      int H2 = Encoding.ASCII.GetBytes(cell2.Substring(0, 1))[0]; int W2 = Convert.ToInt32(cell2.Substring(1));
      return (W1%2==0?(H1%2==0?true:false):(H1%2==0?false:true)) == (W2%2==0?(H2%2==0?true:false):(H2%2==0?false:true));
    }
  }
}


//Find The Parity Outlier
using System.Collections.Generic;
using System.Linq;
using System;
public class Kata
{
  public static int Find(int[] integers)
  {
    int? e = null;
    int? o = null;
    foreach (int i in integers){
      if (i%2==0){
        if(e==null)e=i;
        else if(e!=null && o!=null)return Convert.ToInt32(o);
      }
      else{
        if(o==null)o=i;
        else if(o!=null && e!=null)return Convert.ToInt32(e);
      } 
    }
    return integers[integers.Length-1];
  }
}
