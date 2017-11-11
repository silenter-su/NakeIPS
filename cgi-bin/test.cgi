#!/usr/bin/perl
 
local ($buffer, @pairs, $pair, $name, $value, %FORM);
# 读取文本信息
$ENV{'REQUEST_METHOD'} =~ tr/a-z/A-Z/;
if ($ENV{'REQUEST_METHOD'} eq "POST")
{
   read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
}else {
   $buffer = $ENV{'QUERY_STRING'};
}
# 读取 name/value 对信息
@pairs = split(/&/, $buffer);
foreach $pair (@pairs)
{
   ($name, $value) = split(/=/, $pair);
   $value =~ tr/+/ /;
   $value =~ s/%(..)/pack("C", hex($1))/eg;
   $FORM{$name} = $value;
}
$name = $FORM{name};
$url  = $FORM{url};
 
print "Content-type:text/html\r\n\r\n";
print "<html>";
print "<head>";
print '<meta charset="utf-8">';
print '<title>菜鸟教程(runoob.com)</title>';
print "</head>";
print "<body>";
print "<h2>$name网址：$url</h2>";
print "</body>";
print "</html>";
 
1;
