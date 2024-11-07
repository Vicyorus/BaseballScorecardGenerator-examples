import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ LAA, 2013-07-05
# https://www.baseball-reference.com/boxes/ANA/ANA201307050.shtml
# https://www.mlb.com/gameday/red-sox-vs-angels/2013/07/05/348027/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-07-05 22:08-01:22 +1",
        "at": "Angel Stadium of Anaheim, Anaheim, CA",
        "att": "37,092",
        "temp": "72F, Clear",
        "wind": "8mph, Out To CF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 22,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                12: "Mike Napoli",
                5: "Jonny Gomes",
                29: "Daniel Nava",
                23: "Brandon Snyder",
                39: "Jarrod Saltalamacchia",
                10: "Jose Iglesias",
                # Starting pitcher
                22: "Felix Doubront",
                # Bench
                37: "Mike Carp",
                76: "Jonathan Diaz",
                34: "David Ortiz",
                20: "Ryan Lavarnway",
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
                46: "Ryan Dempster",
            },
            "lefties": [22, 30, 32, 31],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [12, "0"],
                [5, "7"],
                [29, "3"],
                [23, "5"],
                [39, "2"],
                [10, "6"],
            ],
            "bench": [
                [37, "1B"],
                [76, "SS"],
                [34, "DH"],
                [20, "C"],
            ],
            "bullpen": [63, 65, 40, 41, 30, 32, 31, 36, 64, 19, 46],
        },
        "home": {
            "team": "Los Angeles Angels",
            "starter": 33,
            "roster": {
                # Lineup
                39: "JB Shuck",
                27: "Mike Trout",
                5: "Albert Pujols",
                44: "Mark Trumbo",
                47: "Howie Kendrick",
                32: "Josh Hamilton",
                6: "Alberto Callaspo",
                17: "Chris Iannetta",
                2: "Erick Aybar",
                # Starting pitcher
                33: "C.J. Wilson",
                # Bench
                16: "Hank Conger",
                20: "Brendan Harris",
                19: "Collin Cowgill",
                10: "Brad Hawpe",
                # Bullpen
                55: "Joe Blanton",
                49: "Ernesto Frieri",
                65: "Dane De La Rosa",
                40: "Kevin Jepsen",
                58: "Michael Kohn",
                37: "Scott Downs",
                57: "Jerome Williams",
                51: "Michael Roth",
                36: "Jered Weaver",
                31: "Billy Buckner",
            },
            "lefties": [33, 37, 51],
            "lineup": [
                [39, "7"],
                [27, "8"],
                [5, "0"],
                [44, "3"],
                [47, "4"],
                [32, "9"],
                [6, "5"],
                [17, "2"],
                [2, "6"],
            ],
            "bench": [
                [16, "C"],
                [20, "SS"],
                [19, "LF"],
                [10, "RF"],
            ],
            "bullpen": [55, 49, 65, 40, 58, 37, 57, 51, 36, 31],
        },
        "umpires": {
            "HP": "Laz Diaz",
            "1B": "Tim Timmons",
            "2B": "Mike Winters",
            "3B": "Mark Wegner",
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
# Pitching: LAA #33 C.J. Wilson
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.pitch_list("c")
t1.out("G1-3")

# 2. BOS #18 Shane Victorino (X - X - X)
t1.new_ab()
t1.pitch_list("b b c")
t1.out("(F)P3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t1.new_ab()
t1.pitch_list("c b")
t1.out("G4-3")


# Bot 1st
# Pitching: BOS #22 Felix Doubront
b1 = game.new_inning()

# 1. LAA #39 JB Shuck (X - X - X)
b1.new_ab()
b1.pitch_list("c")
b1.out("F8")

# 2. LAA #27 Mike Trout (X - X - X)
b1.new_ab()
b1.pitch_list("b b")
b1.hit(2)

# 3. LAA #5  Albert Pujols (X - 27 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("c")
b1.out("G5-3")

# 4. LAA #44 Mark Trumbo (X - 27 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("b b s")
b1.out("F9")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: LAA #33 C.J. Wilson
t2 = game.new_inning()

# 4. BOS #12 Mike Napoli (X - X - X)
t2.new_ab()
t2.out("F9")

# 5. BOS #5  Jonny Gomes (X - X - X)
t2.new_ab()
t2.pitch_list("c b b c b b")
t2.reach("BB")
t2.advance(2, "29 1B")
t2.advance(4, "39 1B")

# 6. BOS #29 Daniel Nava (X - X - 5)
t2.new_ab()
t2.pitch_list("b b c 1 b 1 f")
t2.hit(1)
t2.error(7)
t2.advance(2, "39 1B")
t2.advance("U", "39 E7")

# 7. BOS #23 Brandon Snyder (X - 5 - 29)
t2.new_ab(is_risp=True)
t2.pitch_list("b b")
t2.out("F8")

# 8. BOS #39 Jarrod Saltalamacchia (X - 5 - 29)
t2.new_ab(is_risp=True)
t2.pitch_list("c b b")
t2.hit(1, rbis=1)
t2.advance(2, "E7")

# 9. BOS #10 Jose Iglesias (X - 39 - X)
t2.new_ab(is_risp=True)
t2.pitch_list("b b c b f d")
t2.reach("BB")

# 1. BOS #2  Jacoby Ellsbury (X - 39 - 10)
t2.new_ab(is_risp=True)
t2.pitch_list("c")
t2.out("G4-3")


# Bot 2nd
# Pitching: BOS #22 Felix Doubront
b2 = game.new_inning()

# 5. LAA #47 Howie Kendrick (X - X - X)
b2.new_ab()
b2.pitch_list("b c c f b s")
b2.out("K")

# 6. LAA #32 Josh Hamilton (X - X - X)
b2.new_ab()
b2.pitch_list("b s c")
b2.hit(1)
b2.advance(2, "17 BB")

# 7. LAA #6  Alberto Callaspo (X - X - 32)
b2.new_ab()
b2.pitch_list("b")
b2.out("F8")

# 8. LAA #17 Chris Iannetta (X - X - 32)
b2.new_ab()
b2.pitch_list("f b b b f b")
b2.reach("BB")
b2.thrown_out(2, "2 FC6-4", 3, 22)

# 9. LAA #2  Erick Aybar (X - 32 - 17)
b2.new_ab(is_risp=True)
b2.pitch_list("b")
b2.reach("FC6-4")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: LAA #33 C.J. Wilson
t3 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
t3.new_ab()
t3.pitch_list("c b b")
t3.out("F9")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t3.new_ab()
t3.pitch_list("c b b")
t3.hit(1)
t3.thrown_out(2, "12 DP6-4-3", 2, 33)

# 4. BOS #12 Mike Napoli (X - X - 15)
t3.new_ab()
t3.pitch_list("f c")
t3.out("DP6-4-3")


# Bot 3rd
# Pitching: BOS #22 Felix Doubront
b3 = game.new_inning()

# 1. LAA #39 JB Shuck (X - X - X)
b3.new_ab()
b3.pitch_list("b b f b c")
b3.hit(3)
b3.advance(4, "5 DP5-4-3")

# 2. LAA #27 Mike Trout (39 - X - X)
b3.new_ab(is_risp=True)
b3.pitch_list("b b f f b f b")
b3.reach("BB")
b3.thrown_out(2, "5 DP5-4-3", 1, 22)

# 3. LAA #5  Albert Pujols (39 - X - 27)
b3.new_ab(is_risp=True)
b3.pitch_list("d 1 f f b f d")
b3.out("DP5-4-3")

# 4. LAA #44 Mark Trumbo (X - X - X)
b3.new_ab()
b3.pitch_list("c b f f")
b3.out("G6-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: LAA #33 C.J. Wilson
t4 = game.new_inning()

# 5. BOS #5  Jonny Gomes (X - X - X)
t4.new_ab()
t4.pitch_list("b c")
t4.hit(1)
t4.advance(2, "23 1B")

# 6. BOS #29 Daniel Nava (X - X - 5)
t4.new_ab()
t4.pitch_list("b c b 1 f b")
t4.out("L9")

# 7. BOS #23 Brandon Snyder (X - X - 5)
t4.new_ab()
t4.pitch_list("s")
t4.hit(1)

# 8. BOS #39 Jarrod Saltalamacchia (X - 5 - 23)
t4.new_ab(is_risp=True)
t4.out("F9")

# 9. BOS #10 Jose Iglesias (X - 5 - 23)
t4.new_ab(is_risp=True)
t4.pitch_list("2 c b b c f c")
t4.out("!K")


# Bot 4th
# Pitching: BOS #22 Felix Doubront
b4 = game.new_inning()

# 5. LAA #47 Howie Kendrick (X - X - X)
b4.new_ab()
b4.hit(4)

# 6. LAA #32 Josh Hamilton (X - X - X)
b4.new_ab()
b4.pitch_list("f")
b4.out("G4-1")

# 7. LAA #6  Alberto Callaspo (X - X - X)
b4.new_ab()
b4.pitch_list("b")
b4.out("F8")

# 8. LAA #17 Chris Iannetta (X - X - X)
b4.new_ab()
b4.out("P3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: LAA #33 C.J. Wilson
t5 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t5.new_ab()
t5.pitch_list("b")
t5.hit(1)
t5.advance(2, "15 SB")

# 2. BOS #18 Shane Victorino (X - X - 2)
t5.new_ab()
t5.pitch_list("b 1 c d c s")
t5.out("K")

# 3. BOS #15 Dustin Pedroia (X - X - 2)
t5.new_ab(is_risp=True)
t5.pitch_list("1 b b")
t5.out("G6-3")

# 4. BOS #12 Mike Napoli (X - 2 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("c b c s")
t5.out("K")


# Bot 5th
# Pitching: BOS #22 Felix Doubront
b5 = game.new_inning()

# 9. LAA #2  Erick Aybar (X - X - X)
b5.new_ab()
b5.pitch_list("s f b b s")
b5.out("K")

# 1. LAA #39 JB Shuck (X - X - X)
b5.new_ab()
b5.pitch_list("c b c b s")
b5.out("K")

# 2. LAA #27 Mike Trout (X - X - X)
b5.new_ab()
b5.out("L9")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: LAA #33 C.J. Wilson
t6 = game.new_inning()

# 5. BOS #5  Jonny Gomes (X - X - X)
t6.new_ab()
t6.out("F7")

# 6. BOS #29 Daniel Nava (X - X - X)
t6.new_ab()
t6.pitch_list("b c s b c")
t6.out("!K")

# 7. BOS #23 Brandon Snyder (X - X - X)
t6.new_ab()
t6.pitch_list("b b c c f")
t6.hit(1)
t6.advance(2, "39 1B")
t6.advance(3, "10 1B")

# 8. BOS #39 Jarrod Saltalamacchia (X - X - 23)
t6.new_ab()
t6.pitch_list("c")
t6.hit(1)
t6.advance(2, "10 1B")

# 9. BOS #10 Jose Iglesias (X - 23 - 39)
t6.new_ab(is_risp=True)
t6.pitch_list("d c b")
t6.hit(1)

# 1. BOS #2  Jacoby Ellsbury (23 - 39 - 10)
t6.new_ab(is_risp=True)
t6.pitch_list("b c c")
t6.out("L1")


# Bot 6th
# Pitching: BOS #22 Felix Doubront
b6 = game.new_inning()

# 3. LAA #5  Albert Pujols (X - X - X)
b6.new_ab()
b6.pitch_list("c b b")
b6.out("F7")

# 4. LAA #44 Mark Trumbo (X - X - X)
b6.new_ab()
b6.out("G5-3")

# 5. LAA #47 Howie Kendrick (X - X - X)
b6.new_ab()
b6.pitch_list("b f s f f f s")
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: LAA #33 C.J. Wilson
t7 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
t7.new_ab()
t7.pitch_list("c f b")
t7.hit(1)
t7.advance("U", "5 E9")

# 3. BOS #15 Dustin Pedroia (X - X - 18)
t7.new_ab()
t7.pitch_list("1 c b 1 f f")
t7.out("F8")

# 4. BOS #12 Mike Napoli (X - X - 18)
t7.new_ab()
t7.pitch_list("f b 1 b c s")
t7.out("K")

# 5. BOS #5  Jonny Gomes (X - X - 18)
t7.new_ab()
t7.pitch_list("1 c b b b")
t7.error(9)
t7.reach("E9")
t7.thrown_out(1, "29 PO", 3, 65)

# Pitching change (LAA): #65 Dane De La Rosa replaces #33 C.J. Wilson
t7.pitching_substitution(65)

# 6. BOS #29 Daniel Nava (X - X - 5)
t7.new_ab()
t7.pitch_list("b 1 c b f 1")
t7.no_ab("PO")


# Bot 7th
# Pitching: BOS #22 Felix Doubront
b7 = game.new_inning()

# 6. LAA #32 Josh Hamilton (X - X - X)
b7.new_ab()
b7.out("F7")

# 7. LAA #6  Alberto Callaspo (X - X - X)
b7.new_ab()
b7.pitch_list("b c c")
b7.hit(2)

# 8. LAA #17 Chris Iannetta (X - 6 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("b f b b f f c")
b7.out("!K")

# Pitching change (BOS): #32 Craig Breslow replaces #22 Felix Doubront
b7.pitching_substitution(32)

# 9. LAA #2  Erick Aybar (X - 6 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("c")
b7.out("F8")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: LAA #65 Dane De La Rosa
t8 = game.new_inning()

# 6. BOS #29 Daniel Nava (X - X - X)
t8.new_ab()
t8.pitch_list("b f f b b")
t8.hit(2)
t8.advance(4, "34 HR")

# Offensive change (BOS): Pinch-hitter #34 David Ortiz replaces #23 Brandon Snyder, batting 7th
t8.offensive_substitution(7, 34, "PH")

# 7. BOS #34 David Ortiz (X - 29 - X)
t8.new_ab(is_risp=True)
t8.pitch_list("c")
t8.hit(4, rbis=2)

# 8. BOS #39 Jarrod Saltalamacchia (X - X - X)
t8.new_ab()
t8.pitch_list("c b")
t8.out("G4-3")

# 9. BOS #10 Jose Iglesias (X - X - X)
t8.new_ab()
t8.pitch_list("c s f f c")
t8.out("!K")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t8.new_ab()
t8.pitch_list("c f b f s")
t8.out("K")


# Bot 8th
# Pitching: BOS #32 Craig Breslow
b8 = game.new_inning()

# Defensive change (BOS): #76 Jonathan Diaz replaces #34 David Ortiz (PH), playing 3B, batting 7th
b8.defensive_substitution(7, 76, "5")

# 1. LAA #39 JB Shuck (X - X - X)
b8.new_ab()
b8.pitch_list("c s b")
b8.out("G4-3")

# Pitching change (BOS): #36 Junichi Tazawa replaces #32 Craig Breslow
b8.pitching_substitution(36)

# 2. LAA #27 Mike Trout (X - X - X)
b8.new_ab()
b8.pitch_list("c c")
b8.out("F9")

# 3. LAA #5  Albert Pujols (X - X - X)
b8.new_ab()
b8.hit(1)

# 4. LAA #44 Mark Trumbo (X - X - 5)
b8.new_ab()
b8.pitch_list("d b c b s f f f s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: LAA #58 Michael Kohn
t9 = game.new_inning()

# Pitching change (LAA): #58 Michael Kohn replaces #65 Dane De La Rosa
t9.pitching_substitution(58)

# 2. BOS #18 Shane Victorino (X - X - X)
t9.new_ab()
t9.out("P6")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t9.new_ab()
t9.pitch_list("b c c s")
t9.out("K")

# 4. BOS #12 Mike Napoli (X - X - X)
t9.new_ab()
t9.pitch_list("b b")
t9.hit(4)

# 5. BOS #5  Jonny Gomes (X - X - X)
t9.new_ab()
t9.pitch_list("f b b")
t9.out("(F)P3")


# Bot 9th
# Pitching: BOS #19 Koji Uehara
b9 = game.new_inning()

# Pitching change (BOS): #19 Koji Uehara replaces #36 Junichi Tazawa
b9.pitching_substitution(19)

# 5. LAA #47 Howie Kendrick (X - X - X)
b9.new_ab()
b9.pitch_list("b")
b9.out("G4-3")

# 6. LAA #32 Josh Hamilton (X - X - X)
b9.new_ab()
b9.pitch_list("c s s")
b9.out("K")

# 7. LAA #6  Alberto Callaspo (X - X - X)
b9.new_ab()
b9.pitch_list("c")
b9.out("G3")

# Winning team: BOS
# WP: BOS #22 Felix Doubront
game.winning_pitcher(22, is_away_team=True)

# Loser team: LAA
# LP: LAA #33 C.J. Wilson
game.losing_pitcher(33)

# print(game)
game.generate_scorecard()
