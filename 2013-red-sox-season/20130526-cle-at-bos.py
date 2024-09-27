import os
from baseball_scorecard.baseball_scorecard import Scorecard

# CLE @ BOS, 2013-05-26
# https://www.baseball-reference.com/boxes/BOS/BOS201305260.shtml
# https://www.mlb.com/gameday/indians-vs-red-sox/2013/05/26/347482/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-05-26 13:38-16:57",
        "at": "Fenway Park, Boston, MA",
        "att": "37,046",
        "temp": "56F, Partly Cloudy",
        "wind": "17mph, Out To RF",
        "away": {
            "team": "Cleveland Indians",
            "starter": 28,
            "roster": {
                # Lineup
                24: "Michael Bourn",
                22: "Jason Kipnis",
                13: "Asdrúbal Cabrera",
                33: "Nick Swisher",
                12: "Mark Reynolds",
                41: "Carlos Santana",
                23: "Michael Brantley",
                4: "Mike Aviles",
                11: "Drew Stubbs",
                # Starting pitcher
                28: "Corey Kluber",
                # Bench
                9: "Ryan Raburn",
                10: "Yan Gomes",
                25: "Jason Giambi",
                # Bullpen
                26: "Scott Kazmir",
                32: "Matt Albers",
                54: "Chris Perez",
                37: "Cody Allen",
                51: "Scott Barnes",
                63: "Justin Masterson",
                30: "Ubaldo Jiménez",
                27: "Bryan Shaw",
                34: "Zach McAllister",
                53: "Rich Hill",
                38: "Joe Smith",
                52: "Vinnie Pestano",
            },
            "lefties": [26, 51, 53],
            "lineup": [
                [24, "8"],
                [22, "4"],
                [13, "0"],
                [33, "3"],
                [12, "5"],
                [41, "2"],
                [23, "7"],
                [4, "6"],
                [11, "9"],
            ],
            "bench": [
                [9, "LF"],
                [10, "C"],
                [25, "1B"],
            ],
            "bullpen": [26, 32, 54, 37, 51, 63, 30, 27, 34, 53, 38, 52],
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
                5: "Jonny Gomes",
                3: "David Ross",
                23: "Pedro Ciriaco",
                # Bullpen
                63: "Alex Wilson",
                40: "Andrew Bailey",
                41: "John Lackey",
                30: "Andrew Miller",
                32: "Craig Breslow",
                91: "Alfredo Aceves",
                31: "Jon Lester",
                59: "Clayton Mortensen",
                36: "Junichi Tazawa",
                11: "Clay Buchholz",
                19: "Koji Uehara",
                46: "Ryan Dempster",
            },
            "lefties": [22, 30, 32, 31],
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
            "bullpen": [63, 40, 41, 30, 32, 91, 31, 59, 36, 11, 19, 46],
        },
        "umpires": {
            "HP": "Chris Guccione",
            "1B": "Phil Cuzzi",
            "2B": "Tom Hallion",
            "3B": "Ron Kulpa",
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

# 1. CLE #24 Michael Bourn (X - X - X)
t1.new_ab()
t1.pitch_list("b f b")
t1.hit(1)
t1.advance(2, "22 SB")
t1.advance(3, "33 1B")
t1.advance("U", "41 1B")

# 2. CLE #22 Jason Kipnis (X - X - 24)
t1.new_ab()
t1.pitch_list("b c c b f")
t1.error(8)
t1.reach("E8")
t1.advance(2, "33 1B")
t1.advance("U", "41 1B")

# 3. CLE #13 Asdrúbal Cabrera (X - 24 - 22)
t1.new_ab()
t1.pitch_list("c f s")
t1.out("K")

# 4. CLE #33 Nick Swisher (X - 24 - 22)
t1.new_ab()
t1.pitch_list("b b c c f")
t1.hit(1)
t1.advance(3, "41 1B")

# 5. CLE #12 Mark Reynolds (24 - 22 - 33)
t1.new_ab()
t1.pitch_list("b b s c s")
t1.out("K")

# 6. CLE #41 Carlos Santana (24 - 22 - 33)
t1.new_ab()
t1.pitch_list("c c")
t1.hit(1, rbis=2)
t1.thrown_out(2, "8-5-4", 3, 22)


# Bot 1st
# Pitching: CLE #28 Corey Kluber
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("c b b f s")
b1.out("K")

# 2. BOS #29 Daniel Nava (X - X - X)
b1.new_ab()
b1.pitch_list("c b f b s")
b1.out("K")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b1.new_ab()
b1.pitch_list("c c f b f b b f b")
b1.reach("BB")

# 4. BOS #34 David Ortiz (X - X - 15)
b1.new_ab()
b1.pitch_list("c b f b d")
b1.out("G6-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #22 Felix Doubront
t2 = game.new_inning()

# 7. CLE #23 Michael Brantley (X - X - X)
t2.new_ab()
t2.pitch_list("c b")
t2.out("G4-3")

# 8. CLE #4  Mike Aviles (X - X - X)
t2.new_ab()
t2.pitch_list("b b b c c f b")
t2.reach("BB")
t2.advance(2, "11 BB")
t2.advance(3, "22 SB")

# 9. CLE #11 Drew Stubbs (X - X - 4)
t2.new_ab()
t2.pitch_list("1 c s f d 1 b b f b")
t2.reach("BB")

# 1. CLE #24 Michael Bourn (X - 4 - 11)
t2.new_ab()
t2.pitch_list("c s f d b s")
t2.out("K")

# 2. CLE #22 Jason Kipnis (X - 4 - 11)
t2.new_ab()
t2.pitch_list("c c s")
t2.out("K")


# Bot 2nd
# Pitching: CLE #28 Corey Kluber
b2 = game.new_inning()

# 5. BOS #12 Mike Napoli (X - X - X)
b2.new_ab()
b2.pitch_list("b c b c b c")
b2.out("!K")

# 6. BOS #39 Jarrod Saltalamacchia (X - X - X)
b2.new_ab()
b2.pitch_list("c f t")
b2.out("KT")

# 7. BOS #37 Mike Carp (X - X - X)
b2.new_ab()
b2.pitch_list("b f c b")
b2.out("G6-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #22 Felix Doubront
t3 = game.new_inning()

# 3. CLE #13 Asdrúbal Cabrera (X - X - X)
t3.new_ab()
t3.pitch_list("c s f s")
t3.out("K")

# 4. CLE #33 Nick Swisher (X - X - X)
t3.new_ab()
t3.pitch_list("b c f s")
t3.out("K")

# 5. CLE #12 Mark Reynolds (X - X - X)
t3.new_ab()
t3.pitch_list("b b b c")
t3.out("G4-3")


# Bot 3rd
# Pitching: CLE #28 Corey Kluber
b3 = game.new_inning()

# 8. BOS #7  Stephen Drew (X - X - X)
b3.new_ab()
b3.pitch_list("c c b")
b3.hit(2)
b3.advance(3, "2 DP4-6-3")
b3.advance(4, "29 1B")

# 9. BOS #10 Jose Iglesias (X - 7 - X)
b3.new_ab()
b3.pitch_list("c")
b3.reach("HBP")
b3.thrown_out(2, "2 DP4-6-3", 1, 28)

# 1. BOS #2  Jacoby Ellsbury (X - 7 - 10)
b3.new_ab()
b3.pitch_list("s b")
b3.out("DP4-6-3")

# 2. BOS #29 Daniel Nava (7 - X - X)
b3.new_ab()
b3.pitch_list("b d b c")
b3.hit(1, rbis=1)
b3.thrown_out(2, "7-4", 3, 28)


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #22 Felix Doubront
t4 = game.new_inning()

# 6. CLE #41 Carlos Santana (X - X - X)
t4.new_ab()
t4.pitch_list("b c b c")
t4.out("G4-3")

# 7. CLE #23 Michael Brantley (X - X - X)
t4.new_ab()
t4.pitch_list("f b f b b c")
t4.out("!K")

# 8. CLE #4  Mike Aviles (X - X - X)
t4.new_ab()
t4.pitch_list("c f")
t4.out("G1-3")


# Bot 4th
# Pitching: CLE #28 Corey Kluber
b4 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
b4.new_ab()
b4.pitch_list("b b c b")
b4.out("G6-3")

# 4. BOS #34 David Ortiz (X - X - X)
b4.new_ab()
b4.pitch_list("b s b")
b4.out("G5-3")

# 5. BOS #12 Mike Napoli (X - X - X)
b4.new_ab()
b4.pitch_list("b c c b s")
b4.out("K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #22 Felix Doubront
t5 = game.new_inning()

# 9. CLE #11 Drew Stubbs (X - X - X)
t5.new_ab()
t5.pitch_list("c c b b")
t5.out("G5-3")

# 1. CLE #24 Michael Bourn (X - X - X)
t5.new_ab()
t5.out("B2")

# 2. CLE #22 Jason Kipnis (X - X - X)
t5.new_ab()
t5.pitch_list("c f")
t5.hit(4)

# 3. CLE #13 Asdrúbal Cabrera (X - X - X)
t5.new_ab()
t5.pitch_list("f s b b s")
t5.out("K")


# Bot 5th
# Pitching: CLE #28 Corey Kluber
b5 = game.new_inning()

# 6. BOS #39 Jarrod Saltalamacchia (X - X - X)
b5.new_ab()
b5.pitch_list("b s b b f s")
b5.out("K")

# 7. BOS #37 Mike Carp (X - X - X)
b5.new_ab()
b5.pitch_list("b f b s b c")
b5.out("!K")

# 8. BOS #7  Stephen Drew (X - X - X)
b5.new_ab()
b5.pitch_list("b")
b5.out("F9")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #22 Felix Doubront
t6 = game.new_inning()

# 4. CLE #33 Nick Swisher (X - X - X)
t6.new_ab()
t6.pitch_list("c f f b b")
t6.hit(4)

# 5. CLE #12 Mark Reynolds (X - X - X)
t6.new_ab()
t6.pitch_list("c b")
t6.out("P1")

# 6. CLE #41 Carlos Santana (X - X - X)
t6.new_ab()
t6.pitch_list("b b c f b")
t6.out("G4-3")

# 7. CLE #23 Michael Brantley (X - X - X)
t6.new_ab()
t6.pitch_list("b")
t6.out("G4-3")


# Bot 6th
# Pitching: CLE #28 Corey Kluber
b6 = game.new_inning()

# 9. BOS #10 Jose Iglesias (X - X - X)
b6.new_ab()
b6.pitch_list("c c b")
b6.out("G5-3")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b6.new_ab()
b6.pitch_list("b b f s f")
b6.hit(1)
b6.advance(2, "29 SB")

# 2. BOS #29 Daniel Nava (X - X - 2)
b6.new_ab()
b6.pitch_list("c 1 b 1 b d c s")
b6.out("K")

# 3. BOS #15 Dustin Pedroia (X - 2 - X)
b6.new_ab()
b6.pitch_list("c s f s")
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #63 Alex Wilson
t7 = game.new_inning()

# Pitching change (BOS): #63 Alex Wilson replaces #22 Felix Doubront
t7.pitching_substitution(63)

# 8. CLE #4  Mike Aviles (X - X - X)
t7.new_ab()
t7.pitch_list("b f")
t7.out("G1-3")

# 9. CLE #11 Drew Stubbs (X - X - X)
t7.new_ab()
t7.pitch_list("c b b s c")
t7.out("!K")

# 1. CLE #24 Michael Bourn (X - X - X)
t7.new_ab()
t7.pitch_list("b b b c b")
t7.reach("BB")
t7.thrown_out(2, "22 CS", 3, 63)

# 2. CLE #22 Jason Kipnis (X - X - 24)
t7.new_ab()
t7.pitch_list("c 1 1 b f 1 p")
t7.no_ab("CS")


# Bot 7th
# Pitching: CLE #28 Corey Kluber
b7 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
b7.new_ab()
b7.pitch_list("c b s b b f")
b7.out("G6-3")

# 5. BOS #12 Mike Napoli (X - X - X)
b7.new_ab()
b7.pitch_list("f b c s")
b7.out("K")

# Pitching change (CLE): #53 Rich Hill replaces #28 Corey Kluber
b7.pitching_substitution(53)

# 6. BOS #39 Jarrod Saltalamacchia (X - X - X)
b7.new_ab()
b7.pitch_list("b b c b b")
b7.reach("BB")

# Pitching change (CLE): #37 Cody Allen replaces #53 Rich Hill
b7.pitching_substitution(37)

# Offensive change (BOS): Pinch-hitter #5 Jonny Gomes replaces #37 Mike Carp, batting 7th
b7.offensive_substitution(7, 5, "PH")

# 7. BOS #5  Jonny Gomes (X - X - 39)
b7.new_ab()
b7.out("F7")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #32 Craig Breslow
t8 = game.new_inning()

# Pitching change (BOS): #32 Craig Breslow replaces #63 Alex Wilson
t8.pitching_substitution(32)

# Defensive switch (BOS): #5 Jonny Gomes moves to LF
t8.defensive_switch(5, "7")

# 2. CLE #22 Jason Kipnis (X - X - X)
t8.new_ab()
t8.pitch_list("c")
t8.hit(2)
t8.advance(3, "13 1B")
t8.advance(4, "33 SFDP7-2-3")

# 3. CLE #13 Asdrúbal Cabrera (X - 22 - X)
t8.new_ab()
t8.pitch_list("d")
t8.hit(1)
t8.thrown_out(1, "33 SFDP7-2-3", 2, 32)

# 4. CLE #33 Nick Swisher (22 - X - 13)
t8.new_ab()
t8.pitch_list("b b d")
t8.out("SFDP7-2-3", rbis=1)

# 5. CLE #12 Mark Reynolds (X - X - X)
t8.new_ab()
t8.pitch_list("b b c b c")
t8.out("G5-3")


# Bot 8th
# Pitching: CLE #37 Cody Allen
b8 = game.new_inning()

# 8. BOS #7  Stephen Drew (X - X - X)
b8.new_ab()
b8.pitch_list("b b c")
b8.hit(3)
b8.advance(4, "10 SF7")

# 9. BOS #10 Jose Iglesias (7 - X - X)
b8.new_ab()
b8.pitch_list("f b b")
b8.out("SF7", rbis=1)

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b8.new_ab()
b8.pitch_list("c b")
b8.out("G4-3")

# 2. BOS #29 Daniel Nava (X - X - X)
b8.new_ab()
b8.pitch_list("b c b")
b8.out("F8")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #32 Craig Breslow
t9 = game.new_inning()

# 6. CLE #41 Carlos Santana (X - X - X)
t9.new_ab()
t9.pitch_list("c f b f f")
t9.out("G5-3")

# 7. CLE #23 Michael Brantley (X - X - X)
t9.new_ab()
t9.out("G3-1")

# 8. CLE #4  Mike Aviles (X - X - X)
t9.new_ab()
t9.pitch_list("c b b f")
t9.out("G6-3")


# Bot 9th
# Pitching: CLE #54 Chris Perez
b9 = game.new_inning()

# Pitching change (CLE): #54 Chris Perez replaces #37 Cody Allen
b9.pitching_substitution(54)

# 3. BOS #15 Dustin Pedroia (X - X - X)
b9.new_ab()
b9.pitch_list("c b b c b b")
b9.reach("BB")
b9.advance(3, "34 2B")
b9.advance(4, "12 G6-3")

# 4. BOS #34 David Ortiz (X - X - 15)
b9.new_ab()
b9.pitch_list("c")
b9.hit(2)
b9.advance(3, "39 SB")
b9.advance(4, "39 G3-1")

# 5. BOS #12 Mike Napoli (15 - 34 - X)
b9.new_ab()
b9.pitch_list("b b")
b9.out("G6-3", rbis=1)

# 6. BOS #39 Jarrod Saltalamacchia (X - 34 - X)
b9.new_ab()
b9.pitch_list("s b")
b9.out("G3-1", rbis=1)

# 7. BOS #5  Jonny Gomes (X - X - X)
b9.new_ab()
b9.pitch_list("b b c b b")
b9.reach("BB")
b9.advance(3, "7 1B")
b9.advance(4, "2 2B")

# 8. BOS #7  Stephen Drew (X - X - 5)
b9.new_ab()
b9.pitch_list("c")
b9.hit(1)
b9.advance(2, "10 SB")
b9.advance(4, "2 2B")

# 9. BOS #10 Jose Iglesias (5 - X - 7)
b9.new_ab()
b9.pitch_list("c d b f f b b")
b9.reach("BB")
b9.advance(3, "2 2B")

# Pitching change (CLE): #38 Joe Smith replaces #54 Chris Perez
b9.pitching_substitution(38)

# 1. BOS #2  Jacoby Ellsbury (5 - 7 - 10)
b9.new_ab()
b9.pitch_list("b c b")
b9.hit(2, rbis=2)

# Winning team: BOS
# WP: BOS #32 Craig Breslow
game.winning_pitcher(32)

# Loser team: CLE
# LP: CLE #54 Chris Perez
game.losing_pitcher(54, is_away_team=True)

# print(game)
game.generate_scorecard()
