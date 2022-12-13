<?php

function biggest_total(array $elves): int
{
    $biggest  = 0;
    $elfTotal = 0;
    foreach ($elves as $elf) {
        foreach ($elf as $calories) {
            $elfTotal += $calories;
        }

        if ($elfTotal > $biggest) {
            $biggest = $elfTotal;
        }
        $elfTotal = 0;
    }

    return $biggest;
}

function process(string $file): int
{
    $handle = fopen($file, 'rb');
    if ($handle) {
        $elves = [];
        while (($line = fgets($handle)) !== false) {
            $line = trim($line);
            if ($line) {
                $elf[] = $line;
            } else {
                $elves[] = $elf;
                unset($elf);
            }
        }
        fclose($handle);

        return biggest_total($elves);
    } else {
        throw new \http\Exception\RuntimeException('no file derp');
    }
}


function test()
{
    $result = process('01/test-input.txt');
    assert(24000 === $result);
}

function real()
{
    echo process('01/input.txt');
}

test();
real();
