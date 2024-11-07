import os
from baseball_scorecard.baseball_scorecard import Scorecard

# TB @ BOS, 2013-04-13
# https://www.baseball-reference.com/boxes/BOS/BOS201304130.shtml
# https://www.mlb.com/gameday/rays-vs-red-sox/2013/04/13/346907/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-04-13 13:07-16:30",
        "at": "Fenway Park, Boston, MA",
        "att": "33,039",
        "temp": "45F, Cloudy",
        "wind": "7mph, Out To RF",
        "away": {
            "team": "Tampa Bay Rays",
            "starter": 14,
            "roster": {
                # Lineup
                8: "Desmond Jennings",
                1: "Sean Rodríguez",
                3: "Evan Longoria",
                18: "Ben Zobrist",
                15: "Shelley Duncan",
                11: "Yunel Escobar",
                19: "Ryan Roberts",
                28: "José Molina",
                20: "Matt Joyce",
                # Starting pitcher
                14: "David Price",
                # Bench
                21: "James Loney",
                59: "Jose Lobaton",
                5: "Sam Fuld",
                2: "Kelly Johnson",
                # Bullpen
                58: "Jeremy Hellickson",
                53: "Alex Cobb",
                47: "Brandon Gomes",
                55: "Matt Moore",
                62: "Joel Peralta",
                35: "Jamey Wright",
                43: "Kyle Farnsworth",
                57: "Jake McGee",
                27: "Cesár Ramos",
                56: "Fernando Rodney",
                40: "Roberto Hernandez",
            },
            "lefties": [14, 55, 57, 27],
            "lineup": [
                [8, "8"],
                [1, "3"],
                [3, "5"],
                [18, "9"],
                [15, "0"],
                [11, "6"],
                [19, "4"],
                [28, "2"],
                [20, "7"],
            ],
            "bench": [
                [21, "1B"],
                [59, "C"],
                [5, "LF"],
                [2, "2B"],
            ],
            "bullpen": [58, 53, 47, 55, 62, 35, 43, 57, 27, 56, 40],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 31,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                12: "Mike Napoli",
                16: "Will Middlebrooks",
                29: "Daniel Nava",
                5: "Jonny Gomes",
                7: "Stephen Drew",
                3: "David Ross",
                # Starting pitcher
                31: "Jon Lester",
                # Bench
                39: "Jarrod Saltalamacchia",
                37: "Mike Carp",
                23: "Pedro Ciriaco",
                44: "Jackie Bradley Jr.",
                # Bullpen
                63: "Alex Wilson",
                40: "Andrew Bailey",
                30: "Andrew Miller",
                91: "Alfredo Aceves",
                52: "Joel Hanrahan",
                59: "Clayton Mortensen",
                36: "Junichi Tazawa",
                11: "Clay Buchholz",
                19: "Koji Uehara",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [31, 30, 22],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [12, "3"],
                [16, "5"],
                [29, "7"],
                [5, "0"],
                [7, "6"],
                [3, "2"],
            ],
            "bench": [
                [39, "C"],
                [37, "1B"],
                [23, "3B"],
                [44, "CF"],
            ],
            "bullpen": [63, 40, 30, 91, 52, 59, 36, 11, 19, 22, 46],
        },
        "umpires": {
            "HP": "Doug Eddings",
            "1B": "John Tumpane",
            "2B": "Dana DeMuth",
            "3B": "Angel Hernandez",
        },
    },
)

##########################################################
# PLAY BALL!
##########################################################


##########################################################
# 1st Inning
##########################################################
# Top 1st
# Pitching: BOS #31 Jon Lester
t1 = game.new_inning()

# 1. TBR #8  Desmond Jennings (X - X - X)
t1.new_ab()
t1.pitch_list("b b c f f")
t1.out("L5-6")

# 2. TBR #1  Sean Rodríguez (X - X - X)
t1.new_ab()
t1.pitch_list("s b c b b b")
t1.reach("BB")
t1.advance(2, "3 SB")

# 3. TBR #3  Evan Longoria (X - X - 1)
t1.new_ab()
t1.pitch_list("c f b b d c")
t1.out("!K")

# 4. TBR #18 Ben Zobrist (X - 1 - X)
t1.new_ab(is_risp=True)
t1.pitch_list("b")
t1.out("F8")


# Bot 1st
# Pitching: TBR #14 David Price
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("b f b c b")
b1.out("(F)L5")

# 2. BOS #18 Shane Victorino (X - X - X)
b1.new_ab()
b1.pitch_list("b c b f c")
b1.out("!K")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b1.new_ab()
b1.pitch_list("b b c b s b")
b1.reach("BB")

