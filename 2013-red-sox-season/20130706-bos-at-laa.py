import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ LAA, 2013-07-06
# https://www.baseball-reference.com/boxes/ANA/ANA201307060.shtml
# https://www.mlb.com/gameday/red-sox-vs-angels/2013/07/06/348042/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-07-06 22:07-02:29 +1",
        "at": "Angel Stadium of Anaheim, Anaheim, CA",
        "att": "36,112",
        "temp": "72F, Partly Cloudy",
        "wind": "6mph, Out To CF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 46,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                29: "Daniel Nava",
                39: "Jarrod Saltalamacchia",
                26: "Brock Holt",
                10: "Jose Iglesias",
                # Starting pitcher
                46: "Ryan Dempster",
                # Bench
                37: "Mike Carp",
                5: "Jonny Gomes",
                20: "Ryan Lavarnway",
                23: "Brandon Snyder",
                # Bullpen
                63: "Alex Wilson",
                65: "Jose De La Torre",
                40: "Andrew Bailey",
                41: "John Lackey",
                30: "Andrew Miller",
                32: "Craig Breslow",
                31: "Jon Lester",
                36: "Junichi Tazawa",
                64: "Allen Webster",
                19: "Koji Uehara",
                22: "Felix Doubront",
            },
            "lefties": [30, 32, 31, 22],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [29, "7"],
                [39, "2"],
                [26, "5"],
                [10, "6"],
            ],
            "bench": [
                [37, "1B"],
                [5, "LF"],
                [20, "C"],
                [23, "1B"],
            ],
            "bullpen": [63, 65, 40, 41, 30, 32, 31, 36, 64, 19, 22],
        },
        "home": {
            "team": "Los Angeles Angels",
            "starter": 57,
            "roster": {
                # Lineup
                39: "JB Shuck",
                27: "Mike Trout",
                5: "Albert Pujols",
                32: "Josh Hamilton",
                47: "Howie Kendrick",
                44: "Mark Trumbo",
                2: "Erick Aybar",
                17: "Chris Iannetta",
                20: "Brendan Harris",
                # Starting pitcher
                57: "Jerome Williams",
                # Bench
                16: "Hank Conger",
                19: "Collin Cowgill",
                10: "Brad Hawpe",
                6: "Alberto Callaspo",
                # Bullpen
                55: "Joe Blanton",
                49: "Ernesto Frieri",
                65: "Dane De La Rosa",
                33: "C.J. Wilson",
                40: "Kevin Jepsen",
                58: "Michael Kohn",
                37: "Scott Downs",
                43: "Garrett Richards",
                51: "Michael Roth",
                36: "Jered Weaver",
                31: "Billy Buckner",
            },
            "lefties": [33, 37, 51],
            "lineup": [
                [39, "7"],
                [27, "8"],
                [5, "3"],
                [32, "9"],
                [47, "4"],
                [44, "0"],
                [2, "6"],
                [17, "2"],
                [20, "5"],
            ],
            "bench": [
                [16, "C"],
                [19, "LF"],
                [10, "RF"],
                [6, "3B"],
            ],
            "bullpen": [55, 49, 65, 33, 40, 58, 37, 43, 51, 36, 31],
        },
        "umpires": {
            "HP": "Tim Timmons",
            "1B": "Mike Winters",
            "2B": "Mark Wegner",
            "3B": "Laz Diaz",
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
# Pitching: LAA #57 Jerome Williams
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.pitch_list("b")
t1.hit(1)
t1.advance(2, "34 1B")
t1.error(2)
t1.advance(3, "12 SB")
t1.advance("U", "12 E2")

# 2. BOS #18 Shane Victorino (X - X - 2)
t1.new_ab()
t1.pitch_list("c s b 1 1 s")
t1.out("K")

# 3. BOS #15 Dustin Pedroia (X - X - 2)
t1.new_ab()
t1.out("L8")

# 4. BOS #34 David Ortiz (X - X - 2)
t1.new_ab()
t1.pitch_list("f 1 f p 1")
t1.hit(1)
t1.advance(2, "12 E2")

# 5. BOS #12 Mike Napoli (X - 2 - 34)
t1.new_ab()
t1.pitch_list("b f b")
t1.out("F8")


# Bot 1st
# Pitching: BOS #46 Ryan Dempster
b1 = game.new_inning()

# 1. LAA #39 JB Shuck (X - X - X)
b1.new_ab()
b1.pitch_list("c b c f f b b f")
b1.out("F7")

# 2. LAA #27 Mike Trout (X - X - X)
b1.new_ab()
b1.hit(2)

# 3. LAA #5  Albert Pujols (X - 27 - X)
b1.new_ab()
b1.pitch_list("f f")
b1.out("G6-3")

# 4. LAA #32 Josh Hamilton (X - 27 - X)
b1.new_ab()
b1.pitch_list("b f b")
b1.out("L8")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: LAA #57 Jerome Williams
t2 = game.new_inning()

# 6. BOS #29 Daniel Nava (X - X - X)
t2.new_ab()
t2.pitch_list("b c b")
t2.hit(1)
t2.advance(3, "39 2B")
t2.advance(4, "26 SF7")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - 29)
t2.new_ab()
t2.pitch_list("f b 1 s b")
t2.hit(2)

