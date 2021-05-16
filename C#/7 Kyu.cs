//Regex validate PIN code
using System;
using System.Text.RegularExpressions;
public class Kata
{
  public static bool ValidatePin(string pin) => return Regex.IsMatch(pin, @"^(\d{4}|\d{6})\z");
}


//Printer Errors
using System.Linq;
using System;
public class Printer 
{
    public static string PrinterError(String s)=> String.Format("{0}/{1}", s.Count(L=> !"abcdefghijklm".Contains(L)), s.Count());
}
