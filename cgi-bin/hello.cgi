#!/usr/bin/perl -w
use CGI;
{
	my $q = new CGI;
	print $q->header(),
		$q->start_html("hello perl world!"),
		$q->h1('hello perl world'),
		$q->end_html();
}
