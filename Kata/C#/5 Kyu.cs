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
