import os
from baseball_scorecard.baseball_scorecard import Scorecard

# CLE @ BOS, 2013-05-23
# https://www.baseball-reference.com/boxes/BOS/BOS201305230.shtml
# https://www.mlb.com/gameday/indians-vs-red-sox/2013/05/23/347446/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-05-23 19:12-22:46",
        "at": "Fenway Park, Boston, MA",
        "att": "35,254",
        "temp": "72F, Partly Cloudy",
        "wind": "20mph, Out To CF",
        "away": {
            "team": "Cleveland Indians",
            "starter": 34,
            "roster": {
                # Lineup
                24: "Michael Bourn",
                22: "Jason Kipnis",
                13: "Asdrúbal Cabrera",
                23: "Michael Brantley",
                41: "Carlos Santana",
                12: "Mark Reynolds",
                10: "Yan Gomes",
                4: "Mike Aviles",
                11: "Drew Stubbs",
                # Starting pitcher
                34: "Zach McAllister",
                # Bench
                9: "Ryan Raburn",
                25: "Jason Giambi",
                46: "Cord Phelps",
                # Bullpen
                26: "Scott Kazmir",
                32: "Matt Albers",
                54: "Chris Perez",
                37: "Cody Allen",
                51: "Scott Barnes",
                63: "Justin Masterson",
                30: "Ubaldo Jiménez",
                27: "Bryan Shaw",
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
                [23, "7"],
                [41, "3"],
                [12, "0"],
                [10, "2"],
                [4, "5"],
                [11, "9"],
            ],
            "bench": [
                [9, "LF"],
                [25, "1B"],
                [46, "2B"],
            ],
            "bullpen": [26, 32, 54, 37, 51, 63, 30, 27, 53, 38, 52, 28],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 46,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                29: "Daniel Nava",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                39: "Jarrod Saltalamacchia",
                16: "Will Middlebrooks",
                7: "Stephen Drew",
                37: "Mike Carp",
                # Starting pitcher
                46: "Ryan Dempster",
                # Bench
                23: "Pedro Ciriaco",
                20: "Ryan Lavarnway",
                5: "Jonny Gomes",
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
                11: "Clay Buchholz",
            },
            "lefties": [30, 32, 31, 22],
            "lineup": [
                [2, "8"],
                [29, "9"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [39, "2"],
                [16, "5"],
                [7, "6"],
                [37, "7"],
            ],
            "bench": [
                [23, "3B"],
                [20, "C"],
                [5, "LF"],
            ],
            "bullpen": [63, 40, 41, 30, 32, 19, 31, 59, 36, 22, 11],
        },
        "umpires": {
            "HP": "Phil Cuzzi",
            "1B": "Tom Hallion",
            "2B": "Ron Kulpa",
            "3B": "Chris Guccione",
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
# Pitching: BOS #46 Ryan Dempster
t1 = game.new_inning()

# 1. CLE #24 Michael Bourn (X - X - X)
t1.new_ab()
t1.pitch_list("s f c")
t1.out("!K")

# 2. CLE #22 Jason Kipnis (X - X - X)
t1.new_ab()
t1.pitch_list("b c s b")
t1.hit(1)

# 3. CLE #13 Asdrúbal Cabrera (X - X - 22)
t1.new_ab()
t1.pitch_list("b 1 b c d f")
t1.out("F7")

# 4. CLE #23 Michael Brantley (X - X - 22)
t1.new_ab()
t1.out("F7")


# Bot 1st
# Pitching: CLE #34 Zach McAllister
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("l c b b f f s")
b1.out("K")

# 2. BOS #29 Daniel Nava (X - X - X)
b1.new_ab()
b1.pitch_list("c b b c")
b1.hit(2)

# 3. BOS #15 Dustin Pedroia (X - 29 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("c b")
b1.out("P4")

# 4. BOS #34 David Ortiz (X - 29 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("f")
b1.out("(F)P4")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #46 Ryan Dempster
t2 = game.new_inning()

# 5. CLE #41 Carlos Santana (X - X - X)
t2.new_ab()
t2.pitch_list("b b")
t2.hit(1)
t2.advance(2, "12 BB")
t2.advance(4, "11 2B")

# 6. CLE #12 Mark Reynolds (X - X - 41)
t2.new_ab()
t2.pitch_list("b b c b c f f d")
t2.reach("BB")
t2.advance(3, "11 2B")

# 7. CLE #10 Yan Gomes (X - 41 - 12)
t2.new_ab(is_risp=True)
t2.pitch_list("c f b f s")
t2.out("K")

# 8. CLE #4  Mike Aviles (X - 41 - 12)
t2.new_ab(is_risp=True)
t2.pitch_list("s d b f")
t2.out("F9")

# 9. CLE #11 Drew Stubbs (X - 41 - 12)
t2.new_ab(is_risp=True)
t2.pitch_list("c")
t2.hit(2, rbis=1)

# 1. CLE #24 Michael Bourn (12 - 11 - X)
t2.new_ab(is_risp=True)
t2.pitch_list("b c b c f f")
t2.out("G3")


# Bot 2nd
# Pitching: CLE #34 Zach McAllister
b2 = game.new_inning()

# 5. BOS #12 Mike Napoli (X - X - X)
b2.new_ab()
b2.pitch_list("b c")
b2.hit(1)
b2.advance(2, "39 BB")
b2.advance(3, "7 F8")

# 6. BOS #39 Jarrod Saltalamacchia (X - X - 12)
b2.new_ab()
b2.pitch_list("b b b c f f 1 f b")
b2.reach("BB")

# 7. BOS #16 Will Middlebrooks (X - 12 - 39)
b2.new_ab(is_risp=True)
b2.pitch_list("c c f b b f c")
b2.out("!K")

# 8. BOS #7  Stephen Drew (X - 12 - 39)
b2.new_ab(is_risp=True)
b2.pitch_list("c b")
b2.out("F8")

# 9. BOS #37 Mike Carp (12 - X - 39)
b2.new_ab(is_risp=True)
b2.pitch_list("c b")
b2.out("G6-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #46 Ryan Dempster
t3 = game.new_inning()

# 2. CLE #22 Jason Kipnis (X - X - X)
t3.new_ab()
t3.pitch_list("c b b f f f b s")
t3.out("K")

# 3. CLE #13 Asdrúbal Cabrera (X - X - X)
t3.new_ab()
t3.pitch_list("s b")
t3.hit(1)
t3.advance(2, "23 BB")
t3.advance(3, "41 BB")
t3.advance(4, "12 1B")

# 4. CLE #23 Michael Brantley (X - X - 13)
t3.new_ab()
t3.pitch_list("1 b c d b b")
t3.reach("BB")
t3.advance(2, "41 BB")
t3.advance(4, "12 1B")

# 5. CLE #41 Carlos Santana (X - 13 - 23)
t3.new_ab(is_risp=True)
t3.pitch_list("b b c s b f b")
t3.reach("BB")
t3.advance(2, "12 1B")
t3.advance(3, "10 BB")
t3.advance(4, "4 FC6-4")

# 6. CLE #12 Mark Reynolds (13 - 23 - 41)
t3.new_ab(is_risp=True)
t3.pitch_list("c")
t3.hit(1, rbis=2)
t3.advance(2, "10 BB")
t3.advance(3, "4 FC6-4")

# 7. CLE #10 Yan Gomes (X - 41 - 12)
t3.new_ab(is_risp=True)
t3.pitch_list("c d f b b f f f b")
t3.reach("BB")
t3.thrown_out(2, "4 FC6-4", 2, 46)

# 8. CLE #4  Mike Aviles (41 - 12 - 10)
t3.new_ab(is_risp=True)
t3.pitch_list("s")
t3.reach("FC6-4", rbis=1)

# 9. CLE #11 Drew Stubbs (12 - X - 4)
t3.new_ab(is_risp=True)
t3.pitch_list("c c b s")
t3.out("K")


# Bot 3rd
# Pitching: CLE #34 Zach McAllister
b3 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b3.new_ab()
b3.hit(1)
b3.advance(2, "29 BB")
b3.advance(3, "15 1B")
b3.thrown_out(4, "15 8-2", 1, 34)

# 2. BOS #29 Daniel Nava (X - X - 2)
b3.new_ab()
b3.pitch_list("1 b b b c f b")
b3.reach("BB")
b3.advance(2, "15 8-2")
b3.advance(4, "34 HR")

# 3. BOS #15 Dustin Pedroia (X - 2 - 29)
b3.new_ab(is_risp=True)
b3.pitch_list("b s b")
b3.hit(1)
b3.advance(4, "34 HR")

# 4. BOS #34 David Ortiz (X - 29 - 15)
b3.new_ab(is_risp=True)
b3.hit(4, rbis=3)

# 5. BOS #12 Mike Napoli (X - X - X)
b3.new_ab()
b3.pitch_list("b c c s")
b3.out("K")

# 6. BOS #39 Jarrod Saltalamacchia (X - X - X)
b3.new_ab()
b3.pitch_list("c b s")
b3.out("L6")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #59 Clayton Mortensen
t4 = game.new_inning()

# Pitching change (BOS): #59 Clayton Mortensen replaces #46 Ryan Dempster
t4.pitching_substitution(59)

# 1. CLE #24 Michael Bourn (X - X - X)
t4.new_ab()
t4.pitch_list("c c b f b")
t4.hit(2)
t4.advance(4, "13 1B")

# 2. CLE #22 Jason Kipnis (X - 24 - X)
t4.new_ab(is_risp=True)
t4.out("P4")

# 3. CLE #13 Asdrúbal Cabrera (X - 24 - X)
t4.new_ab(is_risp=True)
t4.pitch_list("b c f")
t4.hit(1, rbis=1)
t4.advance(2, "41 BB")

# 4. CLE #23 Michael Brantley (X - X - 13)
t4.new_ab()
t4.pitch_list("b 1 f f 1")
t4.out("F8")

# 5. CLE #41 Carlos Santana (X - X - 13)
t4.new_ab()
t4.pitch_list("l t b b d b")
t4.reach("BB")
t4.thrown_out(2, "12 FC6-4", 3, 59)

# 6. CLE #12 Mark Reynolds (X - 13 - 41)
t4.new_ab(is_risp=True)
t4.reach("FC6-4")


# Bot 4th
# Pitching: CLE #34 Zach McAllister
b4 = game.new_inning()

# 7. BOS #16 Will Middlebrooks (X - X - X)
b4.new_ab()
b4.pitch_list("c f f b f f c")
b4.out("!K")

# 8. BOS #7  Stephen Drew (X - X - X)
b4.new_ab()
b4.pitch_list("b c")
b4.out("G6-3")

# 9. BOS #37 Mike Carp (X - X - X)
b4.new_ab()
b4.pitch_list("c f b b f b")
b4.out("G4-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #59 Clayton Mortensen
t5 = game.new_inning()

# Defensive change (BOS): #23 Pedro Ciriaco replaces #16 Will Middlebrooks (3B), playing 3B, batting 7th
t5.defensive_substitution(7, 23, "5")

# 7. CLE #10 Yan Gomes (X - X - X)
t5.new_ab()
t5.pitch_list("b f s b")
t5.out("F7")

# 8. CLE #4  Mike Aviles (X - X - X)
t5.new_ab()
t5.hit(1)
t5.advance(2, "24 SB")
t5.advance(4, "24 1B")

# 9. CLE #11 Drew Stubbs (X - X - 4)
t5.new_ab()
t5.out("F9")

# 1. CLE #24 Michael Bourn (X - X - 4)
t5.new_ab(is_risp=True)
t5.pitch_list("1 b b")
t5.hit(1, rbis=1)

# 2. CLE #22 Jason Kipnis (X - X - 24)
t5.new_ab()
t5.pitch_list("f b c")
t5.out("F8")


# Bot 5th
# Pitching: CLE #34 Zach McAllister
b5 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b5.new_ab()
b5.pitch_list("c f b c")
b5.out("!K")

# 2. BOS #29 Daniel Nava (X - X - X)
b5.new_ab()
b5.pitch_list("b b c c b f b")
b5.reach("BB")
b5.advance(2, "34 WP")

# 3. BOS #15 Dustin Pedroia (X - X - 29)
b5.new_ab()
b5.pitch_list("b b c 1")
b5.out("F8")

# 4. BOS #34 David Ortiz (X - X - 29)
b5.new_ab(is_risp=True)
b5.pitch_list("b c")
b5.wp()
b5.out("G5-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #59 Clayton Mortensen
t6 = game.new_inning()

# 3. CLE #13 Asdrúbal Cabrera (X - X - X)
t6.new_ab()
t6.pitch_list("b c b b s f d")
t6.reach("BB")
t6.advance(2, "23 1B")
t6.advance(3, "41 BB")
t6.advance(4, "12 1B")

# 4. CLE #23 Michael Brantley (X - X - 13)
t6.new_ab()
t6.pitch_list("d c")
t6.hit(1)
t6.advance(2, "41 BB")
t6.advance(3, "12 1B")
t6.advance(4, "10 2B")

# 5. CLE #41 Carlos Santana (X - 13 - 23)
t6.new_ab(is_risp=True)
t6.pitch_list("b d d b")
t6.reach("BB")
t6.advance(2, "12 1B")
t6.advance(4, "10 2B")

# Pitching change (BOS): #63 Alex Wilson replaces #59 Clayton Mortensen
t6.pitching_substitution(63)

# 6. CLE #12 Mark Reynolds (13 - 23 - 41)
t6.new_ab(is_risp=True)
t6.hit(1, rbis=1)
t6.advance(3, "10 2B")
t6.advance(4, "11 3B")

# 7. CLE #10 Yan Gomes (23 - 41 - 12)
t6.new_ab(is_risp=True)
t6.pitch_list("b b f")
t6.error(3)
t6.hit(2, rbis=2)
t6.advance("U", "11 3B")

# 8. CLE #4  Mike Aviles (12 - 10 - X)
t6.new_ab(is_risp=True)
t6.pitch_list("c b c f")
t6.out("P4")

# 9. CLE #11 Drew Stubbs (12 - 10 - X)
t6.new_ab(is_risp=True)
t6.pitch_list("c s d")
t6.hit(3, rbis=2)
t6.advance(4, "24 1B")

# 1. CLE #24 Michael Bourn (11 - X - X)
t6.new_ab(is_risp=True)
t6.pitch_list("b b c f")
t6.hit(1, rbis=1)

# 2. CLE #22 Jason Kipnis (X - X - 24)
t6.new_ab()
t6.pitch_list("c f b b s")
t6.out("K")

# 3. CLE #13 Asdrúbal Cabrera (X - X - 24)
t6.new_ab()
t6.pitch_list("c s f s")
t6.out("K")


# Bot 6th
# Pitching: CLE #37 Cody Allen
b6 = game.new_inning()

# Pitching change (CLE): #37 Cody Allen replaces #34 Zach McAllister
b6.pitching_substitution(37)

# Defensive change (CLE): #46 Cord Phelps replaces #22 Jason Kipnis (2B), playing 2B, batting 2nd
b6.defensive_substitution(2, 46, "4")

# 5. BOS #12 Mike Napoli (X - X - X)
b6.new_ab()
b6.pitch_list("b c c b f c")
b6.out("!K")

# 6. BOS #39 Jarrod Saltalamacchia (X - X - X)
b6.new_ab()
b6.pitch_list("c b s c")
b6.out("!K")

# 7. BOS #23 Pedro Ciriaco (X - X - X)
b6.new_ab()
b6.pitch_list("b")
b6.out("F9")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #32 Craig Breslow
t7 = game.new_inning()

# Pitching change (BOS): #32 Craig Breslow replaces #63 Alex Wilson
t7.pitching_substitution(32)

# 4. CLE #23 Michael Brantley (X - X - X)
t7.new_ab()
t7.pitch_list("b b c")
t7.out("L6")

# 5. CLE #41 Carlos Santana (X - X - X)
t7.new_ab()
t7.pitch_list("b b b c b")
t7.reach("BB")
t7.advance(3, "12 1B")

# 6. CLE #12 Mark Reynolds (X - X - 41)
t7.new_ab()
t7.pitch_list("f t f")
t7.hit(1)
t7.thrown_out(2, "10 DP1-6-3", 2, 32)

# 7. CLE #10 Yan Gomes (41 - X - 12)
t7.new_ab(is_risp=True)
t7.pitch_list("b b b c")
t7.out("DP1-6-3")


# Bot 7th
# Pitching: CLE #51 Scott Barnes
b7 = game.new_inning()

# Pitching change (CLE): #51 Scott Barnes replaces #37 Cody Allen
b7.pitching_substitution(51)

# 8. BOS #7  Stephen Drew (X - X - X)
b7.new_ab()
b7.pitch_list("b")
b7.out("F8")

# 9. BOS #37 Mike Carp (X - X - X)
b7.new_ab()
b7.pitch_list("c f b s")
b7.out("K")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b7.new_ab()
b7.pitch_list("b f c")
b7.out("G1-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #36 Junichi Tazawa
t8 = game.new_inning()

# Pitching change (BOS): #36 Junichi Tazawa replaces #32 Craig Breslow
t8.pitching_substitution(36)

# 8. CLE #4  Mike Aviles (X - X - X)
t8.new_ab()
t8.pitch_list("f")
t8.out("G6-3")

# 9. CLE #11 Drew Stubbs (X - X - X)
t8.new_ab()
t8.hit(2)
t8.advance(3, "24 G3-1")

# 1. CLE #24 Michael Bourn (X - 11 - X)
t8.new_ab(is_risp=True)
t8.pitch_list("c d")
t8.out("G3-1")

# 2. CLE #46 Cord Phelps (11 - X - X)
t8.new_ab(is_risp=True)
t8.pitch_list("b")
t8.out("G4-3")


# Bot 8th
# Pitching: CLE #51 Scott Barnes
b8 = game.new_inning()

# 2. BOS #29 Daniel Nava (X - X - X)
b8.new_ab()
b8.hit(1)
b8.advance(3, "20 2B")

# 3. BOS #15 Dustin Pedroia (X - X - 29)
b8.new_ab()
b8.pitch_list("b f c s")
b8.out("K")

# Offensive change (BOS): Pinch-hitter #20 Ryan Lavarnway replaces #34 David Ortiz, batting 4th
b8.offensive_substitution(4, 20, "PH")

# 4. BOS #20 Ryan Lavarnway (X - X - 29)
b8.new_ab()
b8.pitch_list("b")
b8.hit(2)

# 5. BOS #12 Mike Napoli (29 - 20 - X)
b8.new_ab(is_risp=True)
b8.pitch_list("c b c s")
b8.out("K")

# 6. BOS #39 Jarrod Saltalamacchia (29 - 20 - X)
b8.new_ab(is_risp=True)
b8.pitch_list("b f b")
b8.out("L5")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #30 Andrew Miller
t9 = game.new_inning()

# Pitching change (BOS): #30 Andrew Miller replaces #36 Junichi Tazawa
t9.pitching_substitution(30)

# Defensive switch (BOS): #20 Ryan Lavarnway moves to DH
t9.defensive_switch(20, "0")

# 3. CLE #13 Asdrúbal Cabrera (X - X - X)
t9.new_ab()
t9.pitch_list("c c b s")
t9.out("K")

# 4. CLE #23 Michael Brantley (X - X - X)
t9.new_ab()
t9.pitch_list("c c b c")
t9.out("!K")

# 5. CLE #41 Carlos Santana (X - X - X)
t9.new_ab()
t9.pitch_list("c f")
t9.out("G6-3")


# Bot 9th
# Pitching: CLE #51 Scott Barnes
b9 = game.new_inning()

# 7. BOS #23 Pedro Ciriaco (X - X - X)
b9.new_ab()
b9.pitch_list("b c s b s")
b9.out("K")

# 8. BOS #7  Stephen Drew (X - X - X)
b9.new_ab()
b9.pitch_list("c b f f f")
b9.out("G4-3")

# 9. BOS #37 Mike Carp (X - X - X)
b9.new_ab()
b9.pitch_list("f b b")
b9.out("G1-3")

# Winning team: CLE
# WP: CLE #34 Zach McAllister
game.winning_pitcher(34, is_away_team=True)
# SV: CLE #51 Scott Barnes
game.save_pitcher(51, is_away_team=True)

# Loser team: BOS
# LP: BOS #46 Ryan Dempster
game.losing_pitcher(46)

# print(game)
game.generate_scorecard()
