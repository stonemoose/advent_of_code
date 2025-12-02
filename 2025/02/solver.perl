#!/usr/bin/perl

@lines = <>;

@ranges = (@lines[0] =~ /(\d+)-(\d+)/g);

$part1 = 0;
$part2 = 0;
$range = @lines[0];
while ($range =~ /(\d+)-(\d+)/g) {
    foreach $id ($1...$2) {
        $part1 = $part1 + $id if ($id =~ /^(\d+)\g1$/);
    }
    foreach $id ($1...$2) {
        $part2 = $part2 + $id if ($id =~ /^(\d+)\g1+$/);
    }
}
print "Part 1: $part1\n";
print "Part 2: $part2\n";