# 8. BOS #26 Brock Holt (29 - 39 - X)
t2.new_ab()
t2.pitch_list("b")
t2.out("SF7", rbis=1)

# 9. BOS #10 Jose Iglesias (X - 39 - X)
t2.new_ab()
t2.pitch_list("b c f")
t2.out("P4")

# 1. BOS #2  Jacoby Ellsbury (X - 39 - X)
t2.new_ab()
t2.out("G1-3")


# Bot 2nd
# Pitching: BOS #46 Ryan Dempster
b2 = game.new_inning()

# 5. LAA #47 Howie Kendrick (X - X - X)
b2.new_ab()
b2.pitch_list("b b b c")
b2.hit(4)

# 6. LAA #44 Mark Trumbo (X - X - X)
b2.new_ab()
b2.pitch_list("b c c")
b2.out("F9")

# 7. LAA #2  Erick Aybar (X - X - X)
b2.new_ab()
b2.hit(1)
b2.error(1)
b2.advance(2, "E1")
b2.advance("U", "17 1B")

# 8. LAA #17 Chris Iannetta (X - 2 - X)
b2.new_ab()
b2.hit(1, rbis=1)

# 9. LAA #20 Brendan Harris (X - X - 17)
b2.new_ab()
b2.pitch_list("1 c f f s")
b2.out("K")

