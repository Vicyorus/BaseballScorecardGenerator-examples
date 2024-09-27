import os
from baseball_scorecard.baseball_scorecard import Scorecard

# LAA @ BOS, 2013-06-08
# https://www.baseball-reference.com/boxes/BOS/BOS201306081.shtml
# https://www.mlb.com/gameday/angels-vs-red-sox/2013/06/08/347649/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-06-08 13:06-17:06",
        "at": "Fenway Park, Boston, MA",
        "att": "34,499",
        "temp": "68F, Cloudy",
        "wind": "13mph, Out To RF",
        "away": {
            "team": "Los Angeles Angels",
            "starter": 48,
            "roster": {
                # Lineup
                27: "Mike Trout",
                32: "Josh Hamilton",
                5: "Albert Pujols",
                44: "Mark Trumbo",
                47: "Howie Kendrick",
                6: "Alberto Callaspo",
                17: "Chris Iannetta",
                2: "Erick Aybar",
                39: "JB Shuck",
                # Starting pitcher
                48: "Tommy Hanson",
                # Bench
                16: "Hank Conger",
                20: "Brendan Harris",
                10: "Brad Hawpe",
                8: "Chris Nelson",
                # Bullpen
                55: "Joe Blanton",
                49: "Ernesto Frieri",
                59: "Robert Coello",
                33: "C.J. Wilson",
                40: "Kevin Jepsen",
                58: "Michael Kohn",
                37: "Scott Downs",
                57: "Jerome Williams",
                43: "Garrett Richards",
                36: "Jered Weaver",
                60: "Jason Vargas",
            },
            "lefties": [33, 37, 60],
            "lineup": [
                [27, "8"],
                [32, "9"],
                [5, "0"],
                [44, "3"],
                [47, "4"],
                [6, "5"],
                [17, "2"],
                [2, "6"],
                [39, "7"],
            ],
            "bench": [
                [16, "C"],
                [20, "SS"],
                [10, "RF"],
                [8, "3B"],
            ],
            "bullpen": [55, 49, 59, 33, 40, 58, 37, 57, 43, 36, 60],
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
                39: "Jarrod Saltalamacchia",
                37: "Mike Carp",
                7: "Stephen Drew",
                10: "Jose Iglesias",
                # Starting pitcher
                22: "Felix Doubront",
                # Bench
                18: "Shane Victorino",
                5: "Jonny Gomes",
                3: "David Ross",
                23: "Pedro Ciriaco",
                # Bullpen
                40: "Andrew Bailey",
                41: "John Lackey",
                56: "Franklin Morales",
                30: "Andrew Miller",
                32: "Craig Breslow",
                31: "Jon Lester",
                59: "Clayton Mortensen",
                36: "Junichi Tazawa",
                11: "Clay Buchholz",
                19: "Koji Uehara",
                46: "Ryan Dempster",
            },
            "lefties": [22, 56, 30, 32, 31],
            "lineup": [
                [2, "8"],
                [29, "9"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [39, "2"],
                [37, "7"],
                [7, "6"],
                [10, "5"],
            ],
            "bench": [
                [18, "CF"],
                [5, "LF"],
                [3, "C"],
                [23, "3B"],
            ],
            "bullpen": [40, 41, 56, 30, 32, 31, 59, 36, 11, 19, 46],
        },
        "umpires": {
            "HP": "Tim McClelland",
            "1B": "Clint Fagan",
            "2B": "Marty Foster",
            "3B": "Wally Bell",
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

# 1. LAA #27 Mike Trout (X - X - X)
t1.new_ab()
t1.pitch_list("c s f f b b")
t1.out("G6-3")

# 2. LAA #32 Josh Hamilton (X - X - X)
t1.new_ab()
t1.pitch_list("b")
t1.hit(2)

# 3. LAA #5  Albert Pujols (X - 32 - X)
t1.new_ab()
t1.pitch_list("f f")
t1.out("L3")

# 4. LAA #44 Mark Trumbo (X - 32 - X)
t1.new_ab()
t1.pitch_list("d b")
t1.out("G6-3")


# Bot 1st
# Pitching: LAA #48 Tommy Hanson
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("b")
b1.hit(1)
b1.advance(2, "29 SB")
b1.thrown_out(3, "29 FC1-5-1", 1, 48)

# 2. BOS #29 Daniel Nava (X - X - 2)
b1.new_ab()
b1.pitch_list("b 1 1 c")
b1.reach("FC1-5-1")
b1.advance(3, "15 2B")

# 3. BOS #15 Dustin Pedroia (X - X - 29)
b1.new_ab()
b1.pitch_list("b c 1")
b1.hit(2)

# 4. BOS #34 David Ortiz (29 - 15 - X)
b1.new_ab()
b1.pitch_list("c s s")
b1.out("K")

# 5. BOS #12 Mike Napoli (29 - 15 - X)
b1.new_ab()
b1.pitch_list("c c d b")
b1.out("G5-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #22 Felix Doubront
t2 = game.new_inning()

# 5. LAA #47 Howie Kendrick (X - X - X)
t2.new_ab()
t2.pitch_list("b f")
t2.hit(1)
t2.advance(2, "6 G3")
t2.advance(4, "2 1B")

# 6. LAA #6  Alberto Callaspo (X - X - 47)
t2.new_ab()
t2.pitch_list("1 b c")
t2.out("G3")

# 7. LAA #17 Chris Iannetta (X - 47 - X)
t2.new_ab()
t2.pitch_list("s b 2 b c b")
t2.out("G5-3")

# 8. LAA #2  Erick Aybar (X - 47 - X)
t2.new_ab()
t2.pitch_list("d c f")
t2.hit(1, rbis=1)
t2.advance(2, "T")

# 9. LAA #39 JB Shuck (X - 2 - X)
t2.new_ab()
t2.pitch_list("f f c")
t2.out("!K")


# Bot 2nd
# Pitching: LAA #48 Tommy Hanson
b2 = game.new_inning()

# 6. BOS #39 Jarrod Saltalamacchia (X - X - X)
b2.new_ab()
b2.pitch_list("b b b b")
b2.reach("BB")
b2.advance(2, "7 BB")
b2.advance(3, "10 F9")

# 7. BOS #37 Mike Carp (X - X - 39)
b2.new_ab()
b2.pitch_list("b c b b")
b2.out("F8")

# 8. BOS #7  Stephen Drew (X - X - 39)
b2.new_ab()
b2.pitch_list("b b b c b")
b2.reach("BB")

# 9. BOS #10 Jose Iglesias (X - 39 - 7)
b2.new_ab()
b2.pitch_list("c c 1 d f b b f")
b2.out("F9")

# 1. BOS #2  Jacoby Ellsbury (39 - X - 7)
b2.new_ab()
b2.pitch_list("b c")
b2.out("G4-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #22 Felix Doubront
t3 = game.new_inning()

# 1. LAA #27 Mike Trout (X - X - X)
t3.new_ab()
t3.pitch_list("c b")
t3.hit(2)
t3.advance(3, "5 SB")
t3.advance(4, "5 SF8")

# 2. LAA #32 Josh Hamilton (X - 27 - X)
t3.new_ab()
t3.pitch_list("s b d f b f f b")
t3.reach("BB")
t3.advance(2, "5 SB")
t3.advance(3, "5 SF8")
t3.advance(4, "44 G6-4-3")

# 3. LAA #5  Albert Pujols (X - 27 - 32)
t3.new_ab()
t3.pitch_list("c f")
t3.out("SF8", rbis=1)

# 4. LAA #44 Mark Trumbo (32 - X - X)
t3.new_ab()
t3.pitch_list("f")
t3.out("G6-4-3", rbis=1)

# 5. LAA #47 Howie Kendrick (X - X - X)
t3.new_ab()
t3.pitch_list("b b c b")
t3.out("L8")


# Bot 3rd
# Pitching: LAA #48 Tommy Hanson
b3 = game.new_inning()

# 2. BOS #29 Daniel Nava (X - X - X)
b3.new_ab()
b3.pitch_list("c c f b")
b3.hit(1)
b3.advance(2, "15 1B")

# 3. BOS #15 Dustin Pedroia (X - X - 29)
b3.new_ab()
b3.pitch_list("c b 1")
b3.hit(1)

# 4. BOS #34 David Ortiz (X - 29 - 15)
b3.new_ab()
b3.pitch_list("s b b c s")
b3.out("K")

# 5. BOS #12 Mike Napoli (X - 29 - 15)
b3.new_ab()
b3.pitch_list("c b c d c")
b3.out("!K")

# 6. BOS #39 Jarrod Saltalamacchia (X - 29 - 15)
b3.new_ab()
b3.out("P5")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #22 Felix Doubront
t4 = game.new_inning()

# 6. LAA #6  Alberto Callaspo (X - X - X)
t4.new_ab()
t4.pitch_list("b")
t4.out("F9")

# 7. LAA #17 Chris Iannetta (X - X - X)
t4.new_ab()
t4.pitch_list("c s b s")
t4.out("K")

# 8. LAA #2  Erick Aybar (X - X - X)
t4.new_ab()
t4.pitch_list("b c l")
t4.out("L5")


# Bot 4th
# Pitching: LAA #48 Tommy Hanson
b4 = game.new_inning()

# 7. BOS #37 Mike Carp (X - X - X)
b4.new_ab()
b4.pitch_list("c c b")
b4.hit(4)

# 8. BOS #7  Stephen Drew (X - X - X)
b4.new_ab()
b4.pitch_list("b b c f b")
b4.out("P6")

# 9. BOS #10 Jose Iglesias (X - X - X)
b4.new_ab()
b4.pitch_list("b c l f b")
b4.out("P6")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b4.new_ab()
b4.pitch_list("b f b b b")
b4.reach("BB")
b4.advance(2, "29 SB")
b4.advance(4, "29 E9")

# 2. BOS #29 Daniel Nava (X - X - 2)
b4.new_ab()
b4.pitch_list("1 1 c p d")
b4.hit(1, rbis=1)
b4.error(9)
b4.advance(2, "E9")
b4.advance(3, "15 WP")

# 3. BOS #15 Dustin Pedroia (X - 29 - X)
b4.new_ab()
b4.pitch_list("b b c d b")
b4.wp()
b4.reach("BB")

# 4. BOS #34 David Ortiz (29 - X - 15)
b4.new_ab()
b4.out("G4-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #22 Felix Doubront
t5 = game.new_inning()

# 9. LAA #39 JB Shuck (X - X - X)
t5.new_ab()
t5.pitch_list("b b b c b")
t5.reach("BB")
t5.advance(3, "5 1B")

# 1. LAA #27 Mike Trout (X - X - 39)
t5.new_ab()
t5.pitch_list("s b f b f s")
t5.out("K")

# 2. LAA #32 Josh Hamilton (X - X - 39)
t5.new_ab()
t5.pitch_list("c d s b f d s")
t5.out("K")

# 3. LAA #5  Albert Pujols (X - X - 39)
t5.new_ab()
t5.hit(1)

# 4. LAA #44 Mark Trumbo (39 - X - 5)
t5.new_ab()
t5.pitch_list("f d")
t5.out("G4-3")


# Bot 5th
# Pitching: LAA #48 Tommy Hanson
b5 = game.new_inning()

# 5. BOS #12 Mike Napoli (X - X - X)
b5.new_ab()
b5.pitch_list("b b c c f b")
b5.out("F8")

# 6. BOS #39 Jarrod Saltalamacchia (X - X - X)
b5.new_ab()
b5.pitch_list("c b s f b b")
b5.out("G3")

# 7. BOS #37 Mike Carp (X - X - X)
b5.new_ab()
b5.pitch_list("c b b")
b5.hit(1)

# 8. BOS #7  Stephen Drew (X - X - 37)
b5.new_ab()
b5.pitch_list("c 1 f d f s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #22 Felix Doubront
t6 = game.new_inning()

# 5. LAA #47 Howie Kendrick (X - X - X)
t6.new_ab()
t6.pitch_list("b b s")
t6.out("G4-3")

# 6. LAA #6  Alberto Callaspo (X - X - X)
t6.new_ab()
t6.pitch_list("b")
t6.hit(2)
t6.advance(3, "17 F9")

# 7. LAA #17 Chris Iannetta (X - 6 - X)
t6.new_ab()
t6.pitch_list("s")
t6.out("F9")

# 8. LAA #2  Erick Aybar (6 - X - X)
t6.new_ab()
t6.pitch_list("c")
t6.out("G3")


# Bot 6th
# Pitching: LAA #58 Michael Kohn
b6 = game.new_inning()

# Pitching change (LAA): #58 Michael Kohn replaces #48 Tommy Hanson
b6.pitching_substitution(58)

# 9. BOS #10 Jose Iglesias (X - X - X)
b6.new_ab()
b6.pitch_list("b b b b")
b6.reach("BB")
b6.thrown_out(2, "2 FC3-6", 1, 58)

# 1. BOS #2  Jacoby Ellsbury (X - X - 10)
b6.new_ab()
b6.pitch_list("b c")
b6.reach("FC3-6")
b6.advance(2, "29 1B")

# 2. BOS #29 Daniel Nava (X - X - 2)
b6.new_ab()
b6.hit(1)
b6.thrown_out(2, "15 DP6-4-3", 2, 58)

# 3. BOS #15 Dustin Pedroia (X - 2 - 29)
b6.new_ab()
b6.pitch_list("c b")
b6.out("DP6-4-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #56 Franklin Morales
t7 = game.new_inning()

# Pitching change (BOS): #56 Franklin Morales replaces #22 Felix Doubront
t7.pitching_substitution(56)

# 9. LAA #39 JB Shuck (X - X - X)
t7.new_ab()
t7.out("G3")

# 1. LAA #27 Mike Trout (X - X - X)
t7.new_ab()
t7.pitch_list("b b f")
t7.hit(2)
t7.advance(4, "44 2B")

# 2. LAA #32 Josh Hamilton (X - 27 - X)
t7.new_ab()
t7.pitch_list("b b")
t7.out("F8")

# 3. LAA #5  Albert Pujols (X - 27 - X)
t7.new_ab()
t7.pitch_list("i i i i")
t7.reach("IBB")
t7.advance(3, "44 2B")
t7.advance(4, "6 BB")

# 4. LAA #44 Mark Trumbo (X - 27 - 5)
t7.new_ab()
t7.pitch_list("c b f")
t7.hit(2, rbis=1)
t7.advance(3, "6 BB")
t7.advance(4, "17 BB")

# 5. LAA #47 Howie Kendrick (5 - 44 - X)
t7.new_ab()
t7.pitch_list("b s b f b d")
t7.reach("BB")
t7.advance(2, "6 BB")
t7.advance(3, "17 BB")
t7.advance(4, "2 1B")

# 6. LAA #6  Alberto Callaspo (5 - 44 - 47)
t7.new_ab()
t7.pitch_list("b d 1 b b")
t7.reach("BB", rbis=1)
t7.advance(2, "17 BB")
t7.advance(3, "2 1B")

# 7. LAA #17 Chris Iannetta (44 - 47 - 6)
t7.new_ab()
t7.pitch_list("d b b b")
t7.reach("BB", rbis=1)
t7.advance(2, "2 1B")

# Pitching change (BOS): #59 Clayton Mortensen replaces #56 Franklin Morales
t7.pitching_substitution(59)

# 8. LAA #2  Erick Aybar (47 - 6 - 17)
t7.new_ab()
t7.pitch_list("b b c f b")
t7.hit(1, rbis=1)

# 9. LAA #39 JB Shuck (6 - 17 - 2)
t7.new_ab()
t7.pitch_list("c")
t7.out("F8")


# Bot 7th
# Pitching: LAA #37 Scott Downs
b7 = game.new_inning()

# Pitching change (LAA): #37 Scott Downs replaces #58 Michael Kohn
b7.pitching_substitution(37)

# 4. BOS #34 David Ortiz (X - X - X)
b7.new_ab()
b7.pitch_list("b f b")
b7.out("F7")

# 5. BOS #12 Mike Napoli (X - X - X)
b7.new_ab()
b7.pitch_list("b c b b")
b7.out("L8")

# 6. BOS #39 Jarrod Saltalamacchia (X - X - X)
b7.new_ab()
b7.pitch_list("b b c c s")
b7.out("K2-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #59 Clayton Mortensen
t8 = game.new_inning()

# 1. LAA #27 Mike Trout (X - X - X)
t8.new_ab()
t8.pitch_list("c c")
t8.hit(1)
t8.advance(2, "32 G4-1")
t8.advance(3, "5 G6-3")

# 2. LAA #32 Josh Hamilton (X - X - 27)
t8.new_ab()
t8.out("G4-1")

# 3. LAA #5  Albert Pujols (X - 27 - X)
t8.new_ab()
t8.pitch_list("b b s")
t8.out("G6-3")

# 4. LAA #44 Mark Trumbo (27 - X - X)
t8.new_ab()
t8.pitch_list("c d c f d")
t8.out("F7")


# Bot 8th
# Pitching: LAA #43 Garrett Richards
b8 = game.new_inning()

# Pitching change (LAA): #43 Garrett Richards replaces #37 Scott Downs
b8.pitching_substitution(43)

# 7. BOS #37 Mike Carp (X - X - X)
b8.new_ab()
b8.pitch_list("b c b")
b8.out("G1-3")

# 8. BOS #7  Stephen Drew (X - X - X)
b8.new_ab()
b8.pitch_list("c s b b b f c")
b8.out("!K")

# 9. BOS #10 Jose Iglesias (X - X - X)
b8.new_ab()
b8.pitch_list("b c")
b8.hit(1)
b8.advance(2, "2 CI")

# 1. BOS #2  Jacoby Ellsbury (X - X - 10)
b8.new_ab()
b8.pitch_list("b f n")
b8.error(2)
b8.reach("CI")

# 2. BOS #29 Daniel Nava (X - 10 - 2)
b8.new_ab()
b8.pitch_list("b b f s")
b8.out("G4-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #59 Clayton Mortensen
t9 = game.new_inning()

# 5. LAA #47 Howie Kendrick (X - X - X)
t9.new_ab()
t9.hit(1)
t9.advance(2, "6 1B")
t9.advance(3, "2 BB")
t9.thrown_out(4, "39 FC3-2", 2, 30)

# 6. LAA #6  Alberto Callaspo (X - X - 47)
t9.new_ab()
t9.pitch_list("f d b 1")
t9.hit(1)
t9.advance(2, "2 BB")
t9.advance(3, "39 FC3-2")
t9.advance(4, "27 BB")

# 7. LAA #17 Chris Iannetta (X - 47 - 6)
t9.new_ab()
t9.pitch_list("s c b b f d")
t9.out("P5")

# Pitching change (BOS): #30 Andrew Miller replaces #59 Clayton Mortensen
t9.pitching_substitution(30)

# 8. LAA #2  Erick Aybar (X - 47 - 6)
t9.new_ab()
t9.pitch_list("b s b b b")
t9.reach("BB")
t9.advance(2, "39 FC3-2")
t9.advance(3, "27 BB")
t9.advance("U", "32 E3")

# 9. LAA #39 JB Shuck (47 - 6 - 2)
t9.new_ab()
t9.pitch_list("b f b f b")
t9.reach("FC3-2")
t9.advance(2, "27 BB")
t9.advance(3, "32 E3")

# 1. LAA #27 Mike Trout (6 - 2 - 39)
t9.new_ab()
t9.pitch_list("b f b b b")
t9.reach("BB", rbis=1)
t9.advance(2, "32 E3")

# 2. LAA #32 Josh Hamilton (2 - 39 - 27)
t9.new_ab()
t9.pitch_list("s s b")
t9.error(3)
t9.reach("E3")
t9.thrown_out(2, "5 FC6-4", 3, 30)

# 3. LAA #5  Albert Pujols (39 - 27 - 32)
t9.new_ab()
t9.pitch_list("b b")
t9.reach("FC6-4")


# Bot 9th
# Pitching: LAA #43 Garrett Richards
b9 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
b9.new_ab()
b9.pitch_list("c b b c")
b9.out("G1-3")

# 4. BOS #34 David Ortiz (X - X - X)
b9.new_ab()
b9.pitch_list("b")
b9.out("G3")

# 5. BOS #12 Mike Napoli (X - X - X)
b9.new_ab()
b9.pitch_list("c b")
b9.hit(1)
b9.advance(2, "39 1B")
b9.advance(4, "37 1B")

# 6. BOS #39 Jarrod Saltalamacchia (X - X - 12)
b9.new_ab()
b9.pitch_list("c")
b9.hit(1)
b9.advance(2, "37 1B")
b9.advance(4, "7 2B")

# 7. BOS #37 Mike Carp (X - 12 - 39)
b9.new_ab()
b9.pitch_list("s")
b9.hit(1, rbis=1)
b9.advance(4, "7 2B")

# 8. BOS #7  Stephen Drew (X - 39 - 37)
b9.new_ab()
b9.pitch_list("b")
b9.hit(2, rbis=2)
b9.advance(3, "10 1B")

# 9. BOS #10 Jose Iglesias (X - 7 - X)
b9.new_ab()
b9.pitch_list("c")
b9.hit(1)
b9.advance(2, "2 DI")

# Pitching change (LAA): #49 Ernesto Frieri replaces #43 Garrett Richards
b9.pitching_substitution(49)

# 1. BOS #2  Jacoby Ellsbury (7 - X - 10)
b9.new_ab()
b9.pitch_list("c b c b f f s")
b9.out("K")

# Winning team: LAA
# WP: LAA #48 Tommy Hanson
game.winning_pitcher(48, is_away_team=True)
# SV: LAA #49 Ernesto Frieri
game.save_pitcher(49, is_away_team=True)

# Loser team: BOS
# LP: BOS #22 Felix Doubront
game.losing_pitcher(22)

# print(game)
game.generate_scorecard()
