//Regex validate PIN code
using System;
using System.Text.RegularExpressions;
public class Kata
{
  public static bool ValidatePin(string pin) => return Regex.IsMatch(pin, @"^(\d{4}|\d{6})\z");
}