# 1. LAA #39 JB Shuck (X - X - 17)
b2.new_ab()
b2.pitch_list("c d c b")
b2.out("G1-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: LAA #57 Jerome Williams
t3 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
t3.new_ab()
t3.pitch_list("s b b f b")
t3.out("G3-1")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t3.new_ab()
t3.pitch_list("c b f")
t3.out("F9")

# 4. BOS #34 David Ortiz (X - X - X)
t3.new_ab()
t3.pitch_list("b")
t3.out("G6-3")


# Bot 3rd
# Pitching: BOS #46 Ryan Dempster
b3 = game.new_inning()

# 2. LAA #27 Mike Trout (X - X - X)
b3.new_ab()
b3.pitch_list("b b")
b3.hit(4)

# 3. LAA #5  Albert Pujols (X - X - X)
b3.new_ab()
b3.pitch_list("c b")
b3.out("F9")

# 4. LAA #32 Josh Hamilton (X - X - X)
b3.new_ab()
b3.pitch_list("c s")
b3.out("G6-3")

# 5. LAA #47 Howie Kendrick (X - X - X)
b3.new_ab()
b3.out("F9")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: LAA #57 Jerome Williams
t4 = game.new_inning()

# 5. BOS #12 Mike Napoli (X - X - X)
t4.new_ab()
t4.pitch_list("c f b b b f b")
t4.reach("BB")
t4.advance(3, "29 2B")
t4.advance(4, "39 2B")

# 6. BOS #29 Daniel Nava (X - X - 12)
t4.new_ab()
t4.pitch_list("c 1 b")
t4.hit(2)
t4.advance(4, "39 2B")

# 7. BOS #39 Jarrod Saltalamacchia (12 - 29 - X)
t4.new_ab()
t4.pitch_list("b b f")
t4.hit(2, rbis=2)
t4.advance(3, "26 FC3")
t4.advance(4, "10 1B")

# 8. BOS #26 Brock Holt (X - 39 - X)
t4.new_ab()
t4.pitch_list("b")
t4.reach("FC3")
t4.advance(2, "10 1B")
t4.advance(3, "2 G3-1")

# 9. BOS #10 Jose Iglesias (39 - X - 26)
t4.new_ab()
t4.pitch_list("c")
t4.hit(1, rbis=1)
t4.advance(2, "2 G3-1")

# Pitching change (LAA): #43 Garrett Richards replaces #57 Jerome Williams
t4.pitching_substitution(43)

# 1. BOS #2  Jacoby Ellsbury (X - 26 - 10)
t4.new_ab()
t4.pitch_list("f b b d")
t4.out("G3-1")

# 2. BOS #18 Shane Victorino (26 - 10 - X)
t4.new_ab()
t4.pitch_list("c s s")
t4.out("K")

# 3. BOS #15 Dustin Pedroia (26 - 10 - X)
t4.new_ab()
t4.pitch_list("b c f d f d d")
t4.reach("BB")

# 4. BOS #34 David Ortiz (26 - 10 - 15)
t4.new_ab()
t4.pitch_list("d f f s")
t4.out("K")


# Bot 4th
# Pitching: BOS #46 Ryan Dempster
b4 = game.new_inning()

# 6. LAA #44 Mark Trumbo (X - X - X)
b4.new_ab()
b4.pitch_list("c b b s c")
b4.out("!K")

# 7. LAA #2  Erick Aybar (X - X - X)
b4.new_ab()
b4.pitch_list("c b c f")
b4.out("L7")

# 8. LAA #17 Chris Iannetta (X - X - X)
b4.new_ab()
b4.pitch_list("s b")
b4.hit(2)

# 9. LAA #20 Brendan Harris (X - 17 - X)
b4.new_ab()
b4.out("L8")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: LAA #43 Garrett Richards
t5 = game.new_inning()

# 5. BOS #12 Mike Napoli (X - X - X)
t5.new_ab()
t5.pitch_list("c s b s")
t5.out("K")

# 6. BOS #29 Daniel Nava (X - X - X)
t5.new_ab()
t5.pitch_list("f")
t5.hit(1)
t5.advance(2, "39 BB")
t5.advance(3, "26 G3")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - 29)
t5.new_ab()
t5.pitch_list("b b 1 f b b")
t5.reach("BB")
t5.advance(2, "26 G3")

# 8. BOS #26 Brock Holt (X - 29 - 39)
t5.new_ab()
t5.pitch_list("b c c d b f")
t5.out("G3")

# 9. BOS #10 Jose Iglesias (29 - 39 - X)
t5.new_ab()
t5.pitch_list("c c")
t5.out("G1-3")


# Bot 5th
# Pitching: BOS #46 Ryan Dempster
b5 = game.new_inning()

# 1. LAA #39 JB Shuck (X - X - X)
b5.new_ab()
b5.pitch_list("b l")
b5.hit(2)
b5.thrown_out(3, "27 DP9-5", 2, 46)

# 2. LAA #27 Mike Trout (X - 39 - X)
b5.new_ab()
b5.pitch_list("b s")
b5.out("DP9-5")

# 3. LAA #5  Albert Pujols (X - X - X)
b5.new_ab()
b5.pitch_list("c s b f b b f b")
b5.reach("BB")

