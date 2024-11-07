import os
from baseball_scorecard.baseball_scorecard import Scorecard

# TB @ BOS, 2013-04-14
# https://www.baseball-reference.com/boxes/BOS/BOS201304140.shtml
# https://www.mlb.com/gameday/rays-vs-red-sox/2013/04/14/346922/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-04-14 13:38-16:27",
        "at": "Fenway Park, Boston, MA",
        "att": "35,198",
        "temp": "50F, Partly Cloudy",
        "wind": "14mph, Out To RF",
        "away": {
            "team": "Tampa Bay Rays",
            "starter": 53,
            "roster": {
                # Lineup
                8: "Desmond Jennings",
                18: "Ben Zobrist",
                3: "Evan Longoria",
                20: "Matt Joyce",
                11: "Yunel Escobar",
                21: "James Loney",
                28: "José Molina",
                2: "Kelly Johnson",
                5: "Sam Fuld",
                # Starting pitcher
                53: "Alex Cobb",
                # Bench
                1: "Sean Rodríguez",
                15: "Shelley Duncan",
                19: "Ryan Roberts",
                59: "Jose Lobaton",
                # Bullpen
                58: "Jeremy Hellickson",
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
                [18, "4"],
                [3, "5"],
                [20, "0"],
                [11, "6"],
                [21, "3"],
                [28, "2"],
                [2, "7"],
                [5, "9"],
            ],
            "bench": [
                [1, "2B"],
                [15, "LF"],
                [19, "3B"],
                [59, "C"],
            ],
            "bullpen": [58, 47, 55, 62, 35, 43, 57, 27, 14, 56, 40],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 11,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                12: "Mike Napoli",
                29: "Daniel Nava",
                16: "Will Middlebrooks",
                7: "Stephen Drew",
                39: "Jarrod Saltalamacchia",
                44: "Jackie Bradley Jr.",
                # Starting pitcher
                11: "Clay Buchholz",
                # Bench
                3: "David Ross",
                37: "Mike Carp",
                23: "Pedro Ciriaco",
                5: "Jonny Gomes",
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
                46: "Ryan Dempster",
            },
            "lefties": [30, 31, 22],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [12, "3"],
                [29, "0"],
                [16, "5"],
                [7, "6"],
                [39, "2"],
                [44, "7"],
            ],
            "bench": [
                [3, "C"],
                [37, "1B"],
                [23, "3B"],
                [5, "LF"],
            ],
            "bullpen": [63, 40, 30, 19, 91, 31, 59, 36, 22, 46],
        },
        "umpires": {
            "HP": "John Tumpane",
            "1B": "Dana DeMuth",
            "2B": "Angel Hernandez",
            "3B": "Doug Eddings",
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
# Pitching: BOS #11 Clay Buchholz
t1 = game.new_inning()

# 1. TBR #8  Desmond Jennings (X - X - X)
t1.new_ab()
t1.pitch_list("c c s")
t1.out("K")

# 2. TBR #18 Ben Zobrist (X - X - X)
t1.new_ab()
t1.out("G6-3")

# 3. TBR #3  Evan Longoria (X - X - X)
t1.new_ab()
t1.pitch_list("c b s b b c")
t1.out("!K")


# Bot 1st
# Pitching: TBR #53 Alex Cobb
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("c b c f b f")
b1.out("L3")

# 2. BOS #18 Shane Victorino (X - X - X)
b1.new_ab()
b1.pitch_list("c")
b1.out("G4-3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b1.new_ab()
b1.pitch_list("b f c f f")
b1.hit(1)
b1.advance(2, "12 SB")

# 4. BOS #12 Mike Napoli (X - X - 15)
b1.new_ab(is_risp=True)
b1.pitch_list("b b f f")
b1.out("F9")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #11 Clay Buchholz
t2 = game.new_inning()

# 4. TBR #20 Matt Joyce (X - X - X)
t2.new_ab()
t2.pitch_list("c b b b f c")
t2.out("!K")

# 5. TBR #11 Yunel Escobar (X - X - X)
t2.new_ab()
t2.out("G3-1")

# 6. TBR #21 James Loney (X - X - X)
t2.new_ab()
t2.pitch_list("b c c b b f b")
t2.reach("BB")
t2.advance(2, "28 SB")

# 7. TBR #28 José Molina (X - X - 21)
t2.new_ab(is_risp=True)
t2.pitch_list("b c f s")
t2.out("K")


# Bot 2nd
# Pitching: TBR #53 Alex Cobb
b2 = game.new_inning()

# 5. BOS #29 Daniel Nava (X - X - X)
b2.new_ab()
b2.pitch_list("b b c")
b2.out("F7")

# 6. BOS #16 Will Middlebrooks (X - X - X)
b2.new_ab()
b2.pitch_list("b b f")
b2.out("G5-3")

# 7. BOS #7  Stephen Drew (X - X - X)
b2.new_ab()
b2.pitch_list("b b b c b")
b2.reach("BB")
b2.advance(2, "39 1B")

# 8. BOS #39 Jarrod Saltalamacchia (X - X - 7)
b2.new_ab()
b2.pitch_list("b 1 b")
b2.hit(1)

# 9. BOS #44 Jackie Bradley Jr. (X - 7 - 39)
b2.new_ab(is_risp=True)
b2.pitch_list("b b b c")
b2.out("F9")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #11 Clay Buchholz
t3 = game.new_inning()

# 8. TBR #2  Kelly Johnson (X - X - X)
t3.new_ab()
t3.pitch_list("c c b s")
t3.out("K")

# 9. TBR #5  Sam Fuld (X - X - X)
t3.new_ab()
t3.pitch_list("b c f f f c")
t3.out("!K")

# 1. TBR #8  Desmond Jennings (X - X - X)
t3.new_ab()
t3.pitch_list("c b b")
t3.out("L8")


# Bot 3rd
# Pitching: TBR #53 Alex Cobb
b3 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b3.new_ab()
b3.pitch_list("f")
b3.hit(1)
b3.advance(2, "18 1B")
b3.advance(3, "15 1B")
b3.advance(4, "12 2B")

# 2. BOS #18 Shane Victorino (X - X - 2)
b3.new_ab()
b3.hit(1)
b3.advance(2, "15 1B")
b3.advance(4, "12 2B")

# 3. BOS #15 Dustin Pedroia (X - 2 - 18)
b3.new_ab(is_risp=True)
b3.pitch_list("b")
b3.hit(1)
b3.advance(3, "12 2B")
b3.thrown_out(4, "16 FC1-2", 1, 53)

# 4. BOS #12 Mike Napoli (2 - 18 - 15)
b3.new_ab(is_risp=True)
b3.pitch_list("b")
b3.hit(2, rbis=2)
b3.advance(3, "16 FC1-2")
b3.advance(4, "7 FC3-6")

# 5. BOS #29 Daniel Nava (15 - 12 - X)
b3.new_ab(is_risp=True)
b3.pitch_list("b")
b3.reach("HBP")
b3.advance(2, "16 FC1-2")
b3.error(6)
b3.advance("U", "7 E6")

# 6. BOS #16 Will Middlebrooks (15 - 12 - 29)
b3.new_ab(is_risp=True)
b3.pitch_list("c")
b3.reach("FC1-2")
b3.thrown_out(2, "7 FC3-6", 2, 53)

# 7. BOS #7  Stephen Drew (12 - 29 - 16)
b3.new_ab(is_risp=True)
b3.pitch_list("c c")
b3.reach("FC3-6", rbis=1)
b3.advance(2, "E6")

# 8. BOS #39 Jarrod Saltalamacchia (X - 7 - X)
b3.new_ab(is_risp=True)
b3.pitch_list("f s s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #11 Clay Buchholz
t4 = game.new_inning()

# 2. TBR #18 Ben Zobrist (X - X - X)
t4.new_ab()
t4.pitch_list("b b b b")
t4.reach("BB")
t4.advance(2, "20 SB")

# 3. TBR #3  Evan Longoria (X - X - 18)
t4.new_ab()
t4.pitch_list("f b 1 f s")
t4.out("K")

# 4. TBR #20 Matt Joyce (X - X - 18)
t4.new_ab(is_risp=True)
t4.pitch_list("b s f s")
t4.out("K")

# 5. TBR #11 Yunel Escobar (X - 18 - X)
t4.new_ab(is_risp=True)
t4.pitch_list("b s b")
t4.out("F9")


# Bot 4th
# Pitching: TBR #53 Alex Cobb
b4 = game.new_inning()

# 9. BOS #44 Jackie Bradley Jr. (X - X - X)
b4.new_ab()
b4.pitch_list("c c b s")
b4.out("K")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b4.new_ab()
b4.pitch_list("c c s")
b4.out("K")

# 2. BOS #18 Shane Victorino (X - X - X)
b4.new_ab()
b4.pitch_list("c")
b4.out("G3-1")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #11 Clay Buchholz
t5 = game.new_inning()

# 6. TBR #21 James Loney (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.out("F7")

# 7. TBR #28 José Molina (X - X - X)
t5.new_ab()
t5.pitch_list("s b f")
t5.out("G6-3")

# 8. TBR #2  Kelly Johnson (X - X - X)
t5.new_ab()
t5.pitch_list("b s s c")
t5.out("!K")


# Bot 5th
# Pitching: TBR #53 Alex Cobb
b5 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
b5.new_ab()
b5.pitch_list("b c b")
b5.out("G5-3")

# 4. BOS #12 Mike Napoli (X - X - X)
b5.new_ab()
b5.pitch_list("c f f b s")
b5.out("K")

# 5. BOS #29 Daniel Nava (X - X - X)
b5.new_ab()
b5.pitch_list("c b b b")
b5.out("F7")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #11 Clay Buchholz
t6 = game.new_inning()

# 9. TBR #5  Sam Fuld (X - X - X)
t6.new_ab()
t6.pitch_list("c b b c b b")
t6.reach("BB")
t6.advance(2, "8 G6-4-3")
t6.advance(3, "3 F9")

# 1. TBR #8  Desmond Jennings (X - X - 5)
t6.new_ab()
t6.pitch_list("b c b c")
t6.out("G6-4-3")

# 2. TBR #18 Ben Zobrist (X - 5 - X)
t6.new_ab(is_risp=True)
t6.pitch_list("b b b c b")
t6.reach("BB")

# 3. TBR #3  Evan Longoria (X - 5 - 18)
t6.new_ab(is_risp=True)
t6.pitch_list("f c b")
t6.out("F9")

# 4. TBR #20 Matt Joyce (5 - X - 18)
t6.new_ab(is_risp=True)
t6.pitch_list("s")
t6.out("G3-1")


# Bot 6th
# Pitching: TBR #53 Alex Cobb
b6 = game.new_inning()

# 6. BOS #16 Will Middlebrooks (X - X - X)
b6.new_ab()
b6.pitch_list("b")
b6.hit(1)
b6.thrown_out(2, "44 CS", 3, 53)

# 7. BOS #7  Stephen Drew (X - X - 16)
b6.new_ab()
b6.pitch_list("c f 1 f d 1 c")
b6.out("!K")

# 8. BOS #39 Jarrod Saltalamacchia (X - X - 16)
b6.new_ab()
b6.pitch_list("b 1 b")
b6.out("F9")

# 9. BOS #44 Jackie Bradley Jr. (X - X - 16)
b6.new_ab()
b6.pitch_list("d s")
b6.no_ab("CS")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #11 Clay Buchholz
t7 = game.new_inning()

# 5. TBR #11 Yunel Escobar (X - X - X)
t7.new_ab()
t7.pitch_list("c t s")
t7.out("K")

# 6. TBR #21 James Loney (X - X - X)
t7.new_ab()
t7.pitch_list("c")
t7.out("G3")

# 7. TBR #28 José Molina (X - X - X)
t7.new_ab()
t7.pitch_list("c b t c")
t7.out("!K")


# Bot 7th
# Pitching: TBR #53 Alex Cobb
b7 = game.new_inning()

# 9. BOS #44 Jackie Bradley Jr. (X - X - X)
b7.new_ab()
b7.pitch_list("c b c f b f s")
b7.out("K")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b7.new_ab()
b7.pitch_list("c")
b7.out("G1-3")

# 2. BOS #18 Shane Victorino (X - X - X)
b7.new_ab()
b7.pitch_list("b b b b")
b7.reach("BB")
b7.thrown_out(1, "15 PO", 3, 35)

# Pitching change (TBR): #35 Jamey Wright replaces #53 Alex Cobb
b7.pitching_substitution(35)

# 3. BOS #15 Dustin Pedroia (X - X - 18)
b7.new_ab()
b7.pitch_list("1")
b7.no_ab("PO")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #11 Clay Buchholz
t8 = game.new_inning()

# 8. TBR #2  Kelly Johnson (X - X - X)
t8.new_ab()
t8.pitch_list("c")
t8.hit(1)
t8.thrown_out(2, "5 DP3-6-1", 1, 11)

# 9. TBR #5  Sam Fuld (X - X - 2)
t8.new_ab()
t8.out("DP3-6-1")

# 1. TBR #8  Desmond Jennings (X - X - X)
t8.new_ab()
t8.pitch_list("c b")
t8.hit(2)

# 2. TBR #18 Ben Zobrist (X - 8 - X)
t8.new_ab(is_risp=True)
t8.pitch_list("b c b")
t8.out("F7")


# Bot 8th
# Pitching: TBR #35 Jamey Wright
b8 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
b8.new_ab()
b8.pitch_list("c b")
b8.hit(2)
b8.advance(3, "12 G6-3")
b8.advance(4, "16 SF9")

# 4. BOS #12 Mike Napoli (X - 15 - X)
b8.new_ab(is_risp=True)
b8.pitch_list("c c f b b")
b8.out("G6-3")

# 5. BOS #29 Daniel Nava (15 - X - X)
b8.new_ab(is_risp=True)
b8.pitch_list("i i i i")
b8.reach("IBB")

# 6. BOS #16 Will Middlebrooks (15 - X - 29)
b8.new_ab(is_risp=True)
b8.out("SF9", rbis=1)

# 7. BOS #7  Stephen Drew (X - X - 29)
b8.new_ab()
b8.pitch_list("f c b b b")
b8.out("G3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #30 Andrew Miller
t9 = game.new_inning()

# Pitching change (BOS): #30 Andrew Miller replaces #11 Clay Buchholz
t9.pitching_substitution(30)

# 3. TBR #3  Evan Longoria (X - X - X)
t9.new_ab()
t9.pitch_list("c b b")
t9.hit(1)
t9.thrown_out(2, "15 DP6-4-3", 1, 30)

# Offensive change (TBR): Pinch-hitter #15 Shelley Duncan replaces #20 Matt Joyce, batting 4th
t9.offensive_substitution(4, 15, "PH")

# 4. TBR #15 Shelley Duncan (X - X - 3)
t9.new_ab()
t9.pitch_list("b c")
t9.out("DP6-4-3")

# 5. TBR #11 Yunel Escobar (X - X - X)
t9.new_ab()
t9.pitch_list("c b f b f b f c")
t9.out("!K")

# Winning team: BOS
# WP: BOS #11 Clay Buchholz
game.winning_pitcher(11)

# Loser team: TBR
# LP: TBR #53 Alex Cobb
game.losing_pitcher(53, is_away_team=True)

# print(game)
game.generate_scorecard()
