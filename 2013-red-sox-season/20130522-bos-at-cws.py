import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ CWS, 2013-05-22
# https://www.baseball-reference.com/boxes/CHA/CHA201305220.shtml
# https://www.mlb.com/gameday/red-sox-vs-white-sox/2013/05/22/347430/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-05-22 20:10-23:25",
        "at": "U.S. Cellular Field, Chicago, IL",
        "att": "21,298",
        "temp": "71F, Partly Cloudy",
        "wind": "12mph, Out To LF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 11,
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
                11: "Clay Buchholz",
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
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [30, 32, 31, 22],
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
            "bullpen": [63, 40, 41, 30, 32, 19, 31, 59, 36, 22, 46],
        },
        "home": {
            "team": "Chicago White Sox",
            "starter": 53,
            "roster": {
                # Lineup
                30: "Alejandro De Aza",
                10: "Alexei Ramirez",
                51: "Alex Rios",
                44: "Adam Dunn",
                14: "Paul Konerko",
                24: "Dayan Viciedo",
                12: "Conor Gillaspie",
                7: "Jeff Keppinger",
                21: "Tyler Flowers",
                # Starting pitcher
                53: "Héctor Santiago",
                # Bench
                38: "Hector Gimenez",
                39: "Casper Wells",
                28: "Dewayne Wise",
                1: "Tyler Greene",
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
                33: "Dylan Axelrod",
                37: "Matt Thornton",
            },
            "lefties": [53, 49, 62, 46, 37],
            "lineup": [
                [30, "8"],
                [10, "6"],
                [51, "9"],
                [44, "0"],
                [14, "3"],
                [24, "7"],
                [12, "5"],
                [7, "4"],
                [21, "2"],
            ],
            "bench": [
                [38, "C"],
                [39, "RF"],
                [28, "CF"],
                [1, "2B"],
            ],
            "bullpen": [27, 65, 48, 43, 49, 44, 62, 26, 46, 33, 37],
        },
        "umpires": {
            "HP": "Mike DiMuro",
            "1B": "Ted Barrett",
            "2B": "Alfonso Márquez",
            "3B": "Chris Conroy",
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
# Pitching: CWS #53 Héctor Santiago
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.pitch_list("c c")
t1.out("G1-3")

# 2. BOS #5  Jonny Gomes (X - X - X)
t1.new_ab()
t1.pitch_list("b c s f")
t1.reach("HBP")
t1.advance(3, "15 2B")
t1.advance(4, "34 1B")

# 3. BOS #15 Dustin Pedroia (X - X - 5)
t1.new_ab()
t1.pitch_list("c b b")
t1.hit(2)
t1.advance(4, "34 1B")

# 4. BOS #34 David Ortiz (5 - 15 - X)
t1.new_ab()
t1.pitch_list("c")
t1.hit(1, rbis=2)
t1.advance(2, "12 BB")
t1.advance(3, "29 SB")

# 5. BOS #12 Mike Napoli (X - X - 34)
t1.new_ab()
t1.pitch_list("b b b b")
t1.reach("BB")

# 6. BOS #29 Daniel Nava (X - 34 - 12)
t1.new_ab()
t1.pitch_list("c b b b s c")
t1.out("!K")

# 7. BOS #16 Will Middlebrooks (34 - X - 12)
t1.new_ab()
t1.pitch_list("c s b b s")
t1.out("K")


# Bot 1st
# Pitching: BOS #11 Clay Buchholz
b1 = game.new_inning()

# 1. CWS #30 Alejandro De Aza (X - X - X)
b1.new_ab()
b1.pitch_list("c")
b1.hit(1)
b1.thrown_out(2, "10 CS", 1, 11)

# 2. CWS #10 Alexei Ramirez (X - X - 30)
b1.new_ab()
b1.pitch_list("1 1 1 1 c b 1 f b b b")
b1.reach("BB")
b1.advance(2, "51 BB")

# 3. CWS #51 Alex Rios (X - X - 10)
b1.new_ab()
b1.pitch_list("b 1 d d b")
b1.reach("BB")

# 4. CWS #44 Adam Dunn (X - 10 - 51)
b1.new_ab()
b1.pitch_list("c b c s")
b1.out("K")

# 5. CWS #14 Paul Konerko (X - 10 - 51)
b1.new_ab()
b1.pitch_list("c b f b b")
b1.out("L7")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: CWS #53 Héctor Santiago
t2 = game.new_inning()

# 8. BOS #7  Stephen Drew (X - X - X)
t2.new_ab()
t2.pitch_list("c b b b s s")
t2.out("K")

# 9. BOS #39 Jarrod Saltalamacchia (X - X - X)
t2.new_ab()
t2.pitch_list("b f b c b s")
t2.out("K")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t2.new_ab()
t2.pitch_list("c")
t2.hit(1)

# 2. BOS #5  Jonny Gomes (X - X - 2)
t2.new_ab()
t2.pitch_list("c s")
t2.out("F7")


# Bot 2nd
# Pitching: BOS #11 Clay Buchholz
b2 = game.new_inning()

# 6. CWS #24 Dayan Viciedo (X - X - X)
b2.new_ab()
b2.pitch_list("c b b f b")
b2.out("G6-3")

# 7. CWS #12 Conor Gillaspie (X - X - X)
b2.new_ab()
b2.pitch_list("c f")
b2.out("F8")

# 8. CWS #7  Jeff Keppinger (X - X - X)
b2.new_ab()
b2.pitch_list("b c f")
b2.out("G6-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: CWS #53 Héctor Santiago
t3 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
t3.new_ab()
t3.pitch_list("c b f f f b b f b")
t3.reach("BB")
t3.thrown_out(2, "34 DP4-6-3", 1, 53)

# 4. BOS #34 David Ortiz (X - X - 15)
t3.new_ab()
t3.pitch_list("b 1")
t3.out("DP4-6-3")

# 5. BOS #12 Mike Napoli (X - X - X)
t3.new_ab()
t3.pitch_list("b b b c c f b")
t3.reach("BB")

# 6. BOS #29 Daniel Nava (X - X - 12)
t3.new_ab()
t3.pitch_list("1 b t s b s")
t3.out("K")


# Bot 3rd
# Pitching: BOS #11 Clay Buchholz
b3 = game.new_inning()

# 9. CWS #21 Tyler Flowers (X - X - X)
b3.new_ab()
b3.pitch_list("b c c b")
b3.hit(1)
b3.advance(2, "30 BB")
b3.advance(3, "10 FC6-4")
b3.advance(4, "51 G6-3")

# 1. CWS #30 Alejandro De Aza (X - X - 21)
b3.new_ab()
b3.pitch_list("b s s b f f f b b")
b3.reach("BB")
b3.thrown_out(2, "10 FC6-4", 1, 11)

# 2. CWS #10 Alexei Ramirez (X - 21 - 30)
b3.new_ab()
b3.pitch_list("c")
b3.reach("FC6-4")
b3.advance(2, "51 G6-3")

# 3. CWS #51 Alex Rios (21 - X - 10)
b3.new_ab()
b3.pitch_list("b b 1 b c s")
b3.out("G6-3", rbis=1)

# 4. CWS #44 Adam Dunn (X - 10 - X)
b3.new_ab()
b3.pitch_list("b b s s s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: CWS #53 Héctor Santiago
t4 = game.new_inning()

# 7. BOS #16 Will Middlebrooks (X - X - X)
t4.new_ab()
t4.pitch_list("b c c b f s")
t4.out("K")

# 8. BOS #7  Stephen Drew (X - X - X)
t4.new_ab()
t4.pitch_list("b b c t s")
t4.out("K")

# 9. BOS #39 Jarrod Saltalamacchia (X - X - X)
t4.new_ab()
t4.pitch_list("c c s")
t4.out("K")


# Bot 4th
# Pitching: BOS #11 Clay Buchholz
b4 = game.new_inning()

# 5. CWS #14 Paul Konerko (X - X - X)
b4.new_ab()
b4.hit(1)
b4.thrown_out(2, "24 FC6-4", 1, 11)

# 6. CWS #24 Dayan Viciedo (X - X - 14)
b4.new_ab()
b4.pitch_list("f")
b4.reach("FC6-4")
b4.thrown_out(2, "12 DP4-6-3", 2, 11)

# 7. CWS #12 Conor Gillaspie (X - X - 24)
b4.new_ab()
b4.pitch_list("b c f f b f")
b4.out("DP4-6-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: CWS #53 Héctor Santiago
t5 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t5.new_ab()
t5.pitch_list("b b b b")
t5.reach("BB")
t5.thrown_out(2, "5 DP5-4-3", 1, 53)

# 2. BOS #5  Jonny Gomes (X - X - 2)
t5.new_ab()
t5.pitch_list("c")
t5.out("DP5-4-3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t5.new_ab()
t5.pitch_list("b f f f")
t5.out("(F)P3")


# Bot 5th
# Pitching: BOS #11 Clay Buchholz
b5 = game.new_inning()

# 8. CWS #7  Jeff Keppinger (X - X - X)
b5.new_ab()
b5.pitch_list("b c c")
b5.hit(1)
b5.thrown_out(2, "30 FC4-6", 2, 11)

# 9. CWS #21 Tyler Flowers (X - X - 7)
b5.new_ab()
b5.pitch_list("b f b s c")
b5.out("!K")

# 1. CWS #30 Alejandro De Aza (X - X - 7)
b5.new_ab()
b5.pitch_list("b b c f")
b5.reach("FC4-6")

# 2. CWS #10 Alexei Ramirez (X - X - 30)
b5.new_ab()
b5.pitch_list("b c f")
b5.out("L8")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: CWS #53 Héctor Santiago
t6 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
t6.new_ab()
t6.pitch_list("c b b f")
t6.out("F8")

# 5. BOS #12 Mike Napoli (X - X - X)
t6.new_ab()
t6.pitch_list("b c c s")
t6.out("K")

# 6. BOS #29 Daniel Nava (X - X - X)
t6.new_ab()
t6.pitch_list("s b b")
t6.out("(F)P3")


# Bot 6th
# Pitching: BOS #11 Clay Buchholz
b6 = game.new_inning()

# 3. CWS #51 Alex Rios (X - X - X)
b6.new_ab()
b6.pitch_list("c f b f")
b6.hit(1)
b6.thrown_out(2, "24 CS", 3, 11)

# 4. CWS #44 Adam Dunn (X - X - 51)
b6.new_ab()
b6.pitch_list("c 1")
b6.out("P4")

# 5. CWS #14 Paul Konerko (X - X - 51)
b6.new_ab()
b6.pitch_list("b b c")
b6.out("F7")

# 6. CWS #24 Dayan Viciedo (X - X - 51)
b6.new_ab()
b6.pitch_list("b f s")
b6.no_ab("CS")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: CWS #48 Brian Omogrosso
t7 = game.new_inning()

# Pitching change (CWS): #48 Brian Omogrosso replaces #53 Héctor Santiago
t7.pitching_substitution(48)

# 7. BOS #16 Will Middlebrooks (X - X - X)
t7.new_ab()
t7.pitch_list("b")
t7.out("F8")

# 8. BOS #7  Stephen Drew (X - X - X)
t7.new_ab()
t7.pitch_list("b c b f")
t7.out("P6")

# 9. BOS #39 Jarrod Saltalamacchia (X - X - X)
t7.new_ab()
t7.pitch_list("b s")
t7.hit(1)
t7.advance(2, "2 1B")

# 1. BOS #2  Jacoby Ellsbury (X - X - 39)
t7.new_ab()
t7.hit(1)

# 2. BOS #5  Jonny Gomes (X - 39 - 2)
t7.new_ab()
t7.out("G4-3")


# Bot 7th
# Pitching: BOS #11 Clay Buchholz
b7 = game.new_inning()

# 6. CWS #24 Dayan Viciedo (X - X - X)
b7.new_ab()
b7.pitch_list("s f s")
b7.out("K")

# 7. CWS #12 Conor Gillaspie (X - X - X)
b7.new_ab()
b7.pitch_list("b")
b7.out("F7")

# 8. CWS #7  Jeff Keppinger (X - X - X)
b7.new_ab()
b7.pitch_list("b c b")
b7.out("L9")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: CWS #48 Brian Omogrosso
t8 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
t8.new_ab()
t8.pitch_list("b b")
t8.out("L7")

# 4. BOS #34 David Ortiz (X - X - X)
t8.new_ab()
t8.pitch_list("c b b f f")
t8.hit(1)
t8.advance(2, "12 1B")
t8.advance(3, "29 BB")
t8.advance(4, "16 SF9")

# 5. BOS #12 Mike Napoli (X - X - 34)
t8.new_ab()
t8.pitch_list("b s b c")
t8.hit(1)
t8.advance(2, "29 BB")
t8.advance(3, "16 SF9")
t8.advance("U", "39 PB")

# 6. BOS #29 Daniel Nava (X - 34 - 12)
t8.new_ab()
t8.pitch_list("b d b b")
t8.reach("BB")
t8.advance(2, "7 BB")
t8.advance(3, "39 PB")

# Pitching change (CWS): #65 Nate Jones replaces #48 Brian Omogrosso
t8.pitching_substitution(65)

# 7. BOS #16 Will Middlebrooks (34 - 12 - 29)
t8.new_ab()
t8.pitch_list("b b c")
t8.out("SF9", rbis=1)

# 8. BOS #7  Stephen Drew (12 - X - 29)
t8.new_ab()
t8.pitch_list("b b b b")
t8.reach("BB")
t8.advance(2, "39 PB")

# 9. BOS #39 Jarrod Saltalamacchia (12 - 29 - 7)
t8.new_ab()
t8.pitch_list("b f f b s")
t8.pb()
t8.out("K")


# Bot 8th
# Pitching: BOS #19 Koji Uehara
b8 = game.new_inning()

# Pitching change (BOS): #19 Koji Uehara replaces #11 Clay Buchholz
b8.pitching_substitution(19)

# 9. CWS #21 Tyler Flowers (X - X - X)
b8.new_ab()
b8.pitch_list("f c b c")
b8.out("!K")

# 1. CWS #30 Alejandro De Aza (X - X - X)
b8.new_ab()
b8.pitch_list("c s b s")
b8.out("K")

# 2. CWS #10 Alexei Ramirez (X - X - X)
b8.new_ab()
b8.out("L7")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: CWS #65 Nate Jones
t9 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t9.new_ab()
t9.pitch_list("b b c t b f f f f b")
t9.reach("BB")
t9.advance(2, "5 1B")
t9.advance(3, "12 BB")
t9.advance(4, "29 1B")

# 2. BOS #5  Jonny Gomes (X - X - 2)
t9.new_ab()
t9.pitch_list("c c")
t9.hit(1)
t9.advance(2, "12 BB")
t9.advance(4, "29 1B")

# 3. BOS #15 Dustin Pedroia (X - 2 - 5)
t9.new_ab()
t9.pitch_list("c c s")
t9.out("K")

# Pitching change (CWS): #46 Donnie Veal replaces #65 Nate Jones
t9.pitching_substitution(46)

# 4. BOS #34 David Ortiz (X - 2 - 5)
t9.new_ab()
t9.pitch_list("b b f")
t9.out("L8")

# 5. BOS #12 Mike Napoli (X - 2 - 5)
t9.new_ab()
t9.pitch_list("b d b b")
t9.reach("BB")
t9.advance(2, "29 1B")
t9.thrown_out(3, "16 FC5", 3, 46)

# 6. BOS #29 Daniel Nava (2 - 5 - 12)
t9.new_ab()
t9.pitch_list("b c b")
t9.hit(1, rbis=2)
t9.advance(2, "16 FC5")

# 7. BOS #16 Will Middlebrooks (X - 12 - 29)
t9.new_ab()
t9.pitch_list("c b b b f f f")
t9.reach("FC5")


# Bot 9th
# Pitching: BOS #40 Andrew Bailey
b9 = game.new_inning()

# Pitching change (BOS): #40 Andrew Bailey replaces #19 Koji Uehara
b9.pitching_substitution(40)

# 3. CWS #51 Alex Rios (X - X - X)
b9.new_ab()
b9.pitch_list("b s")
b9.out("(F)P5")

# 4. CWS #44 Adam Dunn (X - X - X)
b9.new_ab()
b9.pitch_list("c b f")
b9.out("G5-3")

# 5. CWS #14 Paul Konerko (X - X - X)
b9.new_ab()
b9.hit(4)

# 6. CWS #24 Dayan Viciedo (X - X - X)
b9.new_ab()
b9.pitch_list("c s s")
b9.out("K")

# Winning team: BOS
# WP: BOS #11 Clay Buchholz
game.winning_pitcher(11, is_away_team=True)

# Loser team: CWS
# LP: CWS #53 Héctor Santiago
game.losing_pitcher(53)

# print(game)
game.generate_scorecard()
