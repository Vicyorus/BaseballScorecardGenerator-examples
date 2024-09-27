import os
from baseball_scorecard.baseball_scorecard import Scorecard

# TB @ BOS, 2013-06-18
# https://www.baseball-reference.com/boxes/BOS/BOS201306181.shtml
# https://www.mlb.com/gameday/rays-vs-red-sox/2013/06/18/346892/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-06-18 13:06-19:15 (2:59 delay)",
        "at": "Fenway Park, Boston, MA",
        "att": "33,430",
        "temp": "72F, Cloudy",
        "wind": "8mph, In From RF",
        "away": {
            "team": "Tampa Bay Rays",
            "starter": 22,
            "roster": {
                # Lineup
                20: "Matt Joyce",
                8: "Desmond Jennings",
                18: "Ben Zobrist",
                3: "Evan Longoria",
                21: "James Loney",
                9: "Wil Myers",
                30: "Luke Scott",
                28: "José Molina",
                11: "Yunel Escobar",
                # Starting pitcher
                22: "Chris Archer",
                # Bench
                1: "Sean Rodríguez",
                59: "Jose Lobaton",
                5: "Sam Fuld",
                2: "Kelly Johnson",
                # Bullpen
                58: "Jeremy Hellickson",
                55: "Matt Moore",
                62: "Joel Peralta",
                35: "Jamey Wright",
                43: "Kyle Farnsworth",
                23: "Jake Odorizzi",
                57: "Jake McGee",
                54: "Alex Torres",
                27: "Cesár Ramos",
                52: "Josh Lueke",
                56: "Fernando Rodney",
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
                [30, "0"],
                [28, "2"],
                [11, "6"],
            ],
            "bench": [
                [1, "2B"],
                [59, "C"],
                [5, "LF"],
                [2, "2B"],
            ],
            "bullpen": [58, 55, 62, 35, 43, 23, 57, 54, 27, 52, 56, 40],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 91,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                29: "Daniel Nava",
                39: "Jarrod Saltalamacchia",
                16: "Will Middlebrooks",
                7: "Stephen Drew",
                # Starting pitcher
                91: "Alfredo Aceves",
                # Bench
                37: "Mike Carp",
                10: "Jose Iglesias",
                5: "Jonny Gomes",
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
                46: "Ryan Dempster",
            },
            "lefties": [56, 30, 32, 31, 22],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [29, "7"],
                [39, "2"],
                [16, "5"],
                [7, "6"],
            ],
            "bench": [
                [37, "1B"],
                [10, "2B"],
                [5, "LF"],
                [20, "C"],
            ],
            "bullpen": [63, 40, 41, 56, 30, 32, 31, 36, 19, 54, 22, 46],
        },
        "umpires": {
            "HP": "Gerry Davis",
            "1B": "Lance Barrett",
            "2B": "Dan Iassogna",
            "3B": "Mark Carlson",
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
# Pitching: BOS #91 Alfredo Aceves
t1 = game.new_inning()

# 1. TBR #20 Matt Joyce (X - X - X)
t1.new_ab()
t1.pitch_list("c c b b b c")
t1.out("!K")

# 2. TBR #8  Desmond Jennings (X - X - X)
t1.new_ab()
t1.pitch_list("b f")
t1.out("G5-3")

# 3. TBR #18 Ben Zobrist (X - X - X)
t1.new_ab()
t1.out("F9")


# Bot 1st
# Pitching: TBR #22 Chris Archer
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("c b b")
b1.hit(2)
b1.advance(3, "18 F8")
b1.advance(4, "15 SF8")

# 2. BOS #18 Shane Victorino (X - 2 - X)
b1.new_ab()
b1.pitch_list("c")
b1.out("F8")

# 3. BOS #15 Dustin Pedroia (2 - X - X)
b1.new_ab()
b1.pitch_list("b f s")
b1.out("SF8", rbis=1)

# 4. BOS #34 David Ortiz (X - X - X)
b1.new_ab()
b1.pitch_list("s f f f b")
b1.out("F7")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #91 Alfredo Aceves
t2 = game.new_inning()

# 4. TBR #3  Evan Longoria (X - X - X)
t2.new_ab()
t2.pitch_list("b b c s b b")
t2.reach("BB")
t2.advance(2, "21 BB")
t2.advance(4, "30 2B")

# 5. TBR #21 James Loney (X - X - 3)
t2.new_ab()
t2.pitch_list("d b b b")
t2.reach("BB")
t2.advance(3, "30 2B")

# 6. TBR #9  Wil Myers (X - 3 - 21)
t2.new_ab()
t2.out("F8")

# 7. TBR #30 Luke Scott (X - 3 - 21)
t2.new_ab()
t2.pitch_list("c b d b")
t2.hit(2, rbis=1)

# 8. TBR #28 José Molina (21 - 30 - X)
t2.new_ab()
t2.pitch_list("b f b b b")
t2.reach("BB")
t2.thrown_out(2, "11 DP6-4-3", 2, 91)

# 9. TBR #11 Yunel Escobar (21 - 30 - 28)
t2.new_ab()
t2.pitch_list("b c b")
t2.out("DP6-4-3")


# Bot 2nd
# Pitching: TBR #22 Chris Archer
b2 = game.new_inning()

# 5. BOS #12 Mike Napoli (X - X - X)
b2.new_ab()
b2.pitch_list("c b s b f b f d")
b2.reach("BB")
b2.advance(2, "29 BB")
b2.advance(3, "39 DP3-6-1")

# 6. BOS #29 Daniel Nava (X - X - 12)
b2.new_ab()
b2.pitch_list("b b b b")
b2.reach("BB")
b2.thrown_out(2, "39 DP3-6-1", 1, 22)

# 7. BOS #39 Jarrod Saltalamacchia (X - 12 - 29)
b2.new_ab()
b2.pitch_list("c d s f f b")
b2.out("DP3-6-1")

# 8. BOS #16 Will Middlebrooks (12 - X - X)
b2.new_ab()
b2.pitch_list("b b d b")
b2.reach("BB")
b2.thrown_out(2, "7 FC4-6", 3, 22)

# 9. BOS #7  Stephen Drew (12 - X - 16)
b2.new_ab()
b2.pitch_list("c f f b f")
b2.reach("FC4-6")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #91 Alfredo Aceves
t3 = game.new_inning()

# 1. TBR #20 Matt Joyce (X - X - X)
t3.new_ab()
t3.pitch_list("b b c b f f")
t3.out("G4-3")

# 2. TBR #8  Desmond Jennings (X - X - X)
t3.new_ab()
t3.pitch_list("c c b b f s")
t3.out("K")

# 3. TBR #18 Ben Zobrist (X - X - X)
t3.new_ab()
t3.pitch_list("c c b f")
t3.hit(2)

# 4. TBR #3  Evan Longoria (X - 18 - X)
t3.new_ab()
t3.pitch_list("c b")
t3.out("G5-3")


# Bot 3rd
# Pitching: TBR #22 Chris Archer
b3 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b3.new_ab()
b3.pitch_list("c")
b3.hit(1)
b3.advance(3, "18 1B")
b3.advance(4, "34 1B")

# 2. BOS #18 Shane Victorino (X - X - 2)
b3.new_ab()
b3.pitch_list("c 1 d 1 b")
b3.hit(1)
b3.advance(2, "15 SB")
b3.advance(4, "34 1B")

# 3. BOS #15 Dustin Pedroia (2 - X - 18)
b3.new_ab()
b3.pitch_list("b c d 1 b")
b3.out("L4")

# 4. BOS #34 David Ortiz (2 - 18 - X)
b3.new_ab()
b3.pitch_list("f")
b3.hit(1, rbis=2)

# 5. BOS #12 Mike Napoli (X - X - 34)
b3.new_ab()
b3.pitch_list("c c s")
b3.out("K")

# 6. BOS #29 Daniel Nava (X - X - 34)
b3.new_ab()
b3.pitch_list("d f s b f f s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #91 Alfredo Aceves
t4 = game.new_inning()

# 5. TBR #21 James Loney (X - X - X)
t4.new_ab()
t4.out("G3-1")

# 6. TBR #9  Wil Myers (X - X - X)
t4.new_ab()
t4.pitch_list("b b f b f")
t4.out("F9")

# 7. TBR #30 Luke Scott (X - X - X)
t4.new_ab()
t4.pitch_list("f")
t4.out("G4-3")


# Bot 4th
# Pitching: TBR #22 Chris Archer
b4 = game.new_inning()

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b4.new_ab()
b4.pitch_list("f b s b b s")
b4.out("K")

# 8. BOS #16 Will Middlebrooks (X - X - X)
b4.new_ab()
b4.pitch_list("c s b f")
b4.out("G1-3")

# 9. BOS #7  Stephen Drew (X - X - X)
b4.new_ab()
b4.pitch_list("c c b b s")
b4.out("K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #91 Alfredo Aceves
t5 = game.new_inning()

# 8. TBR #28 José Molina (X - X - X)
t5.new_ab()
t5.pitch_list("f s f")
t5.out("G6-3")

# 9. TBR #11 Yunel Escobar (X - X - X)
t5.new_ab()
t5.hit(1)
t5.advance(2, "20 G1-3")

# 1. TBR #20 Matt Joyce (X - X - 11)
t5.new_ab()
t5.pitch_list("c 1")
t5.out("G1-3")

# 2. TBR #8  Desmond Jennings (X - 11 - X)
t5.new_ab()
t5.pitch_list("s b")
t5.out("G6-3")


# Bot 5th
# Pitching: TBR #22 Chris Archer
b5 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b5.new_ab()
b5.pitch_list("c b f")
b5.out("F9")

# 2. BOS #18 Shane Victorino (X - X - X)
b5.new_ab()
b5.pitch_list("c")
b5.error(3)
b5.reach("E3")
b5.advance(2, "15 BB")
b5.advance("U", "34 1B")

# 3. BOS #15 Dustin Pedroia (X - X - 18)
b5.new_ab()
b5.pitch_list("1 b b b b")
b5.reach("BB")
b5.advance(3, "34 1B")

# 4. BOS #34 David Ortiz (X - 18 - 15)
b5.new_ab()
b5.pitch_list("b f b b")
b5.hit(1, rbis=1)
b5.advance(2, "29 BB")

# 5. BOS #12 Mike Napoli (15 - X - 34)
b5.new_ab()
b5.pitch_list("b s f s")
b5.out("K")

# 6. BOS #29 Daniel Nava (15 - X - 34)
b5.new_ab()
b5.pitch_list("b f b d c b")
b5.reach("BB")

# Pitching change (TBR): #52 Josh Lueke replaces #22 Chris Archer
b5.pitching_substitution(52)

# 7. BOS #39 Jarrod Saltalamacchia (15 - 34 - 29)
b5.new_ab()
b5.pitch_list("b b f s t")
b5.out("KT")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #36 Junichi Tazawa
t6 = game.new_inning()

# Pitching change (BOS): #36 Junichi Tazawa replaces #91 Alfredo Aceves
t6.pitching_substitution(36)

# 3. TBR #18 Ben Zobrist (X - X - X)
t6.new_ab()
t6.pitch_list("b t b f s")
t6.out("K")

# 4. TBR #3  Evan Longoria (X - X - X)
t6.new_ab()
t6.pitch_list("c f c")
t6.out("!K")

# 5. TBR #21 James Loney (X - X - X)
t6.new_ab()
t6.pitch_list("b c b")
t6.out("L7")


# Bot 6th
# Pitching: TBR #52 Josh Lueke
b6 = game.new_inning()

# 8. BOS #16 Will Middlebrooks (X - X - X)
b6.new_ab()
b6.pitch_list("t b s s")
b6.out("K")

# 9. BOS #7  Stephen Drew (X - X - X)
b6.new_ab()
b6.pitch_list("c")
b6.out("G4-3")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b6.new_ab()
b6.pitch_list("b c")
b6.hit(3)
b6.advance(4, "18 3B")

# 2. BOS #18 Shane Victorino (2 - X - X)
b6.new_ab()
b6.pitch_list("b c f d f b")
b6.hit(3, rbis=1)

# 3. BOS #15 Dustin Pedroia (18 - X - X)
b6.new_ab()
b6.pitch_list("c b f t")
b6.out("KT")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #30 Andrew Miller
t7 = game.new_inning()

# Pitching change (BOS): #30 Andrew Miller replaces #36 Junichi Tazawa
t7.pitching_substitution(30)

# 6. TBR #9  Wil Myers (X - X - X)
t7.new_ab()
t7.pitch_list("c f b c")
t7.out("!K")

# 7. TBR #30 Luke Scott (X - X - X)
t7.new_ab()
t7.pitch_list("c s b s")
t7.out("K")

# 8. TBR #28 José Molina (X - X - X)
t7.new_ab()
t7.pitch_list("b b f c f")
t7.hit(1)

# 9. TBR #11 Yunel Escobar (X - X - 28)
t7.new_ab()
t7.pitch_list("c d s b f")
t7.out("G4-3")


# Bot 7th
# Pitching: TBR #27 Cesár Ramos
b7 = game.new_inning()

# Pitching change (TBR): #27 Cesár Ramos replaces #52 Josh Lueke
b7.pitching_substitution(27)

# 4. BOS #34 David Ortiz (X - X - X)
b7.new_ab()
b7.pitch_list("c f c")
b7.out("!K")

# 5. BOS #12 Mike Napoli (X - X - X)
b7.new_ab()
b7.pitch_list("b f b")
b7.hit(1)

# 6. BOS #29 Daniel Nava (X - X - 12)
b7.new_ab()
b7.out("P4")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - 12)
b7.new_ab()
b7.pitch_list("f b s f b s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #19 Koji Uehara
t8 = game.new_inning()

# Pitching change (BOS): #19 Koji Uehara replaces #30 Andrew Miller
t8.pitching_substitution(19)

# 1. TBR #20 Matt Joyce (X - X - X)
t8.new_ab()
t8.pitch_list("b b c s")
t8.hit(2)
t8.advance(3, "8 G6-3")

# 2. TBR #8  Desmond Jennings (X - 20 - X)
t8.new_ab()
t8.pitch_list("c s")
t8.out("G6-3")

# 3. TBR #18 Ben Zobrist (20 - X - X)
t8.new_ab()
t8.pitch_list("b c b b f f f f b")
t8.reach("BB")

# 4. TBR #3  Evan Longoria (20 - X - 18)
t8.new_ab()
t8.pitch_list("c f b f")
t8.out("(F)P3")

# 5. TBR #21 James Loney (20 - X - 18)
t8.new_ab()
t8.pitch_list("f f b f f f f f s")
t8.out("K")


# Bot 8th
# Pitching: TBR #27 Cesár Ramos
b8 = game.new_inning()

# 8. BOS #16 Will Middlebrooks (X - X - X)
b8.new_ab()
b8.pitch_list("b f b")
b8.out("(F)P3")

# 9. BOS #7  Stephen Drew (X - X - X)
b8.new_ab()
b8.pitch_list("s b f f")
b8.out("L3-1")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b8.new_ab()
b8.pitch_list("b s f b")
b8.out("L5")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #32 Craig Breslow
t9 = game.new_inning()

# Pitching change (BOS): #32 Craig Breslow replaces #19 Koji Uehara
t9.pitching_substitution(32)

# 6. TBR #9  Wil Myers (X - X - X)
t9.new_ab()
t9.out("F8")

# 7. TBR #30 Luke Scott (X - X - X)
t9.new_ab()
t9.pitch_list("c")
t9.out("G4-3")

# 8. TBR #28 José Molina (X - X - X)
t9.new_ab()
t9.pitch_list("f b")
t9.hit(1)

# 9. TBR #11 Yunel Escobar (X - X - 28)
t9.new_ab()
t9.pitch_list("b b s c b")
t9.out("G4-3")

# Winning team: BOS
# WP: BOS #91 Alfredo Aceves
game.winning_pitcher(91)

# Loser team: TBR
# LP: TBR #22 Chris Archer
game.losing_pitcher(22, is_away_team=True)

# print(game)
game.generate_scorecard()
