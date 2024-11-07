import os
from baseball_scorecard.baseball_scorecard import Scorecard

# AZ @ BOS, 2013-08-02
# https://www.baseball-reference.com/boxes/BOS/BOS201308020.shtml
# https://www.mlb.com/gameday/d-backs-vs-red-sox/2013/08/02/348367/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-08-02 19:13-22:45",
        "at": "Fenway Park, Boston, MA",
        "att": "37,652",
        "temp": "82F, Partly Cloudy",
        "wind": "15mph, Out To RF",
        "away": {
            "team": "Arizona Diamondbacks",
            "starter": 48,
            "roster": {
                # Lineup
                11: "AJ Pollock",
                2: "Aaron Hill",
                44: "Paul Goldschmidt",
                14: "Martín Prado",
                7: "Cody Ross",
                13: "Jason Kubel",
                27: "Wil Nieves",
                8: "Gerardo Parra",
                1: "Didi Gregorius",
                # Starting pitcher
                48: "Randall Delgado",
                # Bench
                6: "Adam Eaton",
                54: "Tuffy Gosewisch",
                12: "Eric Chavez",
                4: "Cliff Pennington",
                # Bullpen
                40: "J.J. Putz",
                38: "Will Harris",
                36: "Wade Miley",
                30: "David Hernandez",
                52: "Zeke Spruill",
                55: "Josh Collmenter",
                46: "Patrick Corbin",
                21: "Heath Bell",
                49: "Tony Sipp",
                29: "Brad Ziegler",
                54: "Joe Thatcher",
            },
            "lefties": [36, 46, 49, 54],
            "lineup": [
                [11, "8"],
                [2, "4"],
                [44, "3"],
                [14, "5"],
                [7, "7"],
                [13, "0"],
                [27, "2"],
                [8, "9"],
                [1, "6"],
            ],
            "bench": [
                [6, "CF"],
                [54, "C"],
                [12, "3B"],
                [4, "SS"],
            ],
            "bullpen": [40, 38, 36, 30, 52, 55, 46, 21, 49, 29, 54],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 31,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                29: "Daniel Nava",
                39: "Jarrod Saltalamacchia",
                7: "Stephen Drew",
                26: "Brock Holt",
                # Starting pitcher
                31: "Jon Lester",
                # Bench
                37: "Mike Carp",
                5: "Jonny Gomes",
                20: "Ryan Lavarnway",
                23: "Brandon Snyder",
                # Bullpen
                35: "Steven Wright",
                41: "John Lackey",
                32: "Craig Breslow",
                66: "Drake Britton",
                44: "Jake Peavy",
                36: "Junichi Tazawa",
                19: "Koji Uehara",
                38: "Matt Thornton",
                54: "Pedro Beato",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [31, 32, 66, 38, 22],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [29, "7"],
                [39, "2"],
                [7, "6"],
                [26, "5"],
            ],
            "bench": [
                [37, "1B"],
                [5, "LF"],
                [20, "C"],
                [23, "1B"],
            ],
            "bullpen": [35, 41, 32, 66, 44, 36, 19, 38, 54, 22, 46],
        },
        "umpires": {
            "HP": "Jeff Kellogg",
            "1B": "Eric Cooper",
            "2B": "Paul Schrieber",
            "3B": "Chad Fairchild",
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

# 1. AZ #11 AJ Pollock (X - X - X)
t1.new_ab()
t1.pitch_list("c f b f f b")
t1.out("L9")

# 2. AZ #2  Aaron Hill (X - X - X)
t1.new_ab()
t1.pitch_list("c b")
t1.hit(1)
t1.advance(4, "44 HR")

# 3. AZ #44 Paul Goldschmidt (X - X - 2)
t1.new_ab()
t1.pitch_list("b s f b")
t1.hit(4, rbis=2)

# 4. AZ #14 Martín Prado (X - X - X)
t1.new_ab()
t1.pitch_list("c b b")
t1.out("G1-3")

# 5. AZ #7  Cody Ross (X - X - X)
t1.new_ab()
t1.pitch_list("c b")
t1.hit(2)

# 6. AZ #13 Jason Kubel (X - 7 - X)
t1.new_ab(is_risp=True)
t1.pitch_list("b f b")
t1.out("(F)P5")


# Bot 1st
# Pitching: AZ #48 Randall Delgado
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("b")
b1.hit(3)
b1.advance(4, "34 HR")

# 2. BOS #18 Shane Victorino (2 - X - X)
b1.new_ab(is_risp=True)
b1.pitch_list("c c b")
b1.out("G3")

# 3. BOS #15 Dustin Pedroia (2 - X - X)
b1.new_ab(is_risp=True)
b1.pitch_list("c b c b s")
b1.out("K")

# 4. BOS #34 David Ortiz (2 - X - X)
b1.new_ab(is_risp=True)
b1.hit(4, rbis=2)

# 5. BOS #12 Mike Napoli (X - X - X)
b1.new_ab()
b1.pitch_list("b b c b s f f s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #31 Jon Lester
t2 = game.new_inning()

# 7. AZ #27 Wil Nieves (X - X - X)
t2.new_ab()
t2.pitch_list("c")
t2.hit(1)
t2.advance(2, "11 1B")

# 8. AZ #8  Gerardo Parra (X - X - 27)
t2.new_ab()
t2.pitch_list("b")
t2.out("L8")

# 9. AZ #1  Didi Gregorius (X - X - 27)
t2.new_ab()
t2.pitch_list("s s b s")
t2.out("K")

# 1. AZ #11 AJ Pollock (X - X - 27)
t2.new_ab()
t2.hit(1)

# 2. AZ #2  Aaron Hill (X - 27 - 11)
t2.new_ab(is_risp=True)
t2.out("L5")


# Bot 2nd
# Pitching: AZ #48 Randall Delgado
b2 = game.new_inning()

# 6. BOS #29 Daniel Nava (X - X - X)
b2.new_ab()
b2.pitch_list("c c")
b2.error(6)
b2.reach("E6")
b2.advance(3, "39 2B")
b2.advance("U", "7 SF8")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - 29)
b2.new_ab()
b2.pitch_list("l b 1 1 b b")
b2.hit(2)
b2.advance(3, "7 SF8")
b2.advance("U", "26 SF8")

# 8. BOS #7  Stephen Drew (29 - 39 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("b")
b2.out("SF8", rbis=1)

# 9. BOS #26 Brock Holt (39 - X - X)
b2.new_ab(is_risp=True)
b2.out("SF8", rbis=1)

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b2.new_ab()
b2.pitch_list("b f f c")
b2.out("!K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #31 Jon Lester
t3 = game.new_inning()

# 3. AZ #44 Paul Goldschmidt (X - X - X)
t3.new_ab()
t3.pitch_list("b c b f c")
t3.out("!K")

# 4. AZ #14 Martín Prado (X - X - X)
t3.new_ab()
t3.pitch_list("b b c s")
t3.hit(2)
t3.advance(4, "7 1B")

# 5. AZ #7  Cody Ross (X - 14 - X)
t3.new_ab(is_risp=True)
t3.pitch_list("b b")
t3.hit(1, rbis=1)
t3.advance(2, "27 SB")

# 6. AZ #13 Jason Kubel (X - X - 7)
t3.new_ab()
t3.pitch_list("f d s b c")
t3.out("!K")

# 7. AZ #27 Wil Nieves (X - X - 7)
t3.new_ab(is_risp=True)
t3.pitch_list("f b d s f f s")
t3.out("K")


# Bot 3rd
# Pitching: AZ #48 Randall Delgado
b3 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
b3.new_ab()
b3.pitch_list("c")
b3.out("F9")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b3.new_ab()
b3.pitch_list("c")
b3.out("L5")

# 4. BOS #34 David Ortiz (X - X - X)
b3.new_ab()
b3.pitch_list("b b f b c s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #31 Jon Lester
t4 = game.new_inning()

# 8. AZ #8  Gerardo Parra (X - X - X)
t4.new_ab()
t4.pitch_list("c")
t4.out("L8")

# 9. AZ #1  Didi Gregorius (X - X - X)
t4.new_ab()
t4.pitch_list("c s b b f b t")
t4.out("KT")

# 1. AZ #11 AJ Pollock (X - X - X)
t4.new_ab()
t4.pitch_list("c f b f f f c")
t4.out("!K")


# Bot 4th
# Pitching: AZ #48 Randall Delgado
b4 = game.new_inning()

# 5. BOS #12 Mike Napoli (X - X - X)
b4.new_ab()
b4.hit(1)
b4.advance(2, "29 HBP")
b4.advance(3, "7 BB")
b4.thrown_out(4, "26 FC1-2", 2, 48)

# 6. BOS #29 Daniel Nava (X - X - 12)
b4.new_ab()
b4.pitch_list("c t")
b4.reach("HBP")
b4.advance(2, "7 BB")
b4.advance(3, "26 FC1-2")

# 7. BOS #39 Jarrod Saltalamacchia (X - 12 - 29)
b4.new_ab(is_risp=True)
b4.pitch_list("c b f f b s")
b4.out("K")

# 8. BOS #7  Stephen Drew (X - 12 - 29)
b4.new_ab(is_risp=True)
b4.pitch_list("b b c b b")
b4.reach("BB")
b4.advance(2, "26 FC1-2")

# 9. BOS #26 Brock Holt (12 - 29 - 7)
b4.new_ab(is_risp=True)
b4.pitch_list("c b f")
b4.reach("FC1-2")

# 1. BOS #2  Jacoby Ellsbury (29 - 7 - 26)
b4.new_ab(is_risp=True)
b4.pitch_list("b b")
b4.out("F7")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #31 Jon Lester
t5 = game.new_inning()

# 2. AZ #2  Aaron Hill (X - X - X)
t5.new_ab()
t5.pitch_list("b b c b")
t5.hit(2)
t5.advance(3, "44 G4-3")
t5.advance(4, "14 2B")

# 3. AZ #44 Paul Goldschmidt (X - 2 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("b c c d")
t5.out("G4-3")

# 4. AZ #14 Martín Prado (2 - X - X)
t5.new_ab(is_risp=True)
t5.pitch_list("b b c f f d f f")
t5.hit(2, rbis=1)
t5.advance(4, "7 2B")

# 5. AZ #7  Cody Ross (X - 14 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("c s b")
t5.hit(2, rbis=1)
t5.advance(4, "13 1B")

# 6. AZ #13 Jason Kubel (X - 7 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("c")
t5.hit(1, rbis=1)
t5.thrown_out(2, "27 FC3-6", 2, 38)

# Pitching change (BOS): #38 Matt Thornton replaces #31 Jon Lester
t5.pitching_substitution(38)

# 7. AZ #27 Wil Nieves (X - X - 13)
t5.new_ab()
t5.pitch_list("1")
t5.reach("FC3-6")
t5.advance(2, "8 1B")

# 8. AZ #8  Gerardo Parra (X - X - 27)
t5.new_ab()
t5.pitch_list("c c")
t5.hit(1)

# 9. AZ #1  Didi Gregorius (X - 27 - 8)
t5.new_ab(is_risp=True)
t5.pitch_list("c b s s")
t5.out("K")


# Bot 5th
# Pitching: AZ #48 Randall Delgado
b5 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
b5.new_ab()
b5.pitch_list("c")
b5.out("F7")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b5.new_ab()
b5.pitch_list("b b")
b5.out("F9")

# 4. BOS #34 David Ortiz (X - X - X)
b5.new_ab()
b5.pitch_list("s b b b s s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #38 Matt Thornton
t6 = game.new_inning()

# 1. AZ #11 AJ Pollock (X - X - X)
t6.new_ab()
t6.out("G4-3")

# 2. AZ #2  Aaron Hill (X - X - X)
t6.new_ab()
t6.pitch_list("b b")
t6.out("G5-3")

# 3. AZ #44 Paul Goldschmidt (X - X - X)
t6.new_ab()
t6.hit(1)
t6.thrown_out(2, "14 FC3-6", 3, 38)

# 4. AZ #14 Martín Prado (X - X - 44)
t6.new_ab()
t6.pitch_list("c b 1 c f")
t6.reach("FC3-6")


# Bot 6th
# Pitching: AZ #48 Randall Delgado
b6 = game.new_inning()

# 5. BOS #12 Mike Napoli (X - X - X)
b6.new_ab()
b6.pitch_list("s b")
b6.hit(1)
b6.advance(4, "7 HR")

# 6. BOS #29 Daniel Nava (X - X - 12)
b6.new_ab()
b6.pitch_list("1 c 1 f f b s")
b6.out("K")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - 12)
b6.new_ab()
b6.pitch_list("c")
b6.out("F8")

# 8. BOS #7  Stephen Drew (X - X - 12)
b6.new_ab()
b6.pitch_list("b")
b6.hit(4, rbis=2)

# 9. BOS #26 Brock Holt (X - X - X)
b6.new_ab()
b6.pitch_list("s b b f b f")
b6.out("L6")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #54 Pedro Beato
t7 = game.new_inning()

# Pitching change (BOS): #54 Pedro Beato replaces #38 Matt Thornton
t7.pitching_substitution(54)

# 5. AZ #7  Cody Ross (X - X - X)
t7.new_ab()
t7.pitch_list("b")
t7.hit(4)

# 6. AZ #13 Jason Kubel (X - X - X)
t7.new_ab()
t7.pitch_list("f b c b f f")
t7.out("F8")

# 7. AZ #27 Wil Nieves (X - X - X)
t7.new_ab()
t7.pitch_list("b")
t7.hit(1)

# 8. AZ #8  Gerardo Parra (X - X - 27)
t7.new_ab()
t7.pitch_list("b b")
t7.out("F7")

# 9. AZ #1  Didi Gregorius (X - X - 27)
t7.new_ab()
t7.pitch_list("f b b b f f f f s")
t7.out("K")


# Bot 7th
# Pitching: AZ #40 J.J. Putz
b7 = game.new_inning()

# Pitching change (AZ): #40 J.J. Putz replaces #48 Randall Delgado
b7.pitching_substitution(40)

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b7.new_ab()
b7.pitch_list("b b f b")
b7.out("G3")

# 2. BOS #18 Shane Victorino (X - X - X)
b7.new_ab()
b7.pitch_list("c f b b")
b7.hit(2)
b7.advance(3, "15 F9")

# 3. BOS #15 Dustin Pedroia (X - 18 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("b c d")
b7.out("F9")

# Pitching change (AZ): #54 Joe Thatcher replaces #40 J.J. Putz
b7.pitching_substitution(54)

# 4. BOS #34 David Ortiz (18 - X - X)
b7.new_ab(is_risp=True)
b7.pitch_list("b f s")
b7.out("(F)P5")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #54 Pedro Beato
t8 = game.new_inning()

# 1. AZ #11 AJ Pollock (X - X - X)
t8.new_ab()
t8.pitch_list("b")
t8.out("L8")

# Pitching change (BOS): #36 Junichi Tazawa replaces #54 Pedro Beato
t8.pitching_substitution(36)

# 2. AZ #2  Aaron Hill (X - X - X)
t8.new_ab()
t8.pitch_list("c c")
t8.out("F8")

# 3. AZ #44 Paul Goldschmidt (X - X - X)
t8.new_ab()
t8.pitch_list("c b f f s")
t8.out("K")


# Bot 8th
# Pitching: AZ #21 Heath Bell
b8 = game.new_inning()

# Pitching change (AZ): #21 Heath Bell replaces #54 Joe Thatcher
b8.pitching_substitution(21)

# 5. BOS #12 Mike Napoli (X - X - X)
b8.new_ab()
b8.pitch_list("c c f b")
b8.reach("HBP")
# Offensive change (BOS): Pinch-runner #23 Brandon Snyder replaces #12 Mike Napoli
b8.offensive_substitution(5, 23, "PR")
b8.atbase("PR")
b8.thrown_out(2, "29 DP6-4-3", 1, 21)

# 6. BOS #29 Daniel Nava (X - X - 12)
b8.new_ab()
b8.pitch_list("c")
b8.out("DP6-4-3")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b8.new_ab()
b8.pitch_list("c c b f b b c")
b8.out("!K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #36 Junichi Tazawa
t9 = game.new_inning()

# Defensive switch (BOS): #23 Brandon Snyder moves to 1B
t9.defensive_switch(23, "3")

# 4. AZ #14 Martín Prado (X - X - X)
t9.new_ab()
t9.pitch_list("b f")
t9.out("G5-3")

# 5. AZ #7  Cody Ross (X - X - X)
t9.new_ab()
t9.pitch_list("b")
t9.out("G6-3")

# 6. AZ #13 Jason Kubel (X - X - X)
t9.new_ab()
t9.pitch_list("b")
t9.hit(1)
# Offensive change (AZ): Pinch-runner #6 Adam Eaton replaces #13 Jason Kubel
t9.offensive_substitution(6, 6, "PR")
t9.atbase("PR")

# 7. AZ #27 Wil Nieves (X - X - 13)
t9.new_ab()
t9.pitch_list("d c s b f")
t9.out("G5-3")


# Bot 9th
# Pitching: AZ #29 Brad Ziegler
b9 = game.new_inning()

# Pitching change (AZ): #29 Brad Ziegler replaces #21 Heath Bell
b9.pitching_substitution(29)

# Defensive switch (AZ): #6 Adam Eaton moves to DH
b9.defensive_switch(6, "0")

# 8. BOS #7  Stephen Drew (X - X - X)
b9.new_ab()
b9.pitch_list("b c")
b9.hit(1)
b9.advance(2, "2 1B")

# 9. BOS #26 Brock Holt (X - X - 7)
b9.new_ab()
b9.pitch_list("m l b c")
b9.out("!K")

# 1. BOS #2  Jacoby Ellsbury (X - X - 7)
b9.new_ab()
b9.pitch_list("b b")
b9.hit(1)

# 2. BOS #18 Shane Victorino (X - 7 - 2)
b9.new_ab(is_risp=True)
b9.pitch_list("b c f")
b9.out("L7")

# 3. BOS #15 Dustin Pedroia (X - 7 - 2)
b9.new_ab(is_risp=True)
b9.pitch_list("b s")
b9.out("G1-3")

# Winning team: AZ
# WP: AZ #48 Randall Delgado
game.winning_pitcher(48, is_away_team=True)
# SV: AZ #29 Brad Ziegler
game.save_pitcher(29, is_away_team=True)

# Loser team: BOS
# LP: BOS #54 Pedro Beato
game.losing_pitcher(54)

# print(game)
game.generate_scorecard()
