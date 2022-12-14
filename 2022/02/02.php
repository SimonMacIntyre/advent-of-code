<?php

const scoringMatrix = [
    'A' => [
        'lose' => 3,
        'win'  => 8,
        'draw' => 4
    ],
    'B' => [
        'lose' => 1,
        'win'  => 9,
        'draw' => 5
    ],
    'C' => [
        'lose' => 2,
        'win'  => 7,
        'draw' => 6
    ],
];

function test()
{
    $result = scoreFromData(parseData('02/test-input.txt'));
    assert(12 === $result);
}

function real()
{
    echo scoreFromData(parseData('02/input.txt'));
}

function parseData(string $file): array
{
    $rounds = [];
    $handle = fopen($file, 'rb');
    while (($line = fgets($handle)) !== false) {
        $line     = str_replace(' ', '', trim($line));
        $rounds[] = [
            'opponent' => substr($line, 0, 1),
            'me'       => substr($line, 1, 1),
        ];
    }
    fclose($handle);

    return $rounds;
}

function scoreFromData(array $data): int
{
    $finalScore = 0;
    foreach ($data as $round) {
        $finalScore += scoreRound($round);
    }

    return $finalScore;
}

function scoreRound(array $round): int
{
    //lose
    if ($round['me'] == 'X') {
        return scoringMatrix[$round['opponent']]['lose'];
    }

    //draw
    if ($round['me'] == 'Y') {
        return scoringMatrix[$round['opponent']]['draw'];
    }

    //win
    if ($round['me'] == 'Z') {
        return scoringMatrix[$round['opponent']]['win'];
    }

    throw new \http\Exception\RuntimeException('derp');
}

test();
real();
