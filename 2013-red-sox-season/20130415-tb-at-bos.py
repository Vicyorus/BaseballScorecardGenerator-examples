import os
from baseball_scorecard.baseball_scorecard import Scorecard

# TB @ BOS, 2013-04-15
# https://www.baseball-reference.com/boxes/BOS/BOS201304150.shtml
# https://www.mlb.com/gameday/rays-vs-red-sox/2013/04/15/346932/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-04-15 11:05-14:08",
        "at": "Fenway Park, Boston, MA",
        "att": "37,449",
        "temp": "48F, Partly Cloudy",
        "wind": "3mph, R To L",
        "away": {
            "team": "Tampa Bay Rays",
            "starter": 58,
            "roster": {
                # Lineup
                8: "Desmond Jennings",
                18: "Ben Zobrist",
                3: "Evan Longoria",
                20: "Matt Joyce",
                19: "Ryan Roberts",
                21: "James Loney",
                11: "Yunel Escobar",
                59: "Jose Lobaton",
                2: "Kelly Johnson",
                # Starting pitcher
                58: "Jeremy Hellickson",
                # Bench
                28: "José Molina",
                1: "Sean Rodríguez",
                15: "Shelley Duncan",
                5: "Sam Fuld",
                # Bullpen
                53: "Alex Cobb",
                47: "Brandon Gomes",
                55: "Matt Moore",
                62: "Joel Peralta",
                35: "Jamey Wright",
                43: "Kyle Farnsworth",
                57: "Jake McGee",
                27: "Cesár Ramos",
                14: "David Price",
                56: "Fernando Rodney",
                40: "Roberto Hernandez",
            },
            "lefties": [55, 57, 27, 14],
            "lineup": [
                [8, "8"],
                [18, "9"],
                [3, "5"],
                [20, "7"],
                [19, "4"],
                [21, "3"],
                [11, "6"],
                [59, "2"],
                [2, "0"],
            ],
            "bench": [
                [28, "C"],
                [1, "2B"],
                [15, "LF"],
                [5, "LF"],
            ],
            "bullpen": [53, 47, 55, 62, 35, 43, 57, 27, 14, 56, 40],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 46,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                12: "Mike Napoli",
                39: "Jarrod Saltalamacchia",
                16: "Will Middlebrooks",
                7: "Stephen Drew",
                5: "Jonny Gomes",
                44: "Jackie Bradley Jr.",
                # Starting pitcher
                46: "Ryan Dempster",
                # Bench
                3: "David Ross",
                37: "Mike Carp",
                29: "Daniel Nava",
                23: "Pedro Ciriaco",
                # Bullpen
                63: "Alex Wilson",
                40: "Andrew Bailey",
                30: "Andrew Miller",
                19: "Koji Uehara",
                91: "Alfredo Aceves",
                31: "Jon Lester",
                59: "Clayton Mortensen",
                36: "Junichi Tazawa",
                22: "Felix Doubront",
                11: "Clay Buchholz",
            },
            "lefties": [30, 31, 22],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [12, "3"],
                [39, "2"],
                [16, "5"],
                [7, "6"],
                [5, "0"],
                [44, "7"],
            ],
            "bench": [
                [3, "C"],
                [37, "1B"],
                [29, "LF"],
                [23, "3B"],
            ],
            "bullpen": [63, 40, 30, 19, 91, 31, 59, 36, 22, 11],
        },
        "umpires": {
            "HP": "Dana DeMuth",
            "1B": "Angel Hernandez",
            "2B": "Doug Eddings",
            "3B": "John Tumpane",
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

# 1. TBR #8  Desmond Jennings (X - X - X)
t1.new_ab()
t1.pitch_list("b s c s")
t1.out("K")

# 2. TBR #18 Ben Zobrist (X - X - X)
t1.new_ab()
t1.pitch_list("b c f b s")
t1.out("K")

# 3. TBR #3  Evan Longoria (X - X - X)
t1.new_ab()
t1.pitch_list("c c")
t1.out("G5-3")


# Bot 1st
# Pitching: TBR #58 Jeremy Hellickson
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("b b c b c f f")
b1.hit(3)
b1.advance(4, "18 G4-3")

# 2. BOS #18 Shane Victorino (2 - X - X)
b1.new_ab()
b1.pitch_list("l d f")
b1.out("G4-3", rbis=1)

# 3. BOS #15 Dustin Pedroia (X - X - X)
b1.new_ab()
b1.pitch_list("c f b b f")
b1.out("G5-3")

# 4. BOS #12 Mike Napoli (X - X - X)
b1.new_ab()
b1.pitch_list("b c f s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #46 Ryan Dempster
t2 = game.new_inning()

# 4. TBR #20 Matt Joyce (X - X - X)
t2.new_ab()
t2.hit(1)
t2.thrown_out(2, "21 DP4-6-3", 2, 46)

# 5. TBR #19 Ryan Roberts (X - X - 20)
t2.new_ab()
t2.pitch_list("c s 1 b 1 f s")
t2.out("K")

# 6. TBR #21 James Loney (X - X - 20)
t2.new_ab()
t2.pitch_list("b 1 b f")
t2.out("DP4-6-3")


# Bot 2nd
# Pitching: TBR #58 Jeremy Hellickson
b2 = game.new_inning()

# 5. BOS #39 Jarrod Saltalamacchia (X - X - X)
b2.new_ab()
b2.pitch_list("f b o b s")
b2.out("K")

# 6. BOS #16 Will Middlebrooks (X - X - X)
b2.new_ab()
b2.out("L9")

# 7. BOS #7  Stephen Drew (X - X - X)
b2.new_ab()
b2.pitch_list("c b s f b b c")
b2.out("!K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #46 Ryan Dempster
t3 = game.new_inning()

# 7. TBR #11 Yunel Escobar (X - X - X)
t3.new_ab()
t3.pitch_list("b c b")
t3.out("G6-3")

# 8. TBR #59 Jose Lobaton (X - X - X)
t3.new_ab()
t3.pitch_list("t b b s b s")
t3.out("K")

# 9. TBR #2  Kelly Johnson (X - X - X)
t3.new_ab()
t3.pitch_list("b s f c")
t3.out("!K")


# Bot 3rd
# Pitching: TBR #58 Jeremy Hellickson
b3 = game.new_inning()

# 8. BOS #5  Jonny Gomes (X - X - X)
b3.new_ab()
b3.pitch_list("c c b f s")
b3.out("K")

# 9. BOS #44 Jackie Bradley Jr. (X - X - X)
b3.new_ab()
b3.pitch_list("c b s s")
b3.out("K")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b3.new_ab()
b3.pitch_list("c")
b3.out("(F)P5")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #46 Ryan Dempster
t4 = game.new_inning()

# 1. TBR #8  Desmond Jennings (X - X - X)
t4.new_ab()
t4.pitch_list("c b")
t4.out("F9")

# 2. TBR #18 Ben Zobrist (X - X - X)
t4.new_ab()
t4.pitch_list("f s")
t4.out("G6-3")

# 3. TBR #3  Evan Longoria (X - X - X)
t4.new_ab()
t4.hit(4)

# 4. TBR #20 Matt Joyce (X - X - X)
t4.new_ab()
t4.pitch_list("s")
t4.out("P6")


# Bot 4th
# Pitching: TBR #58 Jeremy Hellickson
b4 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
b4.new_ab()
b4.pitch_list("b c f f b")
b4.out("F8")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b4.new_ab()
b4.pitch_list("c c b b")
b4.out("G4-3")

# 4. BOS #12 Mike Napoli (X - X - X)
b4.new_ab()
b4.pitch_list("b b c c c")
b4.out("!K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #46 Ryan Dempster
t5 = game.new_inning()

# 5. TBR #19 Ryan Roberts (X - X - X)
t5.new_ab()
t5.pitch_list("b f s b s")
t5.out("K")

# 6. TBR #21 James Loney (X - X - X)
t5.new_ab()
t5.pitch_list("b c c f b f f b s")
t5.out("K")

# 7. TBR #11 Yunel Escobar (X - X - X)
t5.new_ab()
t5.pitch_list("b b b c")
t5.out("F8")


# Bot 5th
# Pitching: TBR #58 Jeremy Hellickson
b5 = game.new_inning()

# 5. BOS #39 Jarrod Saltalamacchia (X - X - X)
b5.new_ab()
b5.pitch_list("c f")
b5.hit(4)

# 6. BOS #16 Will Middlebrooks (X - X - X)
b5.new_ab()
b5.pitch_list("b s b f s")
b5.out("K")

# 7. BOS #7  Stephen Drew (X - X - X)
b5.new_ab()
b5.pitch_list("f b b s")
b5.hit(2)

# 8. BOS #5  Jonny Gomes (X - 7 - X)
b5.new_ab()
b5.pitch_list("b b s s s")
b5.out("K")

# 9. BOS #44 Jackie Bradley Jr. (X - 7 - X)
b5.new_ab()
b5.out("F8")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #46 Ryan Dempster
t6 = game.new_inning()

# 8. TBR #59 Jose Lobaton (X - X - X)
t6.new_ab()
t6.out("F8")

# 9. TBR #2  Kelly Johnson (X - X - X)
t6.new_ab()
t6.pitch_list("l b b s b b")
t6.reach("BB")
t6.advance(2, "8 SB")
t6.advance(3, "18 WP")

# 1. TBR #8  Desmond Jennings (X - X - 2)
t6.new_ab()
t6.pitch_list("1 c b 1 b s b f s")
t6.out("K")

# 2. TBR #18 Ben Zobrist (X - 2 - X)
t6.new_ab()
t6.pitch_list("c b b c b d")
t6.wp()
t6.reach("BB")

# 3. TBR #3  Evan Longoria (2 - X - 18)
t6.new_ab()
t6.pitch_list("c f d b b")
t6.out("G6-3")


# Bot 6th
# Pitching: TBR #58 Jeremy Hellickson
b6 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b6.new_ab()
b6.pitch_list("c")
b6.out("F8")

# 2. BOS #18 Shane Victorino (X - X - X)
b6.new_ab()
b6.pitch_list("b b b c")
b6.out("F9")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b6.new_ab()
b6.pitch_list("b")
b6.out("G5-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #46 Ryan Dempster
t7 = game.new_inning()

# 4. TBR #20 Matt Joyce (X - X - X)
t7.new_ab()
t7.pitch_list("b c s b s")
t7.out("K")

# 5. TBR #19 Ryan Roberts (X - X - X)
t7.new_ab()
t7.pitch_list("b c")
t7.out("F9")

# 6. TBR #21 James Loney (X - X - X)
t7.new_ab()
t7.pitch_list("c f c")
t7.out("!K")


# Bot 7th
# Pitching: TBR #58 Jeremy Hellickson
b7 = game.new_inning()

# 4. BOS #12 Mike Napoli (X - X - X)
b7.new_ab()
b7.out("P4")

# 5. BOS #39 Jarrod Saltalamacchia (X - X - X)
b7.new_ab()
b7.pitch_list("b f b b b")
b7.reach("BB")
b7.thrown_out(2, "16 CS", 3, 58)

# 6. BOS #16 Will Middlebrooks (X - X - 39)
b7.new_ab()
b7.pitch_list("c s d b f 1 d s")
b7.out("KDP2-4")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #19 Koji Uehara
t8 = game.new_inning()

# Pitching change (BOS): #19 Koji Uehara replaces #46 Ryan Dempster
t8.pitching_substitution(19)

# 7. TBR #11 Yunel Escobar (X - X - X)
t8.new_ab()
t8.pitch_list("b b")
t8.out("F8")

# Offensive change (TBR): Pinch-hitter #5 Sam Fuld replaces #59 Jose Lobaton, batting 8th
t8.offensive_substitution(8, 5, "PH")

# 8. TBR #5  Sam Fuld (X - X - X)
t8.new_ab()
t8.pitch_list("c s")
t8.out("G3-1")

# 9. TBR #2  Kelly Johnson (X - X - X)
t8.new_ab()
t8.pitch_list("c s b f f s")
t8.out("K")


# Bot 8th
# Pitching: TBR #57 Jake McGee
b8 = game.new_inning()

# Pitching change (TBR): #57 Jake McGee replaces #58 Jeremy Hellickson
b8.pitching_substitution(57)

# Defensive change (TBR): #28 José Molina replaces #5 Sam Fuld (PH), playing C, batting 8th
b8.defensive_substitution(8, 28, "2")

# 7. BOS #7  Stephen Drew (X - X - X)
b8.new_ab()
b8.pitch_list("f c b b f f b f s")
b8.out("K")

# 8. BOS #5  Jonny Gomes (X - X - X)
b8.new_ab()
b8.pitch_list("b b c b c f b")
b8.reach("BB")

# 9. BOS #44 Jackie Bradley Jr. (X - X - 5)
b8.new_ab()
b8.pitch_list("1 c b b s b s")
b8.out("K")

# 1. BOS #2  Jacoby Ellsbury (X - X - 5)
b8.new_ab()
b8.pitch_list("b b f c")
b8.out("(F)P5")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #40 Andrew Bailey
t9 = game.new_inning()

# Pitching change (BOS): #40 Andrew Bailey replaces #19 Koji Uehara
t9.pitching_substitution(40)

# 1. TBR #8  Desmond Jennings (X - X - X)
t9.new_ab()
t9.pitch_list("b c b f f")
t9.hit(1)
t9.advance(2, "18 SB")
t9.advance(4, "18 1B")

# 2. TBR #18 Ben Zobrist (X - X - 8)
t9.new_ab()
t9.pitch_list("c d b b c")
t9.hit(1, rbis=1)
t9.advance(2, "T")

# 3. TBR #3  Evan Longoria (X - 18 - X)
t9.new_ab()
t9.pitch_list("d s f b f f b s")
t9.out("K")

# 4. TBR #20 Matt Joyce (X - 18 - X)
t9.new_ab()
t9.pitch_list("t b b f c")
t9.out("!K")

# 5. TBR #19 Ryan Roberts (X - 18 - X)
t9.new_ab()
t9.out("P4")


# Bot 9th
# Pitching: TBR #62 Joel Peralta
b9 = game.new_inning()

# Pitching change (TBR): #62 Joel Peralta replaces #57 Jake McGee
b9.pitching_substitution(62)

# 2. BOS #18 Shane Victorino (X - X - X)
b9.new_ab()
b9.pitch_list("c f f")
b9.out("F7")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b9.new_ab()
b9.pitch_list("c b b f b f b")
b9.reach("BB")
b9.advance(4, "12 2B")

# 4. BOS #12 Mike Napoli (X - X - 15)
b9.new_ab()
b9.pitch_list("1 1 b b c f")
b9.hit(2, rbis=1)

# Winning team: BOS
# WP: BOS #40 Andrew Bailey
game.winning_pitcher(40)

# Loser team: TBR
# LP: TBR #62 Joel Peralta
game.losing_pitcher(62, is_away_team=True)

# print(game)
game.generate_scorecard()