# 4. BOS #12 Mike Napoli (X - X - 15)
b1.new_ab()
b1.pitch_list("c s b 1 b c")
b1.out("!K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #31 Jon Lester
t2 = game.new_inning()

# 5. TBR #15 Shelley Duncan (X - X - X)
t2.new_ab()
t2.pitch_list("f")
t2.out("F7")

# 6. TBR #11 Yunel Escobar (X - X - X)
t2.new_ab()
t2.pitch_list("c b c f c")
t2.out("!K")

# 7. TBR #19 Ryan Roberts (X - X - X)
t2.new_ab()
t2.pitch_list("c")
t2.hit(1)
t2.advance(2, "28 1B")

# 8. TBR #28 José Molina (X - X - 19)
t2.new_ab()
t2.pitch_list("1 c b c")
t2.hit(1)

# 9. TBR #20 Matt Joyce (X - 19 - 28)
t2.new_ab(is_risp=True)
t2.pitch_list("c")
t2.out("G1-3")


# Bot 2nd
# Pitching: TBR #14 David Price
b2 = game.new_inning()

# 5. BOS #16 Will Middlebrooks (X - X - X)
b2.new_ab()
b2.pitch_list("c b")
b2.out("G1-3")

# 6. BOS #29 Daniel Nava (X - X - X)
b2.new_ab()
b2.pitch_list("c b c f")
b2.out("G6-3")

# 7. BOS #5  Jonny Gomes (X - X - X)
b2.new_ab()
b2.pitch_list("c b f b b b")
b2.reach("BB")

# 8. BOS #7  Stephen Drew (X - X - 5)
b2.new_ab()
b2.pitch_list("b")
b2.out("F9")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #31 Jon Lester
t3 = game.new_inning()

# 1. TBR #8  Desmond Jennings (X - X - X)
t3.new_ab()
t3.pitch_list("c c b b f")
t3.hit(1)
t3.advance(4, "1 2B")

# 2. TBR #1  Sean Rodríguez (X - X - 8)
t3.new_ab()
t3.pitch_list("f")
t3.hit(2, rbis=1)
t3.advance(3, "3 WP")

# 3. TBR #3  Evan Longoria (X - 1 - X)
t3.new_ab(is_risp=True)
t3.pitch_list("f b c b b s")
t3.wp()
t3.out("K")

# 4. TBR #18 Ben Zobrist (1 - X - X)
t3.new_ab(is_risp=True)
t3.pitch_list("c f b b")
t3.out("L3")

# 5. TBR #15 Shelley Duncan (1 - X - X)
t3.new_ab(is_risp=True)
t3.pitch_list("b")
t3.out("G5-3")


# Bot 3rd
# Pitching: TBR #14 David Price
b3 = game.new_inning()

# 9. BOS #3  David Ross (X - X - X)
b3.new_ab()
b3.pitch_list("f s b")
b3.out("F7")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b3.new_ab()
b3.pitch_list("f c b b c")
b3.out("!K")

# 2. BOS #18 Shane Victorino (X - X - X)
b3.new_ab()
b3.pitch_list("c f")
b3.hit(1)
b3.advance(2, "15 SB")

# 3. BOS #15 Dustin Pedroia (X - X - 18)
b3.new_ab(is_risp=True)
b3.pitch_list("f f 1 1 1 1 b b s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #31 Jon Lester
t4 = game.new_inning()

# 6. TBR #11 Yunel Escobar (X - X - X)
t4.new_ab()
t4.pitch_list("f c b")
t4.out("L8")

# 7. TBR #19 Ryan Roberts (X - X - X)
t4.new_ab()
t4.pitch_list("c s b b b")
t4.out("F9")

# 8. TBR #28 José Molina (X - X - X)
t4.new_ab()
t4.out("G4-3")


# Bot 4th
# Pitching: TBR #14 David Price
b4 = game.new_inning()

# 4. BOS #12 Mike Napoli (X - X - X)
b4.new_ab()
b4.out("F8")

# 5. BOS #16 Will Middlebrooks (X - X - X)
b4.new_ab()
b4.pitch_list("b s b c f f s")
b4.out("K")

# 6. BOS #29 Daniel Nava (X - X - X)
b4.new_ab()
b4.pitch_list("b c c s")
b4.out("K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #31 Jon Lester
t5 = game.new_inning()

# 9. TBR #20 Matt Joyce (X - X - X)
t5.new_ab()
t5.pitch_list("b c c c")
t5.out("!K")

# 1. TBR #8  Desmond Jennings (X - X - X)
t5.new_ab()
t5.pitch_list("b b c c b")
t5.out("P4")

# 2. TBR #1  Sean Rodríguez (X - X - X)
t5.new_ab()
t5.pitch_list("b c b s b f s")
t5.out("K")


# Bot 5th
# Pitching: TBR #14 David Price
b5 = game.new_inning()

# 7. BOS #5  Jonny Gomes (X - X - X)
b5.new_ab()
b5.pitch_list("c f b b b")
b5.out("P3")

# 8. BOS #7  Stephen Drew (X - X - X)
b5.new_ab()
b5.pitch_list("b c c c")
b5.out("!K")

# 9. BOS #3  David Ross (X - X - X)
b5.new_ab()
b5.pitch_list("f b b f f b")
b5.hit(4)

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b5.new_ab()
b5.pitch_list("c f f b f f")
b5.out("G3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #31 Jon Lester
t6 = game.new_inning()

# 3. TBR #3  Evan Longoria (X - X - X)
t6.new_ab()
t6.pitch_list("b")
t6.out("G5-3")

# 4. TBR #18 Ben Zobrist (X - X - X)
t6.new_ab()
t6.pitch_list("b c")
t6.out("G6-3")

# 5. TBR #15 Shelley Duncan (X - X - X)
t6.new_ab()
t6.pitch_list("b s b")
t6.out("G5-3")


# Bot 6th
# Pitching: TBR #14 David Price
b6 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
b6.new_ab()
b6.pitch_list("c b")
b6.out("G1-3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b6.new_ab()
b6.pitch_list("c s c")
b6.out("!K")

# 4. BOS #12 Mike Napoli (X - X - X)
b6.new_ab()
b6.pitch_list("c")
b6.hit(1)
b6.advance(2, "16 1B")

# 5. BOS #16 Will Middlebrooks (X - X - 12)
b6.new_ab()
b6.pitch_list("f b f b 1")
b6.hit(1)

# 6. BOS #29 Daniel Nava (X - 12 - 16)
b6.new_ab(is_risp=True)
b6.pitch_list("f")
b6.out("F8")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #31 Jon Lester
t7 = game.new_inning()

# 6. TBR #11 Yunel Escobar (X - X - X)
t7.new_ab()
t7.pitch_list("c b")
t7.hit(1)
t7.thrown_out(2, "19 DP4-6-3", 1, 31)

# 7. TBR #19 Ryan Roberts (X - X - 11)
t7.new_ab()
t7.pitch_list("l b")
t7.out("DP4-6-3")

# 8. TBR #28 José Molina (X - X - X)
t7.new_ab()
t7.out("G5-3")


# Bot 7th
# Pitching: TBR #57 Jake McGee
b7 = game.new_inning()

# Pitching change (TBR): #57 Jake McGee replaces #14 David Price
b7.pitching_substitution(57)

# 7. BOS #5  Jonny Gomes (X - X - X)
b7.new_ab()
b7.pitch_list("f s b s")
b7.out("K")

# 8. BOS #7  Stephen Drew (X - X - X)
b7.new_ab()
b7.pitch_list("f s f f b")
b7.out("F7")

# 9. BOS #3  David Ross (X - X - X)
b7.new_ab()
b7.pitch_list("f c s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #40 Andrew Bailey
t8 = game.new_inning()

# Pitching change (BOS): #40 Andrew Bailey replaces #31 Jon Lester
t8.pitching_substitution(40)

# 9. TBR #20 Matt Joyce (X - X - X)
t8.new_ab()
t8.pitch_list("c b")
t8.out("F9")

# 1. TBR #8  Desmond Jennings (X - X - X)
t8.new_ab()
t8.pitch_list("b f b c s")
t8.out("K")

# Offensive change (TBR): Pinch-hitter #5 Sam Fuld replaces #1 Sean Rodríguez, batting 2nd
t8.offensive_substitution(2, 5, "PH")

# 2. TBR #5  Sam Fuld (X - X - X)
t8.new_ab()
t8.pitch_list("c b b")
t8.out("(F)P2")


# Bot 8th
# Pitching: TBR #62 Joel Peralta
b8 = game.new_inning()

# Pitching change (TBR): #62 Joel Peralta replaces #57 Jake McGee
b8.pitching_substitution(62)

# Defensive switch (TBR): #5 Sam Fuld moves to RF
b8.defensive_switch(5, "9")

# Defensive switch (TBR): #18 Ben Zobrist moves to 2B
b8.defensive_switch(18, "4")

# Defensive switch (TBR): #19 Ryan Roberts moves to 1B
b8.defensive_switch(19, "3")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b8.new_ab()
b8.pitch_list("c s b")
b8.out("F8")

# 2. BOS #18 Shane Victorino (X - X - X)
b8.new_ab()
b8.pitch_list("b b c f s")
b8.out("K")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b8.new_ab()
b8.pitch_list("t")
b8.out("G3-1")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #52 Joel Hanrahan
t9 = game.new_inning()

# Pitching change (BOS): #52 Joel Hanrahan replaces #40 Andrew Bailey
t9.pitching_substitution(52)

# 3. TBR #3  Evan Longoria (X - X - X)
t9.new_ab()
t9.pitch_list("b b b b")
t9.reach("BB")
t9.advance(2, "18 BB")

# 4. TBR #18 Ben Zobrist (X - X - 3)
t9.new_ab()
t9.pitch_list("b c d 1 1 s f f b b")
t9.reach("BB")

# Pitching change (BOS): #19 Koji Uehara replaces #52 Joel Hanrahan
t9.pitching_substitution(19)

# Offensive change (TBR): Pinch-hitter #21 James Loney replaces #15 Shelley Duncan, batting 5th
t9.offensive_substitution(5, 21, "PH")

# 5. TBR #21 James Loney (X - 3 - 18)
t9.new_ab(is_risp=True)
t9.pitch_list("c b s c")
t9.out("!K")

# 6. TBR #11 Yunel Escobar (X - 3 - 18)
t9.new_ab(is_risp=True)
t9.pitch_list("c")
t9.out("F9")

# 7. TBR #19 Ryan Roberts (X - 3 - 18)
t9.new_ab(is_risp=True)
t9.pitch_list("f b")
t9.out("P4")


# Bot 9th
# Pitching: TBR #43 Kyle Farnsworth
b9 = game.new_inning()

# Pitching change (TBR): #43 Kyle Farnsworth replaces #62 Joel Peralta
b9.pitching_substitution(43)

# Defensive switch (TBR): #21 James Loney moves to DH
b9.defensive_switch(21, "0")

# 4. BOS #12 Mike Napoli (X - X - X)
b9.new_ab()
b9.pitch_list("b f")
b9.out("G6-3")

# 5. BOS #16 Will Middlebrooks (X - X - X)
b9.new_ab()
b9.out("L9")

# Pitching change (TBR): #27 Cesár Ramos replaces #43 Kyle Farnsworth
b9.pitching_substitution(27)

# 6. BOS #29 Daniel Nava (X - X - X)
b9.new_ab()
b9.pitch_list("b")
b9.hit(1)
b9.advance(2, "5 WP")

# Pitching change (TBR): #47 Brandon Gomes replaces #27 Cesár Ramos
b9.pitching_substitution(47)

# 7. BOS #5  Jonny Gomes (X - X - 29)
b9.new_ab(is_risp=True)
b9.pitch_list("s b c b b b")
b9.wp()
b9.reach("BB")

# 8. BOS #7  Stephen Drew (X - 29 - 5)
b9.new_ab(is_risp=True)
b9.pitch_list("b c b f")
b9.out("L8")


##########################################################
# 10th Inning
##########################################################
# Top 10th
# Pitching: BOS #36 Junichi Tazawa
t10 = game.new_inning()

# Pitching change (BOS): #36 Junichi Tazawa replaces #19 Koji Uehara
t10.pitching_substitution(36)

# 8. TBR #28 José Molina (X - X - X)
t10.new_ab()
t10.pitch_list("f")
t10.hit(2)
# Offensive change (TBR): Pinch-runner #2 Kelly Johnson replaces #28 José Molina
t10.offensive_substitution(8, 2, "PR")
t10.atbase("PR")

# 9. TBR #20 Matt Joyce (X - 28 - X)
t10.new_ab(is_risp=True)
t10.out("L7")

# 1. TBR #8  Desmond Jennings (X - 2 - X)
t10.new_ab(is_risp=True)
t10.pitch_list("c f")
t10.out("P4")

# 2. TBR #5  Sam Fuld (X - 2 - X)
t10.new_ab(is_risp=True)
t10.pitch_list("b d b c")
t10.out("G3")


# Bot 10th
# Pitching: TBR #47 Brandon Gomes
b10 = game.new_inning()

# Defensive change (TBR): #59 Jose Lobaton replaces #2 Kelly Johnson (PR), playing C, batting 8th
b10.defensive_substitution(8, 59, "2")

# Offensive change (BOS): Pinch-hitter #39 Jarrod Saltalamacchia replaces #3 David Ross, batting 9th
b10.offensive_substitution(9, 39, "PH")

# 9. BOS #39 Jarrod Saltalamacchia (X - X - X)
b10.new_ab()
b10.pitch_list("b c s b c")
b10.out("!K")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b10.new_ab()
b10.pitch_list("s b")
b10.hit(1)
b10.error(2)
b10.advance(2, "18 SB")
b10.advance(3, "18 E2")
b10.advance("U", "18 1B")

# 2. BOS #18 Shane Victorino (X - X - 2)
b10.new_ab(is_risp=True)
b10.pitch_list("c b b c")
b10.hit(1, rbis=1)

# Winning team: BOS
# WP: BOS #36 Junichi Tazawa
game.winning_pitcher(36)

# Loser team: TBR
# LP: TBR #47 Brandon Gomes
game.losing_pitcher(47, is_away_team=True)

# print(game)
game.generate_scorecard()
