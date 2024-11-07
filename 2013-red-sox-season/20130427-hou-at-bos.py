import os
from baseball_scorecard.baseball_scorecard import Scorecard

# HOU @ BOS, 2013-04-27
# https://www.baseball-reference.com/boxes/BOS/BOS201304270.shtml
# https://www.mlb.com/gameday/astros-vs-red-sox/2013/04/27/347097/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-04-27 19:09-22:49",
        "at": "Fenway Park, Boston, MA",
        "att": "34,726",
        "temp": "59F, Partly Cloudy",
        "wind": "15mph, R To L",
        "away": {
            "team": "Houston Astros",
            "starter": 43,
            "roster": {
                # Lineup
                27: "Jose Altuve",
                2: "Brandon Barnes",
                4: "Brandon Laird",
                23: "Chris Carter",
                13: "Ronny Cedeno",
                22: "Carlos Corporán",
                30: "Matt Dominguez",
                9: "Marwin Gonzalez",
                19: "Robbie Grossman",
                # Starting pitcher
                43: "Brad Peacock",
                # Bench
                15: "Jason Castro",
                28: "Rick Ankiel",
                21: "Fernando Martinez",
                12: "Carlos Pena",
                # Bullpen
                45: "Erik Bedard",
                62: "Hector Ambriz",
                53: "Wesley Wright",
                20: "Bud Norris",
                64: "Lucas Harrell",
                41: "Jose Veras",
                59: "Philip Humber",
                54: "Travis Blackley",
                56: "Paul Clemens",
                68: "José Cisnero",
                55: "Rhiner Cruz",
            },
            "lefties": [45, 53, 54],
            "lineup": [
                [27, "4"],
                [2, "9"],
                [4, "3"],
                [23, "7"],
                [13, "0"],
                [22, "2"],
                [30, "5"],
                [9, "6"],
                [19, "8"],
            ],
            "bench": [
                [15, "C"],
                [28, "CF"],
                [21, "LF"],
                [12, "1B"],
            ],
            "bullpen": [45, 62, 53, 20, 64, 41, 59, 54, 56, 68, 55],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 22,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                29: "Daniel Nava",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                37: "Mike Carp",
                39: "Jarrod Saltalamacchia",
                16: "Will Middlebrooks",
                7: "Stephen Drew",
                # Starting pitcher
                22: "Felix Doubront",
                # Bench
                18: "Shane Victorino",
                5: "Jonny Gomes",
                3: "David Ross",
                23: "Pedro Ciriaco",
                20: "Ryan Lavarnway",
                # Bullpen
                63: "Alex Wilson",
                40: "Andrew Bailey",
                30: "Andrew Miller",
                31: "Jon Lester",
                59: "Clayton Mortensen",
                36: "Junichi Tazawa",
                11: "Clay Buchholz",
                51: "Daniel Bard",
                19: "Koji Uehara",
                46: "Ryan Dempster",
            },
            "lefties": [22, 30, 31],
            "lineup": [
                [2, "8"],
                [29, "9"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [37, "7"],
                [39, "2"],
                [16, "5"],
                [7, "6"],
            ],
            "bench": [
                [18, "CF"],
                [5, "LF"],
                [3, "C"],
                [23, "3B"],
                [20, "C"],
            ],
            "bullpen": [63, 40, 30, 31, 59, 36, 11, 51, 19, 46],
        },
        "umpires": {
            "HP": "Marvin Hudson",
            "1B": "Jordan Baker",
            "2B": "Tim McClelland",
            "3B": "Jerry Meals",
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

# 1. HOU #27 Jose Altuve (X - X - X)
t1.new_ab()
t1.pitch_list("b")
t1.hit(1)
t1.advance(2, "2 HBP")
t1.advance(3, "4 WP")
t1.advance(4, "23 BB")

# 2. HOU #2  Brandon Barnes (X - X - 27)
t1.new_ab()
t1.pitch_list("1 b d 1 1 t f")
t1.reach("HBP")
t1.advance(2, "4 WP")
t1.advance(3, "23 BB")
t1.advance(4, "13 SF8")

# 3. HOU #4  Brandon Laird (X - 27 - 2)
t1.new_ab(is_risp=True)
t1.pitch_list("b b b c b")
t1.wp()
t1.reach("BB")
t1.advance(2, "23 BB")
t1.advance(3, "22 BB")

# 4. HOU #23 Chris Carter (27 - 2 - 4)
t1.new_ab(is_risp=True)
t1.pitch_list("b b c b c b")
t1.reach("BB", rbis=1)
t1.advance(2, "22 BB")

# 5. HOU #13 Ronny Cedeno (2 - 4 - 23)
t1.new_ab(is_risp=True)
t1.out("SF8", rbis=1)

# 6. HOU #22 Carlos Corporán (X - 4 - 23)
t1.new_ab(is_risp=True)
t1.pitch_list("b b b b")
t1.reach("BB")

# 7. HOU #30 Matt Dominguez (4 - 23 - 22)
t1.new_ab(is_risp=True)
t1.pitch_list("c")
t1.out("P6")

# 8. HOU #9  Marwin Gonzalez (4 - 23 - 22)
t1.new_ab(is_risp=True)
t1.pitch_list("c c f b f s")
t1.out("K")


# Bot 1st
# Pitching: HOU #43 Brad Peacock
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("b c f b")
b1.out("G4-3")

# 2. BOS #29 Daniel Nava (X - X - X)
b1.new_ab()
b1.pitch_list("c b b b")
b1.out("L3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b1.new_ab()
b1.pitch_list("c")
b1.hit(1)
b1.error(8)
b1.advance(2, "34 1B")
b1.advance(3, "34 E8")

# 4. BOS #34 David Ortiz (X - X - 15)
b1.new_ab()
b1.pitch_list("b 1 c s")
b1.hit(1)

# 5. BOS #12 Mike Napoli (15 - X - 34)
b1.new_ab(is_risp=True)
b1.pitch_list("b s b f c")
b1.out("!K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #22 Felix Doubront
t2 = game.new_inning()

# 9. HOU #19 Robbie Grossman (X - X - X)
t2.new_ab()
t2.pitch_list("c")
t2.out("G5-3")

# 1. HOU #27 Jose Altuve (X - X - X)
t2.new_ab()
t2.pitch_list("f m b b c")
t2.out("!K")

# 2. HOU #2  Brandon Barnes (X - X - X)
t2.new_ab()
t2.pitch_list("f b f b b b")
t2.reach("BB")

# 3. HOU #4  Brandon Laird (X - X - 2)
t2.new_ab()
t2.pitch_list("t f c")
t2.out("!K")


# Bot 2nd
# Pitching: HOU #43 Brad Peacock
b2 = game.new_inning()

# 6. BOS #37 Mike Carp (X - X - X)
b2.new_ab()
b2.pitch_list("c b")
b2.out("G1-3")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b2.new_ab()
b2.pitch_list("b b s s b b")
b2.reach("BB")
b2.advance(3, "16 2B")
b2.advance(4, "2 1B")

# 8. BOS #16 Will Middlebrooks (X - X - 39)
b2.new_ab()
b2.pitch_list("c b")
b2.hit(2)
b2.advance(4, "2 1B")

# 9. BOS #7  Stephen Drew (39 - 16 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("b c b b c f b")
b2.reach("BB")
b2.advance(2, "2 1B")
b2.advance(3, "29 G4-3")
b2.advance(4, "34 2B")

# 1. BOS #2  Jacoby Ellsbury (39 - 16 - 7)
b2.new_ab(is_risp=True)
b2.pitch_list("c f")
b2.hit(1, rbis=2)
b2.advance(2, "29 G4-3")
b2.advance(4, "34 2B")

# 2. BOS #29 Daniel Nava (X - 7 - 2)
b2.new_ab(is_risp=True)
b2.pitch_list("c f")
b2.out("G4-3")

# 3. BOS #15 Dustin Pedroia (7 - 2 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("b b c b b")
b2.reach("BB")
b2.advance(3, "34 2B")

# 4. BOS #34 David Ortiz (7 - 2 - 15)
b2.new_ab(is_risp=True)
b2.pitch_list("b")
b2.hit(2, rbis=2)

# 5. BOS #12 Mike Napoli (15 - 34 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("f b b b b")
b2.reach("BB")

# 6. BOS #37 Mike Carp (15 - 34 - 12)
b2.new_ab(is_risp=True)
b2.pitch_list("s b s f s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #22 Felix Doubront
t3 = game.new_inning()

# 4. HOU #23 Chris Carter (X - X - X)
t3.new_ab()
t3.pitch_list("c s s")
t3.out("K")

# 5. HOU #13 Ronny Cedeno (X - X - X)
t3.new_ab()
t3.pitch_list("b c s s")
t3.out("K")

# 6. HOU #22 Carlos Corporán (X - X - X)
t3.new_ab()
t3.pitch_list("c b c b s")
t3.out("K")


# Bot 3rd
# Pitching: HOU #43 Brad Peacock
b3 = game.new_inning()

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b3.new_ab()
b3.pitch_list("b c b l f c")
b3.out("!K")

# 8. BOS #16 Will Middlebrooks (X - X - X)
b3.new_ab()
b3.pitch_list("c b f f b")
b3.out("F8")

# 9. BOS #7  Stephen Drew (X - X - X)
b3.new_ab()
b3.pitch_list("b f b b b")
b3.reach("BB")

# 1. BOS #2  Jacoby Ellsbury (X - X - 7)
b3.new_ab()
b3.out("F7")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #22 Felix Doubront
t4 = game.new_inning()

# 7. HOU #30 Matt Dominguez (X - X - X)
t4.new_ab()
t4.pitch_list("c b c")
t4.out("G5-3")

# 8. HOU #9  Marwin Gonzalez (X - X - X)
t4.new_ab()
t4.hit(2)
t4.advance(3, "19 G6-3")

# 9. HOU #19 Robbie Grossman (X - 9 - X)
t4.new_ab(is_risp=True)
t4.pitch_list("d b")
t4.out("G6-3")

# 1. HOU #27 Jose Altuve (9 - X - X)
t4.new_ab(is_risp=True)
t4.pitch_list("b d c b c")
t4.out("G6-3")


# Bot 4th
# Pitching: HOU #43 Brad Peacock
b4 = game.new_inning()

# 2. BOS #29 Daniel Nava (X - X - X)
b4.new_ab()
b4.pitch_list("c b c")
b4.hit(2)
b4.advance(3, "15 G4-3")
b4.advance(4, "34 SF7")

# 3. BOS #15 Dustin Pedroia (X - 29 - X)
b4.new_ab(is_risp=True)
b4.pitch_list("b b f f")
b4.out("G4-3")

# Pitching change (HOU): #54 Travis Blackley replaces #43 Brad Peacock
b4.pitching_substitution(54)

# 4. BOS #34 David Ortiz (29 - X - X)
b4.new_ab(is_risp=True)
b4.pitch_list("s s b")
b4.out("SF7", rbis=1)

# 5. BOS #12 Mike Napoli (X - X - X)
b4.new_ab()
b4.pitch_list("b s b b f")
b4.hit(1)

# 6. BOS #37 Mike Carp (X - X - 12)
b4.new_ab()
b4.pitch_list("s b f 1 b c")
b4.out("!K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #22 Felix Doubront
t5 = game.new_inning()

# 2. HOU #2  Brandon Barnes (X - X - X)
t5.new_ab()
t5.pitch_list("b b c s c")
t5.out("!K")

# 3. HOU #4  Brandon Laird (X - X - X)
t5.new_ab()
t5.pitch_list("b")
t5.out("G5-3")

# 4. HOU #23 Chris Carter (X - X - X)
t5.new_ab()
t5.pitch_list("c f s")
t5.out("K")


# Bot 5th
# Pitching: HOU #54 Travis Blackley
b5 = game.new_inning()

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b5.new_ab()
b5.pitch_list("b f s b s")
b5.out("K")

# 8. BOS #16 Will Middlebrooks (X - X - X)
b5.new_ab()
b5.pitch_list("c b b")
b5.hit(1)
b5.advance(2, "7 G3")

# 9. BOS #7  Stephen Drew (X - X - 16)
b5.new_ab()
b5.pitch_list("f c")
b5.out("G3")

# 1. BOS #2  Jacoby Ellsbury (X - 16 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("d f f b")
b5.out("G1-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #22 Felix Doubront
t6 = game.new_inning()

# 5. HOU #13 Ronny Cedeno (X - X - X)
t6.new_ab()
t6.out("G6-3")

# 6. HOU #22 Carlos Corporán (X - X - X)
t6.new_ab()
t6.pitch_list("b c b")
t6.out("G1-3")

# 7. HOU #30 Matt Dominguez (X - X - X)
t6.new_ab()
t6.pitch_list("c c b f b f")
t6.out("(F)P5")


# Bot 6th
# Pitching: HOU #53 Wesley Wright
b6 = game.new_inning()

# Pitching change (HOU): #53 Wesley Wright replaces #54 Travis Blackley
b6.pitching_substitution(53)

# 2. BOS #29 Daniel Nava (X - X - X)
b6.new_ab()
b6.pitch_list("c c f b f b f s")
b6.out("K")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b6.new_ab()
b6.pitch_list("b b b c b")
b6.reach("BB")
b6.advance(2, "34 SB")
b6.thrown_out(2, "12 DP6-4", 3, 53)

# 4. BOS #34 David Ortiz (X - X - 15)
b6.new_ab(is_risp=True)
b6.pitch_list("b b d b")
b6.reach("BB")

# 5. BOS #12 Mike Napoli (X - 15 - 34)
b6.new_ab(is_risp=True)
b6.pitch_list("c b b 2 b")
b6.out("DP6-4")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #22 Felix Doubront
t7 = game.new_inning()

# 8. HOU #9  Marwin Gonzalez (X - X - X)
t7.new_ab()
t7.hit(1)
t7.advance(2, "19 PB")
t7.advance(3, "27 SB")
t7.advance(4, "27 G5-3")

# 9. HOU #19 Robbie Grossman (X - X - 9)
t7.new_ab(is_risp=True)
t7.pitch_list("b")
t7.pb()
t7.out("G2-3")

# 1. HOU #27 Jose Altuve (X - 9 - X)
t7.new_ab(is_risp=True)
t7.pitch_list("b c")
t7.out("G5-3", rbis=1)

# 2. HOU #2  Brandon Barnes (X - X - X)
t7.new_ab()
t7.pitch_list("c")
t7.hit(1)
t7.advance(2, "21 BLK")

# Pitching change (BOS): #36 Junichi Tazawa replaces #22 Felix Doubront
t7.pitching_substitution(36)

# Offensive change (HOU): Pinch-hitter #21 Fernando Martinez replaces #4 Brandon Laird, batting 3rd
t7.offensive_substitution(3, 21, "PH")

# 3. HOU #21 Fernando Martinez (X - X - 2)
t7.new_ab(is_risp=True)
t7.pitch_list("n f b b s b d")
t7.balk()
t7.reach("BB")

# 4. HOU #23 Chris Carter (X - 2 - 21)
t7.new_ab(is_risp=True)
t7.pitch_list("f f b b s")
t7.out("K")


# Bot 7th
# Pitching: HOU #62 Hector Ambriz
b7 = game.new_inning()

# Pitching change (HOU): #62 Hector Ambriz replaces #53 Wesley Wright
b7.pitching_substitution(62)

# Defensive switch (HOU): #21 Fernando Martinez moves to LF
b7.defensive_switch(21, "7")

# Defensive switch (HOU): #23 Chris Carter moves to 1B
b7.defensive_switch(23, "3")

# Offensive change (BOS): Pinch-hitter #5 Jonny Gomes replaces #37 Mike Carp, batting 6th
b7.offensive_substitution(6, 5, "PH")

# 6. BOS #5  Jonny Gomes (X - X - X)
b7.new_ab()
b7.pitch_list("b c c b")
b7.out("F9")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b7.new_ab()
b7.hit(2)
b7.advance(4, "7 1B")

# 8. BOS #16 Will Middlebrooks (X - 39 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("b b b c c b")
b7.reach("BB")
b7.advance(2, "7 1B")
b7.advance(4, "29 1B")

# 9. BOS #7  Stephen Drew (X - 39 - 16)
b7.new_ab(is_risp=True)
b7.hit(1, rbis=1)
b7.advance(3, "29 1B")
b7.advance(4, "15 1B")

# 1. BOS #2  Jacoby Ellsbury (X - 16 - 7)
b7.new_ab(is_risp=True)
b7.pitch_list("s c f b t")
b7.out("KT")

# 2. BOS #29 Daniel Nava (X - 16 - 7)
b7.new_ab(is_risp=True)
b7.pitch_list("b c b")
b7.hit(1, rbis=1)
b7.advance(2, "15 1B")

# 3. BOS #15 Dustin Pedroia (7 - X - 29)
b7.new_ab(is_risp=True)
b7.pitch_list("c")
b7.hit(1, rbis=1)

# 4. BOS #34 David Ortiz (X - 29 - 15)
b7.new_ab(is_risp=True)
b7.pitch_list("b")
b7.out("F8")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #51 Daniel Bard
t8 = game.new_inning()

# Pitching change (BOS): #51 Daniel Bard replaces #36 Junichi Tazawa
t8.pitching_substitution(51)

# Defensive switch (BOS): #5 Jonny Gomes moves to LF
t8.defensive_switch(5, "7")

# Offensive change (HOU): Pinch-hitter #12 Carlos Pena replaces #13 Ronny Cedeno, batting 5th
t8.offensive_substitution(5, 12, "PH")

# 5. HOU #12 Carlos Pena (X - X - X)
t8.new_ab()
t8.pitch_list("b b b b")
t8.reach("BB")
t8.advance(2, "22 BB")
t8.advance(4, "30 1B")

# 6. HOU #22 Carlos Corporán (X - X - 12)
t8.new_ab()
t8.pitch_list("b b c d b")
t8.reach("BB")
t8.advance(2, "30 1B")
t8.advance(3, "27 E6")

# Pitching change (BOS): #63 Alex Wilson replaces #51 Daniel Bard
t8.pitching_substitution(63)

# 7. HOU #30 Matt Dominguez (X - 12 - 22)
t8.new_ab(is_risp=True)
t8.pitch_list("b")
t8.hit(1, rbis=1)
t8.advance(2, "27 E6")

# 8. HOU #9  Marwin Gonzalez (X - 22 - 30)
t8.new_ab(is_risp=True)
t8.pitch_list("c")
t8.out("F9")

# 9. HOU #19 Robbie Grossman (X - 22 - 30)
t8.new_ab(is_risp=True)
t8.pitch_list("b d f b f")
t8.out("L7")

# 1. HOU #27 Jose Altuve (X - 22 - 30)
t8.new_ab(is_risp=True)
t8.error(6)
t8.reach("E6")

# Offensive change (HOU): Pinch-hitter #28 Rick Ankiel replaces #2 Brandon Barnes, batting 2nd
t8.offensive_substitution(2, 28, "PH")

# 2. HOU #28 Rick Ankiel (22 - 30 - 27)
t8.new_ab(is_risp=True)
t8.pitch_list("d c t s")
t8.out("K")


# Bot 8th
# Pitching: HOU #41 Jose Veras
b8 = game.new_inning()

# Pitching change (HOU): #41 Jose Veras replaces #62 Hector Ambriz
b8.pitching_substitution(41)

# Defensive switch (HOU): #28 Rick Ankiel moves to RF
b8.defensive_switch(28, "9")

# Defensive switch (HOU): #12 Carlos Pena moves to DH
b8.defensive_switch(12, "0")

# 5. BOS #12 Mike Napoli (X - X - X)
b8.new_ab()
b8.pitch_list("b s")
b8.out("G5-3")

# 6. BOS #5  Jonny Gomes (X - X - X)
b8.new_ab()
b8.pitch_list("c c s")
b8.out("K")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b8.new_ab()
b8.pitch_list("b s b s d f")
b8.out("F7")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #30 Andrew Miller
t9 = game.new_inning()

# Pitching change (BOS): #30 Andrew Miller replaces #63 Alex Wilson
t9.pitching_substitution(30)

# 3. HOU #21 Fernando Martinez (X - X - X)
t9.new_ab()
t9.pitch_list("c s b f")
t9.out("G5-3")

# 4. HOU #23 Chris Carter (X - X - X)
t9.new_ab()
t9.pitch_list("c s c")
t9.out("!K")

# 5. HOU #12 Carlos Pena (X - X - X)
t9.new_ab()
t9.pitch_list("b c c b b s")
t9.out("K")

# Winning team: BOS
# WP: BOS #22 Felix Doubront
game.winning_pitcher(22)

# Loser team: HOU
# LP: HOU #43 Brad Peacock
game.losing_pitcher(43, is_away_team=True)

# print(game)
game.generate_scorecard()
