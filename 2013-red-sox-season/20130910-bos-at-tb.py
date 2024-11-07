import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ TB, 2013-09-10
# https://www.baseball-reference.com/boxes/TBA/TBA201309100.shtml
# https://www.mlb.com/gameday/red-sox-vs-rays/2013/09/10/348894/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-09-10 19:11-22:20",
        "at": "Tropicana Field, St. Petersburg, FL",
        "att": "18,605",
        "temp": "72F, Dome",
        "wind": "0mph, None",
        "away": {
            "team": "Boston Red Sox",
            "starter": 11,
            "roster": {
                # Lineup
                15: "Dustin Pedroia",
                18: "Shane Victorino",
                34: "David Ortiz",
                12: "Mike Napoli",
                5: "Jonny Gomes",
                29: "Daniel Nava",
                39: "Jarrod Saltalamacchia",
                16: "Will Middlebrooks",
                7: "Stephen Drew",
                # Starting pitcher
                11: "Clay Buchholz",
                # Bench
                50: "Quintin Berry",
                2: "Jacoby Ellsbury",
                37: "Mike Carp",
                3: "David Ross",
                72: "Xander Bogaerts",
                25: "Jackie Bradley Jr.",
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
                31: "Jon Lester",
                36: "Junichi Tazawa",
                64: "Allen Webster",
                19: "Koji Uehara",
                38: "Matt Thornton",
                62: "Rubby De La Rosa",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [56, 32, 66, 31, 38, 22],
            "lineup": [
                [15, "4"],
                [18, "8"],
                [34, "0"],
                [12, "3"],
                [5, "7"],
                [29, "9"],
                [39, "2"],
                [16, "5"],
                [7, "6"],
            ],
            "bench": [
                [50, "LF"],
                [2, "CF"],
                [37, "1B"],
                [3, "C"],
                [72, "2B"],
                [25, "CF"],
                [20, "C"],
                [10, "SS"],
                [23, "1B"],
            ],
            "bullpen": [41, 67, 56, 32, 66, 44, 31, 36, 64, 19, 38, 62, 22, 46],
        },
        "home": {
            "team": "Tampa Bay Rays",
            "starter": 14,
            "roster": {
                # Lineup
                7: "David DeJesus",
                18: "Ben Zobrist",
                3: "Evan Longoria",
                20: "Matt Joyce",
                21: "James Loney",
                30: "Luke Scott",
                8: "Desmond Jennings",
                28: "José Molina",
                11: "Yunel Escobar",
                # Starting pitcher
                14: "David Price",
                # Bench
                16: "Chris Gimenez",
                1: "Sean Rodríguez",
                15: "Delmon Young",
                9: "Wil Myers",
                59: "Jose Lobaton",
                5: "Sam Fuld",
                2: "Kelly Johnson",
                # Bullpen
                58: "Jeremy Hellickson",
                49: "Wesley Wright",
                53: "Alex Cobb",
                47: "Brandon Gomes",
                55: "Matt Moore",
                62: "Joel Peralta",
                35: "Jamey Wright",
                57: "Jake McGee",
                54: "Alex Torres",
                27: "Cesár Ramos",
                52: "Josh Lueke",
                56: "Fernando Rodney",
                22: "Chris Archer",
                40: "Roberto Hernandez",
            },
            "lefties": [14, 49, 55, 57, 54, 27],
            "lineup": [
                [7, "9"],
                [18, "4"],
                [3, "5"],
                [20, "7"],
                [21, "3"],
                [30, "0"],
                [8, "8"],
                [28, "2"],
                [11, "6"],
            ],
            "bench": [
                [16, "C"],
                [1, "2B"],
                [15, "LF"],
                [9, "RF"],
                [59, "C"],
                [5, "LF"],
                [2, "2B"],
            ],
            "bullpen": [58, 49, 53, 47, 55, 62, 35, 57, 54, 27, 52, 56, 22, 40],
        },
        "umpires": {
            "HP": "Angel Hernandez",
            "1B": "Vic Carapazza",
            "2B": "Lance Barksdale",
            "3B": "Gary Cederstrom",
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
# Pitching: TBR #14 David Price
t1 = game.new_inning()

# 1. BOS #15 Dustin Pedroia (X - X - X)
t1.new_ab()
t1.pitch_list("c f f s")
t1.out("K")

# 2. BOS #18 Shane Victorino (X - X - X)
t1.new_ab()
t1.pitch_list("c b f s")
t1.out("K")

# 3. BOS #34 David Ortiz (X - X - X)
t1.new_ab()
t1.pitch_list("c b c f b f f f b")
t1.out("L9")


# Bot 1st
# Pitching: BOS #11 Clay Buchholz
b1 = game.new_inning()

# 1. TBR #7  David DeJesus (X - X - X)
b1.new_ab()
b1.pitch_list("b b c f b")
b1.out("F8")

# 2. TBR #18 Ben Zobrist (X - X - X)
b1.new_ab()
b1.pitch_list("b b c c")
b1.out("L1-4-3")

# 3. TBR #3  Evan Longoria (X - X - X)
b1.new_ab()
b1.pitch_list("b c c b s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: TBR #14 David Price
t2 = game.new_inning()

# 4. BOS #12 Mike Napoli (X - X - X)
t2.new_ab()
t2.pitch_list("c c b f b")
t2.out("L9")

# 5. BOS #5  Jonny Gomes (X - X - X)
t2.new_ab()
t2.pitch_list("c")
t2.out("G6-3")

# 6. BOS #29 Daniel Nava (X - X - X)
t2.new_ab()
t2.pitch_list("c s b f f b b")
t2.out("L8")


# Bot 2nd
# Pitching: BOS #11 Clay Buchholz
b2 = game.new_inning()

# 4. TBR #20 Matt Joyce (X - X - X)
b2.new_ab()
b2.pitch_list("b c c")
b2.out("G5-3")

# 5. TBR #21 James Loney (X - X - X)
b2.new_ab()
b2.hit(1)
b2.advance(2, "8 1B")

# 6. TBR #30 Luke Scott (X - X - 21)
b2.new_ab()
b2.pitch_list("1 b c b b c s")
b2.out("K")

# 7. TBR #8  Desmond Jennings (X - X - 21)
b2.new_ab()
b2.hit(1)

# 8. TBR #28 José Molina (X - 21 - 8)
b2.new_ab(is_risp=True)
b2.pitch_list("c b b b f f t")
b2.out("KT")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: TBR #14 David Price
t3 = game.new_inning()

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
t3.new_ab()
t3.pitch_list("c b f b f b f c")
t3.out("!K")

# 8. BOS #16 Will Middlebrooks (X - X - X)
t3.new_ab()
t3.pitch_list("s b b")
t3.out("G6-3")

# 9. BOS #7  Stephen Drew (X - X - X)
t3.new_ab()
t3.out("(F)P1")


# Bot 3rd
# Pitching: BOS #11 Clay Buchholz
b3 = game.new_inning()

# 9. TBR #11 Yunel Escobar (X - X - X)
b3.new_ab()
b3.pitch_list("b f f")
b3.out("(F)P2")

# 1. TBR #7  David DeJesus (X - X - X)
b3.new_ab()
b3.pitch_list("b c b t b")
b3.hit(1)
b3.thrown_out(2, "18 CS", 2, 11)

# 2. TBR #18 Ben Zobrist (X - X - 7)
b3.new_ab()
b3.pitch_list("1 1 1 f b")
b3.out("G3-1")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: TBR #14 David Price
t4 = game.new_inning()

# 1. BOS #15 Dustin Pedroia (X - X - X)
t4.new_ab()
t4.pitch_list("f")
t4.out("L9")

# 2. BOS #18 Shane Victorino (X - X - X)
t4.new_ab()
t4.pitch_list("c b")
t4.out("G1-3")

# 3. BOS #34 David Ortiz (X - X - X)
t4.new_ab()
t4.pitch_list("f b b b c f")
t4.out("F7")


# Bot 4th
# Pitching: BOS #11 Clay Buchholz
b4 = game.new_inning()

# 3. TBR #3  Evan Longoria (X - X - X)
b4.new_ab()
b4.pitch_list("f b f c")
b4.out("!K")

# 4. TBR #20 Matt Joyce (X - X - X)
b4.new_ab()
b4.pitch_list("b f b f b b")
b4.reach("BB")
b4.thrown_out(2, "21 CS", 3, 11)

# 5. TBR #21 James Loney (X - X - 20)
b4.new_ab()
b4.pitch_list("1 b b 1 c b c 1 c")
b4.out("KDP2-6")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: TBR #14 David Price
t5 = game.new_inning()

# 4. BOS #12 Mike Napoli (X - X - X)
t5.new_ab()
t5.pitch_list("b f b c f f")
t5.hit(2)
t5.advance(4, "5 1B")

# 5. BOS #5  Jonny Gomes (X - 12 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("c f b f")
t5.hit(1, rbis=1)
t5.advance(2, "T")
t5.advance(3, "29 SAC2-3")
t5.advance(4, "39 SF8")

# 6. BOS #29 Daniel Nava (X - 5 - X)
t5.new_ab(is_risp=True)
t5.out("SAC2-3")

# 7. BOS #39 Jarrod Saltalamacchia (5 - X - X)
t5.new_ab(is_risp=True)
t5.pitch_list("b t b f f f b")
t5.out("SF8", rbis=1)

# 8. BOS #16 Will Middlebrooks (X - X - X)
t5.new_ab()
t5.pitch_list("c c s")
t5.out("K")


# Bot 5th
# Pitching: BOS #11 Clay Buchholz
b5 = game.new_inning()

# 6. TBR #30 Luke Scott (X - X - X)
b5.new_ab()
b5.pitch_list("b c b c b s")
b5.out("K")

# 7. TBR #8  Desmond Jennings (X - X - X)
b5.new_ab()
b5.pitch_list("c f")
b5.out("F8")

# 8. TBR #28 José Molina (X - X - X)
b5.new_ab()
b5.out("L8")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: TBR #14 David Price
t6 = game.new_inning()

# 9. BOS #7  Stephen Drew (X - X - X)
t6.new_ab()
t6.pitch_list("c b f c")
t6.out("!K")

# 1. BOS #15 Dustin Pedroia (X - X - X)
t6.new_ab()
t6.pitch_list("c b b f s")
t6.out("K")

# 2. BOS #18 Shane Victorino (X - X - X)
t6.new_ab()
t6.pitch_list("b s b c c")
t6.out("!K")


# Bot 6th
# Pitching: BOS #32 Craig Breslow
b6 = game.new_inning()

# Pitching change (BOS): #32 Craig Breslow replaces #11 Clay Buchholz
b6.pitching_substitution(32)

# 9. TBR #11 Yunel Escobar (X - X - X)
b6.new_ab()
b6.pitch_list("b b b c b")
b6.reach("BB")
b6.thrown_out(2, "9 FC6-4", 1, 32)

# Offensive change (TBR): Pinch-hitter #9 Wil Myers replaces #7 David DeJesus, batting 1st
b6.offensive_substitution(1, 9, "PH")

# 1. TBR #9  Wil Myers (X - X - 11)
b6.new_ab()
b6.pitch_list("b f s b f d f")
b6.reach("FC6-4")
b6.thrown_out(2, "18 DP4-3", 2, 32)

# 2. TBR #18 Ben Zobrist (X - X - 9)
b6.new_ab()
b6.pitch_list("b")
b6.out("DP4-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: TBR #14 David Price
t7 = game.new_inning()

# Defensive switch (TBR): #9 Wil Myers moves to RF
t7.defensive_switch(9, "9")

# 3. BOS #34 David Ortiz (X - X - X)
t7.new_ab()
t7.pitch_list("c")
t7.out("G3")

# 4. BOS #12 Mike Napoli (X - X - X)
t7.new_ab()
t7.pitch_list("c f f b c")
t7.out("!K")

# 5. BOS #5  Jonny Gomes (X - X - X)
t7.new_ab()
t7.pitch_list("b b")
t7.out("G6-3")


# Bot 7th
# Pitching: BOS #32 Craig Breslow
b7 = game.new_inning()

# 3. TBR #3  Evan Longoria (X - X - X)
b7.new_ab()
b7.pitch_list("c s f b")
b7.out("G6-3")

# 4. TBR #20 Matt Joyce (X - X - X)
b7.new_ab()
b7.pitch_list("b b b c c b")
b7.reach("BB")

# 5. TBR #21 James Loney (X - X - 20)
b7.new_ab()
b7.out("L6")

# Offensive change (TBR): Pinch-hitter #15 Delmon Young replaces #30 Luke Scott, batting 6th
b7.offensive_substitution(6, 15, "PH")

# 6. TBR #15 Delmon Young (X - X - 20)
b7.new_ab()
b7.pitch_list("c d b b f")
b7.out("G5-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: TBR #14 David Price
t8 = game.new_inning()

# Defensive switch (TBR): #15 Delmon Young moves to DH
t8.defensive_switch(15, "0")

# 6. BOS #29 Daniel Nava (X - X - X)
t8.new_ab()
t8.pitch_list("c")
t8.hit(1)
t8.advance(2, "16 WP")
t8.advance(3, "16 WP")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - 29)
t8.new_ab()
t8.pitch_list("f")
t8.out("F8")

# 8. BOS #16 Will Middlebrooks (X - X - 29)
t8.new_ab(is_risp=True)
t8.pitch_list("f b t f f f f f f f b")
t8.wp()
t8.wp()
t8.out("G6-3")

# 9. BOS #7  Stephen Drew (29 - X - X)
t8.new_ab(is_risp=True)
t8.pitch_list("c c b s")
t8.out("K")


# Bot 8th
# Pitching: BOS #36 Junichi Tazawa
b8 = game.new_inning()

# Pitching change (BOS): #36 Junichi Tazawa replaces #32 Craig Breslow
b8.pitching_substitution(36)

# 7. TBR #8  Desmond Jennings (X - X - X)
b8.new_ab()
b8.pitch_list("c b b s b s")
b8.out("K")

# 8. TBR #28 José Molina (X - X - X)
b8.new_ab()
b8.pitch_list("c t b b f b")
b8.out("P4")

# 9. TBR #11 Yunel Escobar (X - X - X)
b8.new_ab()
b8.hit(2)

# Pitching change (BOS): #19 Koji Uehara replaces #36 Junichi Tazawa
b8.pitching_substitution(19)

# 1. TBR #9  Wil Myers (X - 11 - X)
b8.new_ab(is_risp=True)
b8.pitch_list("c c")
b8.out("(F)P3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: TBR #62 Joel Peralta
t9 = game.new_inning()

# Pitching change (TBR): #62 Joel Peralta replaces #14 David Price
t9.pitching_substitution(62)

# 1. BOS #15 Dustin Pedroia (X - X - X)
t9.new_ab()
t9.pitch_list("c")
t9.hit(1)
t9.advance(2, "12 SB")

# 2. BOS #18 Shane Victorino (X - X - 15)
t9.new_ab()
t9.pitch_list("c")
t9.out("F9")

# 3. BOS #34 David Ortiz (X - X - 15)
t9.new_ab()
t9.pitch_list("f f")
t9.out("L9")

# 4. BOS #12 Mike Napoli (X - X - 15)
t9.new_ab(is_risp=True)
t9.pitch_list("b b b d")
t9.reach("BB")

# 5. BOS #5  Jonny Gomes (X - 15 - 12)
t9.new_ab(is_risp=True)
t9.pitch_list("s b s")
t9.out("F8")


# Bot 9th
# Pitching: BOS #19 Koji Uehara
b9 = game.new_inning()

# 2. TBR #18 Ben Zobrist (X - X - X)
b9.new_ab()
b9.pitch_list("f f")
b9.out("G4-3")

# 3. TBR #3  Evan Longoria (X - X - X)
b9.new_ab()
b9.pitch_list("c f s")
b9.out("K")

# 4. TBR #20 Matt Joyce (X - X - X)
b9.new_ab()
b9.pitch_list("c f b s")
b9.out("K")

# Winning team: BOS
# WP: BOS #11 Clay Buchholz
game.winning_pitcher(11, is_away_team=True)
# SV: BOS #19 Koji Uehara
game.save_pitcher(19, is_away_team=True)

# Loser team: TBR
# LP: TBR #14 David Price
game.losing_pitcher(14)

# print(game)
game.generate_scorecard()
