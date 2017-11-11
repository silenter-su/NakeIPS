#!/usr/bin/perl
 
print "Set-Cookie:UserID=XYZ;\n";
print "Set-Cookie:Password=XYZ123;\n";
print "Set-Cookie:Expires=Tuesday, 31-Dec-2017 23:12:40 GMT;\n";
print "Set-Cookie:Domain=www.runoob.com;\n";
print "Set-Cookie:Path=/perl;\n";
print "Content-type:text/html\r\n\r\n";

print "<!DOCTYPE html>";
print "<html>";
print "<head>";
print "<meta charset=utf-8>";
print "<title>菜鸟教程(runoob.com)</title>";
print "</head>";
print "<body>";
print "    <h1>Cookie set!!!</h1>";
print "    <p>我的第一个段落。</p>";
print "</body>";
print "</html>";