# 4. LAA #32 Josh Hamilton (X - X - 5)
b5.new_ab()
b5.pitch_list("b s")
b5.out("G1-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: LAA #58 Michael Kohn
t6 = game.new_inning()

# Pitching change (LAA): #58 Michael Kohn replaces #43 Garrett Richards
t6.pitching_substitution(58)

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t6.new_ab()
t6.pitch_list("c c b")
t6.out("G5-3")

# 2. BOS #18 Shane Victorino (X - X - X)
t6.new_ab()
t6.pitch_list("c s b")
t6.hit(3)
t6.advance(4, "15 1B")

# 3. BOS #15 Dustin Pedroia (18 - X - X)
t6.new_ab()
t6.pitch_list("b")
t6.hit(1, rbis=1)
t6.advance(2, "12 BB")

# 4. BOS #34 David Ortiz (X - X - 15)
t6.new_ab()
t6.pitch_list("c f f")
t6.out("F8")

# 5. BOS #12 Mike Napoli (X - X - 15)
t6.new_ab()
t6.pitch_list("1 b b c b c b")
t6.reach("BB")

# 6. BOS #29 Daniel Nava (X - 15 - 12)
t6.new_ab()
t6.pitch_list("b")
t6.out("P6")


# Bot 6th
# Pitching: BOS #46 Ryan Dempster
b6 = game.new_inning()

# 5. LAA #47 Howie Kendrick (X - X - X)
b6.new_ab()
b6.pitch_list("c b s s")
b6.out("K")

# 6. LAA #44 Mark Trumbo (X - X - X)
b6.new_ab()
b6.pitch_list("s b b f")
b6.out("F9")

# 7. LAA #2  Erick Aybar (X - X - X)
b6.new_ab()
b6.pitch_list("b c t")
b6.out("L3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: LAA #51 Michael Roth
t7 = game.new_inning()

# Pitching change (LAA): #51 Michael Roth replaces #58 Michael Kohn
t7.pitching_substitution(51)

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
t7.new_ab()
t7.pitch_list("f b c b f c")
t7.out("!K")

# Offensive change (BOS): Pinch-hitter #23 Brandon Snyder replaces #26 Brock Holt, batting 8th
t7.offensive_substitution(8, 23, "PH")

# 8. BOS #23 Brandon Snyder (X - X - X)
t7.new_ab()
t7.pitch_list("c s f b f b b s")
t7.out("K")

# 9. BOS #10 Jose Iglesias (X - X - X)
t7.new_ab()
t7.pitch_list("b b b c b")
t7.reach("BB")
t7.advance(2, "2 CI")

# 1. BOS #2  Jacoby Ellsbury (X - X - 10)
t7.new_ab()
t7.pitch_list("b s b f f n")
t7.error(2)
t7.reach("CI")

# 2. BOS #18 Shane Victorino (X - 10 - 2)
t7.new_ab()
t7.pitch_list("b f")
t7.out("F7")


# Bot 7th
# Pitching: BOS #46 Ryan Dempster
b7 = game.new_inning()

# Defensive switch (BOS): #23 Brandon Snyder moves to 3B
b7.defensive_switch(23, "5")

# 8. LAA #17 Chris Iannetta (X - X - X)
b7.new_ab()
b7.pitch_list("s b s b f b b")
b7.reach("BB")
b7.advance(2, "39 WP")
b7.advance(3, "39 1B")

# 9. LAA #20 Brendan Harris (X - X - 17)
b7.new_ab()
b7.pitch_list("f c b b s")
b7.out("K")

# Pitching change (BOS): #30 Andrew Miller replaces #46 Ryan Dempster
b7.pitching_substitution(30)

# 1. LAA #39 JB Shuck (X - X - 17)
b7.new_ab()
b7.pitch_list("b c s b")
b7.wp()
b7.hit(1)
b7.thrown_out(2, "27 DP6-4-3", 2, 40)

# Pitching change (BOS): #40 Andrew Bailey replaces #30 Andrew Miller
b7.pitching_substitution(40)

# 2. LAA #27 Mike Trout (17 - X - 39)
b7.new_ab()
b7.out("DP6-4-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: LAA #40 Kevin Jepsen
t8 = game.new_inning()

# Pitching change (LAA): #40 Kevin Jepsen replaces #51 Michael Roth
t8.pitching_substitution(40)

# 3. BOS #15 Dustin Pedroia (X - X - X)
t8.new_ab()
t8.pitch_list("b")
t8.hit(1)
t8.advance(4, "29 E9")

# 4. BOS #34 David Ortiz (X - X - 15)
t8.new_ab()
t8.pitch_list("c")
t8.out("F8")

# 5. BOS #12 Mike Napoli (X - X - 15)
t8.new_ab()
t8.pitch_list("s 1 f b 1 b 1 b t")
t8.out("KT")

# 6. BOS #29 Daniel Nava (X - X - 15)
t8.new_ab()
t8.pitch_list("1")
t8.hit(2, rbis=1)
t8.error(9)
t8.advance(3, "E9")

# 7. BOS #39 Jarrod Saltalamacchia (29 - X - X)
t8.new_ab()
t8.pitch_list("i i i i")
t8.reach("IBB")

# 8. BOS #23 Brandon Snyder (29 - X - 39)
t8.new_ab()
t8.pitch_list("b f")
t8.out("F9")


# Bot 8th
# Pitching: BOS #40 Andrew Bailey
b8 = game.new_inning()

# 3. LAA #5  Albert Pujols (X - X - X)
b8.new_ab()
b8.pitch_list("b c c f")
b8.hit(1)
b8.advance(2, "47 G4-3")

# 4. LAA #32 Josh Hamilton (X - X - 5)
b8.new_ab()
b8.pitch_list("f f f s")
b8.out("K")

# 5. LAA #47 Howie Kendrick (X - X - 5)
b8.new_ab()
b8.pitch_list("c f")
b8.out("G4-3")

# 6. LAA #44 Mark Trumbo (X - 5 - X)
b8.new_ab()
b8.pitch_list("b c f s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: LAA #49 Ernesto Frieri
t9 = game.new_inning()

# Pitching change (LAA): #49 Ernesto Frieri replaces #40 Kevin Jepsen
t9.pitching_substitution(49)

# 9. BOS #10 Jose Iglesias (X - X - X)
t9.new_ab()
t9.pitch_list("b c")
t9.out("F8")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t9.new_ab()
t9.pitch_list("b b f b b")
t9.reach("BB")
t9.advance(2, "5 SB")

# Offensive change (BOS): Pinch-hitter #5 Jonny Gomes replaces #18 Shane Victorino, batting 2nd
t9.offensive_substitution(2, 5, "PH")

# 2. BOS #5  Jonny Gomes (X - X - 2)
t9.new_ab()
t9.pitch_list("b c c b c")
t9.out("!K")

# 3. BOS #15 Dustin Pedroia (X - 2 - X)
t9.new_ab()
t9.pitch_list("c c s")
t9.out("K")


# Bot 9th
# Pitching: BOS #63 Alex Wilson
b9 = game.new_inning()

# Pitching change (BOS): #63 Alex Wilson replaces #40 Andrew Bailey
b9.pitching_substitution(63)

# Defensive switch (BOS): #5 Jonny Gomes moves to LF
b9.defensive_switch(5, "7")

# Defensive switch (BOS): #29 Daniel Nava moves to RF
b9.defensive_switch(29, "9")

# 7. LAA #2  Erick Aybar (X - X - X)
b9.new_ab()
b9.pitch_list("c b c f f s")
b9.out("K2-3")

# 8. LAA #17 Chris Iannetta (X - X - X)
b9.new_ab()
b9.hit(1)
b9.advance(2, "39 1B")
b9.advance(3, "27 HBP")
b9.advance(4, "5 1B")

# Offensive change (LAA): Pinch-hitter #6 Alberto Callaspo replaces #20 Brendan Harris, batting 9th
b9.offensive_substitution(9, 6, "PH")

# 9. LAA #6  Alberto Callaspo (X - X - 17)
b9.new_ab()
b9.pitch_list("b f c b b")
b9.out("F8")

# 1. LAA #39 JB Shuck (X - X - 17)
b9.new_ab()
b9.pitch_list("b c")
b9.hit(1)
b9.advance(2, "27 HBP")
b9.advance(4, "5 1B")

# 2. LAA #27 Mike Trout (X - 17 - 39)
b9.new_ab()
b9.pitch_list("c")
b9.reach("HBP")
b9.advance(2, "5 1B")
b9.advance(4, "32 1B")

# Pitching change (BOS): #19 Koji Uehara replaces #63 Alex Wilson
b9.pitching_substitution(19)

# 3. LAA #5  Albert Pujols (17 - 39 - 27)
b9.new_ab()
b9.pitch_list("c b f d f f")
b9.hit(1, rbis=2)
# Offensive change (LAA): Pinch-runner #19 Collin Cowgill replaces #5 Albert Pujols
b9.offensive_substitution(3, 19, "PR")
b9.atbase("PR")
b9.advance(3, "32 1B")
b9.advance("U", "47 FC5")

# 4. LAA #32 Josh Hamilton (X - 27 - 5)
b9.new_ab()
b9.pitch_list("f d")
b9.hit(1, rbis=1)
b9.error(5)
b9.advance(2, "47 FC5")
b9.advance(3, "47 E5")

# 5. LAA #47 Howie Kendrick (19 - X - 32)
b9.new_ab()
b9.pitch_list("s s f")
b9.reach("FC5")
b9.advance(2, "44 DI")

# 6. LAA #44 Mark Trumbo (32 - X - 47)
b9.new_ab()
b9.pitch_list("s s s")
b9.out("K")


##########################################################
# 10th Inning
##########################################################
# Top 10th
# Pitching: LAA #49 Ernesto Frieri
t10 = game.new_inning()

# Defensive change (LAA): #10 Brad Hawpe replaces #19 Collin Cowgill (PR), playing 1B, batting 3rd
t10.defensive_substitution(3, 10, "3")

# Defensive switch (LAA): #6 Alberto Callaspo moves to 3B
t10.defensive_switch(6, "5")

# 4. BOS #34 David Ortiz (X - X - X)
t10.new_ab()
t10.pitch_list("c s t")
t10.out("KT")

# 5. BOS #12 Mike Napoli (X - X - X)
t10.new_ab()
t10.pitch_list("s c f s")
t10.out("K")

# 6. BOS #29 Daniel Nava (X - X - X)
t10.new_ab()
t10.pitch_list("s c b s")
t10.out("K")


# Bot 10th
# Pitching: BOS #32 Craig Breslow
b10 = game.new_inning()

# Pitching change (BOS): #32 Craig Breslow replaces #19 Koji Uehara
b10.pitching_substitution(32)

# 7. LAA #2  Erick Aybar (X - X - X)
b10.new_ab()
b10.pitch_list("b")
b10.hit(1)
b10.thrown_out(2, "6 POCS", 2, 32)

# 8. LAA #17 Chris Iannetta (X - X - 2)
b10.new_ab()
b10.pitch_list("l c c")
b10.out("!K")

# 9. LAA #6  Alberto Callaspo (X - X - 2)
b10.new_ab()
b10.pitch_list("c 1 1 b f b f")
b10.hit(1)

# 1. LAA #39 JB Shuck (X - X - 6)
b10.new_ab()
b10.out("F7")


##########################################################
# 11th Inning
##########################################################
# Top 11th
# Pitching: LAA #65 Dane De La Rosa
t11 = game.new_inning()

# Pitching change (LAA): #65 Dane De La Rosa replaces #49 Ernesto Frieri
t11.pitching_substitution(65)

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
t11.new_ab()
t11.pitch_list("c b s")
t11.out("G5-3")

# 8. BOS #23 Brandon Snyder (X - X - X)
t11.new_ab()
t11.pitch_list("b")
t11.out("G5-3")

# 9. BOS #10 Jose Iglesias (X - X - X)
t11.new_ab()
t11.out("P3")


# Bot 11th
# Pitching: BOS #32 Craig Breslow
b11 = game.new_inning()

# 2. LAA #27 Mike Trout (X - X - X)
b11.new_ab()
b11.pitch_list("c b s f c")
b11.out("!K")

# 3. LAA #10 Brad Hawpe (X - X - X)
b11.new_ab()
b11.pitch_list("f s b")
b11.hit(1)
b11.advance(4, "32 HR")

# 4. LAA #32 Josh Hamilton (X - X - 10)
b11.new_ab()
b11.hit(4, rbis=2)

# Winning team: LAA
# WP: LAA #65 Dane De La Rosa
game.winning_pitcher(65)

# Loser team: BOS
# LP: BOS #32 Craig Breslow
game.losing_pitcher(32, is_away_team=True)

# print(game)
game.generate_scorecard()
