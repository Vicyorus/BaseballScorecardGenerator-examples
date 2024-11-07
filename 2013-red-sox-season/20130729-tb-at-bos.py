import os
from baseball_scorecard.baseball_scorecard import Scorecard

# TB @ BOS, 2013-07-29
# https://www.baseball-reference.com/boxes/BOS/BOS201307290.shtml
# https://www.mlb.com/gameday/rays-vs-red-sox/2013/07/29/348268/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-07-29 18:13-22:13 (0:39 delay)",
        "at": "Fenway Park, Boston, MA",
        "att": "37,242",
        "temp": "75F, Partly Cloudy",
        "wind": "9mph, R To L",
        "away": {
            "team": "Tampa Bay Rays",
            "starter": 14,
            "roster": {
                # Lineup
                8: "Desmond Jennings",
                3: "Evan Longoria",
                18: "Ben Zobrist",
                9: "Wil Myers",
                30: "Luke Scott",
                11: "Yunel Escobar",
                21: "James Loney",
                28: "José Molina",
                1: "Sean Rodríguez",
                # Starting pitcher
                14: "David Price",
                # Bench
                20: "Matt Joyce",
                59: "Jose Lobaton",
                5: "Sam Fuld",
                2: "Kelly Johnson",
                # Bullpen
                58: "Jeremy Hellickson",
                57: "Jake McGee",
                54: "Alex Torres",
                27: "Cesár Ramos",
                56: "Fernando Rodney",
                62: "Joel Peralta",
                35: "Jamey Wright",
                22: "Chris Archer",
                40: "Roberto Hernandez",
                43: "Kyle Farnsworth",
            },
            "lefties": [14, 57, 54, 27],
            "lineup": [
                [8, "8"],
                [3, "5"],
                [18, "4"],
                [9, "9"],
                [30, "0"],
                [11, "6"],
                [21, "3"],
                [28, "2"],
                [1, "7"],
            ],
            "bench": [
                [20, "RF"],
                [59, "C"],
                [5, "LF"],
                [2, "2B"],
            ],
            "bullpen": [58, 57, 54, 27, 56, 62, 35, 22, 40, 43],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 22,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                5: "Jonny Gomes",
                20: "Ryan Lavarnway",
                7: "Stephen Drew",
                23: "Brandon Snyder",
                # Starting pitcher
                22: "Felix Doubront",
                # Bench
                39: "Jarrod Saltalamacchia",
                37: "Mike Carp",
                29: "Daniel Nava",
                10: "Jose Iglesias",
                # Bullpen
                65: "Jose De La Torre",
                41: "John Lackey",
                67: "Brandon Workman",
                32: "Craig Breslow",
                66: "Drake Britton",
                31: "Jon Lester",
                36: "Junichi Tazawa",
                19: "Koji Uehara",
                38: "Matt Thornton",
                54: "Pedro Beato",
                46: "Ryan Dempster",
            },
            "lefties": [22, 32, 66, 31, 38],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [5, "7"],
                [20, "2"],
                [7, "6"],
                [23, "5"],
            ],
            "bench": [
                [39, "C"],
                [37, "1B"],
                [29, "LF"],
                [10, "2B"],
            ],
            "bullpen": [65, 41, 67, 32, 66, 31, 36, 19, 38, 54, 46],
        },
        "umpires": {
            "HP": "Jerry Meals",
            "1B": "Chris Conroy",
            "2B": "Gary Darling",
            "3B": "David Rackley",
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
# Pitching: BOS #22 Felix Doubront
t1 = game.new_inning()

# 1. TBR #8  Desmond Jennings (X - X - X)
t1.new_ab()
t1.pitch_list("b")
t1.out("G4-3")

# 2. TBR #3  Evan Longoria (X - X - X)
t1.new_ab()
t1.pitch_list("c")
t1.hit(1)
t1.advance(3, "9 1B")

# 3. TBR #18 Ben Zobrist (X - X - 3)
t1.new_ab()
t1.pitch_list("f f c")
t1.out("!K")

# 4. TBR #9  Wil Myers (X - X - 3)
t1.new_ab()
t1.pitch_list("b s f b b")
t1.hit(1)

# 5. TBR #30 Luke Scott (3 - X - 9)
t1.new_ab(is_risp=True)
t1.pitch_list("s c s")
t1.out("K")


# Bot 1st
# Pitching: TBR #14 David Price
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("c f")
b1.out("G4-3")

# 2. BOS #18 Shane Victorino (X - X - X)
b1.new_ab()
b1.pitch_list("c")
b1.out("G5-3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b1.new_ab()
b1.pitch_list("c")
b1.out("G4-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #22 Felix Doubront
t2 = game.new_inning()

# 6. TBR #11 Yunel Escobar (X - X - X)
t2.new_ab()
t2.pitch_list("c b b t b f f")
t2.hit(1)
t2.thrown_out(2, "21 DP6-3", 1, 22)

# 7. TBR #21 James Loney (X - X - 11)
t2.new_ab()
t2.out("DP6-3")

# 8. TBR #28 José Molina (X - X - X)
t2.new_ab()
t2.pitch_list("b b b c b")
t2.reach("BB")
t2.thrown_out(2, "1 FC6-4", 3, 22)

# 9. TBR #1  Sean Rodríguez (X - X - 28)
t2.new_ab()
t2.pitch_list("b s")
t2.reach("FC6-4")


# Bot 2nd
# Pitching: TBR #14 David Price
b2 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
b2.new_ab()
b2.hit(2)

# 5. BOS #12 Mike Napoli (X - 34 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("t f b b f")
b2.out("G6-3")

# 6. BOS #5  Jonny Gomes (X - 34 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("b c")
b2.out("F8")

# 7. BOS #20 Ryan Lavarnway (X - 34 - X)
b2.new_ab(is_risp=True)
b2.out("G5-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #22 Felix Doubront
t3 = game.new_inning()

# 1. TBR #8  Desmond Jennings (X - X - X)
t3.new_ab()
t3.pitch_list("b b b b")
t3.reach("BB")
t3.advance(2, "18 BB")

# 2. TBR #3  Evan Longoria (X - X - 8)
t3.new_ab()
t3.pitch_list("b 1 c b c f s")
t3.out("K")

# 3. TBR #18 Ben Zobrist (X - X - 8)
t3.new_ab()
t3.pitch_list("1 1 d b b c d")
t3.reach("BB")
t3.thrown_out(2, "9 DP5-4-3", 2, 22)

# 4. TBR #9  Wil Myers (X - 8 - 18)
t3.new_ab(is_risp=True)
t3.pitch_list("b s s 2")
t3.out("DP5-4-3")


# Bot 3rd
# Pitching: TBR #14 David Price
b3 = game.new_inning()

# 8. BOS #7  Stephen Drew (X - X - X)
b3.new_ab()
b3.pitch_list("f c c")
b3.out("!K")

# 9. BOS #23 Brandon Snyder (X - X - X)
b3.new_ab()
b3.pitch_list("c c b f")
b3.out("G5-3")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b3.new_ab()
b3.pitch_list("b")
b3.out("G4-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #22 Felix Doubront
t4 = game.new_inning()

# 5. TBR #30 Luke Scott (X - X - X)
t4.new_ab()
t4.pitch_list("b s b b f f s")
t4.out("K")

# 6. TBR #11 Yunel Escobar (X - X - X)
t4.new_ab()
t4.pitch_list("b b f f")
t4.hit(1)
t4.advance(3, "28 1B")
t4.advance(4, "1 2B")

# 7. TBR #21 James Loney (X - X - 11)
t4.new_ab()
t4.pitch_list("d")
t4.out("F9")

# 8. TBR #28 José Molina (X - X - 11)
t4.new_ab()
t4.pitch_list("d f b b 1 c")
t4.hit(1)
t4.advance(3, "1 2B")

# 9. TBR #1  Sean Rodríguez (11 - X - 28)
t4.new_ab(is_risp=True)
t4.pitch_list("b c")
t4.hit(2, rbis=1)

# 1. TBR #8  Desmond Jennings (28 - 1 - X)
t4.new_ab(is_risp=True)
t4.pitch_list("b b s b c")
t4.out("L9")


# Bot 4th
# Pitching: TBR #14 David Price
b4 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
b4.new_ab()
b4.pitch_list("c b")
b4.out("(F)P2")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b4.new_ab()
b4.pitch_list("c b c f b b f s")
b4.out("K")

# 4. BOS #34 David Ortiz (X - X - X)
b4.new_ab()
b4.out("L3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #22 Felix Doubront
t5 = game.new_inning()

# 2. TBR #3  Evan Longoria (X - X - X)
t5.new_ab()
t5.pitch_list("b c b")
t5.hit(2)
t5.advance(3, "18 1B")
t5.advance(4, "9 FC6-4")

# 3. TBR #18 Ben Zobrist (X - 3 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("c f d")
t5.hit(1)
t5.thrown_out(2, "9 FC6-4", 1, 22)

# 4. TBR #9  Wil Myers (3 - X - 18)
t5.new_ab(is_risp=True)
t5.pitch_list("f c f 1 d d")
t5.reach("FC6-4", rbis=1)
t5.advance(2, "30 B1-3")
t5.advance(3, "11 SB")

# 5. TBR #30 Luke Scott (X - X - 9)
t5.new_ab()
t5.out("B1-3")

# 6. TBR #11 Yunel Escobar (X - 9 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("b b b")
t5.reach("HBP")

# 7. TBR #21 James Loney (9 - X - 11)
t5.new_ab(is_risp=True)
t5.pitch_list("l d b")
t5.out("L9")


# Bot 5th
# Pitching: TBR #14 David Price
b5 = game.new_inning()

# 5. BOS #12 Mike Napoli (X - X - X)
b5.new_ab()
b5.pitch_list("c s s")
b5.out("K")

# 6. BOS #5  Jonny Gomes (X - X - X)
b5.new_ab()
b5.pitch_list("b f s b b c")
b5.out("!K")

# 7. BOS #20 Ryan Lavarnway (X - X - X)
b5.new_ab()
b5.pitch_list("b b f c f c")
b5.out("!K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #65 Jose De La Torre
t6 = game.new_inning()

# Pitching change (BOS): #65 Jose De La Torre replaces #22 Felix Doubront
t6.pitching_substitution(65)

# 8. TBR #28 José Molina (X - X - X)
t6.new_ab()
t6.pitch_list("c b b b f f b")
t6.reach("BB")
t6.advance(2, "20 1B")

# Offensive change (TBR): Pinch-hitter #20 Matt Joyce replaces #1 Sean Rodríguez, batting 9th
t6.offensive_substitution(9, 20, "PH")

# 9. TBR #20 Matt Joyce (X - X - 28)
t6.new_ab()
t6.pitch_list("c b b f b")
t6.hit(1)

# 1. TBR #8  Desmond Jennings (X - 28 - 20)
t6.new_ab(is_risp=True)
t6.pitch_list("b s f s")
t6.out("K")

# 2. TBR #3  Evan Longoria (X - 28 - 20)
t6.new_ab(is_risp=True)
t6.pitch_list("c f f b f s")
t6.out("K")

# 3. TBR #18 Ben Zobrist (X - 28 - 20)
t6.new_ab(is_risp=True)
t6.pitch_list("b b c f c")
t6.out("!K")


# Bot 6th
# Pitching: TBR #14 David Price
b6 = game.new_inning()

# Defensive switch (TBR): #20 Matt Joyce moves to LF
b6.defensive_switch(20, "7")

# 8. BOS #7  Stephen Drew (X - X - X)
b6.new_ab()
b6.pitch_list("b c f b f c")
b6.out("!K")

# 9. BOS #23 Brandon Snyder (X - X - X)
b6.new_ab()
b6.pitch_list("b s f")
b6.hit(4)

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b6.new_ab()
b6.pitch_list("b f c f")
b6.out("G5-3")

# 2. BOS #18 Shane Victorino (X - X - X)
b6.new_ab()
b6.pitch_list("c")
b6.out("F8")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #65 Jose De La Torre
t7 = game.new_inning()

# 4. TBR #9  Wil Myers (X - X - X)
t7.new_ab()
t7.pitch_list("b b b b")
t7.reach("BB")
t7.thrown_out(2, "11 DP5-4-3", 2, 66)

# Pitching change (BOS): #66 Drake Britton replaces #65 Jose De La Torre
t7.pitching_substitution(66)

# 5. TBR #30 Luke Scott (X - X - 9)
t7.new_ab()
t7.pitch_list("c b")
t7.out("F9")

# 6. TBR #11 Yunel Escobar (X - X - 9)
t7.new_ab()
t7.pitch_list("b c b")
t7.out("DP5-4-3")


# Bot 7th
# Pitching: TBR #14 David Price
b7 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
b7.new_ab()
b7.pitch_list("c")
b7.out("F8")

# 4. BOS #34 David Ortiz (X - X - X)
b7.new_ab()
b7.pitch_list("c")
b7.out("F7")

# 5. BOS #12 Mike Napoli (X - X - X)
b7.new_ab()
b7.pitch_list("b c s b f s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #66 Drake Britton
t8 = game.new_inning()

# 7. TBR #21 James Loney (X - X - X)
t8.new_ab()
t8.pitch_list("b b c b")
t8.out("G4-3")

# 8. TBR #28 José Molina (X - X - X)
t8.new_ab()
t8.pitch_list("f f f s")
t8.out("K")

# 9. TBR #20 Matt Joyce (X - X - X)
t8.new_ab()
t8.pitch_list("c f b b t")
t8.out("KT")


# Bot 8th
# Pitching: TBR #14 David Price
b8 = game.new_inning()

# Defensive change (TBR): #5 Sam Fuld replaces #20 Matt Joyce (PH), playing LF, batting 9th
b8.defensive_substitution(9, 5, "7")

# 6. BOS #5  Jonny Gomes (X - X - X)
b8.new_ab()
b8.pitch_list("b b b c f f f c")
b8.out("!K")

# Pitching change (TBR): #62 Joel Peralta replaces #14 David Price
b8.pitching_substitution(62)

# 7. BOS #20 Ryan Lavarnway (X - X - X)
b8.new_ab()
b8.pitch_list("c f f f b")
b8.hit(2)
# Offensive change (BOS): Pinch-runner #29 Daniel Nava replaces #20 Ryan Lavarnway
b8.offensive_substitution(7, 29, "PR")
b8.atbase("PR")
b8.advance(3, "7 2B")
b8.thrown_out(4, "23 DP7-2", 3, 62)

# 8. BOS #7  Stephen Drew (X - 20 - X)
b8.new_ab(is_risp=True)
b8.hit(2)

# 9. BOS #23 Brandon Snyder (29 - 7 - X)
b8.new_ab(is_risp=True)
b8.pitch_list("c")
b8.out("DP7-2")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #19 Koji Uehara
t9 = game.new_inning()

# Pitching change (BOS): #19 Koji Uehara replaces #66 Drake Britton
t9.pitching_substitution(19)

# Defensive change (BOS): #39 Jarrod Saltalamacchia replaces #29 Daniel Nava (PR), playing C, batting 7th
t9.defensive_substitution(7, 39, "2")

# 1. TBR #8  Desmond Jennings (X - X - X)
t9.new_ab()
t9.out("B1-3")

# 2. TBR #3  Evan Longoria (X - X - X)
t9.new_ab()
t9.pitch_list("b c s s")
t9.out("K")

# 3. TBR #18 Ben Zobrist (X - X - X)
t9.new_ab()
t9.pitch_list("b")
t9.out("P5")


# Bot 9th
# Pitching: TBR #56 Fernando Rodney
b9 = game.new_inning()

# Pitching change (TBR): #56 Fernando Rodney replaces #62 Joel Peralta
b9.pitching_substitution(56)

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b9.new_ab()
b9.pitch_list("c")
b9.hit(1)
b9.advance(2, "15 SB")
b9.advance(3, "12 WP")

# 2. BOS #18 Shane Victorino (X - X - 2)
b9.new_ab()
b9.pitch_list("l l")
b9.out("P4")

# 3. BOS #15 Dustin Pedroia (X - X - 2)
b9.new_ab(is_risp=True)
b9.pitch_list("b c b s f f")
b9.out("G6-3")

# 4. BOS #34 David Ortiz (X - 2 - X)
b9.new_ab(is_risp=True)
b9.pitch_list("i i i i")
b9.reach("IBB")
# Offensive change (BOS): Pinch-runner #10 Jose Iglesias replaces #34 David Ortiz
b9.offensive_substitution(4, 10, "PR")
b9.atbase("PR")
b9.advance(2, "12 WP")

# 5. BOS #12 Mike Napoli (X - 2 - 34)
b9.new_ab(is_risp=True)
b9.pitch_list("b d s s f b s")
b9.wp()
b9.out("K")

# Winning team: TBR
# WP: TBR #14 David Price
game.winning_pitcher(14, is_away_team=True)
# SV: TBR #56 Fernando Rodney
game.save_pitcher(56, is_away_team=True)

# Loser team: BOS
# LP: BOS #22 Felix Doubront
game.losing_pitcher(22)

# print(game)
game.generate_scorecard()
