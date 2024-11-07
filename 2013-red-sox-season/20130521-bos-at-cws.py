import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ CWS, 2013-05-21
# https://www.baseball-reference.com/boxes/CHA/CHA201305210.shtml
# https://www.mlb.com/gameday/red-sox-vs-white-sox/2013/05/21/347415/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-05-21 20:11-22:56",
        "at": "U.S. Cellular Field, Chicago, IL",
        "att": "21,984",
        "temp": "79F, Partly Cloudy",
        "wind": "18mph, R To L",
        "away": {
            "team": "Boston Red Sox",
            "starter": 22,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                5: "Jonny Gomes",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                29: "Daniel Nava",
                16: "Will Middlebrooks",
                7: "Stephen Drew",
                39: "Jarrod Saltalamacchia",
                # Starting pitcher
                22: "Felix Doubront",
                # Bench
                37: "Mike Carp",
                23: "Pedro Ciriaco",
                20: "Ryan Lavarnway",
                # Bullpen
                63: "Alex Wilson",
                40: "Andrew Bailey",
                41: "John Lackey",
                30: "Andrew Miller",
                32: "Craig Breslow",
                19: "Koji Uehara",
                31: "Jon Lester",
                59: "Clayton Mortensen",
                36: "Junichi Tazawa",
                46: "Ryan Dempster",
                11: "Clay Buchholz",
            },
            "lefties": [22, 30, 32, 31],
            "lineup": [
                [2, "8"],
                [5, "7"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [29, "9"],
                [16, "5"],
                [7, "6"],
                [39, "2"],
            ],
            "bench": [
                [37, "1B"],
                [23, "3B"],
                [20, "C"],
            ],
            "bullpen": [63, 40, 41, 30, 32, 19, 31, 59, 36, 46, 11],
        },
        "home": {
            "team": "Chicago White Sox",
            "starter": 62,
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
                62: "Jose Quintana",
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
                26: "Jesse Crain",
                46: "Donnie Veal",
                33: "Dylan Axelrod",
                53: "Héctor Santiago",
                37: "Matt Thornton",
            },
            "lefties": [62, 49, 46, 53, 37],
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
            "bullpen": [27, 65, 48, 43, 49, 44, 26, 46, 33, 53, 37],
        },
        "umpires": {
            "HP": "Chris Conroy",
            "1B": "Mike DiMuro",
            "2B": "Ted Barrett",
            "3B": "Alfonso Márquez",
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
# Pitching: CWS #62 Jose Quintana
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.pitch_list("c c b f")
t1.out("L8")

# 2. BOS #5  Jonny Gomes (X - X - X)
t1.new_ab()
t1.pitch_list("b c f s")
t1.out("K")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t1.new_ab()
t1.pitch_list("s s f b b s")
t1.out("K")


# Bot 1st
# Pitching: BOS #22 Felix Doubront
b1 = game.new_inning()

# 1. CWS #30 Alejandro De Aza (X - X - X)
b1.new_ab()
b1.pitch_list("c")
b1.out("G3-1")

# 2. CWS #10 Alexei Ramirez (X - X - X)
b1.new_ab()
b1.pitch_list("c s")
b1.hit(1)
b1.thrown_out(2, "51 DP6-4-3", 2, 22)

# 3. CWS #51 Alex Rios (X - X - 10)
b1.new_ab()
b1.pitch_list("1 c b c b b")
b1.out("DP6-4-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: CWS #62 Jose Quintana
t2 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
t2.new_ab()
t2.pitch_list("c b b s")
t2.out("P5")

# 5. BOS #12 Mike Napoli (X - X - X)
t2.new_ab()
t2.pitch_list("b b c s s")
t2.out("K")

# 6. BOS #29 Daniel Nava (X - X - X)
t2.new_ab()
t2.pitch_list("c c b f f f f b f f b b")
t2.reach("BB")
t2.thrown_out(2, "16 FC6-4", 3, 62)

# 7. BOS #16 Will Middlebrooks (X - X - 29)
t2.new_ab()
t2.pitch_list("f b")
t2.reach("FC6-4")


# Bot 2nd
# Pitching: BOS #22 Felix Doubront
b2 = game.new_inning()

# 4. CWS #14 Paul Konerko (X - X - X)
b2.new_ab()
b2.pitch_list("b f f")
b2.out("G5-3")

# 5. CWS #44 Adam Dunn (X - X - X)
b2.new_ab()
b2.pitch_list("c c f f s")
b2.out("K")

# 6. CWS #24 Dayan Viciedo (X - X - X)
b2.new_ab()
b2.pitch_list("b f b s s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: CWS #62 Jose Quintana
t3 = game.new_inning()

# 8. BOS #7  Stephen Drew (X - X - X)
t3.new_ab()
t3.pitch_list("c")
t3.out("F9")

# 9. BOS #39 Jarrod Saltalamacchia (X - X - X)
t3.new_ab()
t3.pitch_list("c c")
t3.out("F7")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t3.new_ab()
t3.out("P6")


# Bot 3rd
# Pitching: BOS #22 Felix Doubront
b3 = game.new_inning()

# 7. CWS #7  Jeff Keppinger (X - X - X)
b3.new_ab()
b3.pitch_list("b c")
b3.out("G6-3")

# 8. CWS #21 Tyler Flowers (X - X - X)
b3.new_ab()
b3.pitch_list("b s s s")
b3.out("K")

# 9. CWS #1  Tyler Greene (X - X - X)
b3.new_ab()
b3.pitch_list("b")
b3.out("F9")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: CWS #62 Jose Quintana
t4 = game.new_inning()

# 2. BOS #5  Jonny Gomes (X - X - X)
t4.new_ab()
t4.pitch_list("b")
t4.out("G5-3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t4.new_ab()
t4.pitch_list("c f b")
t4.out("G5-3")

# 4. BOS #34 David Ortiz (X - X - X)
t4.new_ab()
t4.pitch_list("c b b b s")
t4.out("G4-3")


# Bot 4th
# Pitching: BOS #22 Felix Doubront
b4 = game.new_inning()

# 1. CWS #30 Alejandro De Aza (X - X - X)
b4.new_ab()
b4.pitch_list("c b b b c b")
b4.reach("BB")
b4.thrown_out(2, "10 DP3-6", 2, 22)

# 2. CWS #10 Alexei Ramirez (X - X - 30)
b4.new_ab()
b4.pitch_list("b 1")
b4.out("DP3-6")

# 3. CWS #51 Alex Rios (X - X - X)
b4.new_ab()
b4.pitch_list("c b f")
b4.out("G6-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: CWS #62 Jose Quintana
t5 = game.new_inning()

# 5. BOS #12 Mike Napoli (X - X - X)
t5.new_ab()
t5.pitch_list("c f b")
t5.out("F9")

# 6. BOS #29 Daniel Nava (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.out("L9")

# 7. BOS #16 Will Middlebrooks (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.out("F8")


# Bot 5th
# Pitching: BOS #22 Felix Doubront
b5 = game.new_inning()

# 4. CWS #14 Paul Konerko (X - X - X)
b5.new_ab()
b5.pitch_list("b c b")
b5.out("(F)P3")

# 5. CWS #44 Adam Dunn (X - X - X)
b5.new_ab()
b5.pitch_list("b f")
b5.out("G3")

# 6. CWS #24 Dayan Viciedo (X - X - X)
b5.new_ab()
b5.pitch_list("f c")
b5.hit(1)
b5.advance(4, "7 HR")

# 7. CWS #7  Jeff Keppinger (X - X - 24)
b5.new_ab()
b5.hit(4, rbis=2)

# 8. CWS #21 Tyler Flowers (X - X - X)
b5.new_ab()
b5.pitch_list("b")
b5.hit(2)

# 9. CWS #1  Tyler Greene (X - 21 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("d c f f f b")
b5.out("G5-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: CWS #62 Jose Quintana
t6 = game.new_inning()

# 8. BOS #7  Stephen Drew (X - X - X)
t6.new_ab()
t6.pitch_list("c")
t6.out("P6")

# 9. BOS #39 Jarrod Saltalamacchia (X - X - X)
t6.new_ab()
t6.pitch_list("b f b f s")
t6.out("K")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t6.new_ab()
t6.pitch_list("c b b b f f f b")
t6.reach("BB")

# 2. BOS #5  Jonny Gomes (X - X - 2)
t6.new_ab()
t6.pitch_list("b d c f s")
t6.out("K")


# Bot 6th
# Pitching: BOS #22 Felix Doubront
b6 = game.new_inning()

# 1. CWS #30 Alejandro De Aza (X - X - X)
b6.new_ab()
b6.pitch_list("b")
b6.out("G4-3")

# 2. CWS #10 Alexei Ramirez (X - X - X)
b6.new_ab()
b6.out("G4-3")

# 3. CWS #51 Alex Rios (X - X - X)
b6.new_ab()
b6.pitch_list("c")
b6.hit(1)
b6.advance(2, "14 BB")

# 4. CWS #14 Paul Konerko (X - X - 51)
b6.new_ab()
b6.pitch_list("1 b b 1 b c f f b")
b6.reach("BB")

# 5. CWS #44 Adam Dunn (X - 51 - 14)
b6.new_ab(is_risp=True)
b6.pitch_list("c b b b t f")
b6.out("F9")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: CWS #62 Jose Quintana
t7 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
t7.new_ab()
t7.pitch_list("c f b b f")
t7.out("P5")

# 4. BOS #34 David Ortiz (X - X - X)
t7.new_ab()
t7.pitch_list("c b s f f")
t7.hit(1)
t7.advance(2, "12 1B")
t7.advance(3, "29 1B")

# 5. BOS #12 Mike Napoli (X - X - 34)
t7.new_ab()
t7.pitch_list("b c f b")
t7.hit(1)
t7.advance(2, "29 1B")

# 6. BOS #29 Daniel Nava (X - 34 - 12)
t7.new_ab(is_risp=True)
t7.pitch_list("b c b")
t7.hit(1)

# Pitching change (CWS): #26 Jesse Crain replaces #62 Jose Quintana
t7.pitching_substitution(26)

# 7. BOS #16 Will Middlebrooks (34 - 12 - 29)
t7.new_ab(is_risp=True)
t7.pitch_list("b b c f b s")
t7.out("K")

# 8. BOS #7  Stephen Drew (34 - 12 - 29)
t7.new_ab(is_risp=True)
t7.pitch_list("c b b f f s")
t7.out("K")


# Bot 7th
# Pitching: BOS #63 Alex Wilson
b7 = game.new_inning()

# Pitching change (BOS): #63 Alex Wilson replaces #22 Felix Doubront
b7.pitching_substitution(63)

# 6. CWS #24 Dayan Viciedo (X - X - X)
b7.new_ab()
b7.pitch_list("c s")
b7.out("F9")

# 7. CWS #7  Jeff Keppinger (X - X - X)
b7.new_ab()
b7.pitch_list("c c")
b7.out("F9")

# 8. CWS #21 Tyler Flowers (X - X - X)
b7.new_ab()
b7.pitch_list("c b")
b7.out("G1-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: CWS #37 Matt Thornton
t8 = game.new_inning()

# Pitching change (CWS): #37 Matt Thornton replaces #26 Jesse Crain
t8.pitching_substitution(37)

# Defensive change (CWS): #39 Casper Wells replaces #24 Dayan Viciedo (LF), playing LF, batting 6th
t8.defensive_substitution(6, 39, "7")

# 9. BOS #39 Jarrod Saltalamacchia (X - X - X)
t8.new_ab()
t8.pitch_list("b b s s b b")
t8.reach("BB")
t8.advance(2, "2 1B")
t8.advance(3, "15 WP")
t8.advance(4, "15 E6")

# 1. BOS #2  Jacoby Ellsbury (X - X - 39)
t8.new_ab()
t8.pitch_list("b")
t8.hit(1)
t8.advance(2, "15 WP")
t8.advance(3, "15 E6")

# Pitching change (CWS): #27 Matt Lindstrom replaces #37 Matt Thornton
t8.pitching_substitution(27)

# Offensive change (BOS): Pinch-hitter #37 Mike Carp replaces #5 Jonny Gomes, batting 2nd
t8.offensive_substitution(2, 37, "PH")

# 2. BOS #37 Mike Carp (X - 39 - 2)
t8.new_ab(is_risp=True)
t8.pitch_list("c")
t8.out("F7")

# 3. BOS #15 Dustin Pedroia (X - 39 - 2)
t8.new_ab(is_risp=True)
t8.pitch_list("b c b f d")
t8.wp()
t8.error(6)
t8.reach("E6", rbis=1)
t8.thrown_out(2, "34 DP3-6-3", 2, 27)

# 4. BOS #34 David Ortiz (2 - X - 15)
t8.new_ab(is_risp=True)
t8.out("DP3-6-3")


# Bot 8th
# Pitching: BOS #63 Alex Wilson
b8 = game.new_inning()

# Defensive switch (BOS): #37 Mike Carp moves to LF
b8.defensive_switch(37, "7")

# 9. CWS #1  Tyler Greene (X - X - X)
b8.new_ab()
b8.pitch_list("b f f b s")
b8.out("K")

# 1. CWS #30 Alejandro De Aza (X - X - X)
b8.new_ab()
b8.out("L3")

# 2. CWS #10 Alexei Ramirez (X - X - X)
b8.new_ab()
b8.pitch_list("b b")
b8.hit(1)
b8.advance(4, "51 2B")

# 3. CWS #51 Alex Rios (X - X - 10)
b8.new_ab()
b8.hit(2, rbis=1)

# 4. CWS #14 Paul Konerko (X - 51 - X)
b8.new_ab(is_risp=True)
b8.pitch_list("b f b b b")
b8.reach("BB")

# Pitching change (BOS): #30 Andrew Miller replaces #63 Alex Wilson
b8.pitching_substitution(30)

# 5. CWS #44 Adam Dunn (X - 51 - 14)
b8.new_ab(is_risp=True)
b8.pitch_list("b s b c s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: CWS #43 Addison Reed
t9 = game.new_inning()

# Pitching change (CWS): #43 Addison Reed replaces #27 Matt Lindstrom
t9.pitching_substitution(43)

# 5. BOS #12 Mike Napoli (X - X - X)
t9.new_ab()
t9.pitch_list("b c b f s")
t9.out("K")

# 6. BOS #29 Daniel Nava (X - X - X)
t9.new_ab()
t9.pitch_list("c")
t9.out("F7")

# 7. BOS #16 Will Middlebrooks (X - X - X)
t9.new_ab()
t9.pitch_list("c b c")
t9.out("F8")

# Winning team: CWS
# WP: CWS #62 Jose Quintana
game.winning_pitcher(62)
# SV: CWS #43 Addison Reed
game.save_pitcher(43)

# Loser team: BOS
# LP: BOS #22 Felix Doubront
game.losing_pitcher(22, is_away_team=True)

# print(game)
game.generate_scorecard()
