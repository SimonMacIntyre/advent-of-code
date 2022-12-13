<?php

function sumEachElfCalories(array $elves): array
{
    foreach ($elves as &$elf) {
        $elf = array_sum($elf);
    }

    return $elves;
}

function sumTopThreeElves(array $elves): int
{
    rsort($elves);

    return $elves[0] + $elves[1] + $elves[2];
}


//turn file input into an array of elves[calories[]]
function process(string $file): array
{
    $handle = fopen($file, 'rb');
    if ($handle) {
        $elves = [];
        while (($line = fgets($handle)) !== false) {
            $line = trim($line);
            if ($line) {
                echo $line . "\n";
                $elf[] = $line;
            } else {
                echo $line . "\n";
                $elves[] = $elf;
                unset($elf);
            }
        }
        $elves[] = $elf;
        fclose($handle);

        return $elves;
    } else {
        throw new \http\Exception\RuntimeException('no file derp');
    }
}


function test(): void
{
    $result = sumTopThreeElves(
        sumEachElfCalories(
            process('01/test-input.txt')
        )
    );
    assert(45000 === $result);
}

function real(): void
{
    echo sumTopThreeElves(
        sumEachElfCalories(
            process('01/input.txt')
        )
    );
}

test();
real();
