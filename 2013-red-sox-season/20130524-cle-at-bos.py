import os
from baseball_scorecard.baseball_scorecard import Scorecard

# CLE @ BOS, 2013-05-24
# https://www.baseball-reference.com/boxes/BOS/BOS201305240.shtml
# https://www.mlb.com/gameday/indians-vs-red-sox/2013/05/24/347452/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-05-24 19:52-23:31 (0:44 delay)",
        "at": "Fenway Park, Boston, MA",
        "att": "34,074",
        "temp": "56F, Rain",
        "wind": "12mph, L To R",
        "away": {
            "team": "Cleveland Indians",
            "starter": 63,
            "roster": {
                # Lineup
                24: "Michael Bourn",
                22: "Jason Kipnis",
                13: "Asdrúbal Cabrera",
                33: "Nick Swisher",
                41: "Carlos Santana",
                25: "Jason Giambi",
                12: "Mark Reynolds",
                23: "Michael Brantley",
                11: "Drew Stubbs",
                # Starting pitcher
                63: "Justin Masterson",
                # Bench
                9: "Ryan Raburn",
                10: "Yan Gomes",
                4: "Mike Aviles",
                # Bullpen
                26: "Scott Kazmir",
                32: "Matt Albers",
                54: "Chris Perez",
                37: "Cody Allen",
                51: "Scott Barnes",
                30: "Ubaldo Jiménez",
                27: "Bryan Shaw",
                34: "Zach McAllister",
                53: "Rich Hill",
                38: "Joe Smith",
                52: "Vinnie Pestano",
                28: "Corey Kluber",
            },
            "lefties": [26, 51, 53],
            "lineup": [
                [24, "8"],
                [22, "4"],
                [13, "6"],
                [33, "3"],
                [41, "2"],
                [25, "0"],
                [12, "5"],
                [23, "7"],
                [11, "9"],
            ],
            "bench": [
                [9, "LF"],
                [10, "C"],
                [4, "SS"],
            ],
            "bullpen": [26, 32, 54, 37, 51, 30, 27, 34, 53, 38, 52, 28],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 41,
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
                41: "John Lackey",
                # Bench
                5: "Jonny Gomes",
                3: "David Ross",
                23: "Pedro Ciriaco",
                # Bullpen
                63: "Alex Wilson",
                40: "Andrew Bailey",
                30: "Andrew Miller",
                32: "Craig Breslow",
                91: "Alfredo Aceves",
                31: "Jon Lester",
                59: "Clayton Mortensen",
                36: "Junichi Tazawa",
                11: "Clay Buchholz",
                19: "Koji Uehara",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [30, 32, 31, 22],
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
                [5, "LF"],
                [3, "C"],
                [23, "3B"],
            ],
            "bullpen": [63, 40, 30, 32, 91, 31, 59, 36, 11, 19, 22, 46],
        },
        "umpires": {
            "HP": "Tom Hallion",
            "1B": "Ron Kulpa",
            "2B": "Chris Guccione",
            "3B": "Phil Cuzzi",
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
# Pitching: BOS #41 John Lackey
t1 = game.new_inning()

# 1. CLE #24 Michael Bourn (X - X - X)
t1.new_ab()
t1.pitch_list("c s b c")
t1.out("!K")

# 2. CLE #22 Jason Kipnis (X - X - X)
t1.new_ab()
t1.pitch_list("b c b c")
t1.out("G5-3")

# 3. CLE #13 Asdrúbal Cabrera (X - X - X)
t1.new_ab()
t1.pitch_list("b f f s")
t1.out("K")


# Bot 1st
# Pitching: CLE #63 Justin Masterson
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("c b b s b f s")
b1.out("K")

# 2. BOS #29 Daniel Nava (X - X - X)
b1.new_ab()
b1.pitch_list("c c b f b")
b1.out("G3-1")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b1.new_ab()
b1.pitch_list("b b b c c f")
b1.out("G3-1")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #41 John Lackey
t2 = game.new_inning()

# 4. CLE #33 Nick Swisher (X - X - X)
t2.new_ab()
t2.pitch_list("c")
t2.out("G4-3")

# 5. CLE #41 Carlos Santana (X - X - X)
t2.new_ab()
t2.pitch_list("c b b f b f b")
t2.reach("BB")
t2.thrown_out(2, "25 DP4-6-3", 2, 41)

# 6. CLE #25 Jason Giambi (X - X - 41)
t2.new_ab()
t2.pitch_list("c b c f b")
t2.out("DP4-6-3")


# Bot 2nd
# Pitching: CLE #63 Justin Masterson
b2 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
b2.new_ab()
b2.pitch_list("b c b s f b b")
b2.reach("BB")
b2.advance(2, "12 1B")
b2.advance(3, "39 L9")
b2.advance(4, "37 HR")

# 5. BOS #12 Mike Napoli (X - X - 34)
b2.new_ab()
b2.pitch_list("f b s")
b2.hit(1)
b2.advance(4, "37 HR")

# 6. BOS #39 Jarrod Saltalamacchia (X - 34 - 12)
b2.new_ab()
b2.pitch_list("c")
b2.out("L9")

# 7. BOS #37 Mike Carp (34 - X - 12)
b2.new_ab()
b2.pitch_list("b c")
b2.hit(4, rbis=3)

# 8. BOS #7  Stephen Drew (X - X - X)
b2.new_ab()
b2.pitch_list("b c b")
b2.out("G4-3")

# 9. BOS #10 Jose Iglesias (X - X - X)
b2.new_ab()
b2.pitch_list("c s c")
b2.out("!K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #41 John Lackey
t3 = game.new_inning()

# 7. CLE #12 Mark Reynolds (X - X - X)
t3.new_ab()
t3.pitch_list("b b")
t3.hit(1)
t3.advance(2, "23 1B")
t3.error(2)
t3.advance(3, "22 SB")
t3.advance("U", "22 E2")

# 8. CLE #23 Michael Brantley (X - X - 12)
t3.new_ab()
t3.pitch_list("c f b")
t3.hit(1)
t3.advance(3, "22 SB")

# 9. CLE #11 Drew Stubbs (X - 12 - 23)
t3.new_ab()
t3.pitch_list("b b c")
t3.out("L8")

# 1. CLE #24 Michael Bourn (X - 12 - 23)
t3.new_ab()
t3.pitch_list("c f f s")
t3.out("K")

# 2. CLE #22 Jason Kipnis (X - 12 - 23)
t3.new_ab()
t3.pitch_list("b b c f d b")
t3.reach("BB")
t3.advance(2, "13 SB")

# 3. CLE #13 Asdrúbal Cabrera (23 - X - 22)
t3.new_ab()
t3.pitch_list("c f b f d")
t3.out("G3-1")


# Bot 3rd
# Pitching: CLE #63 Justin Masterson
b3 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b3.new_ab()
b3.pitch_list("b c b f f b f")
b3.out("G6-3")

# 2. BOS #29 Daniel Nava (X - X - X)
b3.new_ab()
b3.pitch_list("b")
b3.hit(1)
b3.thrown_out(2, "15 DP6-4-3", 2, 63)

# 3. BOS #15 Dustin Pedroia (X - X - 29)
b3.new_ab()
b3.pitch_list("b f")
b3.out("DP6-4-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #41 John Lackey
t4 = game.new_inning()

# 4. CLE #33 Nick Swisher (X - X - X)
t4.new_ab()
t4.pitch_list("c b f")
t4.out("G3")

# 5. CLE #41 Carlos Santana (X - X - X)
t4.new_ab()
t4.pitch_list("c f")
t4.out("G6-3")

# 6. CLE #25 Jason Giambi (X - X - X)
t4.new_ab()
t4.pitch_list("b c")
t4.out("G3-1")


# Bot 4th
# Pitching: CLE #63 Justin Masterson
b4 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
b4.new_ab()
b4.out("G3")

# 5. BOS #12 Mike Napoli (X - X - X)
b4.new_ab()
b4.pitch_list("b c c b b c")
b4.out("!K")

# 6. BOS #39 Jarrod Saltalamacchia (X - X - X)
b4.new_ab()
b4.pitch_list("b b")
b4.out("G5-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #41 John Lackey
t5 = game.new_inning()

# 7. CLE #12 Mark Reynolds (X - X - X)
t5.new_ab()
t5.pitch_list("b s s b s")
t5.out("K")

# 8. CLE #23 Michael Brantley (X - X - X)
t5.new_ab()
t5.pitch_list("c c b")
t5.out("G6-3")

# 9. CLE #11 Drew Stubbs (X - X - X)
t5.new_ab()
t5.pitch_list("f b f s")
t5.out("K")


# Bot 5th
# Pitching: CLE #63 Justin Masterson
b5 = game.new_inning()

# 7. BOS #37 Mike Carp (X - X - X)
b5.new_ab()
b5.pitch_list("b s")
b5.out("G5-3")

# 8. BOS #7  Stephen Drew (X - X - X)
b5.new_ab()
b5.pitch_list("b b")
b5.out("G4-3")

# 9. BOS #10 Jose Iglesias (X - X - X)
b5.new_ab()
b5.pitch_list("b s s f s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #41 John Lackey
t6 = game.new_inning()

# 1. CLE #24 Michael Bourn (X - X - X)
t6.new_ab()
t6.out("G1-3")

# 2. CLE #22 Jason Kipnis (X - X - X)
t6.new_ab()
t6.pitch_list("b c b b f b")
t6.reach("BB")
t6.advance(2, "13 G3")

# 3. CLE #13 Asdrúbal Cabrera (X - X - 22)
t6.new_ab()
t6.pitch_list("1 1 1 b s")
t6.out("G3")

# 4. CLE #33 Nick Swisher (X - 22 - X)
t6.new_ab()
t6.pitch_list("s s b s")
t6.out("K")


# Bot 6th
# Pitching: CLE #63 Justin Masterson
b6 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b6.new_ab()
b6.pitch_list("c f f c")
b6.out("!K")

# 2. BOS #29 Daniel Nava (X - X - X)
b6.new_ab()
b6.pitch_list("b c")
b6.reach("HBP")
b6.advance(2, "15 1B")
b6.advance(3, "34 1B")
b6.advance(4, "12 FC6-4-3-2")

# 3. BOS #15 Dustin Pedroia (X - X - 29)
b6.new_ab()
b6.pitch_list("f f 1")
b6.hit(1)
b6.advance(2, "34 1B")
b6.thrown_out(4, "12 6-4-3-2", 3, 63)

# 4. BOS #34 David Ortiz (X - 29 - 15)
b6.new_ab()
b6.pitch_list("c")
b6.hit(1)
b6.thrown_out(2, "12 FC6-4-3-2", 2, 63)

# 5. BOS #12 Mike Napoli (29 - 15 - 34)
b6.new_ab()
b6.reach("FC6-4-3-2", rbis=1)


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #41 John Lackey
t7 = game.new_inning()

# 5. CLE #41 Carlos Santana (X - X - X)
t7.new_ab()
t7.pitch_list("c b b f")
t7.out("G3")

# 6. CLE #25 Jason Giambi (X - X - X)
t7.new_ab()
t7.pitch_list("c f f b b f f s")
t7.out("K")

# 7. CLE #12 Mark Reynolds (X - X - X)
t7.new_ab()
t7.pitch_list("s c b s")
t7.out("K")


# Bot 7th
# Pitching: CLE #63 Justin Masterson
b7 = game.new_inning()

# 6. BOS #39 Jarrod Saltalamacchia (X - X - X)
b7.new_ab()
b7.pitch_list("s b")
b7.hit(2)
b7.advance(3, "10 1B")
b7.advance(4, "2 1B")

# Pitching change (CLE): #53 Rich Hill replaces #63 Justin Masterson
b7.pitching_substitution(53)

# Offensive change (BOS): Pinch-hitter #5 Jonny Gomes replaces #37 Mike Carp, batting 7th
b7.offensive_substitution(7, 5, "PH")

# 7. BOS #5  Jonny Gomes (X - 39 - X)
b7.new_ab()
b7.pitch_list("c b")
b7.reach("HBP")
b7.advance(2, "10 1B")
b7.advance(4, "2 1B")

# 8. BOS #7  Stephen Drew (X - 39 - 5)
b7.new_ab()
b7.pitch_list("l m 2 s")
b7.out("K")

# 9. BOS #10 Jose Iglesias (X - 39 - 5)
b7.new_ab()
b7.pitch_list("b c c")
b7.hit(1)
b7.advance(3, "2 1B")
b7.advance(4, "15 1B")

# 1. BOS #2  Jacoby Ellsbury (39 - 5 - 10)
b7.new_ab()
b7.pitch_list("s c b")
b7.hit(1, rbis=2)
b7.advance(2, "15 SB")
b7.advance(4, "15 1B")

# 2. BOS #29 Daniel Nava (10 - X - 2)
b7.new_ab()
b7.pitch_list("f 1 1")
b7.out("(F)P5")

# Pitching change (CLE): #32 Matt Albers replaces #53 Rich Hill
b7.pitching_substitution(32)

# 3. BOS #15 Dustin Pedroia (10 - X - 2)
b7.new_ab()
b7.pitch_list("1 c 1 b 1 b c")
b7.hit(1, rbis=2)
b7.advance(2, "34 BB")
b7.thrown_out(3, "12 FC5", 3, 32)

# 4. BOS #34 David Ortiz (X - X - 15)
b7.new_ab()
b7.pitch_list("b b c f b f b")
b7.reach("BB")
b7.advance(2, "12 FC5")

# 5. BOS #12 Mike Napoli (X - 15 - 34)
b7.new_ab()
b7.pitch_list("f d")
b7.reach("FC5")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #19 Koji Uehara
t8 = game.new_inning()

# Pitching change (BOS): #19 Koji Uehara replaces #41 John Lackey
t8.pitching_substitution(19)

# Defensive switch (BOS): #5 Jonny Gomes moves to LF
t8.defensive_switch(5, "7")

# 8. CLE #23 Michael Brantley (X - X - X)
t8.new_ab()
t8.pitch_list("b c")
t8.hit(2)
t8.advance(3, "24 F9")

# 9. CLE #11 Drew Stubbs (X - 23 - X)
t8.new_ab()
t8.pitch_list("b c")
t8.out("P4")

# 1. CLE #24 Michael Bourn (X - 23 - X)
t8.new_ab()
t8.pitch_list("s c d b")
t8.out("F9")

# 2. CLE #22 Jason Kipnis (23 - X - X)
t8.new_ab()
t8.pitch_list("c b f f")
t8.out("F8")


# Bot 8th
# Pitching: CLE #52 Vinnie Pestano
b8 = game.new_inning()

# Pitching change (CLE): #52 Vinnie Pestano replaces #32 Matt Albers
b8.pitching_substitution(52)

# 6. BOS #39 Jarrod Saltalamacchia (X - X - X)
b8.new_ab()
b8.pitch_list("s c b b f b")
b8.out("F8")

# 7. BOS #5  Jonny Gomes (X - X - X)
b8.new_ab()
b8.pitch_list("b b c b c s")
b8.out("K")

# 8. BOS #7  Stephen Drew (X - X - X)
b8.new_ab()
b8.pitch_list("b b f c")
b8.out("F9")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #91 Alfredo Aceves
t9 = game.new_inning()

# Pitching change (BOS): #91 Alfredo Aceves replaces #19 Koji Uehara
t9.pitching_substitution(91)

# 3. CLE #13 Asdrúbal Cabrera (X - X - X)
t9.new_ab()
t9.pitch_list("c b b f b f")
t9.hit(1)

# 4. CLE #33 Nick Swisher (X - X - 13)
t9.new_ab()
t9.pitch_list("s b b f f f s")
t9.out("K")

# 5. CLE #41 Carlos Santana (X - X - 13)
t9.new_ab()
t9.pitch_list("c b b s")
t9.out("F8")

# 6. CLE #25 Jason Giambi (X - X - 13)
t9.new_ab()
t9.out("G5-3")

# Winning team: BOS
# WP: BOS #41 John Lackey
game.winning_pitcher(41)

# Loser team: CLE
# LP: CLE #63 Justin Masterson
game.losing_pitcher(63, is_away_team=True)

# print(game)
game.generate_scorecard()
