import os
from baseball_scorecard.baseball_scorecard import Scorecard

# DET @ BOS, 2013-09-03
# https://www.baseball-reference.com/boxes/BOS/BOS201309030.shtml
# https://www.mlb.com/gameday/tigers-vs-red-sox/2013/09/03/348804/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-09-03 19:12-22:08",
        "at": "Fenway Park, Boston, MA",
        "att": "32,071",
        "temp": "76F, Cloudy",
        "wind": "11mph, In From RF",
        "away": {
            "team": "Detroit Tigers",
            "starter": 37,
            "roster": {
                # Lineup
                14: "Austin Jackson",
                48: "Torii Hunter",
                24: "Miguel Cabrera",
                28: "Prince Fielder",
                41: "Victor Martinez",
                4: "Omar Infante",
                18: "Matt Tuiasosopo",
                55: "Brayan Peña",
                1: "Jose Iglesias",
                # Starting pitcher
                37: "Max Scherzer",
                # Bench
                50: "Bryan Holaday",
                29: "Danny Worth",
                39: "Ramon Santiago",
                30: "Nick Castellanos",
                32: "Don Kelly",
                12: "Andy Dirks",
                26: "Hernán Pérez",
                13: "Alex Avila",
                # Bullpen
                40: "Phil Coke",
                33: "Drew Smyly",
                53: "Joaquín Benoit",
                21: "Rick Porcello",
                36: "Luke Putkonen",
                52: "Jose Alvarez",
                31: "Jose Veras",
                62: "Al Alburquerque",
                58: "Doug Fister",
                38: "Jeremy Bonderman",
                57: "Evan Reed",
                19: "Aníbal Sánchez",
                35: "Justin Verlander",
                43: "Bruce Rondón",
            },
            "lefties": [40, 33, 52],
            "lineup": [
                [14, "8"],
                [48, "9"],
                [24, "5"],
                [28, "3"],
                [41, "0"],
                [4, "4"],
                [18, "7"],
                [55, "2"],
                [1, "6"],
            ],
            "bench": [
                [50, "C"],
                [29, "2B"],
                [39, "SS"],
                [30, "RF"],
                [32, "LF"],
                [12, "LF"],
                [26, "SS"],
                [13, "C"],
            ],
            "bullpen": [40, 33, 53, 21, 36, 52, 31, 62, 58, 38, 57, 19, 35, 43],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 31,
            "roster": {
                # Lineup
                18: "Shane Victorino",
                29: "Daniel Nava",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                37: "Mike Carp",
                5: "Jonny Gomes",
                7: "Stephen Drew",
                3: "David Ross",
                16: "Will Middlebrooks",
                # Starting pitcher
                31: "Jon Lester",
                # Bench
                50: "Quintin Berry",
                2: "Jacoby Ellsbury",
                39: "Jarrod Saltalamacchia",
                72: "Xander Bogaerts",
                12: "Mike Napoli",
                20: "Ryan Lavarnway",
                10: "John McDonald",
                23: "Brandon Snyder",
                # Bullpen
                41: "John Lackey",
                67: "Brandon Workman",
                56: "Franklin Morales",
                32: "Craig Breslow",
                66: "Drake Britton",
                44: "Jake Peavy",
                36: "Junichi Tazawa",
                11: "Clay Buchholz",
                19: "Koji Uehara",
                38: "Matt Thornton",
                62: "Rubby De La Rosa",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [31, 56, 32, 66, 38, 22],
            "lineup": [
                [18, "8"],
                [29, "9"],
                [15, "4"],
                [34, "0"],
                [37, "3"],
                [5, "7"],
                [7, "6"],
                [3, "2"],
                [16, "5"],
            ],
            "bench": [
                [50, "LF"],
                [2, "CF"],
                [39, "C"],
                [72, "2B"],
                [12, "1B"],
                [20, "C"],
                [10, "SS"],
                [23, "1B"],
            ],
            "bullpen": [41, 67, 56, 32, 66, 44, 36, 11, 19, 38, 62, 22, 46],
        },
        "umpires": {
            "HP": "Paul Schrieber",
            "1B": "Jeff Kellogg",
            "2B": "Mike Muchlinski",
            "3B": "Eric Cooper",
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

# 1. DET #14 Austin Jackson (X - X - X)
t1.new_ab()
t1.pitch_list("b f c f b f b")
t1.hit(2)
t1.advance(3, "24 F9")

# 2. DET #48 Torii Hunter (X - 14 - X)
t1.new_ab(is_risp=True)
t1.pitch_list("b f f b f f f d")
t1.out("(F)P3")

# 3. DET #24 Miguel Cabrera (X - 14 - X)
t1.new_ab(is_risp=True)
t1.pitch_list("c b f")
t1.out("F9")

# 4. DET #28 Prince Fielder (14 - X - X)
t1.new_ab(is_risp=True)
t1.pitch_list("c b c t")
t1.out("KT")


# Bot 1st
# Pitching: DET #37 Max Scherzer
b1 = game.new_inning()

# 1. BOS #18 Shane Victorino (X - X - X)
b1.new_ab()
b1.pitch_list("c f t")
b1.out("KT")

# 2. BOS #29 Daniel Nava (X - X - X)
b1.new_ab()
b1.pitch_list("b c f b s")
b1.out("K")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b1.new_ab()
b1.pitch_list("c b s b s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #31 Jon Lester
t2 = game.new_inning()

# 5. DET #41 Victor Martinez (X - X - X)
t2.new_ab()
t2.pitch_list("c")
t2.out("F8")

# 6. DET #4  Omar Infante (X - X - X)
t2.new_ab()
t2.pitch_list("c")
t2.hit(1)
t2.advance(3, "55 1B")
t2.advance(4, "1 2B")

# 7. DET #18 Matt Tuiasosopo (X - X - 4)
t2.new_ab()
t2.pitch_list("f f f c")
t2.out("!K")

# 8. DET #55 Brayan Peña (X - X - 4)
t2.new_ab()
t2.hit(1)
t2.advance(3, "1 2B")
t2.thrown_out(4, "1 8-6-2", 3, 31)

# 9. DET #1  Jose Iglesias (4 - X - 55)
t2.new_ab(is_risp=True)
t2.pitch_list("b c")
t2.hit(2, rbis=1)


# Bot 2nd
# Pitching: DET #37 Max Scherzer
b2 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
b2.new_ab()
b2.pitch_list("f f b b b")
b2.out("G3")

# 5. BOS #37 Mike Carp (X - X - X)
b2.new_ab()
b2.out("F8")

# 6. BOS #5  Jonny Gomes (X - X - X)
b2.new_ab()
b2.pitch_list("c b")
b2.hit(1)

# 7. BOS #7  Stephen Drew (X - X - 5)
b2.new_ab()
b2.pitch_list("b c")
b2.out("F7")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #31 Jon Lester
t3 = game.new_inning()

# 1. DET #14 Austin Jackson (X - X - X)
t3.new_ab()
t3.pitch_list("c f b c")
t3.out("!K")

# 2. DET #48 Torii Hunter (X - X - X)
t3.new_ab()
t3.pitch_list("b c f f s")
t3.out("K")

# 3. DET #24 Miguel Cabrera (X - X - X)
t3.new_ab()
t3.pitch_list("s b b s s")
t3.out("K")


# Bot 3rd
# Pitching: DET #37 Max Scherzer
b3 = game.new_inning()

# 8. BOS #3  David Ross (X - X - X)
b3.new_ab()
b3.pitch_list("s b s b")
b3.out("G6-3")

# 9. BOS #16 Will Middlebrooks (X - X - X)
b3.new_ab()
b3.pitch_list("b c t c")
b3.out("!K")

# 1. BOS #18 Shane Victorino (X - X - X)
b3.new_ab()
b3.pitch_list("c b s s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #31 Jon Lester
t4 = game.new_inning()

# 4. DET #28 Prince Fielder (X - X - X)
t4.new_ab()
t4.pitch_list("b")
t4.out("G6-3")

# 5. DET #41 Victor Martinez (X - X - X)
t4.new_ab()
t4.pitch_list("c b")
t4.out("G6-3")

# 6. DET #4  Omar Infante (X - X - X)
t4.new_ab()
t4.pitch_list("c b b b c")
t4.out("G5-3")


# Bot 4th
# Pitching: DET #37 Max Scherzer
b4 = game.new_inning()

# 2. BOS #29 Daniel Nava (X - X - X)
b4.new_ab()
b4.pitch_list("c")
b4.out("L9")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b4.new_ab()
b4.out("P4")

# 4. BOS #34 David Ortiz (X - X - X)
b4.new_ab()
b4.out("F8")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #31 Jon Lester
t5 = game.new_inning()

# 7. DET #18 Matt Tuiasosopo (X - X - X)
t5.new_ab()
t5.pitch_list("c b f c")
t5.out("!K")

# 8. DET #55 Brayan Peña (X - X - X)
t5.new_ab()
t5.pitch_list("c s f")
t5.error(5)
t5.reach("E5")
t5.advance(2, "14 1B")
t5.advance(3, "48 1B")

# 9. DET #1  Jose Iglesias (X - X - 55)
t5.new_ab()
t5.pitch_list("c d f t")
t5.out("KT")

# 1. DET #14 Austin Jackson (X - X - 55)
t5.new_ab()
t5.pitch_list("d c")
t5.hit(1)
t5.advance(2, "48 1B")

# 2. DET #48 Torii Hunter (X - 55 - 14)
t5.new_ab(is_risp=True)
t5.hit(1)
t5.thrown_out(2, "24 FC6-4", 3, 31)

# 3. DET #24 Miguel Cabrera (55 - 14 - 48)
t5.new_ab(is_risp=True)
t5.pitch_list("b b f")
t5.reach("FC6-4")


# Bot 5th
# Pitching: DET #37 Max Scherzer
b5 = game.new_inning()

# 5. BOS #37 Mike Carp (X - X - X)
b5.new_ab()
b5.pitch_list("b c f b f b s")
b5.out("K")

# 6. BOS #5  Jonny Gomes (X - X - X)
b5.new_ab()
b5.pitch_list("c b f f")
b5.hit(1)
b5.advance(3, "7 2B")
b5.advance(4, "16 1B")

# 7. BOS #7  Stephen Drew (X - X - 5)
b5.new_ab()
b5.pitch_list("c")
b5.hit(2)
b5.advance(4, "16 1B")

# 8. BOS #3  David Ross (5 - 7 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("s s t")
b5.out("KT")

# 9. BOS #16 Will Middlebrooks (5 - 7 - X)
b5.new_ab(is_risp=True)
b5.hit(1, rbis=2)
b5.advance(2, "18 SB")

# 1. BOS #18 Shane Victorino (X - X - 16)
b5.new_ab(is_risp=True)
b5.pitch_list("s c b")
b5.out("P3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #31 Jon Lester
t6 = game.new_inning()

# 4. DET #28 Prince Fielder (X - X - X)
t6.new_ab()
t6.pitch_list("f f b f f b")
t6.hit(1)
t6.advance(2, "4 1B")

# 5. DET #41 Victor Martinez (X - X - 28)
t6.new_ab()
t6.pitch_list("c b f f")
t6.out("F8")

# 6. DET #4  Omar Infante (X - X - 28)
t6.new_ab()
t6.hit(1)

# 7. DET #18 Matt Tuiasosopo (X - 28 - 4)
t6.new_ab(is_risp=True)
t6.pitch_list("b c s s")
t6.out("K")

# 8. DET #55 Brayan Peña (X - 28 - 4)
t6.new_ab(is_risp=True)
t6.pitch_list("f")
t6.out("F8")


# Bot 6th
# Pitching: DET #37 Max Scherzer
b6 = game.new_inning()

# 2. BOS #29 Daniel Nava (X - X - X)
b6.new_ab()
b6.pitch_list("c")
b6.out("F7")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b6.new_ab()
b6.pitch_list("c c b")
b6.out("F8")

# 4. BOS #34 David Ortiz (X - X - X)
b6.new_ab()
b6.pitch_list("b b b b")
b6.reach("BB")

# 5. BOS #37 Mike Carp (X - X - 34)
b6.new_ab()
b6.pitch_list("c b b f t")
b6.out("KT")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #31 Jon Lester
t7 = game.new_inning()

# 9. DET #1  Jose Iglesias (X - X - X)
t7.new_ab()
t7.pitch_list("b b c c s")
t7.out("K")

# 1. DET #14 Austin Jackson (X - X - X)
t7.new_ab()
t7.pitch_list("c c")
t7.out("G5-3")

# 2. DET #48 Torii Hunter (X - X - X)
t7.new_ab()
t7.pitch_list("b")
t7.out("G6-3")


# Bot 7th
# Pitching: DET #37 Max Scherzer
b7 = game.new_inning()

# 6. BOS #5  Jonny Gomes (X - X - X)
b7.new_ab()
b7.pitch_list("c b")
b7.out("P6")

# 7. BOS #7  Stephen Drew (X - X - X)
b7.new_ab()
b7.pitch_list("c b b f b f b")
b7.reach("BB")
b7.advance(2, "3 HBP")

# 8. BOS #3  David Ross (X - X - 7)
b7.new_ab()
b7.pitch_list("b c 1 b s b f 1")
b7.reach("HBP")

# 9. BOS #16 Will Middlebrooks (X - 7 - 3)
b7.new_ab(is_risp=True)
b7.pitch_list("b s s d f")
b7.out("F8")

# 1. BOS #18 Shane Victorino (X - 7 - 3)
b7.new_ab(is_risp=True)
b7.out("(F)P2")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #67 Brandon Workman
t8 = game.new_inning()

# Pitching change (BOS): #67 Brandon Workman replaces #31 Jon Lester
t8.pitching_substitution(67)

# 3. DET #24 Miguel Cabrera (X - X - X)
t8.new_ab()
t8.pitch_list("b b")
t8.out("F9")

# Pitching change (BOS): #32 Craig Breslow replaces #67 Brandon Workman
t8.pitching_substitution(32)

# 4. DET #28 Prince Fielder (X - X - X)
t8.new_ab()
t8.pitch_list("c b")
t8.out("G4-3")

# 5. DET #41 Victor Martinez (X - X - X)
t8.new_ab()
t8.pitch_list("b b b")
t8.hit(1)
# Offensive change (DET): Pinch-runner #29 Danny Worth replaces #41 Victor Martinez
t8.offensive_substitution(5, 29, "PR")
t8.atbase("PR")

# Pitching change (BOS): #36 Junichi Tazawa replaces #32 Craig Breslow
t8.pitching_substitution(36)

# 6. DET #4  Omar Infante (X - X - 41)
t8.new_ab()
t8.pitch_list("c b f s")
t8.out("K")


# Bot 8th
# Pitching: DET #37 Max Scherzer
b8 = game.new_inning()

# Defensive switch (DET): #29 Danny Worth moves to DH
b8.defensive_switch(29, "0")

# Defensive change (DET): #12 Andy Dirks replaces #18 Matt Tuiasosopo (LF), playing LF, batting 7th
b8.defensive_substitution(7, 12, "7")

# 2. BOS #29 Daniel Nava (X - X - X)
b8.new_ab()
b8.pitch_list("b b b b")
b8.reach("BB")
b8.advance(2, "15 1B")
b8.advance(3, "12 1B")

# 3. BOS #15 Dustin Pedroia (X - X - 29)
b8.new_ab()
b8.pitch_list("b c")
b8.hit(1)
b8.advance(2, "12 1B")

# Pitching change (DET): #40 Phil Coke replaces #37 Max Scherzer
b8.pitching_substitution(40)

# 4. BOS #34 David Ortiz (X - 29 - 15)
b8.new_ab(is_risp=True)
b8.pitch_list("c f b")
b8.out("F9")

# Pitching change (DET): #36 Luke Putkonen replaces #40 Phil Coke
b8.pitching_substitution(36)

# Offensive change (BOS): Pinch-hitter #12 Mike Napoli replaces #37 Mike Carp, batting 5th
b8.offensive_substitution(5, 12, "PH")

# 5. BOS #12 Mike Napoli (X - 29 - 15)
b8.new_ab(is_risp=True)
b8.pitch_list("b b b c c")
b8.hit(1)
b8.thrown_out(2, "7 FC6", 3, 36)

# 6. BOS #5  Jonny Gomes (29 - 15 - 12)
b8.new_ab(is_risp=True)
b8.pitch_list("c f")
b8.out("IF6")

# 7. BOS #7  Stephen Drew (29 - 15 - 12)
b8.new_ab(is_risp=True)
b8.reach("FC6")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #19 Koji Uehara
t9 = game.new_inning()

# Pitching change (BOS): #19 Koji Uehara replaces #36 Junichi Tazawa
t9.pitching_substitution(19)

# Defensive switch (BOS): #12 Mike Napoli moves to 1B
t9.defensive_switch(12, "3")

# 7. DET #12 Andy Dirks (X - X - X)
t9.new_ab()
t9.pitch_list("b")
t9.out("P4")

# 8. DET #55 Brayan Peña (X - X - X)
t9.new_ab()
t9.pitch_list("b c s s")
t9.out("K")

# 9. DET #1  Jose Iglesias (X - X - X)
t9.new_ab()
t9.pitch_list("c s s")
t9.out("K")

# Winning team: BOS
# WP: BOS #31 Jon Lester
game.winning_pitcher(31)
# SV: BOS #19 Koji Uehara
game.save_pitcher(19)

# Loser team: DET
# LP: DET #37 Max Scherzer
game.losing_pitcher(37, is_away_team=True)

# print(game)
game.generate_scorecard()
