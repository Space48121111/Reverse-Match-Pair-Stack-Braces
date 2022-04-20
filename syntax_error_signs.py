import statistics

txt = open('syntax_error_signs.txt', 'r')
input1 = txt.read()

input = '''\
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
'''

'''
brace matching

incompleted: add closing chars, mulitply score *= 5 += points, median

corrupted:
{([(<{}[<>[] }>{[]{[(<()>  ] -> }
[[<[([]) )<([[{}[[()]]]    ] -> )
[{[{({} ]{}}([{[{{{}}([]   ) -> ]
[<(<(<(<{} ))><([]([]()    > -> )
<{([([[(<>()){}] >(<<{{    ] -> >

syntax error:
) 3 ] 57 } 1197 > 25137

output: 2 * 3 + 57 + 1197 + 25137 = 26397
output1: 288957

algorithm:
= treat as characters
- chunks: pairs_r[i]/starting from { ), ], }, > }
    - must end/close corresponding pairs_l[j] { (, [, {, <}
    - find the corresponding position j
    - count occurrences
pseudo code:
chunk = []
n = 0
for i, val in enumerate(line):
    if char in { ), ], }, > }:
        if val[i - n] not in { (, [, {, <}:
            return corrupted
        else
            pair val[i - n] and the corresponding sign
            chunk += pair val[i - n]
            del chunk

        n++

'''

def reverse_match_braces():
    points = {
    ')' : 3,
    ']' : 57,
    '}' : 1197,
    '>' : 25137,
    }
    points1 = {
    ')' : 1,
    ']' : 2,
    '}' : 3,
    '>' : 4,
    }
    forward = {'(': ')', '{' : '}', '[' : ']', '<' : '>'}
    reverse = {v: k for k, v in forward.items()}

    total = 0
    scores = []
    for line in input.splitlines():
        stack = []
        for c in line:
            if c in forward:
                stack.append(c)
            elif c in reverse:
                # removed the matched after looking back from the stack
                if reverse[c] == stack[-1]:
                    stack.pop()
                else:
                    # not matched
                    total += points[c]
                    break
        # until after the break
        else:
            score = 0
            # all matched in the forward stack
            for s in reversed(stack):
                score *= 5
                score += points1[forward[s]]
            scores.append(score)
            # print('Scores ', scores)
    # del scores[0]
    # scores.pop(0)

    return f'{total}', f'{statistics.median(scores)}'

print(reverse_match_braces())








# end
