import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ LAA, 2013-07-07
# https://www.baseball-reference.com/boxes/ANA/ANA201307070.shtml
# https://www.mlb.com/gameday/red-sox-vs-angels/2013/07/07/348057/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-07-07 20:08-23:05",
        "at": "Angel Stadium of Anaheim, Anaheim, CA",
        "att": "39,018",
        "temp": "81F, Partly Cloudy",
        "wind": "3mph, Out To CF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 41,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                29: "Daniel Nava",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                37: "Mike Carp",
                20: "Ryan Lavarnway",
                26: "Brock Holt",
                10: "Jose Iglesias",
                # Starting pitcher
                41: "John Lackey",
                # Bench
                39: "Jarrod Saltalamacchia",
                18: "Shane Victorino",
                5: "Jonny Gomes",
                23: "Brandon Snyder",
                # Bullpen
                63: "Alex Wilson",
                65: "Jose De La Torre",
                40: "Andrew Bailey",
                32: "Craig Breslow",
                91: "Alfredo Aceves",
                31: "Jon Lester",
                36: "Junichi Tazawa",
                64: "Allen Webster",
                19: "Koji Uehara",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [32, 31, 22],
            "lineup": [
                [2, "8"],
                [29, "9"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [37, "7"],
                [20, "2"],
                [26, "5"],
                [10, "6"],
            ],
            "bench": [
                [39, "C"],
                [18, "CF"],
                [5, "LF"],
                [23, "1B"],
            ],
            "bullpen": [63, 65, 40, 32, 91, 31, 36, 64, 19, 22, 46],
        },
        "home": {
            "team": "Los Angeles Angels",
            "starter": 36,
            "roster": {
                # Lineup
                39: "JB Shuck",
                27: "Mike Trout",
                5: "Albert Pujols",
                32: "Josh Hamilton",
                47: "Howie Kendrick",
                6: "Alberto Callaspo",
                10: "Brad Hawpe",
                16: "Hank Conger",
                2: "Erick Aybar",
                # Starting pitcher
                36: "Jered Weaver",
                # Bench
                17: "Chris Iannetta",
                20: "Brendan Harris",
                19: "Collin Cowgill",
                44: "Mark Trumbo",
                # Bullpen
                55: "Joe Blanton",
                33: "C.J. Wilson",
                49: "Ernesto Frieri",
                65: "Dane De La Rosa",
                40: "Kevin Jepsen",
                58: "Michael Kohn",
                37: "Scott Downs",
                57: "Jerome Williams",
                51: "Michael Roth",
                31: "Billy Buckner",
            },
            "lefties": [33, 37, 51],
            "lineup": [
                [39, "7"],
                [27, "8"],
                [5, "0"],
                [32, "9"],
                [47, "4"],
                [6, "5"],
                [10, "3"],
                [16, "2"],
                [2, "6"],
            ],
            "bench": [
                [17, "C"],
                [20, "SS"],
                [19, "LF"],
                [44, "1B"],
            ],
            "bullpen": [55, 33, 49, 65, 40, 58, 37, 57, 51, 31],
        },
        "umpires": {
            "HP": "Mike Winters",
            "1B": "Mark Wegner",
            "2B": "Laz Diaz",
            "3B": "Tim Timmons",
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
# Pitching: LAA #36 Jered Weaver
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.pitch_list("c")
t1.hit(2)
t1.advance(3, "29 1B")

# 2. BOS #29 Daniel Nava (X - 2 - X)
t1.new_ab()
t1.pitch_list("b s b")
t1.hit(1)

# 3. BOS #15 Dustin Pedroia (2 - X - 29)
t1.new_ab()
t1.pitch_list("c f f")
t1.out("L5")

# 4. BOS #34 David Ortiz (2 - X - 29)
t1.new_ab()
t1.pitch_list("b b c s s")
t1.out("K")

# 5. BOS #12 Mike Napoli (2 - X - 29)
t1.new_ab()
t1.pitch_list("b b s 1 c f b s")
t1.out("K")


# Bot 1st
# Pitching: BOS #41 John Lackey
b1 = game.new_inning()

# 1. LAA #39 JB Shuck (X - X - X)
b1.new_ab()
b1.pitch_list("c c f b s")
b1.out("K")

# 2. LAA #27 Mike Trout (X - X - X)
b1.new_ab()
b1.pitch_list("s b")
b1.hit(4)

# 3. LAA #5  Albert Pujols (X - X - X)
b1.new_ab()
b1.pitch_list("c c f s")
b1.out("K")

# 4. LAA #32 Josh Hamilton (X - X - X)
b1.new_ab()
b1.pitch_list("b b b c c s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: LAA #36 Jered Weaver
t2 = game.new_inning()

# 6. BOS #37 Mike Carp (X - X - X)
t2.new_ab()
t2.pitch_list("c s b b f b c")
t2.out("!K")

# 7. BOS #20 Ryan Lavarnway (X - X - X)
t2.new_ab()
t2.pitch_list("b c b b c f")
t2.hit(1)
t2.advance(2, "26 G4-3")

# 8. BOS #26 Brock Holt (X - X - 20)
t2.new_ab()
t2.pitch_list("b 1 c s b b")
t2.out("G4-3")

# 9. BOS #10 Jose Iglesias (X - 20 - X)
t2.new_ab()
t2.pitch_list("c f")
t2.out("G5-3")


# Bot 2nd
# Pitching: BOS #41 John Lackey
b2 = game.new_inning()

# 5. LAA #47 Howie Kendrick (X - X - X)
b2.new_ab()
b2.pitch_list("s")
b2.out("B1-3")

# 6. LAA #6  Alberto Callaspo (X - X - X)
b2.new_ab()
b2.pitch_list("c b b s f")
b2.hit(1)
b2.thrown_out(2, "10 CS", 3, 41)

# 7. LAA #10 Brad Hawpe (X - X - 6)
b2.new_ab()
b2.pitch_list("b s b b s c")
b2.out("KDP2-6")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: LAA #36 Jered Weaver
t3 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t3.new_ab()
t3.pitch_list("c c")
t3.out("G3")

# 2. BOS #29 Daniel Nava (X - X - X)
t3.new_ab()
t3.pitch_list("c")
t3.out("(F)F7")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t3.new_ab()
t3.pitch_list("b c c f b b")
t3.out("G5-3")


# Bot 3rd
# Pitching: BOS #41 John Lackey
b3 = game.new_inning()

# 8. LAA #16 Hank Conger (X - X - X)
b3.new_ab()
b3.pitch_list("c s s")
b3.out("K")

# 9. LAA #2  Erick Aybar (X - X - X)
b3.new_ab()
b3.out("G5-3")

# 1. LAA #39 JB Shuck (X - X - X)
b3.new_ab()
b3.pitch_list("b")
b3.hit(1)
b3.advance(2, "27 SB")

# 2. LAA #27 Mike Trout (X - X - 39)
b3.new_ab()
b3.pitch_list("c s b f d b t")
b3.out("KT")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: LAA #36 Jered Weaver
t4 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
t4.new_ab()
t4.pitch_list("b c b")
t4.out("G6-3")

# 5. BOS #12 Mike Napoli (X - X - X)
t4.new_ab()
t4.pitch_list("s b b b d")
t4.reach("BB")

# 6. BOS #37 Mike Carp (X - X - 12)
t4.new_ab()
t4.pitch_list("c b s f s")
t4.out("K")

# 7. BOS #20 Ryan Lavarnway (X - X - 12)
t4.new_ab()
t4.pitch_list("c d b f t")
t4.out("KT")


# Bot 4th
# Pitching: BOS #41 John Lackey
b4 = game.new_inning()

# 3. LAA #5  Albert Pujols (X - X - X)
b4.new_ab()
b4.pitch_list("b s b f")
b4.out("F7")

# 4. LAA #32 Josh Hamilton (X - X - X)
b4.new_ab()
b4.pitch_list("c s b b b c")
b4.out("!K")

# 5. LAA #47 Howie Kendrick (X - X - X)
b4.new_ab()
b4.pitch_list("b b b c")
b4.out("G6-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: LAA #36 Jered Weaver
t5 = game.new_inning()

# 8. BOS #26 Brock Holt (X - X - X)
t5.new_ab()
t5.pitch_list("b b c s b f b")
t5.reach("BB")
t5.thrown_out(2, "2 DP6-4-3", 2, 36)

# 9. BOS #10 Jose Iglesias (X - X - 26)
t5.new_ab()
t5.pitch_list("1 l")
t5.out("P4")

# 1. BOS #2  Jacoby Ellsbury (X - X - 26)
t5.new_ab()
t5.pitch_list("b f f b 1 b")
t5.out("DP6-4-3")


# Bot 5th
# Pitching: BOS #41 John Lackey
b5 = game.new_inning()

# 6. LAA #6  Alberto Callaspo (X - X - X)
b5.new_ab()
b5.pitch_list("c s b c")
b5.out("!K")

# 7. LAA #10 Brad Hawpe (X - X - X)
b5.new_ab()
b5.pitch_list("b")
b5.out("G4-3")

# 8. LAA #16 Hank Conger (X - X - X)
b5.new_ab()
b5.pitch_list("b f b")
b5.hit(4)

# 9. LAA #2  Erick Aybar (X - X - X)
b5.new_ab()
b5.pitch_list("c f")
b5.out("G5-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: LAA #36 Jered Weaver
t6 = game.new_inning()

# 2. BOS #29 Daniel Nava (X - X - X)
t6.new_ab()
t6.pitch_list("b c")
t6.out("F8")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t6.new_ab()
t6.pitch_list("c b")
t6.out("G4-3")

# 4. BOS #34 David Ortiz (X - X - X)
t6.new_ab()
t6.pitch_list("b b")
t6.out("G3")


# Bot 6th
# Pitching: BOS #41 John Lackey
b6 = game.new_inning()

# 1. LAA #39 JB Shuck (X - X - X)
b6.new_ab()
b6.pitch_list("b b c")
b6.out("G4-3")

# 2. LAA #27 Mike Trout (X - X - X)
b6.new_ab()
b6.pitch_list("c b b b")
b6.out("G4-3")

# 3. LAA #5  Albert Pujols (X - X - X)
b6.new_ab()
b6.pitch_list("b c b s b")
b6.hit(1)
b6.advance(2, "32 BB")
b6.advance(3, "47 SB")

# 4. LAA #32 Josh Hamilton (X - X - 5)
b6.new_ab()
b6.pitch_list("b b s f b b")
b6.reach("BB")
b6.advance(2, "47 SB")

# 5. LAA #47 Howie Kendrick (X - 5 - 32)
b6.new_ab()
b6.pitch_list("n c d 1 f b f b f")
b6.out("G6-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: LAA #36 Jered Weaver
t7 = game.new_inning()

# 5. BOS #12 Mike Napoli (X - X - X)
t7.new_ab()
t7.pitch_list("c c b f")
t7.hit(1)
t7.advance(2, "26 1B")

# 6. BOS #37 Mike Carp (X - X - 12)
t7.new_ab()
t7.pitch_list("s b f s")
t7.out("K")

# 7. BOS #20 Ryan Lavarnway (X - X - 12)
t7.new_ab()
t7.out("F9")

# 8. BOS #26 Brock Holt (X - X - 12)
t7.new_ab()
t7.pitch_list("f b b")
t7.hit(1)

# Pitching change (LAA): #65 Dane De La Rosa replaces #36 Jered Weaver
t7.pitching_substitution(65)

# 9. BOS #10 Jose Iglesias (X - 12 - 26)
t7.new_ab()
t7.pitch_list("c")
t7.out("F9")


# Bot 7th
# Pitching: BOS #41 John Lackey
b7 = game.new_inning()

# 6. LAA #6  Alberto Callaspo (X - X - X)
b7.new_ab()
b7.pitch_list("b f b b")
b7.out("G1-3")

# 7. LAA #10 Brad Hawpe (X - X - X)
b7.new_ab()
b7.pitch_list("s c b b s")
b7.out("K")

# 8. LAA #16 Hank Conger (X - X - X)
b7.new_ab()
b7.pitch_list("c b")
b7.out("G3-1")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: LAA #37 Scott Downs
t8 = game.new_inning()

# Pitching change (LAA): #37 Scott Downs replaces #65 Dane De La Rosa
t8.pitching_substitution(37)

# Defensive change (LAA): #44 Mark Trumbo replaces #39 JB Shuck (LF), playing 1B, batting 1st
t8.defensive_substitution(1, 44, "3")

# Defensive change (LAA): #19 Collin Cowgill replaces #10 Brad Hawpe (1B), playing LF, batting 7th
t8.defensive_substitution(7, 19, "7")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t8.new_ab()
t8.pitch_list("c b")
t8.out("(F)P5")

# 2. BOS #29 Daniel Nava (X - X - X)
t8.new_ab()
t8.pitch_list("c b c f c")
t8.out("!K")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t8.new_ab()
t8.pitch_list("c b")
t8.out("G5-3")


# Bot 8th
# Pitching: BOS #36 Junichi Tazawa
b8 = game.new_inning()

# Pitching change (BOS): #36 Junichi Tazawa replaces #41 John Lackey
b8.pitching_substitution(36)

# 9. LAA #2  Erick Aybar (X - X - X)
b8.new_ab()
b8.hit(3)
b8.advance(4, "44 SF8")

# 1. LAA #44 Mark Trumbo (2 - X - X)
b8.new_ab()
b8.pitch_list("d")
b8.out("SF8", rbis=1)

# 2. LAA #27 Mike Trout (X - X - X)
b8.new_ab()
b8.pitch_list("b b b b")
b8.reach("BB")
b8.advance(3, "32 2B")

# Pitching change (BOS): #91 Alfredo Aceves replaces #36 Junichi Tazawa
b8.pitching_substitution(91)

# 3. LAA #5  Albert Pujols (X - X - 27)
b8.new_ab()
b8.pitch_list("f")
b8.out("P6")

# 4. LAA #32 Josh Hamilton (X - X - 27)
b8.new_ab()
b8.pitch_list("b")
b8.hit(2)

# 5. LAA #47 Howie Kendrick (27 - 32 - X)
b8.new_ab()
b8.pitch_list("f")
b8.out("G3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: LAA #49 Ernesto Frieri
t9 = game.new_inning()

# Pitching change (LAA): #49 Ernesto Frieri replaces #37 Scott Downs
t9.pitching_substitution(49)

# 4. BOS #34 David Ortiz (X - X - X)
t9.new_ab()
t9.pitch_list("b b s f f")
t9.error(3)
t9.reach("E3", end_base=2)

# 5. BOS #12 Mike Napoli (X - 34 - X)
t9.new_ab()
t9.pitch_list("c f s")
t9.out("K")

# 6. BOS #37 Mike Carp (X - 34 - X)
t9.new_ab()
t9.pitch_list("b s f b s")
t9.out("K")

# 7. BOS #20 Ryan Lavarnway (X - 34 - X)
t9.new_ab()
t9.pitch_list("c b c c")
t9.out("!K")

# Winning team: LAA
# WP: LAA #36 Jered Weaver
game.winning_pitcher(36)
# SV: LAA #49 Ernesto Frieri
game.save_pitcher(49)

# Loser team: BOS
# LP: BOS #41 John Lackey
game.losing_pitcher(41, is_away_team=True)

# print(game)
game.generate_scorecard()
