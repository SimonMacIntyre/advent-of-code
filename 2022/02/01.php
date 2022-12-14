<?php

function test()
{
    $result = scoreFromData(normalizeData(parseData('02/test-input.txt')));
    assert(15 === $result);
}

function real()
{
    echo scoreFromData(normalizeData(parseData('02/input.txt')));
}

function parseData(string $file): array
{
    $rounds = [];
    $handle = fopen($file, 'rb');
    while (($line = fgets($handle)) !== false) {
        $line = str_replace(' ', '', trim($line));
        $rounds[] = [
            'opponent' => substr($line, 0, 1),
            'me'       => substr($line, 1, 1),
        ];
    }
    fclose($handle);

    return $rounds;
}

function normalizeData(array $rounds): array
{
    foreach ($rounds as &$round) {
        $round['me'] = match ($round['me']) {
            'X' => 'A',
            'Y' => 'B',
            'Z' => 'C'
        };
    }
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
    //selection score
    $score = match ($round['me']) {
        'A' => 1,
        'B' => 2,
        'C' => 3,
    };

    //result score
    $score += match (true) {
        //draw
        ($round['opponent'] === $round['me']) => 3,

        //win
        ($round['opponent'] === 'A' && $round['me'] === 'B'),
        ($round['opponent'] === 'B' && $round['me'] === 'C'),
        ($round['opponent'] === 'C' && $round['me'] === 'A') => 6,

        //loss
        ($round['opponent'] === 'A' && $round['me'] === 'C'),
        ($round['opponent'] === 'B' && $round['me'] === 'A'),
        ($round['opponent'] === 'C' && $round['me'] === 'B') => 0,
    };

    return $score;
}


test();
real();
