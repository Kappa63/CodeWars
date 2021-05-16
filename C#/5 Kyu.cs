//First non-repeating character
using System.Linq;
using System;
public class Kata
{
  public static string FirstNonRepeatingLetter(string s)
  {
    foreach(char Letter in s)
      if( s.Count(x=> x==Char.ToUpper(Letter)||x==Char.ToLower(Letter)) ==1) return Char.ToString(Letter);
    return "";
  }
}


//Scramblies
using System.Linq;
public class Scramblies 
{ 
  public static bool Scramble(string str1, string str2) 
  {
    foreach(char ch in str2) if(!(str1.Count(c=> c==ch)>=str2.Count(c=> c==ch))) return false;
    return true;
  }
}


//Not very secure
using System.Linq;
public class Kata
{
  public static bool Alphanumeric(string str)=> str.Length==0?false:str.All(x=> "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890".Contains(x));
}
