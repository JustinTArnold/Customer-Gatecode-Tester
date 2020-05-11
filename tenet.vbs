Dim Arg, var1, var2
Set Arg = WScript.Arguments
var1 = Arg(0)
var2 = Arg(1)
set WshShell = WScript.CreateObject("WScript.Shell")
WshShell.run "Telnet", 2
WScript.Sleep 100
WshShell.SendKeys("set logfile tellog.txt")
WshShell.SendKeys("{Enter}")
WScript.Sleep 100
WshShell.SendKeys("o " _
       & var1 & " 8897")
WshShell.SendKeys("{Enter}")
WScript.Sleep 200
WshShell.SendKeys("Code=128, " _
       & var2)
WshShell.SendKeys("{Enter}")
WScript.Sleep 1000
WshShell.SendKeys("^]")
WshShell.SendKeys("quit")
WshShell.SendKeys("{Enter}")

