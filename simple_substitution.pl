#!/usr/bin/perl
use strict;
use warnings;
use Term::ANSIColor;
use List::MoreUtils qw(first_index);
use IO::Prompt; 
# use IO::Prompt::Tiny qw/prompt/;
use Getopt::Std;

my @alphabet = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z");
my @secret_alphabet = ();
my @colors = ();
my %options=();getopts("e:s:hg:", \%options);

sub print_help{
    print colored( sprintf("simple_substitution.pl"), 'bold'), ": A perl script used to encrypt and decrypt text using the simple substitution algorithm\n";
    print colored( sprintf("\t-h"), 'yellow'), ": Prints this help message\n";
    print colored( sprintf("\t-s"), 'yellow'), ": Reads secret dictioanry from file in the form of: ", colored( sprintf("Z U N W ...\n"), 'blue');
    print colored( sprintf("\t-e"), 'yellow'), ": Reads message to be encrypted from file e..g.: ", colored( sprintf("./simple_substitution.pl -e plaintex.txt\n"), 'blue');
    print colored( sprintf("\t-d"), 'yellow'), ": Reads ciphertext to be decrypted from file e..g.: ", colored( sprintf("./simple_substitution.pl -d .txt\n"), 'blue');
    exit;
}
sub print_alphabet {
    my ($done) = @_;
    my $initcolor = 1;
    print("\r| ");
    for my $letter (@alphabet) {
        if ((grep { $_ eq "$letter"} @secret_alphabet) && (!$done)){
            print "  ";
        }
        else {
            print colored( sprintf("$letter"), 'ansi'.$initcolor ), " ";
        }
        $initcolor += 10;
    }
    print "| ";
}
sub print_secret_alphabet {
    print("| ");
    my $i = 0;
    foreach my $item (@secret_alphabet) {
        print colored( sprintf("$secret_alphabet[$i]"), 'ansi'.$colors[$i++]), " ";
    }
    
    print("|\n-------------------------------------------------------\n");
}

sub print_dict {
    print "\n--------------------Dictionary-------------------------\n";
    print_alphabet(1);
    print "\n";
    print_secret_alphabet;
}

sub prompt_for_subst {
    my $initcolor = 1;
    for (my $i = 0; $i < 26; $i++) {
        print_alphabet(0);
        print "Provide substitute letter for ";
        print colored( sprintf("$alphabet[$i]"), 'ansi'.$initcolor), ": ";
        $initcolor += 10;
        chomp(my $userinput = uc(prompt "", -1 ));
        print ("\n");
        while (! grep { $_ eq "$userinput"} @alphabet ){
            chomp($userinput = uc(prompt "\t\t\t\t\t\t\tPlease provide an English letter: ", -t1 ));
            print ("\n");
        }
        if ( grep { $_ eq "$userinput"} @alphabet ) {
            while ( (grep { $_ eq "$userinput"} @secret_alphabet) || !( grep { $_ eq "$userinput"} @alphabet)) {
                if (! grep { $_ eq "$userinput"} @alphabet) {
                    print ("\t\t\t\t\t\t\tPlease provide an English letter: ");
                }
                else {
                    print("\t\t\t\t\t\t\tPlease provide an different letter: ");
                }
                chomp($userinput = uc(prompt '', -1));
                print("\n");
            }
            my $original_color = ((first_index { $_ eq $userinput } @alphabet)+1)*10;
            push(@secret_alphabet, "$userinput");
            if ($original_color != 260){
                push(@colors, $original_color);
            }
            else {
                push(@colors, 255);
            }
        }
    }
}
if ($options{h})
{
  print_help();
}

prompt_for_subst;
print_dict;
chomp(my $message = prompt "Type you secret: ",);
my @message_array = split '',$message;
my $secret_array = "";
for my $letter (@message_array) {
    if (grep { $_ eq uc($letter)} @alphabet) {
        if ($letter eq uc($letter)){
            $secret_array.= @secret_alphabet[first_index { $_ eq $letter } @alphabet];
        }
        else {
            $secret_array.= lc(@secret_alphabet[first_index { $_ eq uc($letter) } @alphabet]);
        }
    }
    else
    {
        $secret_array.= $letter;
    }
}
print "Cipher-text:     $secret_array\n";
