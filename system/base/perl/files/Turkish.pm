package Turkish;

require Exporter;

@ISA = (Exporter);
@EXPORT = qw(uc lc);

use vars qw($VERSION);
$VERSION = '0.1';

use strict;
use warnings;
use utf8;

sub uc
{
    binmode STDOUT, ':utf8';
    my $result;
    foreach my $char (split(//,$_[0]))
    {
        if ($char eq 'i')
        {
            $result = $result.'İ';
        }
        elsif ($char eq 'ı')
        {
            $result = $result.'I';
        }
        else
        {
            $result = $result.uc($char);
        }
    }

    return $result;
}

sub lc
{
    binmode STDOUT, ':utf8';
    my $result;
    foreach my $char (split(//,$_[0]))
    {
        if ($char eq 'İ')
        {
            $result = $result.'i';
        }
        elsif ($char eq 'I')
        {
            $result = $result.'ı';
        }
        else
        {
            $result = $result.lc($char);
        }
    }

    return $result;
}

1;
__END__
