#!/usr/bin/perl
$rcvd_cookies = $ENV{'HTTP_COOKIE'};
@cookies = split /;/, $rcvd_cookies;
foreach $cookie ( @cookies ){
   ($key, $val) = split(/=/, $cookie); # splits on the first =.
   $key =~ s/^\s+//;
   $val =~ s/^\s+//;
   $key =~ s/\s+$//;
   $val =~ s/\s+$//;
   if( $key eq "UserID" ){
      $user_id = $val;
   }elsif($key eq "Password"){
      $password = $val;
   }
}
print "Content-type:text/html\r\n\r\n";
print "<html>";
print "<head>";
print "<meta charset=utf-8>";
print "<title>菜鸟教程(runoob.com)</title>";
print "</head>";
print "<body>";
print "    <h1>";
print "Cookie set!!!";
print "<br\>";
print "User ID  = $user_id\n";
print "Password = $password\n";
print "    </h1>";
print "    <p>我的第一个段落。</p>";
print "</body>";
print "</html>";
