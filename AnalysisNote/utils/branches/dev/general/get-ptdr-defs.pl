#!/usr/bin/env perl

#############################################################################
#
# Perl script to format the definitions in ptdr-definitions.tex
#
# For help, type:
#
#     >  get-ptdr-defs --help
#
#  Created:     George Alverson     10 May 2007
#  Revised:
#
#############################################################################

use strict;
use Getopt::Long qw(:config require_order); # the require order means that for

my $help = '';
my $verbose = '';
GetOptions ('verbose!'    => \$verbose,    # negatable: --noverbose, turn on TeX screen output
            'help|?'      => \$help,       # echo basic operations and options
            );

#############################################################################
# Main:
#############################################################################

#############################################################################
# Main:
#############################################################################

if ($help || $ARGV[0] eq "help")
{
   &print_usage();
   exit;
}

   my $defs = "ptdr-definitions.sty";
   if (@ARGV == 1) 
   { 
       $defs = $ARGV[0];
   }

   open(FILE, $defs) || die("can't open $defs file: $!");
   while (<FILE>)
   {
#      this should pull the all the commands _except_ those which take arguments
       if (/^\\(newcommand|providecommand|DeclareRobustCommand)\s*\{\\(\w+)\}\s*\{(.+)\}/)
       {
           print "\\symexamp{$2}{\\$2}\n";
       }    
       elsif (/^\\(newcommand|providecommand|DeclareRobustCommand)\s*\{\\(\w+)\}\[1\]\s*\{(.+)\}/) #one arg only
       {
           print "\\symexamp{$2\\\{x\\\}}{\\$2\{x\}}\n";
       }

   }
#############################################################################
sub print_usage {
    print "******************************************************************************\n";
    print "*                                                                            *\n";
    print "* Pulls the definitions from ptdr-definitions and formats for inclusion      *\n";
    print "* the example.tex example note.                                              *\n";
    print "*                                                                            *\n";
    print "* Expects to find the defs in ../general for comptibility with the tdr       *\n";
    print "* script. For execution inside TeX, the -shell-escape flag must be set      *\n";
    print "* under Linux, the -write18 flag under MikTeX.                               *\n";
    print "*                                                                            *\n";
    print "*                                                                            *\n";
    print "******************************************************************************\n";
}    
