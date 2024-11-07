import os
from baseball_scorecard.baseball_scorecard import Scorecard

# TB @ BOS, 2013-06-19
# https://www.baseball-reference.com/boxes/BOS/BOS201306190.shtml
# https://www.mlb.com/gameday/rays-vs-red-sox/2013/06/19/347826/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-06-19 19:10-22:31",
        "at": "Fenway Park, Boston, MA",
        "att": "35,710",
        "temp": "70F, Partly Cloudy",
        "wind": "8mph, R To L",
        "away": {
            "team": "Tampa Bay Rays",
            "starter": 58,
            "roster": {
                # Lineup
                20: "Matt Joyce",
                8: "Desmond Jennings",
                18: "Ben Zobrist",
                3: "Evan Longoria",
                21: "James Loney",
                9: "Wil Myers",
                2: "Kelly Johnson",
                28: "José Molina",
                11: "Yunel Escobar",
                # Starting pitcher
                58: "Jeremy Hellickson",
                # Bench
                30: "Luke Scott",
                1: "Sean Rodríguez",
                59: "Jose Lobaton",
                5: "Sam Fuld",
                # Bullpen
                55: "Matt Moore",
                62: "Joel Peralta",
                35: "Jamey Wright",
                43: "Kyle Farnsworth",
                57: "Jake McGee",
                54: "Alex Torres",
                27: "Cesár Ramos",
                52: "Josh Lueke",
                56: "Fernando Rodney",
                22: "Chris Archer",
                40: "Roberto Hernandez",
            },
            "lefties": [55, 57, 54, 27],
            "lineup": [
                [20, "7"],
                [8, "8"],
                [18, "4"],
                [3, "5"],
                [21, "3"],
                [9, "9"],
                [2, "0"],
                [28, "2"],
                [11, "6"],
            ],
            "bench": [
                [30, "DH"],
                [1, "2B"],
                [59, "C"],
                [5, "LF"],
            ],
            "bullpen": [55, 62, 35, 43, 57, 54, 27, 52, 56, 22, 40],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 46,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                29: "Daniel Nava",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                39: "Jarrod Saltalamacchia",
                5: "Jonny Gomes",
                7: "Stephen Drew",
                10: "Jose Iglesias",
                # Starting pitcher
                46: "Ryan Dempster",
                # Bench
                37: "Mike Carp",
                16: "Will Middlebrooks",
                18: "Shane Victorino",
                20: "Ryan Lavarnway",
                # Bullpen
                63: "Alex Wilson",
                40: "Andrew Bailey",
                41: "John Lackey",
                56: "Franklin Morales",
                30: "Andrew Miller",
                32: "Craig Breslow",
                31: "Jon Lester",
                36: "Junichi Tazawa",
                19: "Koji Uehara",
                54: "Pedro Beato",
                22: "Felix Doubront",
            },
            "lefties": [56, 30, 32, 31, 22],
            "lineup": [
                [2, "8"],
                [29, "9"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [39, "2"],
                [5, "7"],
                [7, "6"],
                [10, "5"],
            ],
            "bench": [
                [37, "1B"],
                [16, "3B"],
                [18, "CF"],
                [20, "C"],
            ],
            "bullpen": [63, 40, 41, 56, 30, 32, 31, 36, 19, 54, 22],
        },
        "umpires": {
            "HP": "Dan Iassogna",
            "1B": "Mark Carlson",
            "2B": "Gerry Davis",
            "3B": "Brian Knight",
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
# Pitching: BOS #46 Ryan Dempster
t1 = game.new_inning()

# 1. TBR #20 Matt Joyce (X - X - X)
t1.new_ab()
t1.pitch_list("c")
t1.out("F8")

# 2. TBR #8  Desmond Jennings (X - X - X)
t1.new_ab()
t1.pitch_list("b c f")
t1.hit(4)

# 3. TBR #18 Ben Zobrist (X - X - X)
t1.new_ab()
t1.pitch_list("c b")
t1.hit(1)
t1.advance(3, "3 E5")
t1.advance(4, "21 SF9")

# 4. TBR #3  Evan Longoria (X - X - 18)
t1.new_ab()
t1.pitch_list("c")
t1.hit(1)
t1.error(5)
t1.advance(2, "E5")

# 5. TBR #21 James Loney (18 - 3 - X)
t1.new_ab(is_risp=True)
t1.pitch_list("d")
t1.out("SF9", rbis=1)

# 6. TBR #9  Wil Myers (X - 3 - X)
t1.new_ab(is_risp=True)
t1.pitch_list("b b c f")
t1.out("G6-3")


# Bot 1st
# Pitching: TBR #58 Jeremy Hellickson
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("b c s f")
b1.out("G3-1")

# 2. BOS #29 Daniel Nava (X - X - X)
b1.new_ab()
b1.pitch_list("b c b")
b1.out("F7")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b1.new_ab()
b1.pitch_list("b b c")
b1.out("F8")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #46 Ryan Dempster
t2 = game.new_inning()

# 7. TBR #2  Kelly Johnson (X - X - X)
t2.new_ab()
t2.pitch_list("c f b b c")
t2.out("!K")

# 8. TBR #28 José Molina (X - X - X)
t2.new_ab()
t2.pitch_list("b f b c")
t2.hit(1)
t2.advance(2, "11 1B")

# 9. TBR #11 Yunel Escobar (X - X - 28)
t2.new_ab()
t2.pitch_list("b c")
t2.hit(1)
t2.thrown_out(2, "20 DP4-6-3", 2, 46)

# 1. TBR #20 Matt Joyce (X - 28 - 11)
t2.new_ab(is_risp=True)
t2.pitch_list("f f b b d f")
t2.out("DP4-6-3")


# Bot 2nd
# Pitching: TBR #58 Jeremy Hellickson
b2 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
b2.new_ab()
b2.pitch_list("s b b")
b2.hit(2)
b2.advance(3, "12 G3-1")
b2.advance(4, "5 1B")

# 5. BOS #12 Mike Napoli (X - 34 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("c")
b2.out("G3-1")

# 6. BOS #39 Jarrod Saltalamacchia (34 - X - X)
b2.new_ab(is_risp=True)
b2.pitch_list("d s b c s")
b2.out("K")

# 7. BOS #5  Jonny Gomes (34 - X - X)
b2.new_ab(is_risp=True)
b2.pitch_list("b")
b2.hit(1, rbis=1)
b2.advance(2, "7 1B")

# 8. BOS #7  Stephen Drew (X - X - 5)
b2.new_ab()
b2.pitch_list("b")
b2.hit(1)
b2.thrown_out(2, "10 FC6-4", 3, 58)

# 9. BOS #10 Jose Iglesias (X - 5 - 7)
b2.new_ab(is_risp=True)
b2.pitch_list("b c c f b")
b2.reach("FC6-4")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #46 Ryan Dempster
t3 = game.new_inning()

# 2. TBR #8  Desmond Jennings (X - X - X)
t3.new_ab()
t3.pitch_list("b c")
t3.out("G5-3")

# 3. TBR #18 Ben Zobrist (X - X - X)
t3.new_ab()
t3.pitch_list("f b b c b")
t3.out("F9")

# 4. TBR #3  Evan Longoria (X - X - X)
t3.new_ab()
t3.pitch_list("c b b")
t3.out("P4")


# Bot 3rd
# Pitching: TBR #58 Jeremy Hellickson
b3 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b3.new_ab()
b3.pitch_list("b")
b3.hit(1)
b3.thrown_out(2, "29 DP6-3", 1, 58)

# 2. BOS #29 Daniel Nava (X - X - 2)
b3.new_ab()
b3.pitch_list("1 b c")
b3.out("DP6-3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b3.new_ab()
b3.pitch_list("c f")
b3.out("G4-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #46 Ryan Dempster
t4 = game.new_inning()

# 5. TBR #21 James Loney (X - X - X)
t4.new_ab()
t4.pitch_list("f b b s c")
t4.out("!K")

# 6. TBR #9  Wil Myers (X - X - X)
t4.new_ab()
t4.pitch_list("b c b s")
t4.out("P4")

# 7. TBR #2  Kelly Johnson (X - X - X)
t4.new_ab()
t4.pitch_list("s b c f s")
t4.out("K")


# Bot 4th
# Pitching: TBR #58 Jeremy Hellickson
b4 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
b4.new_ab()
b4.pitch_list("t")
b4.out("F9")

# 5. BOS #12 Mike Napoli (X - X - X)
b4.new_ab()
b4.pitch_list("b b b s")
b4.out("G4-3")

# 6. BOS #39 Jarrod Saltalamacchia (X - X - X)
b4.new_ab()
b4.hit(2)
b4.advance(3, "5 WP")
b4.advance(4, "5 1B")

# 7. BOS #5  Jonny Gomes (X - 39 - X)
b4.new_ab(is_risp=True)
b4.pitch_list("b d b c c")
b4.wp()
b4.hit(1, rbis=1)
b4.thrown_out(2, "7 FC6", 3, 58)

# 8. BOS #7  Stephen Drew (X - X - 5)
b4.new_ab()
b4.pitch_list("1")
b4.reach("FC6")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #46 Ryan Dempster
t5 = game.new_inning()

# 8. TBR #28 José Molina (X - X - X)
t5.new_ab()
t5.pitch_list("b")
t5.hit(1)
t5.advance(2, "8 BB")
t5.advance(4, "18 1B")

# 9. TBR #11 Yunel Escobar (X - X - 28)
t5.new_ab()
t5.pitch_list("b f")
t5.out("F9")

# 1. TBR #20 Matt Joyce (X - X - 28)
t5.new_ab()
t5.pitch_list("s")
t5.out("F8")

# 2. TBR #8  Desmond Jennings (X - X - 28)
t5.new_ab()
t5.pitch_list("c b b b b")
t5.reach("BB")
t5.advance(3, "18 1B")

# 3. TBR #18 Ben Zobrist (X - 28 - 8)
t5.new_ab(is_risp=True)
t5.pitch_list("b f s d")
t5.hit(1, rbis=1)
t5.advance(2, "T")

# 4. TBR #3  Evan Longoria (8 - 18 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("c d")
t5.out("(F)P3")


# Bot 5th
# Pitching: TBR #58 Jeremy Hellickson
b5 = game.new_inning()

# 9. BOS #10 Jose Iglesias (X - X - X)
b5.new_ab()
b5.pitch_list("b")
b5.out("G5-3")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b5.new_ab()
b5.pitch_list("c b b")
b5.hit(1)
b5.advance(2, "29 WP")
b5.advance(3, "15 BLK")

# 2. BOS #29 Daniel Nava (X - X - 2)
b5.new_ab()
b5.pitch_list("f t 1 s")
b5.wp()
b5.out("K")

# 3. BOS #15 Dustin Pedroia (X - 2 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("b f b n b")
b5.balk()
b5.out("G5-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #46 Ryan Dempster
t6 = game.new_inning()

# 5. TBR #21 James Loney (X - X - X)
t6.new_ab()
t6.pitch_list("l f")
t6.out("G3")

# 6. TBR #9  Wil Myers (X - X - X)
t6.new_ab()
t6.pitch_list("b")
t6.out("F8")

# 7. TBR #2  Kelly Johnson (X - X - X)
t6.new_ab()
t6.pitch_list("b b s b b")
t6.reach("BB")
t6.advance(3, "28 1B")

# 8. TBR #28 José Molina (X - X - 2)
t6.new_ab()
t6.pitch_list("1 c f b")
t6.hit(1)

# 9. TBR #11 Yunel Escobar (2 - X - 28)
t6.new_ab(is_risp=True)
t6.pitch_list("c b c d b f f")
t6.out("F8")


# Bot 6th
# Pitching: TBR #58 Jeremy Hellickson
b6 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
b6.new_ab()
b6.pitch_list("c b b")
b6.out("L9")

# 5. BOS #12 Mike Napoli (X - X - X)
b6.new_ab()
b6.pitch_list("f b t b f b s")
b6.out("K")

# 6. BOS #39 Jarrod Saltalamacchia (X - X - X)
b6.new_ab()
b6.pitch_list("b f b f b c")
b6.out("!K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #32 Craig Breslow
t7 = game.new_inning()

# Pitching change (BOS): #32 Craig Breslow replaces #46 Ryan Dempster
t7.pitching_substitution(32)

# 1. TBR #20 Matt Joyce (X - X - X)
t7.new_ab()
t7.pitch_list("b")
t7.out("L4-3")

# 2. TBR #8  Desmond Jennings (X - X - X)
t7.new_ab()
t7.pitch_list("b c b")
t7.hit(1)
t7.advance(4, "3 1B")

# 3. TBR #18 Ben Zobrist (X - X - 8)
t7.new_ab()
t7.pitch_list("b 1 1 b 1 f")
t7.out("F9")

# 4. TBR #3  Evan Longoria (X - X - 8)
t7.new_ab()
t7.pitch_list("1 f b f b b")
t7.hit(1, rbis=1)
t7.advance(3, "21 2B")
t7.advance(4, "9 2B")

# 5. TBR #21 James Loney (X - X - 3)
t7.new_ab()
t7.hit(2)
t7.advance(4, "9 2B")

# Pitching change (BOS): #63 Alex Wilson replaces #32 Craig Breslow
t7.pitching_substitution(63)

# 6. TBR #9  Wil Myers (3 - 21 - X)
t7.new_ab(is_risp=True)
t7.pitch_list("c s")
t7.hit(2, rbis=2)

# 7. TBR #2  Kelly Johnson (X - 9 - X)
t7.new_ab(is_risp=True)
t7.pitch_list("c c d b")
t7.out("P4")


# Bot 7th
# Pitching: TBR #57 Jake McGee
b7 = game.new_inning()

# Pitching change (TBR): #57 Jake McGee replaces #58 Jeremy Hellickson
b7.pitching_substitution(57)

# 7. BOS #5  Jonny Gomes (X - X - X)
b7.new_ab()
b7.pitch_list("c c f f f s")
b7.out("K")

# 8. BOS #7  Stephen Drew (X - X - X)
b7.new_ab()
b7.pitch_list("b c b t f f c")
b7.out("!K")

# 9. BOS #10 Jose Iglesias (X - X - X)
b7.new_ab()
b7.pitch_list("c b b b d")
b7.reach("BB")

# 1. BOS #2  Jacoby Ellsbury (X - X - 10)
b7.new_ab()
b7.pitch_list("c f 1 f")
b7.out("L5")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #56 Franklin Morales
t8 = game.new_inning()

# Pitching change (BOS): #56 Franklin Morales replaces #63 Alex Wilson
t8.pitching_substitution(56)

# 8. TBR #28 José Molina (X - X - X)
t8.new_ab()
t8.pitch_list("c s s")
t8.out("K")

# 9. TBR #11 Yunel Escobar (X - X - X)
t8.new_ab()
t8.pitch_list("b c f b")
t8.out("G1-3")

# Offensive change (TBR): Pinch-hitter #1 Sean Rodríguez replaces #20 Matt Joyce, batting 1st
t8.offensive_substitution(1, 1, "PH")

# 1. TBR #1  Sean Rodríguez (X - X - X)
t8.new_ab()
t8.pitch_list("c b f b b")
t8.hit(1)

# 2. TBR #8  Desmond Jennings (X - X - 1)
t8.new_ab()
t8.pitch_list("c b c s")
t8.out("K")


# Bot 8th
# Pitching: TBR #62 Joel Peralta
b8 = game.new_inning()

# Pitching change (TBR): #62 Joel Peralta replaces #57 Jake McGee
b8.pitching_substitution(62)

# Defensive switch (TBR): #1 Sean Rodríguez moves to LF
b8.defensive_switch(1, "7")

# 2. BOS #29 Daniel Nava (X - X - X)
b8.new_ab()
b8.pitch_list("c c b b f b f f f")
b8.out("F8")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b8.new_ab()
b8.pitch_list("c c f c")
b8.out("!K")

# 4. BOS #34 David Ortiz (X - X - X)
b8.new_ab()
b8.pitch_list("b c f")
b8.out("F7")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #54 Pedro Beato
t9 = game.new_inning()

# Pitching change (BOS): #54 Pedro Beato replaces #56 Franklin Morales
t9.pitching_substitution(54)

# 3. TBR #18 Ben Zobrist (X - X - X)
t9.new_ab()
t9.pitch_list("b s s s")
t9.out("K")

# 4. TBR #3  Evan Longoria (X - X - X)
t9.new_ab()
t9.pitch_list("c f")
t9.hit(1)
t9.advance(2, "21 1B")

# 5. TBR #21 James Loney (X - X - 3)
t9.new_ab()
t9.pitch_list("f s f")
t9.hit(1)

# 6. TBR #9  Wil Myers (X - 3 - 21)
t9.new_ab(is_risp=True)
t9.pitch_list("b")
t9.out("L7")

# 7. TBR #2  Kelly Johnson (X - 3 - 21)
t9.new_ab(is_risp=True)
t9.pitch_list("c")
t9.out("G4-3")


# Bot 9th
# Pitching: TBR #35 Jamey Wright
b9 = game.new_inning()

# Pitching change (TBR): #35 Jamey Wright replaces #62 Joel Peralta
b9.pitching_substitution(35)

# Defensive change (TBR): #5 Sam Fuld replaces #9 Wil Myers (RF), playing RF, batting 6th
b9.defensive_substitution(6, 5, "9")

# 5. BOS #12 Mike Napoli (X - X - X)
b9.new_ab()
b9.pitch_list("c b c")
b9.out("G1-3")

# 6. BOS #39 Jarrod Saltalamacchia (X - X - X)
b9.new_ab()
b9.pitch_list("c b c s")
b9.out("K")

# Pitching change (TBR): #56 Fernando Rodney replaces #35 Jamey Wright
b9.pitching_substitution(56)

# 7. BOS #5  Jonny Gomes (X - X - X)
b9.new_ab()
b9.pitch_list("b c c b b s")
b9.out("K")

# Winning team: TBR
# WP: TBR #58 Jeremy Hellickson
game.winning_pitcher(58, is_away_team=True)

# Loser team: BOS
# LP: BOS #46 Ryan Dempster
game.losing_pitcher(46)

# print(game)
game.generate_scorecard()
