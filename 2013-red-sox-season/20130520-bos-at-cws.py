import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ CWS, 2013-05-20
# https://www.baseball-reference.com/boxes/CHA/CHA201305200.shtml
# https://www.mlb.com/gameday/red-sox-vs-white-sox/2013/05/20/347402/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-05-20 20:11-23:03",
        "at": "U.S. Cellular Field, Chicago, IL",
        "att": "21,816",
        "temp": "86F, Partly Cloudy",
        "wind": "9mph, In From RF",
        "away": {
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
                16: "Will Middlebrooks",
                7: "Stephen Drew",
                39: "Jarrod Saltalamacchia",
                # Starting pitcher
                31: "Jon Lester",
                # Bench
                37: "Mike Carp",
                5: "Jonny Gomes",
                23: "Pedro Ciriaco",
                20: "Ryan Lavarnway",
                # Bullpen
                63: "Alex Wilson",
                40: "Andrew Bailey",
                41: "John Lackey",
                30: "Andrew Miller",
                32: "Craig Breslow",
                59: "Clayton Mortensen",
                36: "Junichi Tazawa",
                11: "Clay Buchholz",
                19: "Koji Uehara",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [31, 30, 32, 22],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [29, "7"],
                [16, "5"],
                [7, "6"],
                [39, "2"],
            ],
            "bench": [
                [37, "1B"],
                [5, "LF"],
                [23, "3B"],
                [20, "C"],
            ],
            "bullpen": [63, 40, 41, 30, 32, 59, 36, 11, 19, 22, 46],
        },
        "home": {
            "team": "Chicago White Sox",
            "starter": 33,
            "roster": {
                # Lineup
                30: "Alejandro De Aza",
                10: "Alexei Ramirez",
                51: "Alex Rios",
                14: "Paul Konerko",
                44: "Adam Dunn",
                24: "Dayan Viciedo",
                7: "Jeff Keppinger",
                21: "Tyler Flowers",
                1: "Tyler Greene",
                # Starting pitcher
                33: "Dylan Axelrod",
                # Bench
                38: "Hector Gimenez",
                39: "Casper Wells",
                28: "Dewayne Wise",
                12: "Conor Gillaspie",
                # Bullpen
                27: "Matt Lindstrom",
                65: "Nate Jones",
                48: "Brian Omogrosso",
                43: "Addison Reed",
                49: "Chris Sale",
                44: "Jake Peavy",
                62: "Jose Quintana",
                26: "Jesse Crain",
                46: "Donnie Veal",
                53: "Héctor Santiago",
                37: "Matt Thornton",
            },
            "lefties": [49, 62, 46, 53, 37],
            "lineup": [
                [30, "8"],
                [10, "6"],
                [51, "9"],
                [14, "3"],
                [44, "0"],
                [24, "7"],
                [7, "5"],
                [21, "2"],
                [1, "4"],
            ],
            "bench": [
                [38, "C"],
                [39, "RF"],
                [28, "CF"],
                [12, "3B"],
            ],
            "bullpen": [27, 65, 48, 43, 49, 44, 62, 26, 46, 53, 37],
        },
        "umpires": {
            "HP": "Alfonso Márquez",
            "1B": "Chris Conroy",
            "2B": "Mike DiMuro",
            "3B": "Ted Barrett",
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
# Pitching: CWS #33 Dylan Axelrod
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.pitch_list("b")
t1.out("G4-3")

# 2. BOS #18 Shane Victorino (X - X - X)
t1.new_ab()
t1.pitch_list("c f")
t1.out("G4-3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t1.new_ab()
t1.pitch_list("b b s")
t1.out("F9")


# Bot 1st
# Pitching: BOS #31 Jon Lester
b1 = game.new_inning()

# 1. CWS #30 Alejandro De Aza (X - X - X)
b1.new_ab()
b1.pitch_list("b s f b")
b1.out("P6")

# 2. CWS #10 Alexei Ramirez (X - X - X)
b1.new_ab()
b1.pitch_list("b f s s")
b1.out("K")

# 3. CWS #51 Alex Rios (X - X - X)
b1.new_ab()
b1.pitch_list("b c f b")
b1.hit(1)
b1.advance(2, "14 SB")
b1.advance(4, "44 HR")

# 4. CWS #14 Paul Konerko (X - X - 51)
b1.new_ab()
b1.pitch_list("b b c b b")
b1.reach("BB")
b1.advance(4, "44 HR")

# 5. CWS #44 Adam Dunn (X - 51 - 14)
b1.new_ab()
b1.pitch_list("b d")
b1.hit(4, rbis=3)

# 6. CWS #24 Dayan Viciedo (X - X - X)
b1.new_ab()
b1.pitch_list("c b f")
b1.out("G6-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: CWS #33 Dylan Axelrod
t2 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
t2.new_ab()
t2.out("G6-3")

# 5. BOS #12 Mike Napoli (X - X - X)
t2.new_ab()
t2.pitch_list("b c")
t2.out("G6-3")

# 6. BOS #29 Daniel Nava (X - X - X)
t2.new_ab()
t2.pitch_list("c f f b b")
t2.out("F8")


# Bot 2nd
# Pitching: BOS #31 Jon Lester
b2 = game.new_inning()

# 7. CWS #7  Jeff Keppinger (X - X - X)
b2.new_ab()
b2.out("G3-1")

# 8. CWS #21 Tyler Flowers (X - X - X)
b2.new_ab()
b2.pitch_list("c s")
b2.out("G6-3")

# 9. CWS #1  Tyler Greene (X - X - X)
b2.new_ab()
b2.pitch_list("b b")
b2.hit(2)
b2.advance(4, "30 2B")

# 1. CWS #30 Alejandro De Aza (X - 1 - X)
b2.new_ab()
b2.pitch_list("c s b f")
b2.hit(2, rbis=1)
b2.advance(4, "10 2B")

# 2. CWS #10 Alexei Ramirez (X - 30 - X)
b2.new_ab()
b2.hit(2, rbis=1)

# 3. CWS #51 Alex Rios (X - 10 - X)
b2.new_ab()
b2.out("F8")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: CWS #33 Dylan Axelrod
t3 = game.new_inning()

# 7. BOS #16 Will Middlebrooks (X - X - X)
t3.new_ab()
t3.pitch_list("c s b b")
t3.out("F9")

# 8. BOS #7  Stephen Drew (X - X - X)
t3.new_ab()
t3.pitch_list("b f b b f b")
t3.reach("BB")
t3.advance(4, "39 HR")

# 9. BOS #39 Jarrod Saltalamacchia (X - X - 7)
t3.new_ab()
t3.pitch_list("b f b s")
t3.hit(4, rbis=2)

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t3.new_ab()
t3.pitch_list("c b f b")
t3.out("G4-3")

# 2. BOS #18 Shane Victorino (X - X - X)
t3.new_ab()
t3.pitch_list("c b")
t3.out("P6")


# Bot 3rd
# Pitching: BOS #31 Jon Lester
b3 = game.new_inning()

# 4. CWS #14 Paul Konerko (X - X - X)
b3.new_ab()
b3.pitch_list("b c f f f t")
b3.out("KT")

# 5. CWS #44 Adam Dunn (X - X - X)
b3.new_ab()
b3.pitch_list("b c s")
b3.out("F9")

# 6. CWS #24 Dayan Viciedo (X - X - X)
b3.new_ab()
b3.pitch_list("s")
b3.hit(1)

# 7. CWS #7  Jeff Keppinger (X - X - 24)
b3.new_ab()
b3.pitch_list("c c b f d f b f")
b3.out("G6-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: CWS #33 Dylan Axelrod
t4 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
t4.new_ab()
t4.pitch_list("c")
t4.hit(1)
t4.thrown_out(2, "34 DP3-6-3", 1, 33)

# 4. BOS #34 David Ortiz (X - X - 15)
t4.new_ab()
t4.pitch_list("c b")
t4.out("DP3-6-3")

# 5. BOS #12 Mike Napoli (X - X - X)
t4.new_ab()
t4.pitch_list("c b c b s")
t4.out("K")


# Bot 4th
# Pitching: BOS #31 Jon Lester
b4 = game.new_inning()

# 8. CWS #21 Tyler Flowers (X - X - X)
b4.new_ab()
b4.pitch_list("c s f b")
b4.out("G6-3")

# 9. CWS #1  Tyler Greene (X - X - X)
b4.new_ab()
b4.out("G5-3")

# 1. CWS #30 Alejandro De Aza (X - X - X)
b4.new_ab()
b4.pitch_list("b c")
b4.out("B1")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: CWS #33 Dylan Axelrod
t5 = game.new_inning()

# 6. BOS #29 Daniel Nava (X - X - X)
t5.new_ab()
t5.pitch_list("b b b c c")
t5.out("L9")

# 7. BOS #16 Will Middlebrooks (X - X - X)
t5.new_ab()
t5.pitch_list("c f s")
t5.out("K")

# 8. BOS #7  Stephen Drew (X - X - X)
t5.new_ab()
t5.pitch_list("b b b c f")
t5.out("F7")


# Bot 5th
# Pitching: BOS #31 Jon Lester
b5 = game.new_inning()

# 2. CWS #10 Alexei Ramirez (X - X - X)
b5.new_ab()
b5.pitch_list("b b f")
b5.error(5)
b5.reach("E5")
b5.advance(2, "51 SB")
b5.advance(3, "14 DP4-6-3")
b5.advance("U", "24 1B")

# 3. CWS #51 Alex Rios (X - X - 10)
b5.new_ab()
b5.pitch_list("b b b b")
b5.reach("BB")
b5.thrown_out(2, "14 DP4-6-3", 1, 31)

# 4. CWS #14 Paul Konerko (X - 10 - 51)
b5.new_ab()
b5.pitch_list("f s b")
b5.out("DP4-6-3")

# 5. CWS #44 Adam Dunn (10 - X - X)
b5.new_ab()
b5.pitch_list("c f b d b b")
b5.reach("BB")
b5.advance(2, "24 1B")

# 6. CWS #24 Dayan Viciedo (10 - X - 44)
b5.new_ab()
b5.pitch_list("f b f d f f b f")
b5.hit(1, rbis=1)

# 7. CWS #7  Jeff Keppinger (X - 44 - 24)
b5.new_ab()
b5.pitch_list("c")
b5.out("(F)P3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: CWS #33 Dylan Axelrod
t6 = game.new_inning()

# 9. BOS #39 Jarrod Saltalamacchia (X - X - X)
t6.new_ab()
t6.pitch_list("b b c")
t6.hit(1)
t6.thrown_out(2, "2 DP4-6-3", 1, 33)

# 1. BOS #2  Jacoby Ellsbury (X - X - 39)
t6.new_ab()
t6.pitch_list("f b f f f b")
t6.out("DP4-6-3")

# 2. BOS #18 Shane Victorino (X - X - X)
t6.new_ab()
t6.pitch_list("c b")
t6.hit(1)

# 3. BOS #15 Dustin Pedroia (X - X - 18)
t6.new_ab()
t6.out("F8")


# Bot 6th
# Pitching: BOS #31 Jon Lester
b6 = game.new_inning()

# Defensive change (BOS): #5 Jonny Gomes replaces #18 Shane Victorino (RF), playing LF, batting 2nd
b6.defensive_substitution(2, 5, "7")

# Defensive switch (BOS): #29 Daniel Nava moves to RF
b6.defensive_switch(29, "9")

# 8. CWS #21 Tyler Flowers (X - X - X)
b6.new_ab()
b6.out("P4")

# 9. CWS #1  Tyler Greene (X - X - X)
b6.new_ab()
b6.pitch_list("c f b b f")
b6.out("F8")

# 1. CWS #30 Alejandro De Aza (X - X - X)
b6.new_ab()
b6.pitch_list("c b")
b6.out("G4-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: CWS #37 Matt Thornton
t7 = game.new_inning()

# Pitching change (CWS): #37 Matt Thornton replaces #33 Dylan Axelrod
t7.pitching_substitution(37)

# 4. BOS #34 David Ortiz (X - X - X)
t7.new_ab()
t7.pitch_list("b f f b b b")
t7.reach("BB")
t7.advance(2, "12 BB")
t7.advance(3, "29 F9")
t7.advance(4, "16 2B")

# 5. BOS #12 Mike Napoli (X - X - 34)
t7.new_ab()
t7.pitch_list("c d b b f b")
t7.reach("BB")
t7.advance(4, "16 2B")

# 6. BOS #29 Daniel Nava (X - 34 - 12)
t7.new_ab()
t7.out("F9")

# 7. BOS #16 Will Middlebrooks (34 - X - 12)
t7.new_ab()
t7.pitch_list("b f")
t7.hit(2, rbis=2)

# 8. BOS #7  Stephen Drew (X - 16 - X)
t7.new_ab()
t7.pitch_list("c f d b f c")
t7.out("!K")

# 9. BOS #39 Jarrod Saltalamacchia (X - 16 - X)
t7.new_ab()
t7.pitch_list("b f t b")
t7.out("F7")


# Bot 7th
# Pitching: BOS #59 Clayton Mortensen
b7 = game.new_inning()

# Pitching change (BOS): #59 Clayton Mortensen replaces #31 Jon Lester
b7.pitching_substitution(59)

# 2. CWS #10 Alexei Ramirez (X - X - X)
b7.new_ab()
b7.pitch_list("c b")
b7.out("G6-3")

# 3. CWS #51 Alex Rios (X - X - X)
b7.new_ab()
b7.pitch_list("b f b")
b7.out("G6-3")

# 4. CWS #14 Paul Konerko (X - X - X)
b7.new_ab()
b7.pitch_list("b f c b b")
b7.out("G5-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: CWS #26 Jesse Crain
t8 = game.new_inning()

# Pitching change (CWS): #26 Jesse Crain replaces #37 Matt Thornton
t8.pitching_substitution(26)

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t8.new_ab()
t8.pitch_list("b c b b f")
t8.out("G4-3")

# 2. BOS #5  Jonny Gomes (X - X - X)
t8.new_ab()
t8.pitch_list("b b c b b")
t8.reach("BB")
t8.thrown_out(2, "15 FC6-4", 2, 26)

# 3. BOS #15 Dustin Pedroia (X - X - 5)
t8.new_ab()
t8.pitch_list("c f f b")
t8.reach("FC6-4")

# 4. BOS #34 David Ortiz (X - X - 15)
t8.new_ab()
t8.pitch_list("b")
t8.out("P6")


# Bot 8th
# Pitching: BOS #32 Craig Breslow
b8 = game.new_inning()

# Pitching change (BOS): #32 Craig Breslow replaces #59 Clayton Mortensen
b8.pitching_substitution(32)

# 5. CWS #44 Adam Dunn (X - X - X)
b8.new_ab()
b8.pitch_list("c b")
b8.out("F8")

# 6. CWS #24 Dayan Viciedo (X - X - X)
b8.new_ab()
b8.pitch_list("c b f b b d")
b8.reach("BB")
# Offensive change (CWS): Pinch-runner #39 Casper Wells replaces #24 Dayan Viciedo
b8.offensive_substitution(6, 39, "PR")
b8.atbase("PR")
b8.advance(3, "7 2B")

# 7. CWS #7  Jeff Keppinger (X - X - 24)
b8.new_ab()
b8.pitch_list("d")
b8.hit(2)

# 8. CWS #21 Tyler Flowers (39 - 7 - X)
b8.new_ab()
b8.pitch_list("b")
b8.out("P5")

# 9. CWS #1  Tyler Greene (39 - 7 - X)
b8.new_ab()
b8.pitch_list("c s f d")
b8.out("L3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: CWS #43 Addison Reed
t9 = game.new_inning()

# Pitching change (CWS): #43 Addison Reed replaces #26 Jesse Crain
t9.pitching_substitution(43)

# Defensive switch (CWS): #39 Casper Wells moves to LF
t9.defensive_switch(39, "7")

# 5. BOS #12 Mike Napoli (X - X - X)
t9.new_ab()
t9.pitch_list("c")
t9.hit(1)
t9.advance(2, "7 DI")

# 6. BOS #29 Daniel Nava (X - X - 12)
t9.new_ab()
t9.pitch_list("c d s s")
t9.out("K")

# 7. BOS #16 Will Middlebrooks (X - X - 12)
t9.new_ab()
t9.pitch_list("s t b b")
t9.out("F8")

# 8. BOS #7  Stephen Drew (X - X - 12)
t9.new_ab()
t9.pitch_list("b c")
t9.out("G3-1")

# Winning team: CWS
# WP: CWS #33 Dylan Axelrod
game.winning_pitcher(33)
# SV: CWS #43 Addison Reed
game.save_pitcher(43)

# Loser team: BOS
# LP: BOS #31 Jon Lester
game.losing_pitcher(31, is_away_team=True)

# print(game)
game.generate_scorecard()
